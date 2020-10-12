#
# * Intro 57, File Name
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

# * Solution 1, this way is faster than #2, one loop + hash
def fileNaming1(names: list)-> list:
    fileNames = {}
    n = len(names)

    for i in range(n):
        name = names[i]
        # ! consider base name only one level down
        baseName = name.rsplit('(', 1)[0]


        if not name in fileNames:
            fileNames[name] = 0
            # ! need update base name as well
            if baseName != name and baseName in fileNames:
                fileNames[baseName] += 1
        else:
            fileNames[name] +=1
            # ! find newName, name + NO. may added before
            newName = names[i] + '(' + str(fileNames[name]) + ')'
            
            while newName in fileNames:
                fileNames[newName] += 1
                tokens = newName.rsplit('(',1)
                newName = tokens[0] + '(' + str(int(tokens[1].replace(')', ''))+1) + ')'

            fileNames[newName] = 0
            names[i] = newName
            
    return names


# * Solution 2, 
# ! nice but slower, 3 x loop
def fileNaming2(names):
    for i in range(len(names)):
        if names[i] in names[:i]:
            j=1
            while names[i]+"("+str(j)+")" in names[:i]:
                j+=1
            names[i]+="("+str(j)+")"
    return names


# a1 = ["doc", "doc", "image", "doc(1)", "doc"]
# e1 = ["doc", "doc(1)", "image", "doc(1)(1)", "doc(2)"]
# r1 = fileNaming1(a1.copy())
# print('For {}, expected: {}, result: {}'.format(a1, e1, r1))

# a1 = ["dd", "dd(1)", "dd(2)", "dd"]
# e1 = ["dd", "dd(1)", "dd(2)", "dd(3)"]
# r1 = fileNaming1(a1.copy())
# print('For {}, expected: {}, result: {}'.format(a1, e1, r1))

a1 = ["a(1)", "a(6)", "a", "a"]
e1 = ["a(1)", "a(6)", "a", "a(2)"]
r1 = fileNaming1(a1.copy())
print('For {}, expected: {}, result: {}'.format(a1, e1, r1))

# %%
