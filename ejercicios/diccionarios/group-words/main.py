def run(words: list) -> dict:
    group_words = {}
    for w in words:
        inicial = w[0]
        if inicial not in group_words:
            group_words[inicial] = [w]
        else:
            group_words[inicial].append(w)
    return group_words


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
