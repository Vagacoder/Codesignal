#
# * Python 52, Kth Permutation
# * Easy

# * You found your old bike in the attic, and would love to refresh your childhood 
# * memories and give it a ride. Unfortunately there is a chain lock on the bike, 
# * and the code is a permutation of a set of distinct numbers. Of course, you 
# * don't remember it after all these years.

# * You do remember, however, that the last time you picked up your bike you also 
# * couldn't remember the code, so had to run over all possible numbers permutations. 
# * Being a programmer, you tried them in the lexicographical order. It took you 
# * a couple of days, and in the first day you managed to check k - 1 permutations.

# Now that you need to open the lock again, you can start checking the permutations from the kth one. Given the list of numbers, return the kth (1-based) permutation that you should begin with.

# Example

# For numbers = [1, 2, 3, 4, 5] and k = 4, the output should be
# kthPermutation(numbers, k) = [1, 2, 4, 5, 3].

# Here are the first 4 permutations:

#     [1, 2, 3, 4, 5]
#     [1, 2, 3, 5, 4]
#     [1, 2, 4, 3, 5]
#     [1, 2, 4, 5, 3]

# Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.integer numbers

#     A sorted list of distinct integers.

#     Guaranteed constraints:
#     2 ≤ numbers.length ≤ 10,
#     1 ≤ numbers[i] ≤ 1000.

#     [input] integer k

#     The 1-based index of the first permutation that you should try.

#     Guaranteed constraints:
#     1 ≤ k ≤ numbers.length!.

#     [output] array.integer

#     The kth permutation of numbers.

#     Note: if your solution returns a tuple, it will be converted to list automatically.

#%%

# * Solution 1
from itertools import permutations

def kthPermutation1(numbers:list, k:int)->list:
    return list(permutations(sorted(numbers)))[k-1]


# * Solution 2
# ! itertools islice()
from itertools import islice

def kthPermutation2(numbers:list, k:int)->list:
    return next(islice(permutations(sorted(numbers)), k, None))


a1 = [1, 2, 3, 4, 5]
a2 = 4
r1 = kthPermutation2(a1, a2)
print(r1)


# %%
