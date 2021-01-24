#
# * Core 70, Alphabet Subsequence
# * Easy

# * Check whether the given string is a subsequence of the plaintext alphabet.

# * Example

#     For s = "effg", the output should be
#     alphabetSubsequence(s) = false;
#     For s = "cdce", the output should be
#     alphabetSubsequence(s) = false;
#     For s = "ace", the output should be
#     alphabetSubsequence(s) = true;
#     For s = "bxz", the output should be
#     alphabetSubsequence(s) = true.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string s

#     Guaranteed constraints:
#     2 ≤ s.length ≤ 15.

#     [output] boolean

#     true if the given string is a subsequence of the alphabet, false otherwise.



#%%

# * Solution 1
def alphabetSubsequence(s:str)->bool:
    return all([ord(s[i]) > ord(s[i-1]) for i in range(1, len(s))])

a1 = 'effg'
r1 = alphabetSubsequence(a1)
print(r1)

a1 = 'ace'
r1 = alphabetSubsequence(a1)
print(r1)
