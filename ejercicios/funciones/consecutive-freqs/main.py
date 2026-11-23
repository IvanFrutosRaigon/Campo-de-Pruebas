def cfreq(lista, /,salida_cadena = False):
    if not lista:
        return '' if salida_cadena else []
    pares = []
    actual = lista[0]
    frec = 1

    for numero in lista[1:]:
        if numero==actual:
            frec+=1
        else:
            pares.append((actual, frec))
            actual = numero
            frec = 1

    pares.append((actual, frec))

    if salida_cadena:
        return (','.join(f"{num}:{fre}" for num, fre in pares))
    else:
        return pares
                




# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(cfreq)
