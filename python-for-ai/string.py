first_name = "dhinesh"
last_name = "kumar"

full_name = first_name+" "+last_name
print(full_name)

#Greetings
greeting = f"Hello, {first_name}"
print(greeting)

# multiple variables
age = 25
intro = f"I'm {first_name} with age {age} old!"
print(intro)

# repetition
star = "*"
stars = star*5
print(stars)


#String methods
text = "Python programming"
print(text.lower())
print(text.upper())
print(text.title()) # first letter every word would be capital

#Cleaning Strings
messy = " Hello world "
print(messy.strip())

price = "$20.12"
print(price.strip("$"))


#Finding and replacing

message = "I love python programming with python"
print("python" in message)
print("love" in message)

print(message.startswith("I"))
print(message.endswith("python"))

# Finding the position
print(message.find("programming"))
print(message.count("python"))

# replace
new_message = message.replace("python","Java")
print(new_message)

