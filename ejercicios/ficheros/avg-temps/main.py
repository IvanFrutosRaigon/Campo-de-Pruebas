def run(input_path: str, output_path: str) -> None:
    with open(input_path, 'r') as f, open(output_path, 'w') as f2:
        for linea in f:
            temps = linea.split(',')
            temps_int = [int(t) for t in temps]
            total = 0
            for t in temps_int:
                total +=t
            media = round(total/31, 2)
            media = str(media) + '\n'
            f2.write(media)




# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor
    run('ejercicios/ficheros/avg-temps/data/temps1.input.dat','ejercicios/ficheros/avg-temps/data/temps1.expected.dat')
    vendor.launch(run)
