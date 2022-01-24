import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from scipy import signal


RC = 2.2*10**(-5)
KC = 3.2
KO = 4775
K = 1/KO

wn2 = RC*KC*KO
e_1 = 0.7
e_2 = 0.1

# The system
sys1 = signal.lti([K], [RC/(KC*KO), 1/(KC*KO), 1])


sys2 = signal.lti([K], [wn2, e_1 * 2 / wn2 ** 0.5, 1])


sys3 = signal.lti([K], [wn2, e_2 * 2 / wn2 ** 0.5, 1])


# Bode Diagram
# w1, mag1, phase1 = signal.bode(sys1)
# fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 6))
# w2, mag2, phase2 = signal.bode(sys2)
# fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 6))
# w3, mag3, phase3 = signal.bode(sys3)
# fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 6))

# logX axis
# ax1.semilogx(w1, mag1)
# ax2.semilogx(w1, phase1)
# ax1.semilogx(w2, mag2)
# ax2.semilogx(w2, phase2)
# ax1.semilogx(w3, mag3)
# ax2.semilogx(w3, phase3)
# plt.show()


# Transient response
t, y1 = signal.step2(sys1)
t, y2 = signal.step2(sys2)
t, y3 = signal.step2(sys3)


# plt.plot(t, (110*10**3) * y1,"r",t,(110*10**3) * y2,"b",t,(110*10**3) * y3,"g")


plt.plot(t, (110*10**3)*y1, color="blue", linewidth=2, linestyle="-", label="e = 0.89")
plt.plot(t, (110*10**3)*y2, color="red",  linewidth=2, linestyle="-", label="e=0.7")
plt.plot(t, (110*10**3)*y3, color="green",  linewidth=2, linestyle="-", label="e=0.1")

plt.legend(loc='upper right')
plt.xlabel('Time  t(s)')
plt.ylabel('Out Vd(V)')
plt.show()
