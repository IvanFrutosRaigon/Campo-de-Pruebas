def run(farm: list) -> str:
    pos_lobo = farm.index('lobo')
    pos_ovejas = len(farm) -1 -pos_lobo
    if pos_ovejas == 0: msg = 'Oye lobo no te quiero ver más por aquí'
    else: msg = f'Cuidado oveja {pos_ovejas}, el lobo te va a comer'
    return msg


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
