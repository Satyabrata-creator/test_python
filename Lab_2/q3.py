a=int(input("Enter a Number"))
b=int(input("Enter a Number"))
c=int(input("Enter a Number"))
if a>b and b>c:
    print(a,"is largest")
if b>c and b>a:
    print(b,"is largest")
if c>b and c>a:
    print(c,"is largest")