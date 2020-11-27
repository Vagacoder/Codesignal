#
# * Python 87, Build Command
# * Medium

# * While migrating to a new operation system, you faced an unexpected problem: 
# * now you need to create a new build command for your favorite text editor plugin. 
# * The build command is stored as a JSON file that you should now update. In order 
# * to make the transition simpler, you decided to write a program that will create 
# * a template of the build command by replacing everything but dictionaries in 
# * given jsonFile with their default values: numbers with 0, strings with "" and 
# * lists with [].

# It is guaranteed that there are only aforementioned types in the given JSON file.

# * Example

# For

# jsonFile =
# """
# {
#     "version": "0.1.0",
#     "command": "c:python",
#     "args": ["app.py"],
#     "problemMatcher": {
#         "fileLocation": ["relative", "${workspaceRoot}"],
#         "pattern": {
#             "regexp": "^(.*)+s$",
#             "message": 1
#         }
#     }
# }
# """

# the output should be

# buildCommand(jsonFile) =
# """
# {
#     "version": "",
#     "command": "",
#     "args": [],
#     "problemMatcher": {
#         "fileLocation": [],
#         "pattern": {
#             "regexp": "",
#             "message": 0
#         }
#     }
# }
# """

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string jsonFile

#     A correct JSON file of build command for your favorite plugin. It is guaranteed 
#       that it contains only lists, dictionaries, strings and numbers. It is also 
#       guaranteed that the entire file consists of a single dictionary.

#     Guaranteed constraints:
#     2 ≤ jsonFile.length ≤ 1000.

#     [output] string

#     Modified jsonFile.

#%%
'''
https://www.geeksforgeeks.org/json-load-in-python/?ref=lbp
https://docs.python.org/3/library/json.html
'''
def buildCommand(jsonFile):
    import json

    #  * json.loads(), parse string to dict
    obj1 = json.loads(jsonFile)
    
    # print(obj1)
    # print(type(obj1))

    def resetJsonValue(jsObject):
        for key, val in jsObject.items():
            # print('key: ', key)
            # print('value: ', val)
            # print('value type: ', type(val))
            if type(val) is str:
                jsObject[key] = ''
            elif type(val) is int:
                jsObject[key] = 0
            elif type(val) is float:
                jsObject[key] = 0
            elif type(val) is list:
                jsObject[key] = []
            elif type(val) is tuple:
                jsObject[key] = (0,)
            elif type(val) is set:
                jsObject[key] = set()
            elif type(val) is bool:
                jsObject[key] = False
            else:
                jsObject[key] = resetJsonValue(jsObject[key])
            
        return jsObject

    # * json.dumps(), convert dict to string
    return json.dumps(resetJsonValue(obj1))



jsonFile1 ="""
{
    "version": "0.1.0",
    "command": "c:python",
    "args": ["app.py"],
    "problemMatcher": {
        "fileLocation": ["relative", "${workspaceRoot}"],
        "pattern": {
            "regexp": "^(.*)+s$",
            "message": 1
        }
    }
}
"""
r1 = buildCommand(jsonFile1)
print(r1)

jsonFile1 ="""
{"one": "1", "two": [2], "three": 3, "four": 4.6}
"""
r1 = buildCommand(jsonFile1)
print(r1)

# %%
