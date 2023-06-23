
#Escribe un programa en la consola de python que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, e imprima por pantalla la frase Tu índice de masa corporal es donde es el índice de masa corporal calculado redondeado con dos decimales. Tienes que subir capturas de pantalla en una carpeta comprimida zip.


peso=(float(input("Ingresa tu peso en KILOS ")))
estatura=(float(input("Escribe tu estaura en METROS ")))
IMC= peso / estatura ** 2

print(f"Your IMC is  {IMC:.2f} ")
