def run(items: list) -> bool:
    first=items[0]
    all_same = True
    for item in items:
        if first!=item: all_same = False
    return all_same


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
