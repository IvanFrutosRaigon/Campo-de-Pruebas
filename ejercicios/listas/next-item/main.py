def run(items: list, ref_item: object) -> object:
    target_item = None
    try:
        target_item = items[items.index(ref_item) + 1]
    except:
        target_item = None
        
    return target_item


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
