def run(input: tuple) -> tuple[set, set]:
    s1 = set()
    s2 = set()
    for i in input:
        s1.add(i[0])
        s2.add(i[1])
    output = (s1,s2)
    return output


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
