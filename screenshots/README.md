# Capturas de pantalla — DHCP Starvation

Capturas del laboratorio en orden de demostración.

| Archivo | Descripción |
|---------|-------------|
| `01_topologia.png` | Topología en PNETLab con nombre y matrícula visibles |
| `02_pool_antes.png` | Salida de `show ip dhcp binding` en R1 antes del ataque — pool vacío |
| `03_script_ejecutandose.png` | Terminal Kali Linux ejecutando el script DHCP Starvation |
| `04_pool_agotado.png` | R1 mostrando el pool `20.25.37.0/24` exhausto con MACs falsas |
| `05_vpc1_sin_ip.png` | VPC1 intentando `ip dhcp` sin obtener respuesta — DoS confirmado |
| `06_contramedida_aplicada.png` | Configuración de Port Security en SW2 interfaz e0/3 |
| `07_post_mitigacion.png` | VPC1 obteniendo IP correctamente tras aplicar la contramedida |
