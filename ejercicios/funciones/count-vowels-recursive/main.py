def count_vowels(cadena:str):
    combinaciones = 'aeiouáéíóúAEIOUÁÉÍÓÚ'
    if not cadena:
        return 0
    is_vowel = 1 if cadena[0].lower() in combinaciones else 0
    return is_vowel + count_vowels(cadena[1:])




# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(count_vowels)
