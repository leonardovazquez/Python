# ---------------------------------------

#      Main Program (ESP32) for
#   Iot Aplication (using MQTT Protocol)

# ---------------------------------------

#  Libraries
import time
import network
from   machine import Pin, ADC,  PWM, Timer 
from   dht import DHT11
from   time import sleep_ms
from   neopixel import NeoPixel
from   umqtt.robust import MQTTClient
from   functions import *

#  Set Pins I/O
adc    = ADC(Pin(35), atten=ADC.ATTN_11DB)
butt_1 = Pin(33, Pin.IN, Pin.PULL_UP)
butt_2 = Pin(26, Pin.IN, Pin.PULL_UP)
dhta   = DHT11(Pin(32))
np     = NeoPixel(Pin(27), 3)
led1   = Pin(0, Pin.OUT)
led2   = Pin(2, Pin.OUT)
led3   = Pin(15, Pin.OUT)
servo  = PWM(Pin(14), freq=50)

#  Initial Conditions
servo.duty(51)
np[0]   = (0,0,0)
np[1]   = (0,0,0)
np[2]   = (0,0,0)
state_1 = False
state_2 = False
last_butt_1 = False
last_butt_2 = False

#  Network Connection 
time.sleep(4)
wlan = network.WLAN(network.STA_IF)

if not wlan.active():
    wlan.active(True)

if not wlan.isconnected():
    wlan.connect("FIWIFI", "")
    print("Conectando...")
    while not wlan.isconnected():
        sleep_ms(1000)

config = wlan.ifconfig()
print(f"Conected with {config[0]} ip")

def callback(topic, msg):
    print(f"{msg.decode()} from {topic.decode()}")
    topic_2  = topic.decode()
    msg_2 = msg.decode()
    #if (topico.find("vazquez") != -1):
    if (topic_2.find("led") != -1 ): 
        LEDs(msg_2,topic_2)
    elif (topic_2.find("servo") != -1 ):
        SERVO(msg_2)
    elif (topic_2.find("neopixel") != -1 ):
        NEOPIXEL(msg_2,topic_2)

client = MQTTClient("leo", "livra.local", port=1884)
print("Conecting with a MQTT server...")
client.set_callback(callback)
client.connect()
client.subscribe("/vazquez/#")
print("Conected")

#  Timer
timer=Timer(-1) #create an instance of Timer method
timer.init(period=5000, mode=Timer.PERIODIC, callback=lambda t: temp_hum())

#  Buttons Function
def buttons():
    global  last_butt_1, last_butt_2, state_1, state_2
    now_butt_1 = not butt_1.value()
    if now_butt_1 != last_butt_1 and now_butt_1:
        state_1 = not state_1
        pote_adc = int(adc.read())
        client.publish("/vazquez/entradas/nivel",str(pote_adc))
    last_butt_1 = now_butt_1
    
    now_butt_2 = not butt_2.value()
    if  now_butt_2 != last_butt_2 and  now_butt_2:
        state_2 = not state_2
        client.publish("/vazquez/entradas/alarma","1")
    last_butt_2 =  now_butt_2

# Temp & Hum Measure
def temp_hum():
    dhta.measure()
    temp = int(dhta.temperature())
    hum = int(dhta.humidity())
    client.publish("/vazquez/entradas/temperatura",str(temp))
    client.publish("/vazquez/entradas/humedad",str(hum))

#  NeoPixel Function
def NEOPIXEL(msg,topic):
    i = int(topic[-1])
    values= msg.split(",")
    np[i] = (int(values[0]), int(values[1]), int(values[2]))
    np.write()

#  LEDs Function
def LEDs(msg,topic):
    print(msg,topic)
    i = int(topic[-1])
    j = int(msg)
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

#   Servo Function
def SERVO(msg):
    i = int(mapeo(int(msg),10,170,54,99))
    #print(i)
    servo.duty(i)

#  Main Program
while True:
    buttons()
    client.check_msg()
    sleep_ms(10)
client.disconnect()