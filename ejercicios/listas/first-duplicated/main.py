def run(items: list) -> int | None:
    fdup = None
    if len(items)>0:
        primer = items[0]
        aux = []
        aux.append(primer)
        res = []
        for i in items[1:]:
            if i in aux: res.append(i)
            else: aux.append(i)

        if len(res)>0:
            fdup = res[0]

    return fdup


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
