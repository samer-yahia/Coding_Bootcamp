# Countdown
def countdown(num):
    newArray = []
    for x in range(num, -1, -1):
        newArray.append(x)
    return newArray
print(countdown(5))

# Print and Return
def print_and_return(a,b):
    print(a)
    return b
variable = print_and_return(1,2)
print(variable) #check if return works

# First Plus Length
def first_plus_length(list):
    return list[0] + len(list)
print(first_plus_length([1,2,3,4,5]))

#Values Greater than Second
def val_greater_second(list):
    if len(list) < 2:
        return False
    newArray = []
    for x in range(0, len(list)):
        if list[x] > list[1]:
            newArray.append(list[x])
    print(len(newArray))
    return newArray
print(val_greater_second([5,2,3,2,1,4]))
print(val_greater_second([3]))

# This Length, That Value
def length_and_value(size,value):
    newArray = []
    for i in range(0,size):
        newArray.append(value)
    return newArray
print(length_and_value(4,7))
print(length_and_value(6,2))