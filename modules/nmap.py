from scripts.utils import *


def nmap_search(command, data_command):
    try:
        data = remove_first_space(data_command.replace(command, ''))
        host = data.split(' ')[0]
        args = remove_first_space(data.replace(host, ''))
        if args == '' or args == None or args == ' ':
            nm.scan(hosts=host)
        else:
            nm.scan(hosts=host, arguments=args)
        for host in nm.all_hosts():
            print(f'Nmap scan report for %s' % host)
            print(f'Host is %s (%slatency)' % (nm[host].state(), nm[host]['hostnames'][0]['name']))

            for proto in nm[host].all_protocols():
                print(f'PORT\t\tSTATE\tSERVICE\t\tVERSION')
                for port in nm[host][proto]:
                    state = nm[host][proto][port]['state']
                    service = nm[host][proto][port]['name']
                    version = nm[host][proto][port]['product'] + ' ' + nm[host][proto][port]['version']
                    print(f"{port}/{proto}\t\t{state}\t{service}\t\t{version}")
    except:
        print(f'{red}Инструмент nmap не установлен на вашем устройстве.')
