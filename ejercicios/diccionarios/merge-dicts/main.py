def run(d1: dict, d2: dict) -> dict:
    merged = {}
    for llave,valor in d1.items():
        merged[llave] = valor
    for llave,valor in d2.items():
            merged[llave] = valor
    return merged


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
