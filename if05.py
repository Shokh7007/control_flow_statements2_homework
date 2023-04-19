def main(n):
    """
    Find the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    a=n%10
    b=n%100//10
    c=n%1000//100
    d=n%10000//1000
    e=n%100000//10000
    x=a
    if x<b:
        x=b
    if x<c:
        x=c
    if x<d:
        x=d
    if x<e:
        x=e
    return x
print(main(12745))