def run(stock: dict, merch: str, amount: int) -> bool:
    if merch not in stock:
        available = False
    else: 
        if (stock[merch]-amount)<0:
            available=False
        else:
            available = True
    return available


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
