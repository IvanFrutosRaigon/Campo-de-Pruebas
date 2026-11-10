def run(cinfo: str) -> dict:
    lista_ciudades = cinfo.split(';')
    cities = {}
    for c in lista_ciudades:
        l = c.split(':')
        l[1].replace('_','')
        population = int(l[1])
        cities[l[0]] = population

    return cities


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
