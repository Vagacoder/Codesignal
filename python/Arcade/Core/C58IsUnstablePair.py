#
# * Core 58. Is Unstable Pair
# * Medium

# * Some file managers sort filenames taking into account case of the letters, 
# * others compare strings as if all of the letters are of the same case. That 
# * may lead to different ways of filename ordering.

# Call two filenames an unstable pair if their ordering depends on the case.

# To compare two filenames a and b, find the first position i at which a[i] ≠ b[i]. 
# If a[i] < b[i], then a < b. Otherwise a > b. If such position doesn't exist, 
# the shorter string goes first.

# Given two filenames, check whether they form an unstable pair.

# * Example

#     For filename1 = "aa" and filename2 = "AAB", the output should be
#     isUnstablePair(filename1, filename2) = true.

#     Because "AAB" < "aa", but "AAB" > "AA".

#     For filename1 = "A" and filename2 = "z", the output should be
#     isUnstablePair(filename1, filename2) = false.

#     Both "A" < "z" and "a" < "z".

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string filename1

#     A non-empty string of English letters and digits.

#     Guaranteed constraints:
#     1 ≤ filename1.length ≤ 10.

#     [input] string filename2

#     A non-empty string of English letters and digits. It's guaranteed that there is no ambiguity, i.e. even being considered in the same case strings are never equal.

#     Guaranteed constraints:
#     1 ≤ filename2.length ≤ 10.

#     [output] boolean

#     true if filename1 and filename2 form an unstable pair, false otherwise.

#%%

# * Solution 1
def isUnstablePair(filename1: str, filename2: str)-> bool:

    def helper(s1: str, s2: str)-> int:
        n = len(s1)
        m = len(s2)
        i = 0

        while i < n and i < m:
            if s1[i] < s2[i]:
                return -1
            elif s1[i] > s2[i]:
                return 1
            else:
                i += 1

        if i == n:
            return -1
        else: 
            return 1


    # f1U = filename1.upper()
    f1L = filename1.lower()
    # f2U = filename2.upper()
    f2L = filename2.lower()

    # print(f1L)
    # print(f2L)

    result = helper(filename1, filename2) + helper(f1L, f2L)
    # print(result)
    return not(result == 2 or result == -2)

f1 = 'aa'
f2 = 'AAB'
r1 = isUnstablePair(f1, f2)
print(r1)

f1 = 'A'
f2 = 'z'
r1 = isUnstablePair(f1, f2)
print(r1)

f1 = 'qwerTyu123'
f2 = 'qwertyu'
r1 = isUnstablePair(f1, f2)
print(r1)

# %%
