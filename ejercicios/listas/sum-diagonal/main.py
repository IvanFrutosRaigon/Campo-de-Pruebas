def run(matrix: list) -> int | None:
    items = []
    if len(matrix)!=len(matrix[0]): sum_diagonal=None
    else: 
        for r_id, row in enumerate(matrix):
                for c_id, value in enumerate(row):
                    if r_id==c_id:
                        items.append(value)
        sum_diagonal = sum(items)
    return sum_diagonal

    


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
