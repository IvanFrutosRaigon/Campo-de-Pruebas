def run(items: dict) -> dict:
    fitems={}
    for c,v in items.items():
        c = c.replace(' ','')
        fitems[c]=v
    return fitems


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
