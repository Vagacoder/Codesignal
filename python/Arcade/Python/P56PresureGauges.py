#
# * Python 56, Pressure Gauges
# * Easy

# * Harry dropped out of school to pursue his dreams and work in Pipes Corporations. 
# * He is now in charge of a lot of pipes, and his task is to check the gauges 
# * twice a day. By analyzing the morning and evening pressures of each pipe, 
# * Harry should write a report about the minimum and the maximum pressure during 
# * the day.

# * Given the pressures Harry wrote down for each pipe, return two lists: the 
# * first one containing the minimum, and the second one containing the maximum 
# * pressure of each pipe during the day.

# * Example

# For morning = [3, 5, 2, 6] and evening = [1, 6, 6, 6],
# the output should be
# pressureGauges(morning, evening) = [[1, 5, 2, 6], [3, 6, 6, 6]].

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.integer morning

#     A list of pressures, where the ith element is the value the pressure gauge 
#       showed for the ith pipe in the morning.

#     Guaranteed constraints:
#     1 ≤ morning.length ≤ 10,
#     0 ≤ morning[i] ≤ 1000.

#     [input] array.integer evening

#     A list of evening pressures in the same format as morning.

#     Guaranteed constraints:
#     evening.length = morning.length,
#     0 ≤ evening[i] ≤ 1000.

#     [output] array.array.integer

#     A list containing two lists, where the ith elements of the first and the 
#       second lists are the minimum and the maximum pressures the ith pipe had, 
#       respectively.

#%%
# * Solution 1
def pressureGauges1(morning:list, evening:list)-> list:
    return [[min(a, b) for a, b in zip(morning, evening)],[max(a, b) for a, b in zip(morning, evening)]]


# * Solution 2
def pressureGauges2(morning:list, evening:list)-> list:
    return [list(map(op, zip(morning, evening))) for op in [min, max]]



a1 = [3, 5, 2, 6]
a2 = [1, 6, 6, 6]
r1 = pressureGauges2(a1, a2)
print(r1)

# %%
