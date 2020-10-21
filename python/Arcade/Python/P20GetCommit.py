#
# * Python 20, Get Commit
# * Easy

# * The Abanamama Version System (AVS) is a software versioning and revision 
# * control system used in highly secure environments. In this system, each commit 
# * is assigned a unique name, the first part of which consists of the username 
# * encrypted in the base-4 system using symbols '0', '?', '+', and '!', and the 
# * second part consists of symbols of English alphabet.

# * Given such commit, your task is go remove the username part from it and return 
# * the second part as an answer.

# * Example

# For commit = "0??+0+!!someCommIdhsSt", the output should be
# getCommit(commit) = "someCommIdhsSt".

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string commit

#     Commit in the format given above. Note, that it is possible that it doesn't contain the first or the second part.

#     Guaranteed constraints:
#     5 ≤ commit.length ≤ 45.

#     [output] string

#     The second part of the commit.

#%%

# * Solution 1
import re

def getCommit1(commit:str)->str:
    return re.sub('^[0?+!]+', '', commit)


# * Solution 2
def getCommit2(commit:str)->str:
    return commit.lstrip('0?+!')


a1 = '0??+0+!!someCommIdhsSt'
e1 = 'someCommIdhsSt'
r1 = getCommit2(a1)
print('Expected:', e1)
print('Result:', r1)


# %%
