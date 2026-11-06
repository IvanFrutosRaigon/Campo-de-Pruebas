def run(values: list, ref_value: int) -> list:
    l1 = []
    l2 = []
    vpartition = []
    for v in values:
        if v<ref_value:
            l1.append(v)
        else:
            l2.append(v)
    vpartition.append(l1)
    vpartition.append(l2)
    return vpartition


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
