def run(values: list, oper: str) -> bool:
    result = values[0]
    if oper=='and':
        for v in values[1:]:
            result = result and v
    elif oper=='or':
        for v in values[1:]:
            result = result or v
    return result


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
