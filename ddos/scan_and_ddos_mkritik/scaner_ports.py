import socket # для соединения
import threading
import os
from colorama import init, Fore, Back, Style
# несколько цветов
init()
GREEN = Fore.GREEN
RESET = Fore.RESET
BLUE= Fore.BLUE
RED = Fore.RED
GRAY = Fore.LIGHTBLACK_EX
port ={}
def start_scan():
# адрес сайта вводит пользователь
    host = str(input(f'{GREEN}[{RESET} {RED}====>{RESET} {GREEN}]{RESET} {BLUE}IP/HOST цели : {RESET} '))
    try:
        if socket.gethostbyname(host) == host:
            print(f'{GREEN}[{RESET} {RED}Info{RESET} {GREEN}]{RESET} {RED}ЦЕЛЬ ВЫБРАНА{RESET} {BLUE}>{RESET}{host.format(host)}{BLUE}<{RESET}')
            pass
        elif socket.gethostbyname(host) != host:
            print(f'{GREEN}[{RESET} {RED}Info{RESET} {GREEN}]{RESET} {RED}ЦЕЛЬ ВЫБРАНА > {RESET}{host.format(host)}')
            pass
    except socket.gaierror:
        print("Вы что то ввели не так")

    print(f'{GREEN}Порт можно указывать либо{RESET} {RED}один{RESET} {GREEN}либо через {RESET}{RED}-{RESET}\n{GREEN}Пример : {RESET}{RED}1-65536{RESET} {GREEN}или {RESET}{RED}443{RESET}\n{GREEN}Если вы просто нажмёте {RESET}{RED}Enter {GREEN}то будут сканироваться {RESET}{RED}все порты{RESET}' )
    try:
        port = input(f'{GREEN}[{RESET} {RED}====>{RESET} {GREEN}]{RESET} {BLUE}Порт цели : {RESET} ')
        if ("-" in port):
            port = port.split("-")
            end = int(port[1])
            start = int(port[0])
        elif int(port) > 0 and int(port) <= 65536:
            start = int(port)
            end = int(port)+1
        else:
            print(f'Взято значение по умаолчанию')
            start = 1
            end = 65536
    except:
        print(f'Взято значение по умаолчанию')
        start = 1
        end = 65536

    def is_port_open(port):
        """
        определяем, имеет ли `хост` открытый `порт`
        """
        # создаем новый сокет
        s = socket.socket()
        try:
            # попытка присоединения к хосту через порт
            s.connect((host, port))
            # установите таймаут для чуть большей скорости
            s.settimeout(0.5)
            print(f"{GREEN}[{RESET}{RED}+{RESET}{GREEN}]{RESET} {RED}{host}:{port} {RESET}{GREEN}открыт {RESET}")

        except:
            return False
        else:
            return True

    r = start
    for port in range(r, end):
        try:
            t = threading.Thread(target=is_port_open, kwargs={'port':port})
            r += 1
            t.start()
        except KeyboardInterrupt:
            os._exit(0)
        except Exception as e:
            is_port_open(r)
            r += 1
