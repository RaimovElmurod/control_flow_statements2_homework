def main(a,b,c):
    mx = a
    mn = a
    if mx<b:
        mx = b
    if mx<c:
        mx = c
    if mn > b:
        mn = b
    if mn > c:
        mn = c
    return (a+b+c)-(mx+mn)
print(main(3,7,1))
print(main(5,5,-1))