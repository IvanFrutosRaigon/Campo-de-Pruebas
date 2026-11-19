def run(input_path: str) -> str:
    longest_word = ''
    fronteras = ",.;:()"

    with open(input_path, 'r') as f:
        for line in f:
            palabras = line.split()

            for palabra in palabras:
                palabra_limpia = palabra.strip(fronteras)

                if len(palabra_limpia) >= len(longest_word):
                    longest_word = palabra_limpia    
    return longest_word


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
