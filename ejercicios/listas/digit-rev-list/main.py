def run(number: int) -> list:
    cadena = str(number)
    lista_cadena = list(cadena)
    lista = reversed(lista_cadena)
    rev_digits = [int(number) for number in lista]
    return rev_digits


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
