#
# * Python 29, Is Test Solvable
# * Easy

# * You've been preparing all night for the upcoming test and entered the class 
# * certain that you will ace it. Now that you received the test questions, you 
# * died inside a little: looks like you prepared for the test on a completely 
# * different topic.

# * You're not even sure if you should bother to answer the questions. You still 
# * have some hope though: it is known that there's a glitch in the test preparing 
# * system, so that if the sum of digits of question ids is divisible by k, the 
# * answer to each question has a 90% probability to be an A.

# * Given the list of question ids, determine if the sum of their digits is 
# * divisible by k to see if it's worth trying to pass the test.

# * Example

# For ids = [529665, 909767, 644200] and k = 3, the output should be
# isTestSolvable(ids, k) = true.

# The sum of digits is

# (5 + 2 + 9 + 6 + 6 + 5) + (9 + 0 + 9 + 7 + 6 + 7) + (6 + 4 + 4 + 2 + 0 + 0) = 87

# which is divisible by 3. Today is your lucky day after all!

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.integer ids

#     Array of unique question ids.

#     Guaranteed constraints:
#     1 ≤ ids.length ≤ 50,
#     0 ≤ ids[i] ≤ 106.

#     [input] integer k

#     The number that causes a glitch in the test preparing system.

#     Guaranteed constraints:
#     2 ≤ k ≤ 10.

#     [output] boolean

#     true if the total sum of digits in ids is divisible by k, false otherwise.

#%%
# * Solution 1
def isTestSolvable(ids, k):
    digitSum = lambda id: sum([int(c) for c in str(id)])

    sm = 0
    for questionId in ids:
        sm += digitSum(questionId)
    return sm % k == 0


a1 = [529665, 909767, 644200]
k = 3
r1 = isTestSolvable(a1, k)
print(r1)
# %%
