def run(input_path: str, replacements: str, output_path: str) -> None:
    aux = replacements.split('|')
    changes = []
    for r in aux:
        t = list(r)
        changes.append(t)
    with open(input_path, 'r') as f, open(output_path, 'w') as f2:
        for line in f:
            lista = list(line.strip())

            for i,letra in enumerate(lista):
                for c in changes:
                    if letra == c[0]: lista[i] = c[1]

            nueva_linea = ''.join(lista)  + '\n'
            f2.write(nueva_linea)
        



# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor
    run('ejercicios/ficheros/replace-chars/data/noticia.input.txt',
            'aA|eE|iI|oO|uU',
            'ejercicios/ficheros/replace-chars/data/noticia.output.1.txt')
    vendor.launch(run)
