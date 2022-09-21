#!/usr/bin/python3

# Information Security
# Certification Project #3

import socket
import common_ports
import re

open_ports = []

def get_open_ports(target, port_range, verbose=None):
    # Test if target is URL or IP address, if invalid give correct error message
    target_ip = None
    target_url = None
    try:
        ip_addr = socket.gethostbyname(target)
    except socket.gaierror or socket.error:
        if re.search('^[0-9]+', target):
            target_ip = True
            print('Error: Invalid IP address')
            s.close()
            exit()
        elif re.search('^[A-Za-z]+', target):
            target_url = True
            print('Error: Invalid hostname')
            s.close()
            exit()
    except:
        print('Error: Invalid hostname or IP address')
        s.close()
        exit()
    
    # Creates list of ports from starting and ending ports given
    ports_list = list()
    for port in port_range:
        while port < port_range[1]:
            port += 1
            ports_list.append(port)
            # print('ports_list:', ports_list)

    # Connects (if url/ip is valid) and checks for open ports
    # for each port in list, connect
    # for port in range(port_range[0], port_range[1]):
    for port in ports_list:
        # try to connect
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)

            # if port is open, add to open_ports
            if s.connect_ex((target, port)) == 0:
                open_ports.append(port)
                # print('Port', port, 'is open')

        except KeyboardInterrupt:
            print('Exit: KeyboardInterrupt')

        # if it can't connect, display correct output
        except socket.error or socket.gaierror or socket.getaddrinfo:
            if target_ip:
                print('Error 2: Invalid IP address')
                s.close()
                exit()
            elif target_url:
                print('Error 2: Invalid hostname')
                s.close()
                exit()

        # ****************************************************** #
        # Verbose Output

        serv_d = common_ports.ports_and_services
        svcs_dict = {port: serv_d[port] for port in open_ports}
        
        # svcs_dict output
        sk = svcs_dict.keys()
        sv = svcs_dict.values()

        sk = str(svcs_dict.keys() for port in open_ports)
        sk = '\n{svcs_dict.keys(x)}'
        for k in svcs_dict():


        if verbose:
            return print(f'\nOpen ports for {target} ({ip_addr}) \
                    \nPORT     SERVICE \
                    \n{svcs_dict[port]}     {svcs_dict[v]}')
                    # \n{serv_d[port: serv_d[port] for port in open_ports]}     {serv_d[value]}')

            
            # for k,v in common ports dictionary (if in open_ports)
            for port, service in svcs_dict.items():
                print(f'{port}     {service}') # , end='\r')
            return(str(open_ports))
            

        elif not verbose:
            return(open_ports)
        
    s.close()
    return(open_ports)