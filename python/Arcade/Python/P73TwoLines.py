#
# * Python 73, Two Lines
# * Easy

# * Consider two straight lines given as y = mx + b. You forgot what they mean 
# * but you're sure that the destiny of the universe depends on them. To save the 
# * world, you have to choose one of these lines. Here is how to make the proper 
# * choice:

#     Consider all integer coordinates a for all possible values of a from l to r, inclusive.
#     For each vertical x = a, find the points where this vertical intersects with 
#       line1 and line2. Denote these points as p1 and p2, respectively. If p1 
#       and p2 don't coincide, give one point to the line which is higher in that vertical.
#     Choose the line which has a larger score. Return "first" for line1, "second" 
#       for line2 and "any" if both lines have the same score.

# * Example

#     For line1 = [1, 2], line2 = [2, 1], l = 0, and r = 2, the output should be
#     twoLines(line1, line2, l, r) = "any";
#     For line1 = [1, 2], line2 = [2, 1], l = -1, and r = 2, the output should be
#     twoLines(line1, line2, l, r) = "first";
#     For line1 = [1, 2], line2 = [2, 1], l = 0, and r = 3, the output should be
#     twoLines(line1, line2, l, r) = "second".

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.integer line1

#     An array containing two integers, m and b, respectively. These integers 
#       correspond to line equation coefficients.

#     Guaranteed constraints:
#     -1000 ≤ line1[i] ≤ 1000,
#     line1[0] * line1[1] ≠ 0.

#     [input] array.integer line2

#     An array in the same format as line1.

#     Guaranteed constraints:
#     -1000 ≤ line2[i] ≤ 1000,
#     line2[0] * line2[1] ≠ 0.

#     [input] integer l

#     Guaranteed constraints:
#     -1000 ≤ l ≤ r ≤ 1000.

#     [input] integer r

#     Guaranteed constraints:
#     -1000 ≤ l ≤ r ≤ 1000.

#     [output] string

#%%
from functools import partial

def line_y(m, b, x):
    return m * x + b

# * Solution 1
# ! functools.partial()
def twoLines1(line1, line2, l, r):
    line1_y = partial(line_y, line1[0], line1[1])
    line2_y = partial(line_y, line2[0], line2[1])
    balance = 0
    for x in range(l, r + 1):
        y1 = line1_y(x)
        y2 = line2_y(x)
        if y1 > y2:
            balance += 1
        elif y1 < y2:
            balance -= 1
    if balance > 0:
        return "first"
    if balance < 0:
        return "second"
    return "any"


# * Solution 2
# ! unpack list
def twoLines2(line1, line2, l, r):
    line1_y = partial(line_y, *line1)
    line2_y = partial(line_y, *line2)
    balance = 0
    for x in range(l, r + 1):
        y1 = line1_y(x)
        y2 = line2_y(x)
        if y1 > y2:
            balance += 1
        elif y1 < y2:
            balance -= 1
    if balance > 0:
        return "first"
    if balance < 0:
        return "second"
    return "any"



l1 = [1, 2]
l2 = [2, 1]
l = 0
r = 2
r1 = twoLines2(l1, l2, l, r)
print(r1)

# %%
