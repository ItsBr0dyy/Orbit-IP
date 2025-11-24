import os
import time
import json
import requests
import colorama
from colorama import Fore, Back, Style

# colorama
colorama.init()

logo = '''

 ▒█████   ██▀███   ▄▄▄▄    ██▓▄▄▄█████▓
▒██▒  ██▒▓██ ▒ ██▒▓█████▄ ▓██▒▓  ██▒ ▓▒
▒██░  ██▒▓██ ░▄█ ▒▒██▒ ▄██▒██▒▒ ▓██░ ▒░
▒██   ██░▒██▀▀█▄  ▒██░█▀  ░██░░ ▓██▓ ░ 
░ ████▓▒░░██▓ ▒██▒░▓█  ▀█▓░██░  ▒██▒ ░ 
░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░▒▓███▀▒░▓    ▒ ░░   
  ░ ▒ ▒░   ░▒ ░ ▒░▒░▒   ░  ▒ ░    ░    
░ ░ ░ ▒    ░░   ░  ░    ░  ▒ ░  ░      
    ░ ░     ░      ░       ░           
                        ░              

'''

while True:
    os.system('cls')
    print(Fore.GREEN + logo)
    os.system('title Orbit IP - by ItsBr0dyy')
    print(Fore.RED + 'This tool does not harm you or anybody in any sort of way.' + Style.RESET_ALL)
    print(Fore.RED + 'Orbit is mean to locate including country, region, city, zip, timezone, internet service provider, etc. using an IP. ')
    print(Fore.RED + 'The developer is not liable for any damage caused with this if used wrong.' + Style.RESET_ALL) 
    print('')
    x = input('Press Enter to Start!')

    if x == '':
        os.system('cls')
        IP = input(Fore.RED + 'ENTER TARGET IP: ' + Style.RESET_ALL)
        r = requests.get(f'http://ip-api.com/json/{IP}')
        data = r.json()
        print
        print(Fore.GREEN + 'Data is processing...' + Style.RESET_ALL)
        print(Fore.GREEN + 'Data has been collected...' + Style.RESET_ALL)
        print(Fore.GREEN + 'Here is the data retrieved: ' + Style.RESET_ALL)
        print('')
        print(Fore.GREEN + '')
        print(f"The status of tracking this IP was a {data['status']}!")
        print(f"Country: {data['country']}")
        print(f"Region: {data['regionName']}")
        print(f"City: {data['city']}")
        print(f"Zip: {data['zip']}")
        print(f"Timezone: {data['timezone']}")
        print(f"ISP: {data['isp']}")
        print(f"IP: {data['query']}" + Style.RESET_ALL)
        print('')
        pause = input('Press Enter to Proceed...' + Style.RESET_ALL)
