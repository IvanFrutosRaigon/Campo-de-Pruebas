def run(items: dict) -> bool:
    values = list(items.values())
    all_same = True
    if len(values)>0:
        first = values[0]
        for v in values[1:]:
            if v!=first:
                all_same = False
                return all_same
    return all_same


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
