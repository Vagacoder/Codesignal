#
# * Python 51, Rock, Paper, Scissor
# * Easy

# * The greatest ever Rock-Paper-Scissors Championship will take place in your 
# * town! The best players will battle each other to see who's the best player in 
# * the world. Each player will compete against each other player twice, once home 
# * and once away.

# Given the list of the players, your task is to come up with the list of all the 
# games between them, and return them sorted lexicographically.

# * Example

# For players = ["trainee", "warrior", "ninja"], the output should be

# rockPaperScissors(players) = [["ninja", "trainee"], ["ninja", "warrior"], 
#                               ["trainee", "ninja"], ["trainee", "warrior"], 
#                               ["warrior", "ninja"], ["warrior", "trainee"]]

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.string players

#     A list of distinct players, where each player is given by their nickname that can consist of English letters and whitespace characters.

#     Guaranteed constraints:
#     2 ≤ players.length ≤ 10,
#     1 ≤ players[i].length ≤ 50.

#     [output] array.array.string

#     Array of pairs of players that will play against one another sorted lexicographically.

#     Note: if your solution returns a list of tuples, the tuples will be converted to list automatically.

#%%

# * Solution 1
from itertools import permutations

def rockPaperScissors(players):
    return sorted([list(x) for x in permutations(players, 2)])


a1 = ["trainee", "warrior", "ninja"]
r1 = rockPaperScissors(a1)
print(r1)

# %%
