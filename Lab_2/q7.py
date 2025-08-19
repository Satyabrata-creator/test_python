a=int(input("Enter the cost price"))
b=int(input("Enter the sewlling price"))
if a>b:
    c=a-b
    print(c,"amount of loss inccured")
else:
    c=b-a
    print(c,"amount of profit made")