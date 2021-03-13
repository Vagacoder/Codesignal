#
# * Core 97, File Name, Same as Intro 57.
# * Medium

# * You are given an array of desired filenames in the order of their creation. 
# * Since two files cannot have equal names, the one which comes later will have 
# * an addition to its name in a form of (k), where k is the smallest positive 
# * integer such that the obtained name is not used yet.

# * Return an array of names that will be given to the files.

# * Example

# For names = ["doc", "doc", "image", "doc(1)", "doc"], the output should be
# fileNaming(names) = ["doc", "doc(1)", "image", "doc(1)(1)", "doc(2)"].

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.string names

#     Guaranteed constraints:
#     5 ≤ names.length ≤ 1000,
#     1 ≤ names[i].length ≤ 15.

#     [output] array.string

#%%

# * Solution 1
def fileNaming(names):
    for i in range(len(names)):
        if names[i] in names[:i]:
            j=1
            while names[i]+"("+str(j)+")" in names[:i]:
                j+=1
            names[i]+="("+str(j)+")"
    return names


a1 = ["doc", "doc", "image", "doc(1)", "doc"]
r1 = fileNaming(a1)
print(r1)
