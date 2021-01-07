#
# * Core 56. HTML End Tag by Start Tag
# * Easy

# * You are implementing your own HTML editor. To make it more comfortable for 
# * developers you would like to add an auto-completion feature to it.

# * Given the starting HTML tag, find the appropriate end tag which your editor should propose.

# If you are not familiar with HTML, consult with this note.

# * Example

#     For startTag = "<button type='button' disabled>", the output should be
#     htmlEndTagByStartTag(startTag) = "</button>";
#     For startTag = "<i>", the output should be
#     htmlEndTagByStartTag(startTag) = "</i>".

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string startTag

#     Guaranteed constraints:
#     3 ≤ startTag.length ≤ 75.

#     [output] string

#%%

# * Solution 1
def htmlEndTagByStartTag1(startTag:str)-> str:
    return '</' + startTag.split()[0][1:].split('>')[0] + '>'



# * Solution 2
import re
def htmlEndTagByStartTag2(startTag: str)-> str:
    return '</' + re.findall('<(\S*)\s*.*>', startTag)[0] + '>'


a1 = "<div id='my_area' class='data' title='This is a test for title on Div tag'>"
r1 = htmlEndTagByStartTag2(a1)
print(r1)

a1 = "<html>"
r1 = htmlEndTagByStartTag2(a1)
print(r1)


# %%
