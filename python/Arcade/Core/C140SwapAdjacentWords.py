#
# * Core 140. Swap Adjacent Words

# You are given a string consisting of words separated by whitespace characters, 
# where the words consist only of English letters. Your task is to swap pairs of 
# consecutive words and return the result.

# * Example

#     For s = "CodeFight On", the output should be
#     swapAdjacentWords(s) = "On CodeFight";
#     For s = "How are you today guys", the output should be
#     swapAdjacentWords(s) = "are How today you guys".

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string s

#     A string consisting of whitespace characters (' ') and English letters. There is exactly one whitespace character between two consecutive words, and both the first and the last characters of s are not equal to ' '.

#     Guaranteed constraints:
#     0 ≤ s.length ≤ 100.

#     [output] string

#     String s with pairs of adjacent words swapped.

#%%

# * Solution 1
import re

def swapAdjacentWords(s: str)-> str:
    # return re.sub('(\w+)\s(\w+)', lambda a: ' '.join(a.toString().split(' ').reverse()), s)
    # return re.sub('(\w+)\s(\w+)', lambda a: print(a), s)
    # return re.sub('(\w+)\s(\w+)', lambda a: print(a.group(0)), s)
    return re.sub('(\w+)\s(\w+)', lambda a: a.group(0).split(' ')[1] + ' ' + a.group(0).split(' ')[0], s)


def swapAdjacentWords2(s: str)-> str:
    # ! these two do not work
    # return re.sub('(\w+)\s(\w+)', '\2\s\1', s)
    # return re.sub('(\w+)\s(\w+)', '\2 \1', s)
    # ! this one works, 1st \ escape in string, 2nd \ escape in regex
    return re.sub('(\w+)\s(\w+)', '\\2 \\1', s)

    # ! this one ussing raw string, no need escape for string
    # return re.sub('(\w+)\s(\w+)', r'\2 \1', s)


s1 = 'How are you today guys'
r1 = swapAdjacentWords2(s1)
print(r1)
