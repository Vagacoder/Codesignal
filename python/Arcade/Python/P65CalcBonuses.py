#
# * Python 65, Calc Bounuses
# * Easy

# * You are working on a revolutionary video game. In this game the player will 
# * be able to collect several types of bonuses on each level, and his total score 
# * for the level is equal to the sum of the first n bonuses he collected. However, 
# * if he collects less than n bonuses, his score will be equal to 0.

# Given the bonuses the player got, your task is to return his final score for the level.

# * Example

#     For bonuses = [4, 2, 4, 5] and n = 3,
#     the output should be
#     calcBonuses(bonuses, n) = 10.

#     4 + 2 + 4 = 10.

#     For bonuses = [4, 2, 4, 5] and n = 5,
#     the output should be
#     calcBonuses(bonuses, n) = 0.

#     The player has collected only 4 bonuses, so his final score is 0.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.integer bonuses

#     A list of bonuses the player collected.

#     Guaranteed constraints:
#     0 ≤ bonuses.length ≤ 20,
#     0 ≤ bonuses[i] ≤ 50.

#     [input] integer n

#     The number of bonuses that should be collected to obtain non-zero final score.

#     Guaranteed constraints:
#     1 ≤ n ≤ 20.

#     [output] integer

#     Final score for the level.

#%%

# * Solution 1
def calcBonuses(bonuses:list, n:int)-> int:

    # ! generator
    it = (x for x in bonuses)
    res = 0

    try:
        for _ in range(n):
            res += next(it)
    except StopIteration:
        res = 0

    return res


# * Solution 2
# ! iter()
def calcBonuses2(bonuses:list, n:int)-> int:
    it = iter(bonuses)
    res = 0

    try:
        for _ in range(n):
            res += next(it)
    except StopIteration:
        res = 0

    return res


# * Solution 3
# ! yield inside a list
def calcBonuses3(bonuses:list, n:int)-> int:
    it = [(yield x) for x in bonuses]
    res = 0

    try:
        for _ in range(n):
            res += next(it)
    except StopIteration:
        res = 0

    return res


a1 = [4, 2, 4, 5]
b1 = 3
r1 = calcBonuses(a1, b1)
print(r1)

a1 = [4, 2, 4, 5]
b1 = 5
r1 = calcBonuses(a1, b1)
print(r1)

# %%
