
# function is a resuable block of code

def greet():
    print("Hello from function")

greet()    

# funtion with logic

def check_weather():
    temperatue = 25
    if temperatue > 30:
        print("it's hot!")
    else:
        print("normal")

check_weather()


### scope of the variables

#local variable
def calculate_price():
    price = 100
    tax = price*0.1
    print(f"Total: {price + tax}")

calculate_price()

#print(price) #name 'price' is not defined


# global variable
discount_rate = 0.15
price = 100

def apply_discount():
    discount = price * discount_rate
    return discount

discount_amount = apply_discount()
print(f"Discount Amount: {discount_amount}")
print(f"Total amount to pay: {price - discount_amount}")


# parameters

def introduce(name,age):
    print(f"I'm {name}")
    print(f"{age} old!")

introduce("Kumar",20)

# returing the multiple values
def simple_function():
    numbers = [1,2,3,4,5]
    first_number = numbers[0]
    last_number = numbers[4]

    return first_number,last_number

f,l = simple_function()
print(f)
print(l)
