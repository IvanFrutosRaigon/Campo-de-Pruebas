def find_divisores(n:int):
    for i in range(1, n+1):
        if n%i==0 and i!=n:
            yield i

def is_perfect(n: int) -> bool:
    divisores_generador = find_divisores(n)
    divisores = list(divisores_generador)
    return sum(divisores)==n
    


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor
    is_perfect(28)
    vendor.launch(is_perfect)
