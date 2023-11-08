def main(n):
    x1=n%10
    n//=10
    x2=n%10
    n//=10
    x3=n%10
    n//=10
    x4=n%10
    n//=10
    x5=n
    a=x1
    if x2>a:
        a=x2
    if x3>a:
        a=x3
    if x4>a:
        a=x4
    if x5>a:
        a=x5
    return a
print(main(23546))