def find_upperCase(lista:list[str]):
    res = [p for p in lista if p.isupper()]
    return res

def find_lowerCase(lista:list[str]):
    res = [p for p in lista if p.islower()]
    return res 

def split_case(lista:list[str]):
    lower_list = find_lowerCase(lista)
    upper_list = find_upperCase(lista)
    return lower_list, upper_list



# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(split_case)
