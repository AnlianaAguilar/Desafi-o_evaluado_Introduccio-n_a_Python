#variables de solicitud de datos
precio_suscripcion = float(input("Ingrese el precio de la suscripcion, (Recuede el dato debe ser numerico): "))
numero_usuario = float(input("Ingrese el numero de ususario, (Recuede el dato debe ser numerico): "))
gastos_totales = float(input("Ingrese el gasto total, (Recuede el dato debe ser numerico): "))

#calculo de utilidades
utilidades = precio_suscripcion * numero_usuario - gastos_totales

#resultado que se muestra en consola
print(f"Utilidades: {utilidades}" )
