def run(text1: str, text2: str) -> str:
    v = {'a','e','i','o','u',' '}
    s1 = text1.lower()
    s2 = text2.lower()
    s1 = set(s1)
    s2 = set(s2)
    res = s1 & s2
    cconst = res - v
    cconst = ''.join(sorted(cconst))
    return cconst


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor
    run('Flat is bEtter than nested', 'Readability counts')
    vendor.launch(run)
