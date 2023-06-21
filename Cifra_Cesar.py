from Fuctions import *
import time


while True:
    
    flag = menu()
    time.sleep(1)

    if flag == '1':
        Criptografar()
        time.sleep(1)
    elif flag == '0':
        #tela de bye
        time.sleep(0.5)
        break
