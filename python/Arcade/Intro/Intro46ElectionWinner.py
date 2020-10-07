#
# * Intro 46. Election Winners
# * Medium

# * Elections are in progress!

# * Given an array of the numbers of votes given to each of the candidates so far, 
# * and an integer k equal to the number of voters who haven't cast their vote 
# * yet, find the number of candidates who still have a chance to win the election.

# * The winner of the election must secure strictly more votes than any other 
# * candidate. If two or more candidates receive the same (maximum) number of 
# * votes, assume there is no winner at all.

# * Example

# For votes = [2, 3, 5, 2] and k = 3, the output should be
# electionsWinners(votes, k) = 2.

#     The first candidate got 2 votes. Even if all of the remaining 3 candidates 
#       vote for him, he will still have only 5 votes, i.e. the same number as 
#       the third candidate, so there will be no winner.
#     The second candidate can win if all the remaining candidates vote for him 
#       (3 + 3 = 6 > 5).
#     The third candidate can win even if none of the remaining candidates vote 
#       for him. For example, if each of the remaining voters cast their votes for each of his opponents, he will still be the winner (the votes array will thus be [3, 4, 5, 3]).
#     The last candidate can't win no matter what (for the same reason as the 
#       first candidate).

# Thus, only 2 candidates can win (the second and the third), which is the answer.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.integer votes

#     A non-empty array of non-negative integers. Its ith element denotes the number of votes cast for the ith candidate.

#     Guaranteed constraints:
#     4 ≤ votes.length ≤ 105,
#     0 ≤ votes[i] ≤ 104.

#     [input] integer k

#     The number of voters who haven't cast their vote yet.

#     Guaranteed constraints:
#     0 ≤ k ≤ 105.

#     [output] integer

#%%

# ! Timeout
# * Solution 1
def electionsWinners1(votes: list, k:int)->int:
    # maxVote = max(votes)
    # print(maxVote)

    # newList = [x+k for x in votes]
    # print(newList)
    # result = filter(lambda x: x>maxVote, newList)
    # print(result)
    # print(list(result))
    # for x in result:
    #     print(x)

    if k == 0:
        return 0 if votes.count(max(votes))>1 else 1
    else:
        return len(list(filter(lambda x: x>max(votes), [x+k for x in votes])))


# * Solution 2
def electionsWinners2(votes: list, k:int)->int:
    maxVote = max(votes)
    newList = [x+k for x in votes]
    largeThanMax = 0
    equalToMax = 0

    for v in newList:
        if v > maxVote:
            largeThanMax += 1
        elif v == maxVote:
            equalToMax +=1

    if largeThanMax > 0:
        return largeThanMax
    elif equalToMax < 2:
        return equalToMax
    else:
        return 0


# * Solution 3, Improved from solution 1
def electionsWinners3(votes: list, k:int)->int:
    maxV = max(votes)
    if k == 0:
        return int(votes.count(maxV)==1)
    else:
        # ! list comprehesion
        return len([x for x in votes if x+k > maxV])



a1 = [2,3,5,2]
a2 = 3
e1 = 2
r1 = electionsWinners3(a1, a2)
print('For {}, {}, expected: {}, result: {}'.format(a1, a2, e1, r1))


a1 = [5, 1, 3, 4, 1]
a2 = 0
e1 = 1
r1 = electionsWinners3(a1, a2)
print('For {}, {}, expected: {}, result: {}'.format(a1, a2, e1, r1))
# %%
