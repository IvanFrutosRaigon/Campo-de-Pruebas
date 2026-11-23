def run(input_path: str, output_path: str) -> None:
    with open(input_path, 'r') as f, open(output_path, 'w') as f2:
        aux = [line.strip().lower() for line in f]
        
        for i in range(len(aux)):
            for j in range(i+1, len(aux)):
                palabras1 = set(aux[i].split())
                palabras2 = set(aux[j].split())

                common_words = len(palabras1 & palabras2)
                f2.write(str(common_words) + '\n')

                


        
                
            
        


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
