#
# * Core 65, Most Frequenct Digit Sum
# * Medium

# * A step(x) operation works like this: it changes a number x into x - s(x), 
# * where s(x) is the sum of x's digits. You like applying functions to numbers, 
# * so given the number n, you decide to build a decreasing sequence of numbers: 
# * n, step(n), step(step(n)), etc., with 0 as the last element.

# Building a single sequence isn't enough for you, so you replace all elements of 
# the sequence with the sums of their digits (s(x)). Now you're curious as to which 
# number appears in the new sequence most often. If there are several answers, 
# return the maximal one.

# * Example

#     For n = 88, the output should be
#     mostFrequentDigitSum(n) = 9.
#         Here is the first sequence you built: 88, 72, 63, 54, 45, 36, 27, 18, 9, 0;
#         And here is s(x) for each of its elements: 16, 9, 9, 9, 9, 9, 9, 9, 9, 0.

#     As you can see, the most frequent number in the second sequence is 9.

#     For n = 8, the output should be
#     mostFrequentDigitSum(n) = 8.
#         At first you built the following sequence: 8, 0
#         s(x) for each of its elements is: 8, 0

#     As you can see, the answer is 8 (it appears as often as 0, but is greater than it).

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] integer n
#     Guaranteed constraints:
#     1 ≤ n ≤ 105.

#     [output] integer
#     The most frequent number in the sequence s(n), s(step(n)), s(step(step(n))), etc.

#%%

# * Solution 1
def mostFrequentDigitSum(n: int) -> int:

    # * helper 
    def s(n:int) -> int:
        sum = 0
        while n > 0:
            sum += n%10
            n //= 10

        return sum


    # numbers = []
    # numbers.append(n)
    sx = []

    while n > 0:
        sn = s(n)
        sx.append(sn)
        n = n - sn
        # numbers.append(n)
    
    sx.append(0)

    # print(numbers)
    print(sx)

    count = {}
    for x in sx:
        if x in count:
            count[x] += 1
        else:
            count[x] = 1
    
    maxKey = float('-inf')
    maxValue = float('-inf')
    for k, v in count.items():
        if v > maxValue or (v == maxValue and k > maxKey):
            maxValue = v
            maxKey = k

    return maxKey




a1 = 88
r1 = mostFrequentDigitSum(a1)
print(r1)

a1 = 17
r1 = mostFrequentDigitSum(a1)
print(r1)

# a1 = 99999
# r1 = mostFrequentDigitSum(a1)
# print(r1)


# %%
