def run(items: list) -> int:
    all_int = []
    for item in items:
        if type(item)!=int:
            item=int(item)
        all_int.append(item)
        
    sum_items = sum(all_int)
    return sum_items


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
