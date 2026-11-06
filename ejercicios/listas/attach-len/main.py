def run(text: str) -> list:
    lista = text.split()
    words_length = []
    for w in lista: 
        pair = w + ":" + str(len(w))
        words_length.append(pair)
    return words_length


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
