def run(text: str) -> dict:
    counter = {}
    for l in text:
        if l not in counter:
            counter[l] = 1
        else:
            counter[l] = counter[l] + 1
        
    return counter


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
