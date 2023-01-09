# Leonardo Vazquez
# blink problem

from machine import Pin, disable_irq, enable_irq
from time import sleep_ms

# Pin definitions

led = Pin(4, Pin.OUT)
button_1 = Pin(33, Pin.IN, Pin.PULL_UP)
button_2 = Pin(34, Pin.IN, Pin.PULL_UP)
estado = False

# Period Functions
Period = 3000 #ms
def Period_function(i):
  global Period
  if (i == Pin(33)):
    Period += 1000
    if Period >= 5000:
      Period = 5000
  elif (i == Pin(34)):
    Period -= 1000
    if Period <= 0:
      Period = 1000
  #print(Period)

# IRQ FUNCTION
def irq_button(pin):
  s = disable_irq()
  global estado, led
  sleep_ms(10)
  if pin.value() == False:
    Period_function(pin)
    #estado = not estado
    #led.value(estado)
  enable_irq(s)



button_1.irq(handler = irq_button, trigger = Pin.IRQ_FALLING)
button_2.irq(handler = irq_button, trigger = Pin.IRQ_FALLING)
# loop

while True:
  print(Period)
  led.on()
  sleep_ms(Period)
  led.off()
  sleep_ms(Period) ####

