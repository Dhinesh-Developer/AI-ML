
# empty list
empty_list = []

# list with values
fruits = ["apple","banana","cherry"]
nums = [1,4,5,3,2]
diff = ["kumar",1,True,45.43]

print(fruits)
print(nums)
print(diff)


# Accessing the item
print(fruits[0])
print(fruits[1])
print(fruits[-1])

# slicing
print(fruits[1:2])
print(fruits[1:])
print(fruits[:1])

# changing the list
fruits = ["apple","banana","cherry","mango","graphe"]
fruits[0] = "orange"
print(fruits)

fruits.append("honey")
fruits.insert(1,"guava")
print(fruits)

# removing the items
fruits.remove("graphe")
last = fruits.pop() # removing and returing the values
print(fruits)


# list methods
print(fruits.count("banana"))
print(fruits.index("cherry"))
print(len(fruits))

nums.sort()
print(nums)

fruits.reverse()
print(fruits)

new_list = fruits.copy()
print(new_list)