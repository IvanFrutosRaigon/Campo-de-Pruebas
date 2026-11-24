# TODO
def fabs(func):
    def wrapper(*args):
        mod_args = [abs(a) for a in args[:2]]
        rest = args[2:]
        return func(*mod_args, *rest)
    return wrapper


# DO NOT TOUCH THE CODE BELOW
def run(func, func_args):
    return fabs(func)(*func_args)


if __name__ == '__main__':
    import vendor

    vendor.launch(run)
