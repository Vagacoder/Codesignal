#
# * Python 55, Twins Score
# * Easy

# * Billy and Mandy are twins, and as such they do everything together. Unfortunately 
# * during the finals they were forced to write their exams separately, which 
# * explains why they got such low scores. However, they are not too sad about it: 
# * since they are twins, it's only natural for them to work together, so they 
# * are going to sum up their scores for each exam and show them to their mom.

# * Given two lists of equal size representing the scores Billy and Mandy got for 
# * each exam (b and m, respectively), return a single list containing their combined 
# * score.

# * Example

# For b = [22, 13, 45, 32] and m = [28, 41, 13, 32],
# the output should be
# twinsScore(b, m) = [50, 54, 58, 64].

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.integer b

#     The scores Billy got during the finals.

#     Guaranteed constraints:
#     1 ≤ b.length ≤ 20,
#     0 ≤ b[i] ≤ 100.

#     [input] array.integer m

#     The scores Mandy got during the finals.

#     Guaranteed constraints:
#     m.length = b.length,
#     0 ≤ m[i] ≤ 100.

#     [output] array.integer

#     The total scores the twins got during the finals.

#%%

# * Solution 1
def twinsScore1(b:list, m:list)->list:
    return list(a+b for a, b in zip(b, m))


# * Solution 2
def twinsScore2(b:list, m:list)->list:
    return list(map(sum, zip(b, m)))


a1 = [22, 13, 45, 32]
a2 = [28, 41, 13, 32]
r1 = twinsScore2(a1, a2)
print(r1)

# %%
