#
# * Python 69, Check Password
# * Medium

# * You're implementing a web application. Like most applications, yours also has 
# * the authorization function. Now you need to implement a server function that 
# * will check password attempts made by users. Since you expect heavy loads, the 
# * function should be able to accept a bunch of requests that will be sent 
# * simultaneously.

# In order to validate your function, you want to test it locally. Given a list 
# of attempts and the correct password, return the 1-based index of the first 
# correct attempt, or -1 if there were none.

# * Example

# For attempts = ["hello", "world", "I", "like", "coding"] and
# password = "like", the output should be
# checkPassword(attempts, password) = 4.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.string attempts

#     A list of password attempts.

#     Guaranteed constraints:
#     0 ≤ attempts.length ≤ 20,
#     1 ≤ attempts[i].length ≤ 20.

#     [input] string password

#     Correct password.

#     Guaranteed constraints:
#     1 ≤ password.length ≤ 20.

#     [output] integer

#     The 1-based index of the first correct password attempt, or -1 or there were none.

#%% 

# * Solution 1
# ! python generator send()
def checkPassword(attempts:list, password:str)-> int:
    def check():
        while True:
            x = yield
            yield x == password 

    checker = check()
    for i, attempt in enumerate(attempts):
        next(checker)
        if checker.send(attempt):
            return i + 1

    return -1


a1 = ["hello", "world", "I", "like", "coding"]
a2 = 'like'
r1 = checkPassword(a1, a2)
print(r1)


# %%
