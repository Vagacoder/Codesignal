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

def buildCommand(jsonFile):
    pass


