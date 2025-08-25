list=[]
for i in range(10):
    list.append(i)
print(list)
n=int(input("Search a number"))
if n in list:
    print("Found")
else:
    print("Not Found")