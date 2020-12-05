#
# * Core 09, Reach Next Level
# * Easy

# * You are playing an RPG game. Currently your experience points (XP) total is 
# * equal to experience. To reach the next level your XP should be at least at 
# * threshold. If you kill the monster in front of you, you will gain more experience 
# * points in the amount of the reward.

# Given values experience, threshold and reward, check if you reach the next level 
#   after killing the monster.

# * Example

#     For experience = 10, threshold = 15, and reward = 5, the output should be
#     reachNextLevel(experience, threshold, reward) = true;
#     For experience = 10, threshold = 15, and reward = 4, the output should be
#     reachNextLevel(experience, threshold, reward) = false.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] integer experience

#     Guaranteed constraints:
#     3 ≤ experience ≤ 250.

#     [input] integer threshold

#     Guaranteed constraints:
#     5 ≤ threshold ≤ 300.

#     [input] integer reward

#     Guaranteed constraints:
#     2 ≤ reward ≤ 65.

#     [output] boolean

#     true if you reach the next level, false otherwise.

#%%

# * Solution 1
def reachNextLevel(experience, threshold, reward):
    return threshold - experience <= reward


e1 = 10
t1 = 15
re1 = 5
r1 = reachNextLevel(e1, t1, re1)
print(r1)

