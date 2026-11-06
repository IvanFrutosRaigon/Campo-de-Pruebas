def run(formula: list) -> bool:
    valid = True
    if (7  not in formula) and (8 not in formula):
        valid = False
        return valid

    if (1 in formula) and (2 in formula):
        valid = False
        return valid

    if (3 in formula) and (4 in formula):
        valid = False
        return valid

    if (5 in formula) and (6 in formula):
        valid = True

    if (5 not in formula) and (6 in formula):
        valid = False
        return valid

    if (5 in formula) and (6 not in formula):
        valid = False
        return valid
    
    if (5 not in formula) and (6 not in formula):
        valid = True
    return valid 



# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
