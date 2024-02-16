import numpy as np
import matplotlib.pyplot as plt

# Definir la función que deseas graficar (en este caso, coseno)
def funcion(x):
    return np.cos(x)

# Generar datos para la gráfica
x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = funcion(x)

# Graficar la función
plt.plot(x, y)
plt.title('Gráfico de la función coseno')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()

