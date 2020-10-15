#
# * Python 04, Language Difference
# * Easy

# * Your friend is an experienced coder who just started learning Python. Since 
# * she is already proficient in Java and C++, she decided to write all of her 
# * snippets in all three languages, in order to ensure the Python code was working 
# * as expected. Here's the very first function your friend wrote in Python and 
# * Java (the C++ version is the same as Java one):

#     Python:

# def division(x, y):
#     return x // y

#     Java:

# int division(int x, int y) {
#     return x / y;
# }

# * You noticed that the functions aren't quite the same: they won't produce the 
# * same result for some valid values of x and y. For which of the following 
# * example inputs would these two versions produce different outputs?

# ! Java rounds NEGATIVE products UP, Python rounds DOWN
#%%
print(-15//4)
print(15//-4)
print(-10//-3)
# %%
