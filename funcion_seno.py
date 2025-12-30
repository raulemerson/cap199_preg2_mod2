# Código Python completo de la primera solución
import numpy as np
import matplotlib.pyplot as plt

def visualizar_seno_y_tangentes():
    x = np.linspace(-0.5, 5, 400)
    y = np.sin(x)

    puntos = [0, np.pi/4, np.pi/2, np.pi, 3*np.pi/2]

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, color="black", linewidth=2, label="f(x) = sin(x)")

    colores = ["red", "green", "blue", "magenta", "purple"]

    for a, c in zip(puntos, colores):
        pendiente = np.cos(a)
        tangente = np.sin(a) + pendiente * (x - a)

        plt.plot(x, tangente, color=c, linewidth=2)
        plt.scatter(a, np.sin(a), color=c, zorder=5)

    plt.axhline(0)
    plt.axvline(0)
    plt.grid(True)
    plt.title("Rectas tangentes a f(x) = sin(x)")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.show()

visualizar_seno_y_tangentes()
