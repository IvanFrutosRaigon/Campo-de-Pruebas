def run(values: list) -> int:
    if len(values)>0:
        maximo = max(values)
        minimo = min(values)
        tsum = sum([v for v in values if v!=maximo and v!=minimo])
    else: tsum=0
    return tsum


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
