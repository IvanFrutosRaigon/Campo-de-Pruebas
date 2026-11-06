def run(numbers: list[int]) -> list[int]:
    lista = numbers.copy()
    sorted_numbers = []
    while len(lista)>0:
        for l in lista:
            if min(lista)==l:
                sorted_numbers.append(l)
                lista.remove(l)
    return sorted_numbers


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
