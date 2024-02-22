#impoto math
import math

# variables de entrada de datos
radio = float(input("Ingrese el radio en Kilometros, (recuerde que debe ingresar datos numericos): "))
constante_G = float(input("Ingrese la contante G, (Recuerde que ql dato solisitado es numerico): ")) 
velocidad_escape = ((radio * 1000) * constante_G)
print(f"La velocidad de Escape es: {math.sqrt(2 * velocidad_escape)} [m/s]")