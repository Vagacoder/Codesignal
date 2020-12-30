#
# * Core 49, Rectngel Rotation
# * Medium

# # * A rectangle with sides equal to even integers a and b is drawn on the Cartesian 
# * plane. Its center (the intersection point of its diagonals) coincides with 
# * the point (0, 0), but the sides of the rectangle are not parallel to the axes; 
# * instead, they are forming 45 degree angles with the axes.

# How many points with integer coordinates are located inside the given rectangle 
# (including on its sides)?

# * Example

# For a = 6 and b = 4, the output should be
# rectangleRotation(a, b) = 23.

# The following picture illustrates the example, and the 23 points are marked green.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] integer a

#     A positive even integer.

#     Guaranteed constraints:
#     2 ≤ a ≤ 50.

#     [input] integer b

#     A positive even integer.

#     Guaranteed constraints:
#     2 ≤ b ≤ 50.

#     [output] integer

#     The number of inner points with integer coordinates.

#%%
import math

# * Solution 1
# ! NOT working
def rectangleRotation1(a:int, b:int)->int:

    def findMaxNumberOfPoints(n:int)->int:
        count = 0
        dLength = math.sqrt(2)
        totalLength = 0
        while totalLength <= n:
            totalLength += dLength
            count += 1
        
        return count

    
    maxPointsOnA = findMaxNumberOfPoints(a)
    maxPointsOnB = findMaxNumberOfPoints(b)
    
    print(maxPointsOnA)
    print(maxPointsOnB)

    pointsOnA = maxPointsOnA * 2 - 1
    pointsOnB = maxPointsOnB * 2 - 1

    print(pointsOnA)
    print(pointsOnB)

    count = 0
    
    # if (pointsOnA-1)/2%2 == 0 :
    #     for i in range(pointsOnA):
    #         if i%2 == 0:
    #             count += maxPointsOnB
    #         else:
    #             count += maxPointsOnB - 1
    # else:
    #     for i in range(pointsOnA):
    #         if i%2 == 0:
    #             count += maxPointsOnB - 1
    #         else:
    #             count += maxPointsOnB

    for i in range(pointsOnA):
        if i%2 == 0:
            count += maxPointsOnB
        else:
            count += maxPointsOnB - 1



    return count

# * Solution 2
# ! Great
def rectangleRotation2(a:int, b:int)->int:

    def findMaxNumberOfPoints(n:int)->int:
        return int(n // math.sqrt(2))

    
    maxPointsOnA = findMaxNumberOfPoints(a)
    maxPointsOnB = findMaxNumberOfPoints(b)
    
    print(maxPointsOnA)
    print(maxPointsOnB)

    return (2*maxPointsOnA*maxPointsOnB + maxPointsOnA + maxPointsOnB) | 1

# * Solution 3
# ! Great
def rectangleRotation3(a, b):
    [m, n] = [int(math.floor(x / math.sqrt(2))) for x in (a, b)]
    return m * n + (m + 1) * (n + 1) - (m + n) % 2


a1 = 6
b1 = 4 
r1 = rectangleRotation2(a1, b1)
print('ex: {}, res: {}'.format(23, r1))

a1 = 30
b1 = 2
r1 = rectangleRotation2(a1, b1)
print('ex: {}, res: {}'.format(65, r1))

a1 = 8
b1 = 6
r1 = rectangleRotation2(a1, b1)
print('ex: {}, res: {}'.format(49, r1))

a1 = 20
b1 = 32
r1 = rectangleRotation2(a1, b1)
print('ex: {}, res: {}'.format(653, r1))

a1 = 2
b1 = 2
r1 = rectangleRotation2(a1, b1)
print('ex: {}, res: {}'.format(5, r1))

# %%
