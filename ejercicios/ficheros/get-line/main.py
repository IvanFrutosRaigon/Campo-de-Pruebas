def run(input_path: str, line_no: int) -> str | None:
    with open(input_path, 'r') as f:
        dicc = {}
        line = None
        for num, l in enumerate(f, start=1):
            dicc[num] = l.strip()

        for c,v in dicc.items():
            if c==line_no: 
                line = v
                return line
    return line


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
