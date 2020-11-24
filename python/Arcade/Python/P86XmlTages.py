#
# * Python 86, Xml Tags
# * Medium

# * You want to create your local database containing information about the things 
# * you find the coolest. You used to store this information in xml documents, so 
# * now you need to come up with an algorithm that will convert the existing format 
# * into the new one. First you decided to choose a structure for your scheme, and 
# * to do it you want to represent xml document as a tree, i.e. gather all the 
# * tags and print them out as follows:

# tag1()
#  --tag1.1(attribute1, attribute2, ...)
#  ----tag1.1.1(attribute1, attribute2, ...)
#  ----tag1.1.2(attribute1, attribute2, ...)
#  --tag1.2(attribute1, attribute2, ...)
#  ----tag1.2.1(attribute1, attribute2, ...)
# ...

# where attributes of each tag are sorted lexicographically.

# You are a careful person, so the structure of the xml is neatly organized is 
# such a way that:

#     there is a single tag at the root level;
#     each tag has a single parent tag (i.e. if there are several occurrences of 
#       tag a, and in one occurrence it's a child of tag b and in the other one 
#       it's a child of tag c, then b = c);
#     each appearance of the same tag belongs to the same level.

# Given an xml file, return its structure as shown above. The tags of the same 
# level should be sorted in the order they appear in xml, and the attributes should 
# be sorted lexicographically.

# Note: you are given xml represantation in one line.

# * Example

# For

# xml =
# "<data>
#     <animal name="cat">
#     	<genus>Felis</genus>
#         <family name="Felidae" subfamily="Felinae"/>
#         <similar name="tiger" size="bigger"/>
#     </animal>
#     <animal name="dog">
#         <family name="Canidae" member="canid"/>
#         <order>Carnivora</order>
#         <similar name="fox" size="similar"/>
#     </animal>
# </data>"

# the output should be

# xmlTags(xml) =
# ["data()",
#  "--animal(name)",
#  "----genus()",
#  "----family(member, name, subfamily)",
#  "----similar(name, size)",
#  "----order()"]

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string xml

#     xml file as a string.

#     Guaranteed constraints:
#     7 ≤ xml.length ≤ 1000.

#     [output] array.string

#     A list representing the structure of the xml file as described above.

#%%
import re

# * Solution 1
def xmlTags1(xml):
    stack = []
    subTags = {}
    attributes = {}

    n = len(xml)
    cur = 0
    leftAngleIndex = 0

    while cur < n:
        # * find '<'
        if xml[cur] == '<':
            leftAngleIndex = cur
        # * find '>'
        elif xml[cur] == '>':
            # * get whole current tag
            currentTag = xml[leftAngleIndex+1:cur]

            # print('current tag', currentTag)

            # ? if its open tag
            if currentTag[-1] != '/' and currentTag[0] != '/':
                # * split tag to tokens
                tokens = currentTag.split()
                currentTagName = tokens[0]

                # * push tag name into stack
                stack.append(currentTagName)
                # * update attributes
                if currentTagName not in attributes:
                    attributes[currentTagName] = set()

                # * if tag has attributes
                if len(tokens)>1:
                    attrs = re.findall('\s([\s\S]+?)="[\s\S]*?"', currentTag)
                    for attr in attrs:
                        attributes[currentTagName].add(attr)

            # ? if its self-closing tag
            elif currentTag[-1] == '/':
                currentTag = currentTag[:-1]
                # * split tag to tokens
                tokens = currentTag.split()
                currentTagName = tokens[0]

                # * push tag name into stack
                stack.append(currentTagName)
                
                # * add self-closing tag into subTags
                if currentTagName not in subTags:
                    subTags[currentTagName] = []

                # * update attributes
                if currentTagName not in attributes:
                    attributes[currentTagName] = set()

                # * if tag has attributes
                # ! Note: attributes could be empty string, using * instead of +
                if len(tokens)>1:
                    attrs = re.findall('\s([\s\S]+?)="[\s\S]*?"', currentTag)
                    for attr in attrs:
                        attributes[currentTagName].add(attr)

            # ? if its closing tag
            # * elif currentTag[1] == '/':
            else:   
                currentTagName = currentTag[1:]

                # * add closing tag into subTags
                if currentTagName not in subTags:
                    subTags[currentTagName] = []

                # * add nested tags into current tag's subtags
                # * hold sub tags of current tag
                popedTagList = []
                while stack[-1] != currentTagName:
                    # * pop sub tag from the top of stack
                    popedTag = stack.pop()
                    # ! poped sub tag is NEITHER in poptag list, NOR in current tag's sub tag list
                    if popedTag not in subTags[currentTagName] and popedTag not in popedTagList:
                        # ! insert at the beginning of list to ensure correct order
                        popedTagList.insert(0, popedTag)        
                        
                subTags[currentTagName]+=popedTagList

        cur += 1
    
    # print(stack)
    # print(subTags)
    # print(attributes)

    result = []

    # * helper
    def getTagString(tag, prefix):
        # * get attributes for tag
        attrs = ', '.join(sorted(list(attributes[tag])))
        result.append(prefix + tag +'(' + attrs + ')')

        # * recursive visit subtags
        for subTag in subTags[tag]:
            getTagString(subTag, (prefix+'--'))


    root = stack[0]
    getTagString(root, '')

    return result


    
# * Solution 2
import xml
def xmlTags2(xmlf):
    pass


xml1 = '<data>\
            <animal name="cat">\
                <genus>Felis</genus>\
                <family name="Felidae" subfamily="Felinae"/>\
                <similar name="tiger" size="bigger"/>\
            </animal>\
            <animal name="dog">\
                <family name="Canidae" member="canid"/>\
                <order>Carnivora</order>\
                <similar name="fox" size="similar"/>\
            </animal>\
        </data>'
r1 = xmlTags1(xml1)
print(r1)

xml1 = '<data>\
            <a pooh=\"20\">\
                <b meh=\"lksjljk\">\
                    <c/>\
                </b>\
            </a>\
            <a kuku=\"llala\">\
                <b kek=\"q\">\
                    <d test=\"1\"/>\
                </b>\
            </a>\
        </data>'
r1 = xmlTags1(xml1)
print(r1)

xml1 = '<a>\
            <b p="">\
                <c n="" m=""/>\
            </b>\
            <b s="">\
                <d></d>\
                <c l="" o=""/>\
            </b>\
            <b>\
                <c k=""/>\
                <e>\
                    <h></h>\
                </e>\
            </b>\
        </a>'
r1 = xmlTags1(xml1)
print(r1)

# %%
