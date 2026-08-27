def main(a,b,c):
    """
    Find number of negative numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of negative numbers in the given numbers
    """
    if a < 0 and b < 0 and c < 0:
        return 3
    elif a < 0 and b < 0:
        return 2
    elif a < 0 and c < 0:
        return 2
    elif b < 0 and c < 0:
        return 2
    elif a < 0 or b < 0 or c < 0:
        return 1
print(main(7,-2,1))