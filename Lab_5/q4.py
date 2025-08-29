t1=(10,20,30,40,50,60,70)
print(t1[:3])
print(t1[len(t1)-3:])
for item in range (1,7):
    if (item % 2) == 0:
        print(t1[item])