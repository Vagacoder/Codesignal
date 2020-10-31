#
# * Python 49, Memeory Pill
# * Easy

# * Not long ago Greg noticed that he started to forget things, and hurried to 
# * the doctor. The doc told him that it was perfectly normal for his age, and 
# * wrote down a list of pills that Greg can take in order to improve his memory. 
# * He especially recommended one medicine as the most effective one.

# * Unfortunately Greg forgot which medicine is the most effective, and he feels 
# * like he really needs to take them. Greg recalls that the name of the most 
# * effective medicine goes in the list somewhere after the very first name that 
# * has an even length. Your task is to help Greg: given the list of the pills, 
# * return a list of three names that go right after the very first medicine name 
# * of the even length.

# * If there are less than three medicines to return, return empty strings instead 
# * of them.

# * Example

# For pills = ["Notforgetan", "Antimoron", "Rememberin", "Bestmedicen", "Superpillsus"],
# the output should be
# memoryPills(pills) = ["Bestmedicen", "Superpillsus", ""].

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.string pills

#     Array of medicaments written in Greg's prescription. Each title in the list 
#       can consist of English letters, digits and whitespace characters.
#     It is guaranteed that at least one title in the list has an even length.

#     Guaranteed constraints:
#     1 ≤ pills.length ≤ 10,
#     2 ≤ pills[i].length ≤ 30.

#     [output] array.string

#     A list of 3 elements.

#%%

# * Solution 1
from itertools import dropwhile

def memoryPills(pills):
    gen = dropwhile(lambda x: len(x)%2 ==1, pills+ ['']*3)
    next(gen)
    return [next(gen) for _ in range(3)]


a1 = ["Notforgetan", "Antimoron", "Rememberin", "Bestmedicen", "Superpillsus"]
r1 = memoryPills(a1)
print(r1)


# %%
