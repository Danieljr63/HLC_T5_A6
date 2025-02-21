import random

def generar_contrasena(longitud):
    longitud = int(input("Ingrese la longitud de la contraseña: "))
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"
    contrasena = ""
    for i in range(longitud):
        contrasena += random.choice(caracteres)
    return contrasena

print(generar_contrasena(8))