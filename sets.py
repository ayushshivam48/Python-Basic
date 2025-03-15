collection = set()  # it is a empty set
#collection = {}  #it is a empty dictonary

collection.add(1)
collection.add(2)
collection.add(2)
print(collection)

collection.remove(2)
print(collection)

collection.add((2,3,4))
print(collection)

collection.clear()
print(len(collection))

coll1 = {"ayush","shivam","world","new"}
coll2 = {"top","bottom"}
print(coll1.pop())  #pop any random value

print(coll2.union(coll1))
print(coll2.intersection(coll1))