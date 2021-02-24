#
# * Core 92, Strings Crossover
# * Medium

# * Define crossover operation over two equal-length strings A and B as follows:

#     the result of that operation is a string of the same length as the input strings
#     result[i] is either A[i] or B[i], chosen at random

# Given array of strings inputArray and a string result, find for how many pairs 
# of strings from inputArray the result of the crossover operation over them may 
# be equal to result.

# Note that (A, B) and (B, A) are the same pair. Also note that the pair cannot 
# include the same element of the array twice (however, if there are two equal 
# elements in the array, they can form a pair).

# Example

# For inputArray = ["abc", "aaa", "aba", "bab"] and result = "bbb", the output should be
# stringsCrossover(inputArray, result) = 2.

# Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.string inputArray

#     A non-empty array of equal-length strings.

#     Guaranteed constraints:
#     2 ≤ inputArray.length ≤ 10,
#     1 ≤ inputArray[i].length ≤ 10.

#     [input] string result

#     A string of the same length as each of the inputArray elements.

#     Guaranteed constraints:
#     result.length = inputArray[i].length.

#     [output] integer

#%%

# * Solution 1
def stringsCrossover(inputArray: list, result: str)-> int:
    def isCorss(s1: str, s2: str, result: str):
        n = len(s1)
        for i in range(n):
            if s1[i] != result[i] and s2[i] != result[i]:
                return False
        return True

    count = 0

    m = len(inputArray)
    for i in range(m):
        for j in range(i+1, m):
            if isCorss(inputArray[i], inputArray[j], result):
                print(inputArray[i], inputArray[j])
                count += 1

    return count


a1 = ["abc", "aaa", "aba", "bab"]
a2 = 'bbb'
r1 = stringsCrossover(a1, a2)
print('ex: {}, ar: {}'.format(2, r1))

a1 = ["aacccc", "bbcccc"]
a2 = 'abdddd'
r1 = stringsCrossover(a1, a2)
print('ex: {}, ar: {}'.format(0, r1))

a1 = ["a", "b", "c", "d", "e"]
a2 = 'c'
r1 = stringsCrossover(a1, a2)
print('ex: {}, ar: {}'.format(4, r1))
# %%
