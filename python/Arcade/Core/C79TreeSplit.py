#
# * Core 79, Tree Split
# * Medium

# * You have a long strip of paper with integers written on it in a single line 
# * from left to right. You wish to cut the paper into exactly three pieces such 
# * that each piece contains at least one integer and the sum of the integers in 
# * each piece is the same. You cannot cut through a number, i.e. each initial 
# * number will unambiguously belong to one of the pieces after cutting. How many 
# * ways can you do it?

# It is guaranteed that the sum of all elements in the array is divisible by 3.

# Example

# For a = [0, -1, 0, -1, 0, -1], the output should be
# threeSplit(a) = 4.

# Here are all possible ways:

#     [0, -1] [0, -1] [0, -1]
#     [0, -1] [0, -1, 0] [-1]
#     [0, -1, 0] [-1, 0] [-1]
#     [0, -1, 0] [-1] [0, -1]

# Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.integer a

#     Guaranteed constraints:
#     5 ≤ a.length ≤ 104,
#     -108 ≤ a[i] ≤ 108.

#     [output] integer

#     It's guaranteed that for the given test cases the answer always fits signed 32-bit integer type.

#%%

# * Solution 1 
# ! TLE
def threeSplit1(a):
    n = len(a)
    count = 0
    for i in range(1, n):
        for j in range(i+1, n):
            if sum(a[0:i]) == sum(a[i:j]) == sum(a[j:]):
                count +=1

    return count


# * Solution 2
# * add memo
# ! TLE
def threeSplit2(a: list)->int:
    memo  = {}
    n = len(a)
    count = 0
    for i in range(1, n):
        for j in range(i+1, n):
            if (0, i) in memo:
                sum1 = memo[(0,i)]
            else:
                sum1 = sum(a[0:i])
                memo[(0,i)] = sum1
            
            if (i, j) in memo:
                sum2 = memo[(i, j)]
            else:
                sum2 = sum(a[i:j])
                memo[(i,j)] = sum2

            if (j, n) in memo:
                sum3 = memo[(j, n)]
            else:
                sum3 = sum(a[j:])
                memo[(j, n)] = sum3
            
            if sum1== sum2 == sum3:
                count +=1

    return count

# * Solution 3
# ! TLE
def threeSplit3(a:list)-> int:
    count = 0
    n = len(a)
    oneThird = sum(a)/3

    for i in range(1, n):
        sumi = sum(a[:i])
        if sumi == oneThird:
            for j in range(i+1, n):
                sumij = sum(a[i:j])
                if sumij == oneThird:
                    count +=1
                elif oneThird >= 0 and sumij > oneThird:
                    break
                elif oneThird < 0 and sumij < oneThird:
                    break
        elif oneThird >= 0 and sumi > oneThird:
            break
        elif oneThird < 0 and sumi < oneThird:
            break

    return count


# * Solution 4
# ! TLE
def threeSplit4(a:list)-> int:
    n = len(a)
    oneThird = sum(a)/3

    indexI = []
    i = 0
    sumI = 0
    while i < n-1:
        sumI += a[i]
        if sumI == oneThird:
            indexI.append(i+1)
        # elif (oneThird >= 0 and sumI > oneThird) or\
        #     (oneThird < 0 and sumI < oneThird):
        #     break
        i += 1

    indexJ = []
    j = n-1
    sumJ = 0
    while j > 1:
        sumJ += a[j]
        if sumJ == oneThird:
            indexJ.insert(0, j)
        # elif (oneThird >= 0 and sumJ > oneThird) or\
        #     (oneThird < 0 and sumJ < oneThird):
        #     break
        j -= 1

    print(indexI)
    print(indexJ)

    count = 0
    for i in indexI:
        count += len(list(filter(lambda x: x >i, indexJ)))
        
    return count


# * Solution 5
def threeSplit5(a:list)-> int:
    oneThird = sum(a)/3
    count = 0
    n = len(a)
    firstPartCount = 0
    currentSum = 0

    for i in range(n - 1):
        currentSum += a[i]
        if currentSum == oneThird:
            firstPartCount +=1
        if currentSum == 2* oneThird:
            count += firstPartCount
            if oneThird == 0:
                count -= 1

    return count


a1 = [0, -1, 0, -1, 0, -1]
r1 = threeSplit5(a1)
print('ex: 4, re:{}'.format(r1))

a1 = [-1, 0, -1, 0, -1, 0]
r1 = threeSplit5(a1)
print('ex: 4, re:{}'.format(r1))

a1 = [0, 0, 0, 0, 0]
r1 = threeSplit5(a1)
print('ex: 6, re:{}'.format(r1))

a1 = [-1, 1, -1, 1, -1, 1, -1, 1]
r1 = threeSplit5(a1)
print('ex: 3, re:{}'.format(r1))
