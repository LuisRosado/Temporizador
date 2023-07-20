import os
import time

def temp(n):
    for i in range(0,n+1):
        os.system('cls')
        print(n-i)
        time.sleep(1)

num = int(input('Ingrese un numero (En segundos): '))
temp(num)
