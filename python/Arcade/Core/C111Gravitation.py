#
# * Core 111, Gravitation
# * Medium

# * You are given a vertical box divided into equal columns. Someone dropped 
# * several stones from its top through the columns. Stones are falling straight 
# * down at a constant speed (equal for all stones) while possible (i.e. while 
# * they haven't reached the ground or they are not blocked by another motionless 
# * stone). Given the state of the box at some moment in time, find out which 
# * columns become motionless first.

# * Example

# For

# rows = ["#..##",
#         ".##.#",
#         ".#.##",
#         "....."]

# the output should be gravitation(rows) = [1, 4].

# Check out the image below for better understanding:

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.string rows

#     A non-empty array of strings of equal length consisting only of #-s and .-s describing the box at a specific moment in time. Sharps represent stones, and dots represent empty cells. row[0] corresponds to the upper row. Last element of rows corresponds to the ground level.

#     Guaranteed constraints:
#     2 ≤ rows.length ≤ 100,
#     2 ≤ rows[i].length ≤ 100.

#     [output] array.integer

#     A sorted array containing numbers of all columns (leftmost column's number is 0) in which movements will stop at the same second and earlier than in any other column. Assume that if there are no stones in a column then movement stops immediately, i.e. after 0 seconds.


#%%

# * Solution 1
def gravitation(rows: list) -> list:
    n = len(rows)
    m = len(rows[0])

    def checkCol(j: int)-> int:
        count = 0
        isCounting = False
        for i in range(n):
            if not isCounting and rows[i][j] == '#':
                isCounting = True
            elif isCounting and rows[i][j] == '.':
                count += 1
        
        return count

    counts = []
    for j in range(m):
        counts.append(checkCol(j))

    # print(counts)

    minCount = min(counts)

    # print(list(enumerate(counts)))

    return [i for i, x in enumerate(counts) if x == minCount]


# * Solution 2
def gravitation2(rows):
    t = [''.join(r).lstrip('.').count('.') for r in zip(*rows)]
    return [i for i in range(len(t)) if t[i] == min(t)]



a1 = ["#..##",
      ".##.#",
      ".#.##",
      "....."]
r1 = gravitation(a1)
print(r1)
