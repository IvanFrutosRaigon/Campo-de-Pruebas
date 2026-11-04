def run(n: int) -> list:
    powers2 = [2**value for value in range(n+1)]
    return powers2


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
