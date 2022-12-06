# Problem3NumList35.py
#
# Emanuel Ramos
# 12/06/2022
#
# Description:

# make a list where we will store the values created in the loop
L = []

# sum of values
total = 0

# create a while loop to create the list of numbers
while total < 100:
    # ask the user for a value that will be added to the list
    number = int(input('what number do you want?'))
    # add the number to the list
    L.append(number)
    total = sum(L)

# print the list of numbers
print(L)

# print the sum of the numbers
print(total)
