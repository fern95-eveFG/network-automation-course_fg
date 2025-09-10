# Week 3, Exercise 1
# Create a list of dictionaries from ARP table data

arp_table = [
    {"mac_addr": "0062.ec29.70fe", "ip_addr": "10.220.88.1", "interface": "Gi0/0/0"},
    {"mac_addr": "c89c.1dea.0eb6", "ip_addr": "10.220.88.20", "interface": "Gi0/0/0"},
    {"mac_addr": "a093.5141.b780", "ip_addr": "10.220.88.22", "interface": "Gi0/0/0"},
    {"mac_addr": "0001.00ff.0001", "ip_addr": "10.220.88.37", "interface": "Gi0/0/0"},
    {"mac_addr": "0002.00ff.0001", "ip_addr": "10.220.88.38", "interface": "Gi0/0/0"},
]

print("ARP Table List of Dictionaries:")
for entry in arp_table:
    print(entry)
