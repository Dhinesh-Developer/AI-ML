
# work with immutable sequences
# immutable - unchangeable

#empty tuple
empty = ()

my_tuple = (1,2,3,4)
print(type(my_tuple))
print(my_tuple)

# single item na tuple need the comma
tup = (42,)
print(tup)

#implict without paranthesis
coordinates = 10,20

print(my_tuple[1:2])
print(my_tuple[3])
print(my_tuple[:4])

#unpack the values

points = (30,40)
x,y = points

print(x,y)

# swap the values
x,y = y,x
print(x,y)


