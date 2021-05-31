#
# * Core 133. Curious Clock

# * Benjamin recently bought a digital clock at a magic trick shop. The seller 
# * never told Ben what was so special about it, but mentioned that one day Benjamin 
# * would be faced with a surprise.

# Indeed, the clock did surprise Benjamin: without warning, at someTime the clock 
# suddenly started going in the opposite direction! Unfortunately, Benjamin has 
# an important meeting very soon, and knows that at leavingTime he should leave 
# the house so as to not be late. Ben spent all his money on the clock, so has 
# to figure out what time his clock will show when it's time to leave.

# Given the someTime at which the clock started to go backwards, find out what 
# time will be shown on the curious clock at leavingTime.

# For your convenience, here is the list of months lengths (from January to December, respectively):

#     Months lengths: 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31.

# Please, note that in leap years February has 29 days.

# * Example

# For someTime = "2016-08-26 22:40" and leavingTime = "2016-08-29 10:00", the output should be
# curiousClock(someTime, leavingTime) = "2016-08-24 11:20".

# There are 2 days, 11 hours and 20 minutes till the meeting. Thus, the clock 
# will show 2016-08-24 11:20 at the leavingTime.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string someTime

#     The time at which the clock started going backwards. It is guaranteed that 
#       the time is correct.
#     The time is given in the format "YYYY-MM-DD HH:MM".

#     Guaranteed constraints:
#     1970-01-01 00:00 ≤ someTime.

#     [input] string leavingTime

#     The time at which Ben will have to leave for the meeting in the same format 
#       as someTime and with the same constraints.

#     Guaranteed constraints:
#     someTime < leavingTime,
#     leavingTime ≤ 2035-12-31 23:59.

#     [output] string

#     The time Ben's curious clock will show when it's time to leave in the same 
#       format as leavingTime and someTime. It is guaranteed that it will be not 
#       earlier than the midnight of January the 1st, 1970.

#%%

# * Solution 1
def curiousClock(someTime, leavingTime):
    from datetime import datetime as dt
    sTime = dt.strptime(someTime, "%Y-%m-%d %H:%M")
    # print(sTime)
    # print(type(sTime))
    lTime = dt.strptime(leavingTime, "%Y-%m-%d %H:%M")
    # print(lTime)
    # print(type(lTime))
    deltaTime = lTime - sTime
    return dt.strftime((sTime - deltaTime), "%Y-%m-%d %H:%M")


a1 = "2016-08-26 22:40"
b1 = "2016-08-29 10:00"
r1 = curiousClock(a1, b1)
print(r1)
