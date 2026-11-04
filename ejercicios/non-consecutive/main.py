def run(values: list) -> int:
    target = None
    for actual, siguiente in zip(values, values[1:]):
        if siguiente != actual + 1:
            target = siguiente
            return target
    return target


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
