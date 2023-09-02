import scapy.all as scapy
import time
import struct
import sys

# Obtiene el string desde la línea de comandos
if len(sys.argv) != 2:
    print("Uso: sudo python3 p2.py <string>")
    sys.exit(1)

data_string = sys.argv[1]

# Dirección de destino (localhost)
dest_ip = "127.0.0.1"

# Identificador ICMP (cambia este valor a uno diferente de 0 y 1)
identifier = 1234

# Inicialización del número de secuencia
sequence_number = 1

# Construye y envía los paquetes
for char in data_string:
    # Obtiene el valor hexadecimal del carácter
    char_hex = hex(ord(char))[2:]

    # Asegura que el valor hexadecimal tenga dos dígitos
    if len(char_hex) == 1:
        char_hex = "0" + char_hex

    # Obtiene el timestamp actual en segundos
    timestamp = int(time.time())

    # Construye el payload de datos de 48 bytes
    payload = bytes.fromhex(char_hex + "01000000000000101112131415161718191a1b1c1d1e1f202122232425262728292a2b2c2d2e2f3031323334353637")

    # Construye el paquete ICMP
    packet = scapy.IP(dst=dest_ip) / scapy.ICMP(type=8, code=0, id=identifier, seq=sequence_number) / payload

    # Agrega el timestamp al campo ICMP usando options
    packet[scapy.ICMP].options = [(32, struct.pack(">I", timestamp))]

    # Envía el paquete
    scapy.send(packet)

    # Incrementa el número de secuencia
    sequence_number += 1

    # Espera un breve momento (puedes ajustar esto según tus necesidades)
    time.sleep(0.1)

print("Paquetes enviados exitosamente.")