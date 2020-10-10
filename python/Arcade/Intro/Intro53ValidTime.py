#

# * Intro 53, Valid Time
# * Easy

# * Check if the given string is a correct time representation of the 24-hour clock.

# * Example

#     For time = "13:58", the output should be
#     validTime(time) = true;
#     For time = "25:51", the output should be
#     validTime(time) = false;
#     For time = "02:76", the output should be
#     validTime(time) = false.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string time

#     A string representing time in HH:MM format. It is guaranteed that the first two characters, as well as the last two characters, are digits.

#     [output] boolean

#     true if the given representation is correct, false otherwise.

#%%

# * Solution 1
def validTime1(time:str)-> bool:
    tokens = time.split(':')
    hour = int(tokens[0])
    minute = int(tokens[1])
    print(hour, minute)

    if hour < 0 or hour > 23 or minute < 0 or minute > 59:
        return False
    else:
        return True


# * Solution 2
# ! destructure using map(iterable)
def validTime2(time):
    h,m=map(int,time.split(":"))
    return 0<=h<24 and 0<=m<60


a1 = "25:51"
e1 = False
r1 = validTime1(a1)
print('For {}, expected: {}, result: {}'.format(a1, e1, r1))


a1 = "24:00"
e1 = False
r1 = validTime1(a1)
print('For {}, expected: {}, result: {}'.format(a1, e1, r1))

# %%
