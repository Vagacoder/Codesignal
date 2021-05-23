#
# * Core 130. Valid Time

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

#     A string representing time in HH:MM format. It is guaranteed that the first 
#       two characters, as well as the last two characters, are digits.

#     [output] boolean

#     true if the given representation is correct, false otherwise.

#%%
# * Solution 1
def validTime(time:str)->bool:
    timeTokens = time.split(':')
    if len(timeTokens) != 2:
        return False
    hour = int(timeTokens[0])
    if hour < 0 or hour > 23:
        return False
    minute = int(timeTokens[1])
    if minute < 0 or minute > 59:
        return False
    
    return True


# * Solution 2
def validTime2(time:stre) -> bool:
    import time
    try:
        time.strptime(time, "%H:%M")
    except:
        return False
    return True


t1 = "13:58"
r1 = validTime(t1)
print(r1)

t1 = "25:51"
r1 = validTime(t1)
print(r1)

t1 = "02:76"
r1 = validTime(t1)
print(r1)
