#
# * Python 53, Crazy Ball
# * Easy

# * You've been training your whole life, and now your dreams finally came true: 
# * you are a member of the best Crazyball team in the world! Unfortunately since 
# * your team is one of only two teams that play Crazyball, there are already many 
# * players in it, including yourself. For the starting lineup on the upcoming 
# * game the coach will pick k players, and you're curious if it's possible for 
# * you to make it there.

# * To calculate the odds of being a starter, you'd like to come up with a list 
# * of all possible lineups. Given the list of the players and the number of players 
# * k the coach has to pick, return all possible lineups sorted lexicographically. 
# * Players in each lineup should also be sorted lexicographically.

# * Example

# For players = ["Ninja", "Warrior", "Trainee", "Newbie"] and k = 3,
# the output should be

# crazyball(players, k) = [["Newbie", "Ninja", "Trainee"], 
#                          ["Newbie", "Ninja", "Warrior"], 
#                          ["Newbie", "Trainee", "Warrior"], 
#                          ["Ninja", "Trainee", "Warrior"]]

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.string players

#     Array of distinct strings, where each string is player name. Each name may 
#       consist of English letters and whitespace characters.

#     Guaranteed constraints:
#     1 ≤ players.length ≤ 10,
#     2 ≤ players[i].length ≤ 15.

#     [input] integer k

#     The number of players the coach should pick for the lineup.

#     Guaranteed constraints:
#     1 ≤ k ≤ players.length.

#     [output] array.array.string

#     Array of all possible lineups sorted as described above.

#%%

# * Solution 1
from itertools import combinations

def crazyball(players:list, k:int)-> list:
    return list(combinations(sorted(players), k))



a1 = ["Ninja", "Warrior", "Trainee", "Newbie"]
a2 = 3
r1 = crazyball(a1, a2)
print(r1)

# %%
