def run(input_path: str, output_path: str) -> None:
    with open(input_path, 'r') as f, open(output_path, 'w') as f2:
        for line in f:
            lista = list(line.strip())
            dicc = {}
            for letra in lista:
                if letra not in dicc:
                    dicc[letra] = 1
                else: dicc[letra] = dicc[letra] + 1

            for c,v in dicc.items():
                histo = c + ' ' + ('█'*v) + ' ' + str(v) + '\n'
                f2.write(histo)


    


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor
    run('ejercicios/ficheros/histogram-txt/data/data1.input.txt', 'ejercicios/ficheros/histogram-txt/data/data1.output.txt')
    vendor.launch(run)
