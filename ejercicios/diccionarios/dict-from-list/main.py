def run(items: list) -> dict:
    unpack_items = {}
    for l in items:
        unpack_items[l[0]]=l[1:]
    return unpack_items


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
