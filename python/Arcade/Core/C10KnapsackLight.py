#
# * Core 10, Knapsack Light
# * Easy

# * You found two items in a treasure chest! The first item weighs weight1 and is 
# * worth value1, and the second item weighs weight2 and is worth value2. What is 
# * the total maximum value of the items you can take with you, assuming that your 
# * max weight capacity is maxW and you can't come back for the items later?

# Note that there are only two items and you can't bring more than one item of 
# each type, i.e. you can't take two first items or two second items.

# * Example

#     For value1 = 10, weight1 = 5, value2 = 6, weight2 = 4, and maxW = 8, the 
#       output should be
#     knapsackLight(value1, weight1, value2, weight2, maxW) = 10.

#     You can only carry the first item.

#     For value1 = 10, weight1 = 5, value2 = 6, weight2 = 4, and maxW = 9, the 
#       output should be
#     knapsackLight(value1, weight1, value2, weight2, maxW) = 16.

#     You're strong enough to take both of the items with you.

#     For value1 = 5, weight1 = 3, value2 = 7, weight2 = 4, and maxW = 6, the 
#       output should be
#     knapsackLight(value1, weight1, value2, weight2, maxW) = 7.

#     You can't take both items, but you can take any of them.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] integer value1

#     Guaranteed constraints:
#     2 ≤ value1 ≤ 20.

#     [input] integer weight1

#     Guaranteed constraints:
#     2 ≤ weight1 ≤ 10.

#     [input] integer value2

#     Guaranteed constraints:
#     2 ≤ value2 ≤ 20.

#     [input] integer weight2

#     Guaranteed constraints:
#     2 ≤ weight2 ≤ 10.

#     [input] integer maxW

#     Guaranteed constraints:
#     1 ≤ maxW ≤ 20.

#     [output] integer

#%%

# * Solution 1
def knapsackLight1(value1, weight1, value2, weight2, maxW):
    if weight1 + weight2 <= maxW:
        return value1 + value2
    elif value1 > value2:
        if weight1 <= maxW:
            return value1 
        elif weight2 <= maxW:
            return value2
        else:
            return 0
    else:
        if weight2 <= maxW:
            return value2
        elif weight1 <= maxW:
            return value1
        else:
            return 0


# * Solution 2
# ! Good
def knapsackLight2(value1, weight1, value2, weight2, maxW):
    if weight1 + weight2 <= maxW:
        return value1 + value2
    else:
        return max(value1 if weight1 <= maxW else 0, 
                    value2 if weight2 <= maxW else 0)


# * Solution 3
# ! Better
def knapsackLight3(value1, weight1, value2, weight2, maxW):

    return max((weight1 + weight2 <=maxW) * (value1 + value2), 
                (weight1 <=maxW) * value1, 
                (weight2 <=maxW) * value2)


v1 = 10
w1 = 5
v2 = 6
w2 = 4
mw = 8
r1 = knapsackLight1(v1, w1, v2, w2, mw)
print(r1)
