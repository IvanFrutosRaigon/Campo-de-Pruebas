def run(pdata: dict) -> dict:
    ac = 0
    for p in pdata.values():
        ac +=p
    for k in pdata.keys():
        pdata[k] = round((pdata[k]/ac)*100,3)

    avg_data = pdata
    return avg_data


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
