import os
import ctypes
from scripts.bannner import *
from modules.phone import *
from modules.ip import *
from modules.domain import *
from modules.nmap import *
from modules.mail import *

if operating_system == "Windows":
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW('OSINT Map Framework V.0.5.1 | t.me/OsintMapDev')
else:
    os.system("clear")

def main():
    banner()

    try:
        while True:
            command = input(f'\nomf({blue}0.5.1{white}) >>> ')
            print('')

            exc_com = extract_command(command.lower())

            if command.lower() in help_commands:
                help()
            elif command.lower() in clear_commands:
                if operating_system == "Windows":
                    os.system('cls')
                elif operating_system == "Linux":
                    os.system("clear")
            elif command.lower() in banner_commands:
                banner()
            elif command.lower() in exit_commands:
                os._exit(1)
            elif exc_com in mail_commands:
                mail(exc_com, command.lower())
            elif exc_com in domain_commands:
                domain(exc_com, command.lower())
            elif exc_com in phone_commands:
                phone(exc_com, command.lower())
            elif exc_com in nmap_commands:
                nmap_search(exc_com, command)
            elif exc_com in ip_commands:
                ip(exc_com, command.lower())
            else:
                incorrect_command()
    except:
        os._exit(1)

if __name__ == "__main__":
    main()
