def run(number: int) -> str:
    number_str = str(number)
    lista = list(number_str)
    maximo = len(lista)
    #num_comas = len(lista)//3
    reversed_lista = list(reversed(lista))
    i=3
    while i<=maximo:
        reversed_lista.insert(i, ',')
        i += 4

    if reversed_lista[-1] == ',': del reversed_lista[-1]

    lista_def = list(reversed(reversed_lista))
    qnumber = ''.join(lista_def)
    return qnumber


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
