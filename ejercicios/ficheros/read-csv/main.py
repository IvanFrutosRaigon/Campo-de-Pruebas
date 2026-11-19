import csv

def run(datafile: str) -> list:
    data = []
    with open(datafile,'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            for c,v in row.items():
                es_entero = True
                try: 
                    numero = int(v)
                except ValueError: es_entero = False
                if es_entero: row[c] = numero
                elif v =='': row[c]=None
                elif v == 'True': row[c] = True
                elif v == 'False': row[c] = False
            data.append(row)
    return data


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor
    run('ejercicios/ficheros/read-csv/data/pokemon.csv')
    vendor.launch(run)
