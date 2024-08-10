import re
from ping3 import ping

def parse_arp_table(file_path):
    ip_addresses = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            # Adjust regex based on the actual format of your ARP output
            match = re.match(r'\s*([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)\s+', line)
            if match:
                ip_addresses.append(match.group(1))
    return ip_addresses

def ping_ips(ip_addresses):
    for ip in ip_addresses:
        response = ping(ip, timeout=1)
        if response:
            print(f"{ip} is reachable")
        else:
            print(f"{ip} is not reachable")

if __name__ == "__main__":
    arp_output_file = 'arp_table.txt'
    ip_addresses = parse_arp_table(arp_output_file)
    ping_ips(ip_addresses)
