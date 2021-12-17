import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from scipy import signal


RC = 2.2*10**(-5)
KC = 3.2
KO = 4775
K = 1/KO

wn2 = (RC*KC*KO)
e_rara = 0.7
e_rara_2=0.1


sys1 = signal.lti([K], [RC/(KC*KO), 1/(KC*KO) , 1]) # Creamos el sistemacon erara = 0.89
sys2 = signal.lti([K], [wn2, e_rara*2/(wn2**(0.5)) , 1]) # Creamos el sistema
sys3 = signal.lti([K], [wn2, e_rara_2*2/(wn2**(0.5)) , 1]) # Creamos el sistema

w1, mag1, phase1 = signal.bode(sys1) # Diagrama de bode: frecuencias, magnitud y fase
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 6))
w2, mag2, phase2 = signal.bode(sys2) # Diagrama de bode: frecuencias, magnitud y fase
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 6))
w3, mag3, phase3 = signal.bode(sys3) # Diagrama de bode: frecuencias, magnitud y fase
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 6))
ax1.semilogx(w1, mag1) # Eje x logarítmico
ax2.semilogx(w1, phase1) # Eje x logarítmico
ax1.semilogx(w2, mag2) # Eje x logarítmico
ax2.semilogx(w2, phase2) # Eje x logarítmico
ax1.semilogx(w3, mag3) # Eje x logarítmico
ax2.semilogx(w3, phase3) # Eje x logarítmico
plt.show()

t, y1 = signal.step2(sys1) # Respuesta a escalón unitario
t, y2 = signal.step2(sys2) # Respuesta a escalón unitario
t, y3 = signal.step2(sys3) # Respuesta a escalón unitario

#plt.plot(t, (110*10**3) * y1,"r",t,(110*10**3) * y2,"b",t,(110*10**3) * y3,"g") # Equivalente a una entrada de altura 2250


plt.plot(t, (110*10**3)*y1, color="blue", linewidth=2, linestyle="-", label="e = 0.89")
plt.plot(t, (110*10**3)*y2, color="red",  linewidth=2, linestyle="-", label="e=0.7")
plt.plot(t, (110*10**3)*y3, color="green",  linewidth=2, linestyle="-", label="e=0.1")

plt.legend(loc='upper right')
plt.xlabel('Tiempo  t(s)')
plt.ylabel('Salida Vd(V)')
plt.show()