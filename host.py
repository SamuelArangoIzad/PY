import sys
import nmap
#It is functional to see the open ports on the PC 


nm = nmap.PortScanner()
ip_range = "ip OF YOUR PC"
port_range = "1-100"
nm.scan(hosts=ip_range, arguments=f'-p {port_range} -sS')

for host in nm.all_hosts():
    for proto in nm[host].all_protocols():
        for port, info in nm[host][proto].items():
            state = info['state']
            if state == 'open':
                print(f"Host: {host}, Puerto: {port} => Estado: {state}")
