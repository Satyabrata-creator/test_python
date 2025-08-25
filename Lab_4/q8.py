list=[1,2,2,3,4,4,5]
for item in list:
    while list.count(item) > 1:
        list.remove(item)
        print(list)