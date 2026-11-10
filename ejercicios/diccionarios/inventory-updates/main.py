def run(imoves: str) -> dict:
    inventory = {}

    for movimiento in imoves.split(','):
        letra = movimiento[0]
        cantidad = int(movimiento[1:])

        inventory[letra] = inventory.get(letra, 0) + cantidad

    return inventory


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
