def run(items: list) -> list:
    flatten_items = []
    for item in items:
        if isinstance(item, list):
            sublista = run(item)
            flatten_items.extend(sublista)
        else:
            flatten_items.append(item)
    return flatten_items


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
