import os
import time
import json
import requests
import colorama

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
    print(logo)
    os.system('title Orbit IP - by ItsBr0dyyDev')
    x = input('Press Enter to Start!')

    if x == '':
        os.system('cls')
        IP = input('ENTER TARGET IP: ')
        r = requests.get(f'http://ip-api.com/json/{IP}')
        data = r.json()
        print
        print('Data is processing...')
        print('Data has been collected...')
        print('Here is the data: ')
        print('')
        print('IP Results\n')
        print(f"The status of tracking this IP was a {data['status']}!")
        print(f"Country: {data['country']}")
        print(f"Region: {data['regionName']}")
        print(f"City: {data['city']}")
        print(f"Zip: {data['zip']}")
        print(f"Timezone: {data['timezone']}")
        print(f"ISP: {data['isp']}")
        print(f"IP: {data['query']}")
        print('')
        pause = input('Press Enter to Proceed...')
