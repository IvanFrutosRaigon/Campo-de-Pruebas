def run(numbers: list) -> int:
    rmult = 1
    for valor in numbers:
        rmult*=valor
    return rmult


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
