import os


class NmapScanner:

    def __init__(self, target):
        self.target = target

    def scan_ports(self):
        print(f"Scanning ports in {self.target}...")
        os.system(f"nmap -p- -sV {self.target}")
