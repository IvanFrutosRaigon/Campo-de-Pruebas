def is_palindrome(cadena:str)->bool:
    lista_letras = list(cadena)
    lista = [l.lower() for l in lista_letras if l!=' ']

    umbral = len(lista)//2 +1
    # [a,n,a,l,a,v,a,l,a,n,a]
    primera_mitad = lista[:umbral]
    segunda_mitad = list(reversed(lista[umbral-1:]))

    return primera_mitad==segunda_mitad

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor
    is_palindrome('ana lava lana')
    vendor.launch(is_palindrome)
