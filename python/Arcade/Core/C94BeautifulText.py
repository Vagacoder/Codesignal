#
# * Core 94. Beautiful Text
# * Medium

# * Consider a string containing only letters and whitespaces. It is allowed to 
# * replace some (possibly, none) whitespaces with newline symbols to obtain a 
# * multiline text. Call a multiline text beautiful if and only if each of its 
# * lines (i.e. substrings delimited by a newline character) contains an equal 
# * number of characters (only letters and whitespaces should be taken into account 
# * when counting the total while newline characters shouldn't). Call the length 
# * of the line the text width.

# Given a string and some integers l and r (l ≤ r), check if it's possible to 
# obtain a beautiful text from the string with a text width that's within the 
# range [l, r].

# * Example

#     For inputString = "Look at this example of a correct text", l = 5, and r = 15, the output should be
#     beautifulText(inputString, l, r) = true.

#     We can replace 13th and 26th characters with '\n', and obtain the following multiline text of width 12:

#     Look at this
#     example of a
#     correct text

#     For inputString = "abc def ghi", l = 4, and r = 10, the output should be
#     beautifulText(inputString, l, r) = false.

#     There are two ways to obtain a text with lines of equal length from this input, one has width = 3 and another has width = 11 (this is a one-liner). Both of these values are not within our bounds.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string inputString

#     Guaranteed constraints:
#     10 ≤ inputString.length ≤ 40.

#     [input] integer l

#     A positive integer.

#     Guaranteed constraints:
#     1 ≤ l ≤ r.

#     [input] integer r

#     A positive integer.

#     Guaranteed constraints:
#     l ≤ r ≤ 15.

#     [output] boolean

#%%

# * Solution 1
def beautifulText(inputString: str, l: int, r: int)-> bool:
    n = len(inputString)
    wsIndices = []
    for i in range(n):
        if inputString[i].isspace():
            wsIndices.append(i)
    
    print(n)
    print(wsIndices)

    for j in wsIndices:
        if  l <= j <= r:
            if n%(j+1) != j:
                continue
            good = True
            nextJ = j
            while good and nextJ < n :
                if not nextJ in wsIndices:
                    good = False
                nextJ += (j+1)
            if good:
                return True

    return False

# * Solution 2
def beautifulText2(inputString, l, r):
    for w in range(l, r+1):
        i = w
        while i < len(inputString):
            if inputString[i] != ' ':
                break
            i += w+1
        if i == len(inputString):
            return True
    return False

    

a1 = 'Look at this example of a correct text'
l1 = 5
r1 = 15
r1 = beautifulText(a1, l1, r1)
print(r1)

a1 = 'abc def ghi'
l1 = 4
r1 = 10
r1 = beautifulText(a1, l1, r1)
print(r1)

a1 = 'a a a a a a a a'
l1 = 1
r1 = 10
r1 = beautifulText(a1, l1, r1)
print(r1)

a1 = 'aa aa aaaaa aaaaa aaaaa'
l1 = 6
r1 = 11
r1 = beautifulText(a1, l1, r1)
print(r1)
