# Capturas de pantalla — DHCP Starvation

Capturas del laboratorio en orden de demostración.

| # | Archivo | Descripción |
|---|---------|-------------|
| 1 | [01_topologia.png](screenshots/01_topologia.png) | Vista general de la topología en PNETLab con nombre y matrícula visibles |
| 2 | [02_pool_antes.png](screenshots/02_pool_antes.png) | Salida de `show ip dhcp binding` en R1 **antes** del ataque — pool vacío |
| 3 | [03_script_ejecutandose.png](screenshots/03_script_ejecutandose.png) | Terminal de Kali Linux ejecutando el script DHCP Starvation |
| 4 | [04_pool_agotado.png](screenshots/04_pool_agotado.png) | R1 mostrando `show ip dhcp binding` con el pool `20.25.37.0/24` exhausto |
| 5 | [05_vpc1_sin_ip.png](screenshots/05_vpc1_sin_ip.png) | VPC1 intentando `ip dhcp` sin obtener respuesta — DoS confirmado |
| 6 | [06_contramedida_aplicada.png](screenshots/06_contramedida_aplicada.png) | Configuración de Port Security en SW2 interfaz e0/3 |
| 7 | [07_post_mitigacion.png](screenshots/07_post_mitigacion.png) | VPC1 obteniendo IP correctamente tras aplicar la contramedida |
