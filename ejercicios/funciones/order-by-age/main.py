def order_by_age(lista:list[dict]) -> list[dict]:
    new = sorted(lista, key = lambda l: l['age'])
    return new


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(order_by_age)
