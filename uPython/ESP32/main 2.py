# Leonardo Vazquez
# Traffic lights problem

from machine import Pin, disable_irq, enable_irq
from time import sleep_ms

# Pin Definitions
led_red = Pin(15, Pin.OUT)
led_yellow = Pin(2, Pin.OUT)
led_green = Pin(4, Pin.OUT)
button = Pin(33, Pin.IN, Pin.PULL_UP)

# IRQ FUNCTION
def irq_button(pin):
  global flag, state_vector
  s = disable_irq()
  sleep_ms(20)
  if pin.value() == False:
    flag += 1
    if flag == 4:
      flag = 0
    TLF(flag)
  enable_irq(s)


#  TRAFFIC LIGHTS FUNCTION
def TLF(i):
  led_red.value(state_vector[i][0])
  led_yellow.value(state_vector[i][1])
  led_green.value(state_vector[i][2])

# Settings
flag = 0
state_vector = [[1,0,0],[1,1,0],[0,0,1],[0,1,0],[0,0,0]]
button.irq(handler = irq_button, trigger = Pin.IRQ_FALLING)
TLF(flag)

 

