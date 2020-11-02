#
# * Python 57, Correct Lineup
# * Easy

# * For the opening ceremony of the upcoming sports event an even number of 
# * athletes were picked. They formed a correct lineup, i.e. such a lineup in 
# * which no two boys or two girls stand together. The first person in the lineup 
# * was a girl. As a part of the performance, adjacent pairs of athletes (i.e. 
# * the first one together with the second one, the third one together with the 
# * fourth one, etc.) had to swap positions with each other.

# * Given a list of athletes, return the list of athletes after the changes, i.e. 
# * after each adjacent pair of athletes is swapped.

# * Example

# For athletes = [1, 2, 3, 4, 5, 6], the output should be
# correctLineup(athletes) = [2, 1, 4, 3, 6, 5].

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.integer athletes

#     A list of even length representing the athletes, where each athlete is given 
#       by the number written on their back.

#     Guaranteed constraints:
#     2 ≤ athletes.length ≤ 20,
#     1 ≤ athletes[i] ≤ 100.

#     [output] array.integer

#     Array of athletes with each pair of adjacent elements swapped.

#%%

# * Solution 1
def correctLineup1(athletes:list)-> list:
    return [athletes[i+1] if i%2==0 else athletes[i-1] for i in range(len(athletes))]


# * Solution 2
# ! bitwise operator ^. 
def correctLineup1(athletes:list)-> list:
    return [athletes[i^1] for i in range(len(athletes))]


a1 = [1, 2, 3, 4, 5, 6]
r1 = correctLineup1(a1)
print(r1)


# %%
