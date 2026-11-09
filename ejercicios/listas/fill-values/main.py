def run(values: list) -> list:
    first = values[0]
    last = values[-1]
    fvalues = values.copy()
    for i in range(first,last +1):
        if i not in values:fvalues.append(i)

    fvalues = sorted(fvalues)
    return fvalues


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
