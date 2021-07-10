#
# * Core 152. Count Elements
#

# * You've been invited to a job interview at a famous company that tests programming 
# challenges. To evaluate your coding skills, they have asked you to parse a given 
# problem's input given as an inputString string, and count the number of primitive 
# type elements within it.

# The inputString can be either a primitive type variable or an array (possibly 
# multidimensional) that contains elements of the primitive types.
# A primitive type variable can be:

#     an integer number;
#     a string, which is surrounded by " characters (note that it may contain any 
#       character except ");
#     a boolean, which is either true or false.

# Return the total number of primitive type elements inside inputString.

# Example

#     For inputString = "[[0, 20], [33, 99]]", the output should be
#     countElements(inputString) = 4;
#     For inputString = "[ "one", 2, "three" ]", the output should be
#     countElements(inputString) = 3;
#     For inputString = "true", the output should be
#     countElements(inputString) = 1;
#     For inputString = "[[1, 2, [3]], 4]", the output should be
#     countElements(inputString) = 4.

# Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string inputString

#     Correct input of a given problem.

#     Guaranteed constraints:
#     2 ≤ inputString.length ≤ 60.

#     [output] integer

#     The total number of primitive type elements within the input.

#%%
import re

# * Solution 1
# ! using exec() to execute a STATEMENT
def countElements1(inputString: str) -> int:
    updatedInput = inputString.replace('[', '')
    updatedInput = updatedInput.replace(']', '')
    updatedInput = updatedInput.replace('true', 'True')
    updatedInput = updatedInput.replace('false', 'False')
    print(updatedInput)

    # a = []
    # print(a)
    newArray = 'a=[' + updatedInput + ']'
    # print(newArray)
    lcls = locals()
    exec(newArray, globals(), lcls)
    a = lcls['a']
    # print(a)

    # * try eval()
    # a = eval('[' + updatedInput + ']')
    return len(a)


# * Solution 2
# ! using eval() to execute a EXPRESSION
def countElements2(S:str) -> int:
    S = S.replace('true','True')
    S = S.replace('false','False')
    T = eval(S)
    print(T)
    def count(A):
        ans = 0
        if type(A) in [int,str,bool]:
            return 1
        for x in A:
            if type(x) in [int,str,bool]:
                ans += 1
            else:
                ans += count(x)
        return ans
    return count(T)


# * Solution 3
def countElements(inputString: str) -> int:
    # ! NOTE: .*? is non-greedy for *
    X = re.findall(r'\".*?\"|\d+|true|false', inputString)
   
    # ! another regex
    # X = re.findall(r'(\"[^\"]*\"|\d+|true|false)', inputString)

    print(X)
    return len(X)



i1 = '[]'
r1 = countElements(i1)
print(r1)

i1 = '[[0, 20], [33, 99]]'
r1 = countElements(i1)
print(r1)

i1 = '[ "one", 2, "three" ]'
r1 = countElements(i1)
print(r1)

i1 = "true"
r1 = countElements(i1)
print(r1)

i1 = '[[1, 2, [3]], 4]'
r1 = countElements(i1)
print(r1)

i1 = '[[1, "two, three", [4]], "true", true]'
r1 = countElements(i1)
print(r1)
