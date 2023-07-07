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
        if contador % 10 == 0:
            led.value(not led.value())
            contador=0
        print(contador)
        time.sleep_ms(200)
