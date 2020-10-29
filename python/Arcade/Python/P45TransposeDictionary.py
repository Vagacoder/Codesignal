#
# * Python 45, Transpose Dictionary
# * Easy

# * You're implementing a plugin for your favorite code editor. This plugin launches 
# * various scripts depending on the open file extension. Each script is associated 
# * with exactly one extension, and the information about which script should be 
# * launched for each extension is stored in a dictionary scriptByExtension.

# You are planning to add more supported extensions for some scripts, so now you would also like to store information about the extensions which each script supports. As a starting point, you'd like to obtain the (extension, script) pairs from the dictionary, sorted lexicographically by the extensions.

# Implement a function that will do the job.

# * Example

# For

# scriptByExtension = {
#   "validate": "py",
#   "getLimits": "md",
#   "generateOutputs": "json"
# }

# the output should be

# transposeDictionary(scriptByExtension) = [["json", "generateOutputs"], 
#                                           ["md", "getLimits"], 
#                                           ["py", "validate"]]

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] dictionary scriptByExtension

#     The initial dictionary. Both keys and values of the dictionary are guaranteed 
#       to be strings that contain only English letters. It is also guaranteed 
#       that all dictionary values are unique.

#     Guaranteed constraints:
#     0 ≤ scriptByExtension.length ≤ 10.

#     [output] array.array.string

#     Array of pairs [extension, script], sorted lexicographically by the extension.

#%%

# * Solution 1
def transposeDictionary(scriptByExtension):
    return sorted(list([value, key] for key, value in scriptByExtension.items()), key=lambda x: x[0])



scriptByExtension = {
  "validate": "py",
  "getLimits": "md",
  "generateOutputs": "json"
}
r1 = transposeDictionary(scriptByExtension)
print(r1)

# %%
