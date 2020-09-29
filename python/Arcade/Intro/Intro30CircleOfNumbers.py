#
# * Intro 30. Circle of Numbers
# * Easy

# * Consider integer numbers from 0 to n - 1 written down along the circle in such 
# * a way that the distance between any two neighboring numbers is equal (note 
# * that 0 and n - 1 are neighboring, too).

# * Given n and firstNumber, find the number which is written in the radially 
# * opposite position to firstNumber.

# * Example

# For n = 10 and firstNumber = 2, the output should be
# circleOfNumbers(n, firstNumber) = 7.

# https://codesignal.s3.amazonaws.com/tasks/circleOfNumbers/img/example.png?_tm=1582003395936

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] integer n

#     A positive even integer.

#     Guaranteed constraints:
#     4 ≤ n ≤ 20.

#     [input] integer firstNumber

#     Guaranteed constraints:
#     0 ≤ firstNumber ≤ n - 1.

#     [output] integer

#%%

# * Solution 1
def circleOfNumbers(n:int, firstNumber: int)-> int:
    return (firstNumber + n//2)%n

a1 = 10
a2 = 2
e1 = 7
r1 = circleOfNumbers(a1, a2)
print('For {}, {}, expected: {}, result: {}'.format(a1, a2, e1, r1))


# %%
