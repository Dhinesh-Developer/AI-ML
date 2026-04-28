
# import math

# import specific items from a module
from math import sqrt,pi
import random

val = sqrt(16)
print(val)
print(pi)

# i want random number from 1 to 10
number = random.randint(1,10)
print(number)


choice = random.choice("apple","mango")
print(choice)


import datetime
today = datetime.date.today()
print(today)


import os
current_dir = os.getcwd()
print(current_dir)

import json

# json_string = json.dumps(data)
# print(json_string)


import pandas as pd
data = {
    "Name":{"kumar","dk","dhinesh"},
    "Age":{19,20,20}
}
df = pd.DataFrame(data)
print(df)


