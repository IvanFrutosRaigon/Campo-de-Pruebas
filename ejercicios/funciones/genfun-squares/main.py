def gen_sq(n: int):
    for i in range(n):
        yield i**2


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(gen_sq)
