def run(marks: dict) -> tuple:
    passed = {w.upper():n  for w,n in marks.items() if n>=5 }
    failed = {w.lower():n  for w,n in marks.items() if n<=4}
    return passed, failed


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
