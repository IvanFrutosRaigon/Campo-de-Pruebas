def factorial(a):
    ac = 1
    if a>=0:
        for i in range(a,0,-1):
            ac *=i
        return ac
    else: 
        return None


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(factorial)
