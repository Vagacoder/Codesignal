#
# * Python 68, Calkin Wilf Sequence
# * Medium

# * The Calkin-Wilf tree is a tree in which the vertices correspond 1-for-1 to 
# * the positive rational numbers. The tree is rooted at the number 1, and any 
# * rational number expressed in simplest terms as the fraction a / b has as its 
# * two children the numbers a / (a + b) and (a + b) / b. Every positive rational 
# * number appears exactly once in the tree. Here's what it looks like:

#  https://codesignal.s3.amazonaws.com/tasks/calkinWilfSequence/img/tree.png?_tm=1581999820267

# * The Calkin-Wilf sequence is the sequence of rational numbers generated by a 
# * breadth-first traversal of the Calkin-Wilf tree, where the vertices of the 
# * same level are traversed from left to right (as displayed in the image above). 
# * The sequence thus also contains each rational number exactly once, and can 
# * be represented as follows:

# https://codesignal.s3.amazonaws.com/tasks/calkinWilfSequence/img/sequence.png?_tm=1581999820553

# * Given a rational number, your task is to return its 0-based index in the Calkin-
# * Wilf sequence.

# * Example

# For number = [1, 3], the output should be
# calkinWilfSequence(number) = 3.

# As you can see in the image above, 1 / 3 is the 3rd 0-based number in the sequence.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.integer number

#     A positive rational number given as a reduced fraction.

#     Guaranteed constraints:
#     number.length = 2,
#     1 ≤ number[0] < 7595,
#     1 ≤ number[1] < 2100.

#     [output] integer

#     The 0-based index of the number in the Calkin-Wilf sequence.

#     It is guaranteed that the answer is not greater than 106.

#%%

# * Solution 1
# ! Dynamic programming
def calkinWilfSequence1(number:list)-> int:
    def fractions():
        a = 1
        b = 1
        number = 1
        thisRow = [[a, b]]
        yield thisRow[0]


        while True:
            number *= 2
            nextRow = [[0,0] for _ in range(number)]

            # print('thisRow', thisRow)
            # print('nextRow', nextRow)

            for i in range(0, number,2):
                # print('i', i)

                nextRow[i][0] = thisRow[i//2][0]
                nextRow[i][1] = thisRow[i//2][0] + thisRow[i//2][1]
                nextRow[i+1][0] = thisRow[i//2][0] + thisRow[i//2][1]
                nextRow[i+1][1] = thisRow[i//2][1]

            for i in range(number):
                yield nextRow[i]
            
            thisRow = nextRow
            # number *= 2
            # nextRow = [[0,0] for _ in range(number)]

    gen = fractions()
    res = 0
    while next(gen) != number:
        res += 1
    return res


# * Solution 2
# ! Smart math
def calkinWilfSequence2(number:list)-> int:
    def fractions():
        a = 1
        b = 1
        while True:
            yield [a, b]
            temp = a
            a = b
            b = temp - 2*(temp%b) + b


    gen = fractions()
    res = 0
    while next(gen) != number:
        res += 1
    return res


a1 = [7, 3]
r1 = calkinWilfSequence2(a1)
print(r1)

# %%
