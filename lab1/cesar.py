import sys

def cifrar_cesar(texto, corrimiento):
    resultado = ""
    
    for caracter in texto:
        if caracter.isalpha():
            if caracter.islower():
                resultado += chr(((ord(caracter) - ord('a') + corrimiento) % 26) + ord('a'))
            elif caracter.isupper():
                resultado += chr(((ord(caracter) - ord('A') + corrimiento) % 26) + ord('A'))
        else:
            resultado += caracter
    
    return resultado

if len(sys.argv) != 3:
    print("Uso: python cifrado_cesar.py <texto> <corrimiento>")
    sys.exit(1)

texto_a_cifrar = sys.argv[1]
corrimiento = int(sys.argv[2])

texto_cifrado = cifrar_cesar(texto_a_cifrar, corrimiento)
print(texto_cifrado)
