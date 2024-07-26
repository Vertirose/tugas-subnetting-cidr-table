import pandas as pd
import ipaddress
import openpyxl

def calculate_subnet_details(prefix_length):
    network = ipaddress.IPv4Network(f"0.0.0.0/{prefix_length}")
    subnet_mask = network.netmask
    num_addresses = network.num_addresses
    available_hosts = num_addresses - 2 if num_addresses > 2 else num_addresses
    return {
        "CIDR": f"/{prefix_length}",
        "Total Subnets": 2**(32 - prefix_length),
        "Available Hosts": available_hosts,
        "Subnet Mask": str(subnet_mask)
    }

cidr_table = [calculate_subnet_details(prefix_length) for prefix_length in range(0, 33)]
df = pd.DataFrame(cidr_table)

file_path = "./cidr.xlsx"
df.to_excel(file_path, index=False)