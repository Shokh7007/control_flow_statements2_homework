def main(a,b,c):
    """
    Find the smallest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    x=a
    if x>b:
        x=b
    if x>c:
        x=c
    return x
print(main(3,5,4))