#
# * Python 85, To Human Age
# * Easy

# * After years of practicing psychology you decided that it's time to find the 
# * answer to the following very important question: how can different species 
# * live together in harmony? In order to answer this question, you headed out 
# * for a long journey. After several years of wandering, you finally found what 
# * you were looking for: a village where humans, cats and dogs lived in the perfect 
# * harmony.

# Trying to understand the source of this harmony, you are gathering information 
# about all members of the village community. You're currently working on determining 
# the age of each member converted to human age. Here's how cats and dogs age can 
# be converted:

#     The first and the second years of a cat's life are roughly equal to 12.5 
#       years of a human's, and after this, each additional year is around four 'human years'.
#     The first year of a dog's life is equal to 15 years of a human's life, the 
#       second dog's year is equal to another 9 years of a human's life, and after 
#       this, each additional year is around four 'human years'.

# Given information about the members of the village community, return information 
# about their ages converted to human age.

# * Example

# For members = [["cat", "2"], ["dog", "2"], ["human", "2"]],
# the output should be

# toHumanAge(members) = ["25 y.o. in human age", 
#                        "24 y.o. in human age", 
#                        "2 y.o. in human age"]

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.array.string members

#     A list representing the members of the village community. Each member is 
#       given in the format [type, age], where type can be "cat", "dog" or "human", 
#       and age is an integer in range [0, 20].

#     Guaranteed constraints:
#     1 ≤ members.length ≤ 50,
#     members[i].length = 2,
#     members[i][0] ∈ {"cat", "dog", "human"},
#     0 ≤ int(members[i][1]) ≤ 20.

#     [output] array.string

#     Information about each member (in the same order as they go in members) in 
#       the format <age> y.o. in human age.

#%%

class Mammal(object):
    
    def __init__(self, age):
        self.age = age


    def toHuman(self):
        return self.age


    def __str__(self):
        return '{} y.o. in human age'.format(self.toHuman())


class Cat(Mammal):
    def toHuman(self):
        if self.age == 0:
            return 0
        elif self.age < 3:
            return 25 // (3 - self.age)
        else:
            return 25 + 4 * (self.age - 2)


class Dog(Mammal):
    def toHuman(self):
        if self.age == 0:
            return 0
        elif self.age == 1:
            return 15
        elif self.age == 2:
            return 24
        else:
            return 24 + (self.age - 2) * 4


class Human(Mammal):
    pass


def toHumanAge(members):
    species = {
        'cat': Cat,
        'dog': Dog,
        'human': Human
    }
    res = []
    for spec, age in members:
        res.append(str(species[spec](int(age))))
    return res


members = [["cat", "2"], ["dog", "2"], ["human", "2"]]
r1 = toHumanAge(members)
print(r1)

h1 = Human(10)
Human(11)
print(h1)

# %%
