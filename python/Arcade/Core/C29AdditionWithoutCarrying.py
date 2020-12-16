#
# * COre 29, Addition without Carrying
# * Easy

# * A little boy is studying arithmetic. He has just learned how to add two integers, 
# * written one below another, column by column. But he always forgets about the 
# * important part - carrying.

# * Given two integers, your task is to find the result which the little boy will get.

# Note: The boy had learned from this site, so feel free to check it out too if 
# you are not familiar with column addition.

# * Example

# For param1 = 456 and param2 = 1734, the output should be
# additionWithoutCarrying(param1, param2) = 1180.

#    456
#   1734
# + ____
#   1180

# The boy performs the following operations from right to left:

#     6 + 4 = 10 but he forgets about carrying the 1 and just writes down the 0 
#       in the last column
#     5 + 3 = 8
#     4 + 7 = 11 but he forgets about the leading 1 and just writes down 1 under 
#       4 and 7.
#     There is no digit in the first number corresponding to the leading digit of 
#       the second one, so the boy imagines that 0 is written before 456. Thus, 
#       he gets 0 + 1 = 1.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] integer param1

#     A non-negative integer.

#     Guaranteed constraints:
#     0 ≤ param1 < 105.

#     [input] integer param2

#     A non-negative integer.

#     Guaranteed constraints:
#     0 ≤ param2 < 6 · 104.

#     [output] integer

#     The result that the little boy will get by using column addition without 
#       carrying.

#%%

# * Solution 1
# * Original
def additionWithoutCarrying(param1:int, param2:int)->int:
    result = 0
    digit = 0
    while param1 > 0 and param2 > 0:
        tail1 = param1 % 10
        tail2 = param2 % 10
        result += ((tail1 + tail2) %10)*10**digit
        param1 = param1//10
        param2 = param2//10
        digit +=1

    if param1 > 0:
        result += param1*10**digit
    if param2 > 0:
        result += param2*10**digit

    return result


# * Solution 2
# ! imporved
def additionWithoutCarrying2(param1:int, param2:int)->int:
    result = 0
    digit = 0
    while param1 > 0 or param2 > 0:
        tail1 = param1 % 10
        tail2 = param2 % 10
        result += ((tail1 + tail2) %10)*10**digit
        param1 = param1//10
        param2 = param2//10
        digit +=1

    return result

p1 = 456
p2 = 1734
r1 = additionWithoutCarrying2(p1, p2)
print(r1)
