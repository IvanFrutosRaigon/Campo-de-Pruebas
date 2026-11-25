def extract_evens(lista:list[int]) -> list[int]:
    res = [l for l in lista if l%2==0]
    return res



# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(extract_evens)
