def run(text: str) -> str:
    lista = text.split()
    reversa = lista[::-1]
    reversing = ' '.join(reversa)
    reversing = reversing.lower()
    return reversing


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
