def cycle_alphabet(n_chars: int):
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    mod = len(ALPHABET)
    for i in range(n_chars):
        yield ALPHABET[i%mod]


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(cycle_alphabet)
