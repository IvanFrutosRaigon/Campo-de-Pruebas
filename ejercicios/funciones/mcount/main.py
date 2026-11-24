def mcount(tupla:tuple[int], value:int | None = None)->int:
    if value is None:
        return -1
    else:
        ac = 0
        for i in tupla:
            if i == value:
                ac +=1
        return ac
        





# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(mcount)
