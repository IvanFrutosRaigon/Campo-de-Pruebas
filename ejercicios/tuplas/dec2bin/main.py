def run(n: int) -> str:
    res = []
    quotient, remainder = divmod(n, 2)
    res.append(str(remainder))
    while quotient>0:
        quotient, remainder = divmod(quotient,2)
        res.append(str(remainder))

    reversed_res = reversed(res)
    bin_repr = ''.join(reversed_res)
    return bin_repr


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
