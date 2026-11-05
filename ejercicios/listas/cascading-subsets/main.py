def run(values: list, size: int) -> list:
    rango = len(values) - size + 1
    cascading = [values[i:i+size] for i in range(rango)]
    return cascading


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
