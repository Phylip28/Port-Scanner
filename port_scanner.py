import os
import sys


def scan_ports(ip):
    print(f"Escaneando puertos en {target}...")
    os.system(f"nmap -p- -sV {target}")


if len(sys.argv) != 2:
    print("Forma de uso -> python3 port_scanner.py <direccion IP o dominio>")
    sys.exit(1)

target = sys.argv[1]
scan_ports(target)
