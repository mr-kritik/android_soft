import checking as chek
import os, sys, codecs

# Импорт и установка библиотек если их нет

try:
    import socks, requests, wget, cfscrape, urllib3, socket, threading, random, re, urllib, bs4, threading, keyboard
except:
    if sys.platform.startswith("linux"):
        os.system("pip3 install -r requirements.txt")
        os.system(
            "pip3 install pysocks pysocks requests wget cfscrape urllib3 scapy bs4 keyboard")
    elif sys.platform.startswith("freebsd"):
        os.system("pip3 install -r requirements.txt")
        os.system(
            "pip3 install pysocks pysocks requests wget cfscrape urllib3 scapy bs4 keyboard")
    else:
        os.system("python -m pip install --upgrade pip")
        os.system(
            "pip install pysocks pysocks requests wget cfscrape urllib3 scapy bs4 keyboard")


print("""
Варианты атак :
1)ddos от Tawkun
2)ddos от Zeus
3)ddos (лёгкий) от mr.kritik
4)ddos от No Name
5)Сканирование открытых портов
0) Выход
""")

def vivod(numb):
    if numb == 1:
        print("""
                    1)Получить прокси (https/http)
                    2)Получить прокси (Socks)
                    3)Запустить DDos
                    """)
        kat = chek.is_number(input("Выберите что вы хотите (Просто введите цифру): "))
        kategori = int(kat)
        if kategori == 1:
            from ddos.TawkunDoS.TawkunProxy import start_tawkunproxi
            start_tawkunproxi()
        elif kategori == 2:
            from ddos.TawkunDoS.TawkunSOCKS import start_tawkunsocks
            start_tawkunsocks()
        elif kategori == 3:
            from ddos.TawkunDoS.Tawkun import starturl
            starturl()
    if numb == 2:
        from ddos.Zeus.ZeusCloryV2 import start_zeus
        start_zeus()
    if numb == 3:
        from ddos.mini_ddos.mini_ddos import RUN
        RUN()
    if numb == 4:
        from ddos.DDoS.ddos import start
        start()
    if numb == 5:
        from ddos.scan_and_ddos_mkritik.scaner_ports import start_scan
        start_scan()
    if numb == 0:
        print(f'Досвидание')


if __name__ == '__main__':
    chislo = chek.is_number(input('Выбери через что будешь производить атаку (Просто введите цифру) : '))
    vivod(int(chislo))


