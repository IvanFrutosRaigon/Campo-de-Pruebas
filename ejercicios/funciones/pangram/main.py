def is_pangram(cadena:str):
    ALPHABET = set("abcdefghijklmnopqrstuvwxyz")
    lista = {l.lower() for l in cadena if l!=' ' }

    return len(ALPHABET^lista) == 0



# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(is_pangram)
