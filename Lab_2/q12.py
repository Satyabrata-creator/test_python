print("Enter marks of Three Subjects")
a=float(input(""))
b=float(input(""))
c=float(input(""))
mark=(a + b + c)/3
if (mark>=90) and (mark<=100):
    print("A")
if (mark>=80) and (mark<90):
    print("B")
if (mark>=70) and (mark<80):
    print("C")
if (mark>=60) and (mark<70):
    print("D")
else :
print("F")