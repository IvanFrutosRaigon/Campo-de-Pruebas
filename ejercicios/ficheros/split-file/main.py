def run(input_path: str, ranges: str) -> None:
    # '1-1,3-5,10-12',
    aux = ranges.split(',')
    list_ranges = []
    for a in aux:
        l_aux = [int(a) for a in a.split('-')]
        list_ranges.append(l_aux)

    with open(input_path, 'r') as f:
        lista_fichero = [linea.strip() for linea in f]
        for r in list_ranges:
            ruta = 'data/quijote.output.' + str(r[0]) + '-' + str(r[1])
            with open(ruta, 'w') as f2:
                lista_filtrada = lista_fichero[r[0] -1: r[1]]

                for line in lista_filtrada:
                    l = line + '\n'
                    f2.write(l)




# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
