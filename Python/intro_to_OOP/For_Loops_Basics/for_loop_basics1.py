# Print all integers from 1 to 150
for x in range(1, 151, 1):
    print(x)

# Print multiples of five
for x in range(5, 5001, 5):
    print(x)

# Print int from 1 to 100; unless divisible by 5 then "Coding"; and divisible by 10 then "Coding Dojo"
for x in range(1, 101):
    if x%10 == 0:
        print("Coding Dojo")
    elif x%5 == 0:
        print("Coding")
    else:
        print(x)

# Print sum of odd integers from 0 to 500,000
sum = 0
for x in range(1, 500001):
    if x%2 == 1:
        sum += x
print(sum)

# Countdown by Fours from 2018 to 0
for x in range(2018, -1, -4):
    print(x)

# Flexible COunter
lownum = 5
highnum = 111
mult = 7
for x in range(lownum,highnum):
    if x%mult == 0:
        print(x)