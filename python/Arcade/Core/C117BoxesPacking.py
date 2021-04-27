#
# * Core 117, Boxes Packing
# * Medium

# * You are given n rectangular boxes, the ith box has the length lengthi, the 
# * width widthi and the height heighti. Your task is to check if it is possible 
# * to pack all boxes into one so that inside each box there is no more than one 
# * another box (which, in turn, can contain at most one another box, and so on). 
# * More formally, your task is to check whether there is such sequence of n 
# * different numbers pi (1 ≤ pi ≤ n) that for each 1 ≤ i < n the box number pi 
# * can be put into the box number pi+1.

# A box can be put into another box if all sides of the first one are less than 
# the respective ones of the second one. You can rotate each box as you wish, i.e. 
# you can swap its length, width and height if necessary.

# * Example

#     For length = [1, 3, 2], width = [1, 3, 2], and height = [1, 3, 2], the output should be
#     boxesPacking(length, width, height) = true;
#     For length = [1, 1], width = [1, 1], and height = [1, 1], the output should be
#     boxesPacking(length, width, height) = false;
#     For length = [3, 1, 2], width = [3, 1, 2], and height = [3, 2, 1], the output should be
#     boxesPacking(length, width, height) = false.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.integer length

#     Array of positive integers.

#     Guaranteed constraints:
#     1 ≤ length.length ≤ 104,
#     1 ≤ length[i] ≤ 2 · 104.

#     [input] array.integer width

#     Array of positive integers.

#     Guaranteed constraints:
#     width.length = length.length,
#     1 ≤ width[i] ≤ 2 · 104.

#     [input] array.integer height

#     Array of positive integers.

#     Guaranteed constraints:
#     height.length = length.length,
#     1 ≤ height[i] ≤ 2 · 104.

#     [output] boolean

#     true if it is possible to put all boxes into one, false otherwise.

#%%

# * Solution 1
# ! For no rotation
def boxesPacking1(length: list, width: list, height: list) -> bool:
    lengthSorted = sorted(length)
    print(lengthSorted)
    for i in range(len(lengthSorted)):
        if i!=0:
            if lengthSorted[i-1] >= lengthSorted[i]:
                print(i)
                return False
            index = length.index(lengthSorted[i])
            indexBefore = length.index(lengthSorted[i-1])
            if width[indexBefore] >= width[index]:
                print('width')
                print(i)
                print(index)
                print(indexBefore)
                return False
            if height[indexBefore] >= height[index]:
                print('height')
                print(i)
                print(index)
                print(indexBefore)
                return False
            
    return True


# * Solution 2
# ! For rotatable
def boxesPacking2(length: list, width: list, height: list) -> bool:
    boxes = zip(length, width, height)
    sortedBoxes = []
    for box in boxes:
        # print(sorted([*box]))
        sortedBoxes.append(sorted([*box]))
    
    doubleSorted = sorted(sortedBoxes, key=lambda x: x[0])

    # print(doubleSorted)

    for i in range(1, len(doubleSorted)):
        for j in range(3):
            if doubleSorted[i-1][j] >= doubleSorted[i][j]:
                return False

    return True
    

a1 = [1,3,2]
b1 = [1,3,2]
c1 = [1,3,2]
r1 = boxesPacking2(a1, b1, c1)
print(r1)

a1 = [1,1]
b1 = [1,1]
c1 = [1,1]
r1 = boxesPacking2(a1, b1, c1)
print(r1)

a1 = [3,1,2]
b1 = [3,1,2]
c1 = [3,2,1]
r1 = boxesPacking2(a1, b1, c1)
print(r1)

a1 = [5, 7, 4, 1, 2]
b1 = [4, 10, 3, 1, 4]
c1 = [6, 5, 5, 1, 2]
r1 = boxesPacking2(a1, b1, c1)
print(r1)