def run(number: str) -> bool:
    res = set(number)
    if len(res)<=2:
        for n in res:
            if n not in {'0','1'}:
                binary = False
            else: binary = True
    else: binary = False
    return binary


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor
    run('101011010111')
    vendor.launch(run)
