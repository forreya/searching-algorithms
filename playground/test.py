list1 = [1]*3
list2 = [2]*3

list1 = list2[:]
print(hex(id(list1)))
print(hex(id(list2)))
print(list1)