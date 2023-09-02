import scapy.all as scapy
import argparse
from colorama import Fore, Style  # Importa la biblioteca colorama

# Función para descifrar una cadena utilizando el cifrado César
def cesar_decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                decrypted_char = chr(((ord(char) - ord('a') - shift_amount) % 26) + ord('a'))
            else:
                decrypted_char = chr(((ord(char) - ord('A') - shift_amount) % 26) + ord('A'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

# Parsea el nombre del archivo pcapng desde la línea de comandos
parser = argparse.ArgumentParser(description="Descifra un archivo pcapng usando cifrado César.")
parser.add_argument("pcap_file", help="Nombre del archivo pcapng")
args = parser.parse_args()

# Abre el archivo pcapng para leer paquetes
packets = scapy.rdpcap(args.pcap_file)

# Recorre los paquetes y extrae la carga útil de datos
data_string = ""
for packet in packets:
    if scapy.ICMP in packet and packet[scapy.ICMP].type == 8 and packet[scapy.ICMP].code == 0:
        # Obtiene la carga útil de datos del paquete ICMP
        payload = packet[scapy.ICMP].load

        # Extrae el valor hexadecimal del primer byte (carácter)
        hex_value = payload[0:2].hex()

        # Agrega el carácter al string
        data_string += bytes.fromhex(hex_value).decode('utf-8')

# Imprime el string recuperado
print("String recuperado del archivo pcapng:", data_string)

# Lista de frecuencias de letras en español (de la más frecuente a la menos frecuente)
frequencies = "aeoirlntscudpgmbvhqjzxfykw"

best_combination = data_string
best_score = 0

# Genera todas las combinaciones posibles usando el cifrado César
for shift in range(26):
    decrypted_text = cesar_decrypt(data_string, shift)
    score = sum(decrypted_text.count(char) * (26 - frequencies.index(char) if char in frequencies else 0) for char in decrypted_text)
    
    # Compara el puntaje de la combinación actual con el mejor puntaje encontrado hasta ahora
    if score > best_score:
        best_combination = decrypted_text
        best_score = score

# Genera todas las combinaciones posibles y muestra la palabra más probable en verde
for shift in range(26):
    decrypted_text = cesar_decrypt(data_string, shift)
    
    # Si la combinación actual es la más probable, imprímela en verde
    if decrypted_text == best_combination:
        print(Fore.GREEN + f"{shift}: {decrypted_text}" + Style.RESET_ALL)
    else:
        print(f"{shift}: {decrypted_text}")