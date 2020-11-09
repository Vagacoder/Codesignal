#
# * Python 70. Greeting Generator
# * Easy

# * The web application service you're working on is supposed to be used by 
# * developers teams. To make the service more friendly, you'd like to implement 
# * a feature that will greet each person in a group.

# Given a list of people in a team, return an array of greetings that should be 
# printed out, where each greeting is in the format "Hello, <team[i]>!".

# * Example

# For team = ["Athos", "Porthos", "Aramis"],
# the output should be

# greetingsGenerator(team) = ["Hello, Athos!",
#                             "Hello, Porthos!",
#                             "Hello, Aramis!"]

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.string team

#     A list of team members.

#     Guaranteed constraints:
#     0 ≤ team.length ≤ 10,
#     1 ≤ team[i].length ≤ 10.

#     [output] array.string

#     Array of strings, where the ith string has the format "Hello, <team[i]>!".

#%%

class Greeter(object):
    def __init__(self, names):
        self.cnt = 0
        self.names = names

    def __iter__(self):
        return self

    def __next__(self):
        if self.cnt < len(self.names):
            self.cnt += 1
            return 'Hello, {}!'.format(self.names[self.cnt - 1])
        else:
            raise StopIteration


def greetingsGenerator(team):
    return list(Greeter(team))


a1 = ["Athos", "Porthos", "Aramis"]
r1 = greetingsGenerator(a1)
print(r1)


# %%
