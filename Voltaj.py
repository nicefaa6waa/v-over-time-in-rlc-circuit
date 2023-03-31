import numpy as np
import matplotlib.pyplot as plt

R = float(input("Direnç değerini girin (Ohm): "))
L = float(input("İndüktans değerini girin (H): "))
C = float(input("Kapasitans değerini girin (F): "))

# ω0, damped natural frequency
omega = np.sqrt(1 / (L * C))

# ζ, damping ratio
damping_ratio = R / (2 * np.sqrt(L / C))

if damping_ratio > 1:
    print("Sistem aşırı sönümlüdür.")
else:
    wd = omega * np.sqrt(1 - damping_ratio**2)
    phi = np.arctan(-damping_ratio / np.sqrt(1 - damping_ratio**2))

    # A, amplitude of the forced response
    A = 1 / np.sqrt((1 - damping_ratio**2)**2 + (2*damping_ratio*omega)**2)

    t = np.linspace(0, 1, num=1000)
    V = A * np.exp(-damping_ratio*omega*t) * np.sin(wd*t + phi)

    plt.plot(t, V)
    plt.title("Voltajın zamana göre değişimi")
    plt.xlabel("Zaman (s)")
    plt.ylabel("Voltaj (V)")
    plt.show()