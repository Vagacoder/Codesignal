#
# * Python 82, Sort Codesignal Users
# * Easy

# * At CodeSignal the users can get to the top of the leaderboard by earning XP 
# * (experience points) in different modes. The leaderboard is sorted by players 
# * XP in descending order, and in case of a tie - by their ids in ascending order.

# Your task is to implement an algorithm that will return the state of the weekly 
# leaderboard given a list of users.

# * Example

# For

# users = [["warrior", "1", "1050"],
#          ["Ninja!",  "21", "995"],
#          ["recruit", "3", "995"]]

# the output should be
# sortCodesignalUsers(users) = ["warrior", "recruit", "Ninja!"].

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.array.string users

#     A list of CodeSignal users, where each user is given in the format [username, id, xp].
#     It is guaranteed that all usernames and ids are unique.

#     Guaranteed constraints:
#     0 ≤ users.length ≤ 104,
#     users[i].length = 3,
#     1 ≤ users[i][0].length ≤ 20,
#     1 ≤ int(users[i][1]), int(users[i][2]) ≤ 104.

#     [output] array.string

#     A list of CodeSignal users sorted as described above.

#%%

def sortCodesignalUsers(users: list)-> list:
    res = [CodeSignalUser(*user) for user in users]
    res.sort(reverse=True)
    return list(map(str, res))


class CodeSignalUser(object):
    
    def __init__(self, username, id, xp):
        self.username = username
        self.id = int(id)
        self.xp = int(xp)

    
    def __lt__(self, other):
        return self.lessThan2(other)


    # * Solution 1, regular
    def lessThan1(self, other):
        if other.xp > self.xp:
            return True
        elif other.xp == self.xp:
            return other.id < self.id
        else:
            return False


    # ! Solution 2, tuple comparison
    def lessThan2(self, other):
        return (self.xp, other.id) < (other.xp, self.id)


    def __str__(self):
        return self.username


users = [["warrior", "1", "1050"], ["Ninja!",  "21", "995"], ["recruit", "3", "995"]]
r1 = sortCodesignalUsers(users)
print(r1)

users = [["Corrie","66","5"], 
 ["Arie","99","8"], 
 ["Joann","32","5"], 
 ["Larhonda","9","9"], 
 ["Leda","38","7"], 
 ["Anabel","68","3"], 
 ["Javier","10","7"], 
 ["Vicente","49","9"], 
 ["Deanna","29","6"], 
 ["Tracie","28","7"], 
 ["Stephaine","1","8"], 
 ["Yaeko","2","10"], 
 ["Jared","27","8"], 
 ["Fernando","55","10"], 
 ["Sarita","90","9"], 
 ["Erlene","35","2"], 
 ["Kandace","12","9"], 
 ["Jeane","37","7"], 
 ["Malika","80","4"], 
 ["Malinda","92","7"]]
r1 = sortCodesignalUsers(users)
print(r1)

# %%
