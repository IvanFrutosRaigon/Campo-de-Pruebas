def run(values: list) -> list:
    valores = []
    odds = []
    for v in values:
        if (v%2)==1:
            valores.append(v)
    for v in valores:
        if v not in odds:
            odds.append(v)
    return odds


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
