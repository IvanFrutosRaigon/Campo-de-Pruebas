def run(values: set) -> set:
    half_out_values = set()
    for v in values:
        v_new = v//2
        if v_new not in values:
            half_out_values.add(v_new)
    return half_out_values


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
