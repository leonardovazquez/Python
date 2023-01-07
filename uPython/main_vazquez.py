# TP2: HANDs ON IoT
# VAZQUEZ LEONARDO DAVID
# 2022

# Librerias
from machine import Pin, ADC,  PWM, Timer 
from dht import DHT11
import time
from time import sleep_ms
from neopixel import NeoPixel
import network
from umqtt.robust import MQTTClient

time.sleep(4)

# Seteo de pines y variables
adc = ADC(Pin(35), atten=ADC.ATTN_11DB)
button_1 = Pin(33, Pin.IN, Pin.PULL_UP)
button_2 = Pin(26, Pin.IN, Pin.PULL_UP)
dhta = DHT11(Pin(32))
np = NeoPixel(Pin(27), 3)
led1 = Pin(0, Pin.OUT)
led2 = Pin(2, Pin.OUT)
led3 = Pin(15, Pin.OUT)
servo = PWM(Pin(14), freq=50)
servo.duty(51)
np[0] =(0,0,0)
np[1]=(0,0,0)
np[2]=(0,0,0)

estado1 = False
ultimo_estado_boton1 = False
estado2 = False
ultimo_estado_boton2 = False



# Lectura de Potenciometro y Envio de Alarma 
def botones():
    global  ultimo_estado_boton1, ultimo_estado_boton2, estado1, estado2
    estado_boton1 = not button_1.value()
    if estado_boton1 != ultimo_estado_boton1 and estado_boton1:
        estado1 = not estado1
        pote_adc = int(adc.read())
        cliente.publish("/vazquez/entradas/nivel",str(pote_adc))
    ultimo_estado_boton1 = estado_boton1
    
    estado_boton2 = not button_2.value()
    if estado_boton2 != ultimo_estado_boton2 and estado_boton2:
        estado2 = not estado2
        cliente.publish("/vazquez/entradas/alarma","1")
    ultimo_estado_boton2 = estado_boton2 

# Función de lectura de temperatura y humedad
def temp_hum():
    dhta.measure()
    temp = int(dhta.temperature())
    hum = int(dhta.humidity())
    cliente.publish("/vazquez/entradas/temperatura",str(temp))
    cliente.publish("/vazquez/entradas/humedad",str(hum))

#Funcion del neopixel
def NEOPIXEL(mensaj,topic):
    i = int(topic[-1])
    values= mensaj.split(",")
    np[i] = (int(values[0]), int(values[1]), int(values[2]))
    np.write()

#Funcion de lectura de leds
def LEDs(mensaj,topic):
    print(mensaj,topic)
    i = int(topic[-1])
    j = int(mensaj)
    if (i==1):
        led1.value(j)
    elif (i==2):
        led2.value(j)
    elif (i==3):
        led3.value(j)
    
# Maping function
def mapeo(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin
    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)
    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)

#Funcion de posicion del servo
def SERVO(mensaj):
    i = int(mapeo(int(mensaj),10,170,54,99))
    print(i)
    servo.duty(i)

# REDES 
wlan = network.WLAN(network.STA_IF)
if not wlan.active():
    wlan.active(True)

if not wlan.isconnected():
    wlan.connect("FIWIFI", "")

    print("Conectando...")
    while not wlan.isconnected():
        sleep_ms(1000)

config = wlan.ifconfig()
print(f"Conectado con ip {config[0]}")

def callback(topic, msg):
    print(f"Llegó {msg.decode()} de {topic.decode()}")
    topico = topic.decode()
    mensaje=msg.decode()
    #if (topico.find("vazquez") != -1):
    if (topico.find("led") != -1 ):
        LEDs(mensaje,topico)
    elif (topico.find("servo") != -1 ):
        SERVO(mensaje)
    elif (topico.find("neopixel") != -1 ):
        NEOPIXEL(mensaje,topico)

cliente = MQTTClient("leo", "livra.local", port=1884)
print("Conectando a servidor MQTT...")
cliente.set_callback(callback)
cliente.connect()
cliente.subscribe("/vazquez/#")
print("Conectado")


# Timer
timer=Timer(-1) #create an instance of Timer method
timer.init(period=5000, mode=Timer.PERIODIC, callback=lambda t: temp_hum())

# PROGRAMA PRINCIPAL
while True:
    botones()
    cliente.check_msg()
    sleep_ms(10)
    
cliente.disconnect()



