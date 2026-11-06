def run(numbers: str) -> str:
    lista = numbers.split(',')
    del lista[0]
    if len(lista)>0: del lista[-1]
    strip_numbers = ' '.join(lista)
    return strip_numbers


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
