list = [2, 1, 3]

list.append(4)
print(list)

list.sort()
print(list)

list.sort(reverse=True)
print(list)

list.reverse()
print(list)

list.insert(2,6)      #(idx,ele)
print(list)

print(list[1:3])

list.pop(3)           #(idx)
print(list)

list.remove(2)         #(ele)
print(list)