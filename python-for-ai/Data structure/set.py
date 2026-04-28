
# set are collections not only store unique values,by  removing duplicates data
# it returns the data in order

# empty set
empty_set = set()

my_set = {1,2,3,4,5}
my_set1 = {"apple","banana","mango"}

print(my_set)
print(my_set1)

# automatically removing 
my_set2 = {1,1,1,2,3,4,5,5}
print(my_set2)

# basic operations

colors = {"red","green",'blue'}

colors.add("white")
print(colors)

colors.remove('white') # if not found throw error
colors.discard('white') # if not found no error

if "red" in colors:
    print("red is available")


#remove duplicates
names = ["Alice", "Bob", "Alice", "Charlie", "Bob"]
new_list = list(set(names))
print(new_list)

