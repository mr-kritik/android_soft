
class info:
    def what_to_ddos():
        wtd = input('Что делать с DDoS?\n')
        return wtd
    def get_port():
        port = int(input("Выберите, хотите ли вы указать порт самостоятельно (1) или сканировать порты(2)\n"))
        if port == 1:
            port = int(input("Введите свой порт...\n"))
        else:
            pass
        return port

    def h_many_thr():
        num_of_threads = int(input("Сколько потоков вы бы хотели?"))
        return num_of_threads