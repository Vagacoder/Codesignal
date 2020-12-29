#
# * Core 489, Weak Numbers
# * Easy

# * We define the weakness of number x as the number of positive integers smaller 
# * than x that have more divisors than x.

# It follows that the weaker the number, the greater overall weakness it has. For 
# the given integer n, you need to answer two questions:

#     what is the weakness of the weakest numbers in the range [1, n]?
#     how many numbers in the range [1, n] have this weakness?

# Return the answer as an array of two elements, where the first element is the 
# answer to the first question, and the second element is the answer to the second question.

# * Example

# For n = 9, the output should be
# weakNumbers(n) = [2, 2].

# Here are the number of divisors and the specific weakness of each number in range [1, 9]:

#     1: d(1) = 1, weakness(1) = 0;
#     2: d(2) = 2, weakness(2) = 0;
#     3: d(3) = 2, weakness(3) = 0;
#     4: d(4) = 3, weakness(4) = 0;
#     5: d(5) = 2, weakness(5) = 1;
#     6: d(6) = 4, weakness(6) = 0;
#     7: d(7) = 2, weakness(7) = 2;
#     8: d(8) = 4, weakness(8) = 0;
#     9: d(9) = 3, weakness(9) = 2.

# As you can see, the maximal weakness is 2, and there are 2 numbers with that weakness level.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] integer n

#     Guaranteed constraints:
#     1 ≤ n ≤ 1000.

#     [output] array.integer

#     Array of two elements: the weakness of the weakest number, and the number 
#       of integers in range [1, n] with this weakness.

#%%

# * Solution 1
def weakNumbers(n:int)-> list:

    def findDivisorNumber(n:int):
        if n == 1:
            return 1
        if n == 4:
            return 3
        count = 2
        for i in range(2,n//2):
            if n%i == 0:
                if n/i != i:
                    count += 2
                else:
                    count += 1

        return count


    divsiorNumber = [-1] * (n+1)
    for i in range(1, n+1):
        divsiorNumber[i] = findDivisorNumber(i)

    # print(divsiorNumber)

    weakness = [-1] * (n+1)

    for i in range(1, n+1):
        count = 0
        for j in range(1, i):
            if divsiorNumber[j] > divsiorNumber[i]:
                count += 1
        weakness[i] = count
    
    weakest = max(weakness)
    # print(weakest)
    count = weakness.count(weakest)

    return [weakest, count]

    
# * Solution 2
def weakNumbers2(n:int)-> list:
    d = [sum(i%j==0 for j in range(1,i+1)) for i in range(1,n+1)]
    w = [sum(j>m for j in d[:i]) for i,m in enumerate(d)]
    return [max(w),w.count(max(w))]



n1 = 9
r1 = weakNumbers(n1)
print(r1)

n1 = 500
r1 = weakNumbers(n1)
print(r1)

n1 = 4
r1 = weakNumbers(n1)
print(r1)
