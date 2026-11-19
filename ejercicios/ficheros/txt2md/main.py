def run(input_path: str, output_path: str) -> None:
    with open(input_path, 'r') as f, open(output_path, 'w') as f2:
        for linea in f:
            tabuladores = 0
            if linea.startswith('\t'):
                tabuladores = linea.count('\t')
            almohadillas = tabuladores + 1
            frase = '#'*almohadillas + ' ' +linea.lstrip('\t')
            f2.write(frase)

            



# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
