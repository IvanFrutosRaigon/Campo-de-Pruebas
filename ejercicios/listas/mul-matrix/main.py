def run(A: list, B: list) -> list | None:
    num_filas_A = len(A)
    num_col_A = len(A[0])
    num_filas_B = len(B)
    num_col_B = len(B[0])
    if num_col_A == num_filas_B:
        P = [[] for _ in range(num_filas_A)]
        for i in range(num_filas_A):
            for j in range(num_col_B):
                acumulador = 0
                for k in range(num_col_A):
                    sum = A[i][k]*B[k][j]
                    acumulador+=sum

                P[i].append(acumulador)
    else: 
        P = None
    return P


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
