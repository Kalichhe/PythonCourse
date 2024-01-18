
# Pantalla bloqueada

pinSecreto = 1001

intentos = 3

for i in range(1, intentos + 1):
    pinPedido = int(input("Ingresa el pin: "))
    if (pinPedido == pinSecreto):
        print("Login Correcto")
        break
    print(f"Intento Numero {i}")
else:
    print("Se embalo parcero")