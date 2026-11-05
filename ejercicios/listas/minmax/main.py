def run(values: list) -> tuple:
    max_value = values[0]
    min_value = values[0]
    for v in values:
        if v>max_value: max_value=v
        elif v<min_value: min_value=v
    return min_value, max_value


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
