#
# * Core 66, Number of Clans
# * Medium

# * Let's call two integers A and B friends if each integer from the array divisors 
# * is either a divisor of both A and B or neither A nor B. If two integers are 
# * friends, they are said to be in the same clan. How many clans are the integers 
# * from 1 to k, inclusive, broken into?

# * Example

# For divisors = [2, 3] and k = 6, the output should be
# numberOfClans(divisors, k) = 4.

# The numbers 1 and 5 are friends and form a clan, 2 and 4 are friends and form a clan, and 3 and 6 do not have friends and each is a clan by itself. So the numbers 1 through 6 are broken into 4 clans.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.integer divisors

#     A non-empty array of positive integers.

#     Guaranteed constraints:
#     2 ≤ divisors.length < 10,
#     1 ≤ divisors[i] ≤ 10.

#     [input] integer k

#     A positive integer.

#     Guaranteed constraints:
#     5 ≤ k ≤ 10.

#     [output] integer

#%%

# * Solution 1
# ! Misunderstood. Well, the question description is hard to understand
def numberOfClans(divisors: list, k: int)->int:
    
    def isFriends(a: int, b: int, divisors:list)->bool:
        for d in divisors:
            if not((a%d == 0 and b%d == 0) or (a%d !=0 and b%d != 0)):
                return False
        return True

    # print(isFriends(1, 5, divisors))
    # print(isFriends(1, 2, divisors))

    count = 0
    dic = []
    clanMembers = set()
    for i in range(1, k):
        for j in range(i+1, k+1):
            if isFriends(i, j, divisors):
                count += 1
                dic.append((i, j))
                clanMembers.add(i)
                clanMembers.add(j)
    
    print('count', count)
    print('dic', dic)
    print('clan memebr', clanMembers)
    return count + (k - len(clanMembers))


# * Solution 2
def numberOfClans2(divisors: list, k: int)->int:
    s = set()
    for i in range(1, k+1):
        cur = ''
        for d in divisors:
            cur += '0' if(i%d == 0) else '1'
    
        print(cur)    
    
        s.add(cur)

    print(s)
    return len(s)


d1 = [2, 3]
k1 = 6
r1 = numberOfClans2(d1, k1)
print('ex: {}, re: {}'.format(4, r1))

# d1 = [2, 3, 4]
# k1 = 6
# r1 = numberOfClans(d1, k1)
# print('ex: {}, re: {}'.format(5, r1))

# d1 = [1, 3]
# k1 = 10
# r1 = numberOfClans(d1, k1)
# print('ex: {}, re: {}'.format(2, r1))

# d1 = [5, 6]
# k1 = 5
# r1 = numberOfClans(d1, k1)
# print('ex: {}, re: {}'.format(2, r1))


# d1 = [1, 2, 3]
# k1 = 8
# r1 = numberOfClans(d1, k1)
# print('ex: {}, re: {}'.format(4, r1))
