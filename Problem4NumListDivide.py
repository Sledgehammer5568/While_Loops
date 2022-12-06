# Problem4NumListDivide.py
#
# Emanuel Ramos
# 12/06/2022
#
# Description: makes a loop that will check if values are divisible by 10 and adds them to a list

# make a counter
counter = 0

# make a list to store the values provided by the loop
tens = []

# make a while loop that stops at 50
while counter <= 50:
    if counter % 10 == 0:
        tens.append(counter)
        # add 1 to counter
        counter += 1

    else:
        # add 1 to counter
        counter += 1

# print the values of the list
print(tens)
