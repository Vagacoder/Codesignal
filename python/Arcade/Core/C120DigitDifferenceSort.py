#
# * Core 120, Digit Difference Sort

# * Given an array of integers, sort its elements by the difference of their largest
# * and smallest digits. In the case of a tie, that with the larger index in the
# * array should come first.

# * Example

# For a = [152, 23, 7, 887, 243], the output should be
# digitDifferenceSort(a) = [7, 887, 23, 243, 152].

# Here are the differences of all the numbers:

#     152: difference = 5 - 1 = 4;
#     23: difference = 3 - 2 = 1;
#     7: difference = 7 - 7 = 0;
#     887: difference = 8 - 7 = 1;
#     243: difference = 4 - 2 = 2.

# 23 and 887 have the same difference, but 887 goes after 23 in a, so in the sorted array it comes first.

# Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.integer a

#     An array of integers.

#     Guaranteed constraints:
#     0 ≤ sequence.length ≤ 104,
#     1 ≤ sequence[i] ≤ 105.

#     [output] array.integer

#     Array a sorted as described above.

# %%

# * Solution 1
# ! TLE
def digitDifferenceSort(a: list) -> list:

    def difference(n: int) -> int:
        nStr = str(n)
        minD = int(nStr[0])
        maxD = int(nStr[0])
        for x in nStr:
            curD = int(x)
            if curD > maxD:
                maxD = curD
            if curD < minD:
                minD = curD
        return maxD - minD

    # for x in a:
    #     print(difference(x))

    # a.sort(key=difference)

    n = len(a)

    for i in range(1, n):
        for j in range(i, 0, -1):
            if difference(a[j]) <= difference(a[j-1]):
                a[j], a[j-1] = a[j-1], a[j]
            else:
                break

    return a


# * Solution 2
def digitDifferenceSort2(a: list) -> list:
    from functools import cmp_to_key

    def difference(n: int) -> int:
        nStr = str(n)
        minD = int(nStr[0])
        maxD = int(nStr[0])
        for x in nStr:
            if int(x) > maxD:
                maxD = int(x)
            if int(x) < minD:
                minD = int(x)
        return maxD - minD

    diffA = [difference(x) for x in a]

    # print(diffA)

    indexedDiffA = []

    for i, x in enumerate(diffA):
        indexedDiffA.append((i, x))

    # print(indexedDiffA)

    def cmptuple(t1, t2) -> int:
        if t1[1] != t2[1]:
            return t1[1] - t2[1]
        else:
            return t2[0] - t1[0]

    # indexedDiffA.sort(key=lambda x: x[1])
    indexedDiffA.sort(key=cmp_to_key(cmptuple))

    print(indexedDiffA)

    return [a[x[0]] for x in indexedDiffA]


# * Solution 3
def digitDifferenceSort3(a: list) -> list:

    def k(x):
        return int(max(str(x))) - int(min(str(x)))

    return sorted(a[::-1], key=k)


a1 = [152, 23, 7, 887, 243]
r1 = digitDifferenceSort3(a1)
print(r1)
