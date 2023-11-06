def main(a,b,c):
    if a<b:
        return a
    if b<c:
        return b
    if c<a:
        return c
print(main(1,4,2))
print(main(-5,-3,-1))