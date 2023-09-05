# Luis Fernando Ojeda - 2023
from machine import Pin, Timer
import dht
import time
import json

sw = Pin(23, Pin.IN)
led = Pin(2, Pin.OUT)
d = dht.DHT22(Pin(25))
print("Esperando la primera pulsación...")
contador = 0
estado = False
temperaturas = []
humedades = []

def registrar(pin):
    global contador, estado
    if sw.value():            
            led.value(True)
            contador += 1
            print(f'Pulsación {contador}')
            d.measure()
            temperatura = d.temperature()
            humedad = d.humidity()
            if contador == 1:
                # Primera pulsación: tomar temperatura y humedad
                print(f'Temperatura: {temperatura}°C, Humedad: {humedad}%')
                temperaturas.append(temperatura)
                humedades.append(humedad)
            elif contador == 2:
                # Segunda pulsación: tomar temperatura y humedad y
                # calcular el promedio y imprimirlo
                print(f'Temperatura: {temperatura}°C, Humedad: {humedad}%')
                temperaturas.append(temperatura)
                humedades.append(humedad)
                if temperaturas and humedades:
                    promedio_temp = sum(temperaturas) / len(temperaturas)
                    promedio_hum = sum(humedades) / len(humedades)
                    print(f'Promedio de Temperatura: {promedio_temp:.2f}°C, Promedio de Humedad: {promedio_hum:.2f}%')
                else:
                    print("No se tomaron lecturas en la primera pulsación.")
                contador = 0
                temperaturas.clear()
                humedades.clear()
            led.value(False)


timer1 = Timer(1)
timer1.init(period=50, mode=Timer.PERIODIC, callback=registrar)

while True:
    time.sleep(1)