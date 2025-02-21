def palindromo(cadena):
    if len(cadena) < 2:
        return True
    if cadena[0] == cadena[-1]:
        return palindromo(cadena[1:-1])
    return False

print(palindromo("reconocer")) 
print(palindromo("hola")) 