import os
import requests
import re
from multiprocessing.pool import ThreadPool
from colorama import Fore

os.system('cls' if os.name == 'nt' else 'clear')

def askdns(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36'
        }
        response = requests.get(f'https://askdns.com/ip/{url}', headers=headers, timeout=30)
        content = response.content.decode()

        if 'Domain Name' in content:
            regex = re.findall('<a href="/domain/(.*?)">', content)

            for domain in regex:
                print(f"[+] GET {len(domain)} DOMAIN FROM {url}")
                with open('rdms.txt', 'a') as f:
                    f.write('http://' + domain + '\n')
        else:
            print("BAD RAP " + url)

    except requests.RequestException as e:
        print(f"Error occurred: {e}")

def rapid(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36'
        }
        response = requests.get(f'https://rapiddns.io/s/{url}?full=1&down=1#result/', headers=headers, timeout=30)
        content = response.content.decode()

        if '<th scope="row ">' in content:
            regex = re.findall('<td>(?!\-)(?:[a-zA-Z\d\-]{0,62}[a-zA-Z\d]\.){1,126}(?!\d+)[a-zA-Z]{1,63}</td>', content)

            for domain in regex:
                cok = domain.replace('<td>', '').replace('</td>', '').replace('ftp.', '').replace('images.', '').replace(
                    'cpanel.', '').replace('cpcalendars.', '').replace('cpcontacts.', '').replace('webmail.', '').replace(
                    'webdisk.', '').replace('hostmaster.', '').replace('mail.', '').replace('ns1.', '').replace(
                    'ns2.', '').replace('autodiscover.', '')

                print(f"\033[32m[+] GET {len(cok)} DOMAIN FROM {url}\033[0m\n")
                with open('rdms.txt', 'a') as f:
                    f.write('http://' + cok + '\n')
        else:
            print("\033[31mNOT FOUND\033[0m")

    except requests.RequestException as e:
        print(f"Error occurred: {e}")

def revip(url):
    try:
        rapid(url)
        askdns(url)
    except Exception as e:
        print(f"Error occurred: {e}")

def Main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.RED + r'''
   =======================================================================
               SICARIOS Reverse Shoot - 2023
   =======================================================================
    ''' + Fore.RESET)
    print("\033[35m Pwn by  | SICARIO\033[0m")

    try:
        list_file = input("\033[95mYOUR LIST PLEASE:\033[0m")
        url_list = open(list_file, 'r').read().splitlines()
        THREAD = input("THREAD (for average internet between 50 to 1000): ")

        with ThreadPool(int(THREAD)) as pp:
            pr = pp.map(revip, url_list)

    except KeyboardInterrupt:
        print("\nKeyboard Interrupt! Exiting...")

    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == '__main__':
    Main()
