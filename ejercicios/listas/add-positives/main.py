def run(numbers: list) -> int:
    positivos = [number for number in numbers if number>=0]
    result = sum(positivos)
    return result


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
