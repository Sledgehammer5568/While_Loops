# Problem2NumList10.py
#
# Emanuel Ramos
# 12/06/2022
#
# Description: makes a list using a while loop and a counter variable

# counter variable to count how many times the loop runs
counter = 0

# make a list where we will store the values of counter
L = []

# create a while loop that continues running until counter reaches 10
while counter <= 10:
    # add the value of counter to the list each time the loop runs
    L.append(counter)

    # add 1 to the counter
    counter += 1

# print the list
print(L)
