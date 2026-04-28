
#empty dict
empty_dict = {}

#Dictionary with data
my_dict = {
    "person":"kumar",
    "age" : "30",
    "city" : "mangalore"
}

print(my_dict)

# different ways to create dict
diff_dict = dict(name="kumar",age=20,city="mangalore")
print(diff_dict)


#accessing the values

print(my_dict["person"])
print(my_dict["age"])

#safer with get() because no error
print(my_dict.get("age"))
print(my_dict.get("job","unknown")) # setting the default values if the key and values is not present

# changing the dictionaries
my_dict = {
    "person":"kumar",
    "age" : "30",
    "city" : "mangalore"
}

#adding the modify the data
my_dict["phone"] = 1234567
my_dict["age"] = 20

print(my_dict)

#remove items
del my_dict["age"] # remove by key
last = my_dict.pop("city")
my_dict.clear() # remove all the data

#dictionary methods

my_dict = {
    "person":"kumar",
    "age" : "30",
    "city" : "mangalore"
}
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

#check if the keys exists
if "age" in my_dict:
    print("age key is found")

my_dict.update({"phone":123123123,"email":"email@gmail.com"})
print(my_dict)

#nested dictionaries

new_dict = {
    "alice":{"age":20,"email":"alice@gmail.com"},
    "bob":{"age":45,"email":"bob@gmail.com"}
}

print(new_dict["alice"]["email"])
print(new_dict["bob"]["age"])




