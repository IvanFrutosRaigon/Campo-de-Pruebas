def run(start: float, stop: float, step: float) -> list:
    acum = start
    values = []
    while acum<stop:
        values.append(acum)
        acum += step

    return values


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
