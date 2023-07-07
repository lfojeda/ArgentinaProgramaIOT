# Luis Fernando Ojeda  2023
 
from machine import Pin
import time

print("Esperando pulsador")

sw = Pin(23, Pin.IN)
led = Pin(2, Pin.OUT)

contador=0
while True:
    if sw.value():
        contador+=1
        print(contador)     
    else:
        if contador>=3:
            print("Pulsacion larga")
        if 1<=contador<=2:
            print("Pulsacion corta")  
        contador=0    
    time.sleep_ms(200)
