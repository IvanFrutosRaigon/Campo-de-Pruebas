def run(fullname: str) -> str:
    separado = fullname.split(',')
    apellido = separado[0].split()
    nombre = separado[1]
    letra_nombre = nombre[1].upper() + '.'
    letras_apellido = []
    if len(apellido)==2:
        for item in apellido:
            letras_apellido.append(item[0].upper())
        initials = letra_nombre + '.'.join(letras_apellido) + '.'
    else:
        solo_una = apellido[0][0].upper()+'.'
        initials = letra_nombre+ solo_una   

    return initials


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
