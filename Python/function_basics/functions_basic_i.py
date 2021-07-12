#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
# prediction: Display 5

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# Error. Days in a week function was not defined.

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
# Display 5 because return ends the function

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
# This will print 5 as the function will end before we can print 10.

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
# the function will print 5 but it does not return a value to x so it is undefined.


#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
# The function will print 3 and 5 from the function but no value was returned to print outside the function causing an error

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
# Print will display "25" as it was turned into a string and concatenated

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
# Function will print 100 then exit after else returning 10. This will print outside the function displaying 10


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3)) #Returns 7 then prints 7 here
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3)) # Returns 14 then prints 14 here
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# Returns 7 then returns 14 in the 2nd function. The printed the result is 21

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
# The first return ends the function so the printed result is the sum 8

# 11
b = 500
print(b) #prints 500
def foobar():
    b = 300
    print(b)
print(b) # Prints another 500
foobar() # Will print 300 from within the function
print(b) # Prints out 500


#12
b = 500
print(b) # Prints 500
def foobar():
    b = 300
    print(b)
    return b # nowhere to return
print(b) # Prints an other 500
foobar() # Will print 300 after new b and returns that value
print(b) # Prints 500


#13
b = 500
print(b) # Prints 500
def foobar():
    b = 300
    print(b)
    return b
print(b) # Prints another 500
b=foobar() # Prints 300 from within the function then stores returned b
print(b) # Prints returned value 300 from function


#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
# foo fx is called which prints 1 then calls bar fx which prints 3. Then finally 2 is printed from the end of foo fx

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
# foo fx prints 1, then calls bar which prints 3 and returns 5 to x, foo prints x which is 5 then returns 10 to y. Then 10 is printed