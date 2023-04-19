def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a>b and a>c and b>c:
        return "b"
    elif b>a and b>c and a>c:
        return "a"
    elif c>b and a>c and a>b:
        return "c"
print(main(3,5,4))