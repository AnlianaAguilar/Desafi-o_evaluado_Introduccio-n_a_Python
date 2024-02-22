import math

#variables de solicitud de datos
precio_suscripcion = float(input("Ingrese el precio de la suscripcion, (Recuede el dato debe ser numerico): "))
numero_usuario_normal = float(input("Ingrese el numero de ususario normal, (Recuede el dato debe ser numerico): "))
gastos_totales = float(input("Ingrese el gasto total, (Recuede el dato debe ser numerico): "))
utilidades_anterior = float(input("Ingrese las utilidades del año anterior: "))

#calculo de utilidades
utilidades_actuales = (precio_suscripcion * numero_usuario_normal) - gastos_totales

razon = utilidades_actuales/utilidades_anterior

#resultado que se muestra en consola
print(f"La razon es: {razon:.2f}")