import sys
from scanners.nmap_scanner import NmapScanner

if len(sys.argv) != 2:
    print("Forma de uso -> python3 port_scanner.py <direccion IP o dominio>")
    sys.exit(1)

target = sys.argv[1]
scanner = NmapScanner(target)
scanner.scan_ports()
