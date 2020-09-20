#
# * Intro 11 isLucky
# * Easy

# * Ticket numbers usually consist of an even number of digits. A ticket number 
# * is considered lucky if the sum of the first half of the digits is equal to 
# * the sum of the second half.

# * Given a ticket number n, determine if it's lucky or not.

# * Example

#     For n = 1230, the output should be
#     isLucky(n) = true;
#     For n = 239017, the output should be
#     isLucky(n) = false.

# Input/Output

#     [execution time limit] 3 seconds (java)

#     [input] integer n

#     A ticket number represented as a positive integer with an even number of digits.

#     Guaranteed constraints:
#     10 ≤ n < 106.

#     [output] boolean

#     true if n is a lucky ticket number, false otherwise.

#%%

# * Solution 1
def isLucky(n: int) -> bool:
    strN = str(n)
    # print(strN)
    # print(type(strN))

    length = len(strN)
    if length%2 == 1:
        return False
    
    nList = list(strN)
    # print(nList)

    sumFirst = 0
    for i in range(length//2):
        sumFirst+= int(nList[i])

    sumSecond = 0
    for i in range(length//2, length):
        sumSecond+= int(nList[i])

    return sumFirst == sumSecond


# * Solution 2
def isLucky2(n: int)-> int:
    strN = str(n)
    mid = len(strN)//2
    firstHalf = strN[:mid]
    secondHalf = strN[mid:]
    firstSum = sum([int(i) for i in firstHalf])
    secondSum = sum([int(i) for i in secondHalf])
    return firstSum == secondSum



# * Solution 3
def isLucky3(n: int)-> int:
    strN = str(n)
    mid = len(strN)//2
    firstHalf = strN[:mid]
    secondHalf = strN[mid:]

    # ! map()
    firstSum = sum(map(lambda i: int(i), firstHalf))
    secondSum = sum(map(lambda i: int(i), secondHalf))
    return firstSum == secondSum


# ! Solution 4
def isLucky4(n: int)-> int:
    strN = str(n)
    length = len(strN)
    mid = len(strN)//2
    sum = 0
    for i in range(mid):
        sum += (int(strN[i]) - int(strN[length-i-1]))
    
    return sum == 0
    

n1 = 1230
r1 = isLucky4(n1)
print('{}:\texpected: {},\tresult: {}'.format(n1, True, r1))

n2 = 239017
r2 = isLucky4(n2)
print('{}:\texpected: {},\tresult: {}'.format(n2, False, r2))

n3 = 134008
r3 = isLucky4(n3)
print('{}:\texpected: {},\tresult: {}'.format(n3, True, r3))

n4 = 10
r4 = isLucky4(n4)
print('{}:\texpected: {},\tresult: {}'.format(n4, False, r4))

# %%
