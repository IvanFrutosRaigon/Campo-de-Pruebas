def run(matrix1_path: str, matrix2_path: str, result_path: str) -> None:
    with open(matrix1_path, 'r') as f1, open(matrix2_path, 'r') as f2, open(result_path, 'w') as f3:
        for line1, line2 in zip(f1,f2):
            enteros1 = [int(v) for v in line1.split()]
            enteros2 = [int(v) for v in line2.split()]

            suma = [a + b for a,b in zip(enteros1, enteros2)]
            fila = ' '.join(str(n) for n in suma) + '\n'
            f3.write(fila)

        











        



# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
