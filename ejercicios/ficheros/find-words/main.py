
def run(input_path: str, target_word: str) -> list:
    matches = []
    fronteras = " .,:;()'¡!\n"

    with open(input_path, 'r') as f:
        for num_linea, linea in enumerate(f, start=1):

            linea_lower = linea.lower()
            target_lower = target_word.lower()

            posicion = 0

            while True:
                # Buscar la siguiente aparición
                indice = linea_lower.find(target_lower, posicion)

                # Si no quedan coincidencias, terminar
                if indice == -1:
                    break

                # Comprobar el carácter anterior y posterior
                anterior = indice == 0 or linea_lower[indice - 1] in fronteras
                siguiente = indice + len(target_lower) == len(linea_lower) or linea_lower[indice + len(target_lower)] in fronteras

                # Si es una palabra completa, guardar su posición
                if anterior and siguiente:
                    matches.append((num_linea, indice + 1))

                # Continuar buscando desde la siguiente posición
                posicion = indice + 1

    return matches



# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor
    run('ejercicios/ficheros/find-words/data/help.txt', 'round')
    vendor.launch(run)
