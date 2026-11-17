def run(words: list) -> str:
    dicc = {}
    for w in words:
        t = set(w)
        l = len(t)
        dicc[w] = l

    m = max(dicc.values())
    for c,v in dicc.items():
        if v==m:
            dword = c
            return dword
    
    #return dword


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor
    run(['dictionary', 'turtle', 'flexibility', 'humanity'])
    vendor.launch(run)
