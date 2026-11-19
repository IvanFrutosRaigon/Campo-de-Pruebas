def run(input_path: str, lower_bound: int) -> dict:
    with open(input_path, 'r') as f:
        dicc = {}
        freq = {}
        for line in f:
            aux = line.split()
            palabras = [a.lower() for a in aux]
            for p in palabras:
                if p not in dicc:
                    dicc[p] = 1
                else:
                    dicc[p] = dicc[p] + 1

        for c,v in dicc.items():
            if v>=lower_bound:
                freq[c] = v
    return freq


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
