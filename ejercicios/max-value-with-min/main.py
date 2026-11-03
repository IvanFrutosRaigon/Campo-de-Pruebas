def run(values: list) -> int:
    reversed_list = [value*-1 for value in values]
    max_value = (min(reversed_list))*-1
    return max_value


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
