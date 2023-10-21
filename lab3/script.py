archivo_entrada = 'rockyou.txt'
archivo_salida = 'rockyou_mod.txt'

cont = 0
with open(archivo_entrada, 'r',encoding='utf-8', errors='ignore' ) as entrada, open(archivo_salida, 'w') as salida:
    for linea in entrada: 
        linea = linea.strip()
        if len(linea)>0:
            if linea[0].isdigit()==False: 
                cont += 1
                linea_modificada = linea[0].upper() + linea[1:] + "0"
                salida.write(linea_modificada + '\n')


print ("Contraseñas procesadas:", cont)
print("Contraseñas modificadas y guardadas en", archivo_salida)
