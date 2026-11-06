def run(ids: list) -> int:
    posibles = []
    for i in range(1, max(ids) + 1):
        if i not in ids: posibles.append(i)
    if len(posibles)>0:
        first_unused_id = posibles[0]
    else: first_unused_id = max(ids) + 1
    return first_unused_id


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
