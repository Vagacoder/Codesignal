#
# * Python 83, Is Cool Team
# * Medium

# * You are organizing a team of eSportsmen, and you are determined to make it 
# * cool. You are already thinking about winning the world championship: when it 
# * happens, the names of your teammates will be chanted one after another by a 
# * large audience. You believe that it will sound cool if and only if the first 
# * letter of one player's name will be the same as the last letter in the name 
# * of the player before them.

# Now you are considering one particular team. Its members are definitely 
# professional gamers, but you're not sure if all together they form a cool team. 
# Implement a function that will check if the team is cool.

# * Example

# For team = ["Mark", "Kelly", "Kurt", "Terk"], the output should be
# isCoolTeam(team) = true.

# The following team announcement will sound cool: "Mark", "Kurt", "Terk", "Kelly".

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.string team

#     A list of team members, where each team member is given by their name (a string consisting of English characters). Note that there are no names which start and end on the same letter.

#     Guaranteed constraints:
#     1 ≤ team.length ≤ 100,
#     2 ≤ team[i].length ≤ 20.

#     [output] boolean

#     true if the team is cool, false otherwise.

#%%
import itertools

class Team(object):
    def __init__(self, names):
        self.names = names


    def __bool__(self):
        return self.isTeamCool3();

        
    # * Solution 1, Brute Force
    def isTeamCool1(self):
        permus = itertools.permutations(self.names)
        for permu in permus:
            permuList = list(permu)
            for i in range(1, len(permuList)):
                # print(permuList[i-1], permuList[i])
                if permuList[i-1][-1].lower() != permuList[i][0].lower():
                    break
            else:
                return True

        return False


    # * Solution 2, check in permutation
    def isTeamCool2(self):
        def getPermutation(l: list)->list:
            if len(l) <= 1:
                return [l]

            permutation = []
            
            for i, string in enumerate(l):
                
                # print('i, string:', i ,string)

                shortList = l[:i] + l[(i+1):]

                for shortP in getPermutation(shortList):
                    
                    # print('\t short P:', shortP)

                    if string[-1].lower() == shortP[0][0].lower():

                        tempList = [string]
                        
                        for stringInShortP in shortP:
                            tempList.append(stringInShortP)

                        # print('tempList', tempList)

                        permutation.append(tempList)
                
            return permutation
        
        return len(getPermutation(self.names)) > 0


    # * Solution 3, try DFS
    # ! Ennn, get some good hints from Comments section:
    # ? https://pastebin.com/az7gmEzb
    def isTeamCool3(self):
        namesLow = [i.lower() for i in self.names]
        
        letters = "abcdefghijklmnopqrstuvwxyz"
        FROM  = {i: [] for i in letters}
        TO    = {i: [] for i in letters}
        
        for i in letters:
            for j in namesLow:
                if i == j[-1]:
                    FROM[i].append(j) # Find names that lead to current letter
                if i == j[0]:
                    TO[i].append(j) # Find names that letter can lead to 
        
        
        # Debugging and visualizing the graph
        # for i in letters:
        #     print("____________________")
        #     print("Node: %s" % i)
        #     print("From: ", FROM[i])
        #     print("To: ", TO[i])
        
        print(FROM)
        print(TO)

        # ! Quick rule out impossible cases
        start = False
        end   = False
        for i in letters:
            if len(FROM[i]) + 1 == len(TO[i]):
                # Found the start!
                if start:
                    return False # Whoops, too many starts!
                start = True
            elif len(FROM[i]) == len(TO[i]) + 1:
                # Found the end!
                if end:
                    return False # Whoops, too many ends!
                end = True
            elif len(FROM[i]) != len(TO[i]):
                return False
        
        # * Check if graph is connected
        visited = {0}
        queue = [0]
        
        while queue:
            
            name = queue.pop(0)
            for ind, teammate in enumerate(namesLow):
                if ind in visited:
                    continue
                if namesLow[name][0] == teammate[-1]:
                    visited.add(ind)
                    queue.append(ind)
                elif namesLow[name][-1] == teammate[0]:
                    visited.add(ind)
                    queue.append(ind)
        
        return len(visited) == len(self.names) # Is everyone found?



def isCoolTeam(team):
    return bool(Team(team))


# * Helper from Intro 33, improved for Solution 2
# ! Permutation of list of string, AND check whether last char of i-1 == first char of i
def getPermutation(l: list)->list:
    if len(l) <= 1:
        return [l]

    permutation = []
    
    for i, string in enumerate(l):
        
        # print('i, string:', i ,string)

        shortList = l[:i] + l[(i+1):]

        for shortP in getPermutation(shortList):
            
            # print('\t short P:', shortP)

            if string[-1].lower() == shortP[0][0].lower():

                tempList = [string]
                
                for stringInShortP in shortP:
                    tempList.append(stringInShortP)

                # print('tempList', tempList)

                permutation.append(tempList)
        
    return permutation


team = ["Mark", "Kelly", "Kurt", "Terk"]
r1 = isCoolTeam(team)
print(r1)


# * tester for permutation
# print(getPermutation(["aa", "bb"]))
# print(getPermutation(["aba", "bbb", "bab"]))
print(getPermutation(team))
# %%
