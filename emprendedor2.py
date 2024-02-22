#variables de solicitud de datos
precio_suscripcion = float(input("Ingrese el precio de la suscripcion, (Recuede el dato debe ser numerico): "))
numero_usuario_normal = float(input("Ingrese el numero de ususario normal, (Recuede el dato debe ser numerico): "))
numero_usuario_premium = float(input("Ingrese el numero de ususario premium, (Recuede el dato debe ser numerico): "))
gastos_totales = float(input("Ingrese el gasto total, (Recuede el dato debe ser numerico): "))

#calculo de utilidades
utilidad_usuario_premium = precio_suscripcion * 1.5 * numero_usuario_premium
utilidades = (precio_suscripcion * numero_usuario_normal) + utilidad_usuario_premium - gastos_totales

#resultado que se muestra en consola
print(f"Utilidades: {utilidades}" )