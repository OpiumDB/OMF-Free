import json
from colorama import init, Fore, Style
import platform
import nmap

with open('config.json', 'r') as file:
    file_content = file.read()

token_leak_osint = json.loads(file_content)['api_leak_osint']

init()

nm = nmap.PortScanner()
operating_system = platform.system()

cyan = Style.BRIGHT + Fore.CYAN
red = Style.BRIGHT + Fore.RED
white = Style.NORMAL + Fore.WHITE
yellow = Style.NORMAL + Fore.YELLOW
green = Style.BRIGHT + Fore.GREEN
blue = Style.BRIGHT + Fore.BLUE

help_commands = ['help']
clear_commands = ['clear']
banner_commands = ['banner']
exit_commands = ['exit']
phone_commands = ['phonelookup', 'phoneinfo', 'phoneall']
ip_commands = ['iplookup', 'ipdata', 'ipgeo', 'ipall', 'ipcheckhost']
domain_commands = ['domainlookup', 'whois', 'dnsrecords', 'domainall']
nmap_commands = ['nmap']
mail_commands = ['maillookup', 'mailleaked', 'mailinfo', 'mailall']
