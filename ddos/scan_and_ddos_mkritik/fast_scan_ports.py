import threading
import socket
import os
import subprocess
import sys
import psutil
import time
from colorama import Fore, Back, Style
print("""
Для данного сканирования у вас должен быть установлен Nmap
""")
target = str(input("[ ====> ] IP/HOST цели : "))
# Чтобы использовать инструмент на постоянной основе нужно сделать его удобным, добавим первые аргументы и получим их значения:
# if target != "" :
#     # indexoftarget=sys.argv.index(target)
#     target=sys.argv[str(target)]
# else:
#     print("Target is not specified, see --help")
#     exit()
# def main():
try:
    if socket.gethostbyname(target) == target:
        print("[", Fore.LIGHTCYAN_EX+"Info"+Style.RESET_ALL, "] ЦЕЛЬ ВЫБРАНА > "+target.format(target))
        pass
    elif socket.gethostbyname(target) != target:
        print("[", Fore.LIGHTCYAN_EX+"Info"+Style.RESET_ALL, "] ЦЕЛЬ ВЫБРАНА > "+target.format(target))
        pass
except socket.gaierror:
    print("Вы что то ввели не так")
# if("--help" in sys.argv):
#     print("Usage: python3 rollerscan.py --target [target]")
#     print("Additional flags:")
#     print("--virtual-hosts (-vh) — try to find virtual hosts")
#     print("--vuln (-v) — find possible exploits")
#     print("--censys (-c) — use censys to search for additional info.")
#     print("--port (-p) — specify port range for scan, by default 1-60 000")
#     exit()
#
# if("--port" in sys.argv):
#     indexofport=sys.argv.index("--port")
#     port=sys.argv[indexofport+1]
# def data_taget():

print("""
Порт можно указывать либо один либо через -
Пример 1-65536 или 443
Если вы просто нажмёте Enter 
то будут сканироваться все порты
""")
try:
    port = str(input("[ ====> ] Порт цели : "))
    if ("-" in port):
        port = port.split("-")
        end = int(port[1])
        print(end)
        start = int(port[0])
        print(start)
    else:
        print(f'Взято значение по умаолчанию')
        start = 1
        end = 65536
except:
    pass



# elif("-p" in sys.argv):
#     indexofport=sys.argv.index("-p")
#     port=sys.argv[indexofport+1]
#     if("-" in port):
#         port=port.split("-")
#             end=int(port[1])
#             start=int(port[0])
# else:
#     start=1
#     end=65536

response=os.system("ping -c 1 " + target)
processes=[]
nmapdone={}

if (response==0):
    print("[", Fore.LIGHTCYAN_EX+"Info"+Style.RESET_ALL, "]", Fore.YELLOW+target+Style.RESET_ALL, Fore.GREEN+"Активен"+Style.RESET_ALL)
if (response!=0):
    print("[", Fore.LIGHTCYAN_EX+"^"+Style.RESET_ALL, "]", Fore.LIGHTYELLOW_EX+target+Style.RESET_ALL, Fore.RED+"Выключен"+Style.RESET_ALL)
    choise=input("Хотите ли вы продолжать считать, что цель помечена как выключена? Y/N: ")
    if(choise=="Y" or choise=="y" or choise=="Да" or choise=="да" or choise=="дА" or choise=="д" or choise=="Д"):
        pass
    else:
        print(Fore.RED+"Цель выключена")
        exit()


print("[", Fore.LIGHTCYAN_EX+"Info"+Style.RESET_ALL, "]", Fore.BLUE+"Старт сканирования!"+Style.RESET_ALL)
start_time=time.time()
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print (s)
s.settimeout(0.5)

def portscan(port):
    try:
        con = s.connect((target, port))
        print(type(con))

        print('[', Fore.LIGHTCYAN_EX+'*'+Style.RESET_ALL,']',Fore.YELLOW+f'''Port: {str(port)}'''+Style.RESET_ALL, Fore.GREEN+"is opened."+Style.RESET_ALL)
        process=subprocess.Popen(f'''nmap -sV {target} -p {port}''', shell=True)
        processes.append(process.pid)
        con.close()
    except Exception as e:
        print(f'[{Fore.LIGHTCYAN_EX}Info{Style.RESET_ALL}] port > {str(Fore.RED + str(port) + Style.RESET_ALL)} закрыт')
        pass


r = start
for r in range(start, end):
    try:
        t = threading.Thread(target=portscan, kwargs={'port':r})
        r += 1
        t.start()
    except KeyboardInterrupt:
        os._exit(0)
    except Exception as e:
        portscan(r)
        r += 1

def checkprocess():
    for proc in processes:
        if psutil.pid_exists(proc):
            nmapdone[proc]='False'
        else:
            nmapdone[proc]='True'

while 'False' in nmapdone.values():
    checkprocess()

threadslist=int(threading.active_count())
while threadslist>1:
    threadslist=int(threading.active_count())
    time.sleep(0.000001)

print(Fore.BLUE+"Время сканирования составило:"+Style.RESET_ALL, Fore.GREEN+str(round(time.time()-start_time))+Style.RESET_ALL, "сек")
