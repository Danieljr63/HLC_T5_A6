def romano(numero):
    numero = int(input("Introduce un número para pasar a romano: "))
    romanos = {
        1: "I",
        4: "IV",
        5: "V",
        9: "IX",
        10: "X",
        40: "XL",
        50: "L",
        90: "XC",
        100: "C",
        400: "CD",
        500: "D",
        900: "CM",
        1000: "M"
    }
    resultado = ""
    for valor, letra in sorted(romanos.items(), reverse=True):
        while numero >= valor:
            resultado += letra
            numero -= valor
    return resultado

print(romano(1))