import math
from functools import reduce

# summation
def summation(lower, upper):
    result = 0
    while lower <= upper:
        result += lower
        lower += 1
    return result

# displayRange recursive function
def displayRange(lower, upper):
    if lower <= upper:
        print(lower)
        displayRange(lower + 1, upper)
        

# mapping absolute values
numbers = [1, -3, -4, 9, 12, -16]
absNumbers = list(map(abs, numbers))
print(f"absolute values of the numbers is: {absNumbers} ")

# filtering positive numbers
positiveNums = list(filter(lambda x:x > 0, numbers))
print(f"positive numbers is: {positiveNums}")

# reducing single string
words = ["Hello", " ", "my", " ", "name", " ", "is", " ", "Shifa"]
singleString = reduce(lambda x, y:x+y,words )
print(f"single string from a list words is: {singleString}")

# Modify the summation function
def modifiedSummation(lower, upper, step=1, function=lambda x:x):
    result = 0
    
    while lower <= upper:
        result += function(lower)
        lower += step
    return result

# test
print(f"summation between 1 to 5: {summation(1,5)}")
print("display range from 2 to 7: "),displayRange(2,7)
print(f"modified summation 1 to 5: {modifiedSummation(1,5)}")
print(f"modified summation 1 to 5 with 2 step: {modifiedSummation(1,10,2)}")
print(f"modified summation of square root 1 to 10 with 2 step : {modifiedSummation(1,10,2,math.sqrt)}")



