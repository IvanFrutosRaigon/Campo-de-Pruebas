import sys

#Script muy básico para comprobar como se tratan los argumentos de la llamada mediante comandos.

numeros = [int(valor) for valor in sys.argv[1:]]

print(sys.argv)
print(sum(numeros)/len(numeros))