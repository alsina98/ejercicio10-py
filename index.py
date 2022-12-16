from io import open

archivo_texto = open('archivo.txt', 'w')

frase = "Aprendiendo a programar con Python para hacer aplicaciones o web"

archivo_texto.write(frase)

archivo_texto.close()

archivo_texto = open('archivo.txt', 'r')

texto = archivo_texto.read()

archivo_texto.close()

print(texto)