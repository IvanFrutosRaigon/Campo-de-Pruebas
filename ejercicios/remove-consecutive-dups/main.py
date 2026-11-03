def run(items: list) -> list:
    result = [items[0]]
    for value in items:
        if result[-1]!=value: result.append(value)
    return result


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
