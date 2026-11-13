def run(unsorted_items: dict) -> list[tuple]:
    sorted_items = []

    for c, v in unsorted_items.items():
        sorted_items.append((v, c))

    sorted_items.sort()

    resultado = []
    for v, c in sorted_items:
        resultado.append((c, v))

    return resultado


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
