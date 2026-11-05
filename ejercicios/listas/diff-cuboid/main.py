def run(cuboid1: list, cuboid2: list) -> float:
    vol1 = 1
    vol2 = 1
    for x in cuboid1:
        vol1*=x
    for x in cuboid2:
        vol2*=x
    vol_diff = abs(vol1-vol2)
    return vol_diff


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
