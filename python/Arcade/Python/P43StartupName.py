#
# * Python 43, Startup Name
# * Easy

# * You decided to found your own startup company and now want to choose a proper 
# * name for it. There are three large companies that you want to compete against, 
# * and since their names are quite popular you want to use their names as a 
# * starting point. You want to use only popular characters in the name of your 
# * company, but not too mainstream. You consider a character to be popular if it 
# * appears in at least two company names, and consider it to be mainstream if it 
# * appears in all three.

# * Given the names of the companies, return the list of characters that are popular 
# * but not mainstream sorted by their ASCII codes.

# * Example

# For companies = ["coolcompany", "nicecompany", "legendarycompany"],
# the output should be
# startupName(companies) = ['e', 'l'].

# Here's how the answer can be obtained:

#     these letters appear in all three company names and are thus mainstream: 
#           a', 'c', 'm', 'n', 'o', 'p', 'y';
#     these letters appear only in one of the company names and are thus not 
#       popular: 'd', 'g', 'i', 'r';
#     the remaining letters are popular and not mainstream: 'e', 'l'.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.string companies

#     Array of three strings representing the company names. Each name is 
#       guaranteed to consist only of lowercase English letters.

#     Guaranteed constraints:
#     companies.length = 3,
#     2 ≤ companies[i].length ≤ 20.

#     [output] array.char

#     Array of characters that are popular but not mainstream.

#%%

# * Solution 1
def startupName1(companies):
    cmp1 = set(companies[0])
    cmp2 = set(companies[1])
    cmp3 = set(companies[2])
    res = ((cmp1 & cmp2) | (cmp1 & cmp3) | (cmp2 & cmp3)) - (cmp1 & cmp2 & cmp3)
    return list(sorted(list(res)))


# * Solution 2
def startupName2(companies):
    comp1 = set(companies[0])
    comp2 = set(companies[1])
    comp3 = set(companies[2])
    # ! good usage of operator ^
    res = ((comp1 | comp2 | comp3) - (comp1 ^ comp2 ^comp3))
    return list(sorted(list(res)))



a1 = ["coolcompany", "nicecompany", "legendarycompany"]
r1 = startupName1(a1)
print(r1)
# %%

