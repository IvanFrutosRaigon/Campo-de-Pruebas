def run(values1: list, values2: list) -> list:
    i = j = 0
    lista = []
    merged = []
    while i<len(values1) and j<len(values2):
        if values1[i]<values2[j]:
            lista.append(values1[i])
            i+=1
        elif values1[i]>values2[j]:
            lista.append(values2[j])
            j+=1
        else:
            lista.append(values1[i])
            i+=1
            j+=1

    if len(values1[i:])>0:
        lista.extend(values1[i:])
    else: lista.extend(values2[j:])

    for v in lista:
        if v not in merged:
            merged.append(v)

    return merged


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
