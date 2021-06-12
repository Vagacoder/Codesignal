#
# * Core 137. Holiday
# 

# John Doe likes holidays very much, and he was very happy to hear that his country's 
# government decided to introduce yet another one. He heard that the new holiday 
# will be celebrated each year on the xth week of month, on weekDay.

# Your task is to return the day of month on which the holiday will be celebrated 
# in the year yearNumber.

# For your convenience, here are the lists of months names and lengths and the 
# list of days of the week names.

#     Months: "January", "February", "March", "April", "May", "June", "July", 
#       "August", "September", "October", "November", "December".
#     Months lengths: 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31.
#     Days of the week: "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", 
#       "Saturday", "Sunday".

# Please, note that in leap years February has 29 days.

# Example

#     For x = 3, weekDay = "Wednesday", month = "November", and yearNumber = 2016, 
#       the output should be
#     holiday(x, weekDay, month, yearNumber) = 16.

#     The new holiday will be celebrated every November on the 3rd Wednesday of 
#       the month. In 2016 the 3rd Wednesday falls on the 16th of November.

#     For x = 5, weekDay = "Thursday", month = "November", and yearNumber = 2016, 
#       the output should be holiday(x, weekDay, month, yearNumber) = -1.

#     There are only 4 Thursdays in November 2016.

# Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] integer x

#     A positive integer.

#     Guaranteed constraints:
#     1 ≤ x ≤ 5.

#     [input] string weekDay

#     A string representing a correct name of some day of the week.

#     Guaranteed constraints:
#     weekDay ∈ {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", 
#       "Sunday"}.

#     [input] string month

#     A string representing a correct name of some month.

#     Guaranteed constraints:
#     month ∈ {"January", "February", "March", "April", "May", "June", "July", 
#       "August", "September", "October", "November", "December"}.

#     [input] integer yearNumber

#     Guaranteed constraints:
#     2015 ≤ yearNumber ≤ 2500.

#     [output] integer

#     The day of month on which the holiday will be celebrated in the year 
#       yearNumber. If there is no answer, return -1.

#%%

# * Solution 1
def holiday(x: int, weekDay: str, month: str, yearNumber: int)-> int:
    import datetime as dt
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # print(dt.datetime.now())
    # print(dt.datetime.now().weekday())

    startDate = dt.datetime.strptime((str(yearNumber) + '-' + month), '%Y-%B')
    # print(startDate)
    # print(startDate.weekday())
    # print(startDate.month)
    
    if startDate.month != 12:
        endDate = dt.datetime(yearNumber, startDate.month+1, 1)
    else:
        endDate = dt.datetime(yearNumber+1, 1, 1)
    
    # print(endDate.weekday())

    # deltaDay = dt.timedelta(days=30)
    # startDate = startDate + deltaDay
    # print(startDate)
    # print(startDate == endDate)

    deltaDay = dt.timedelta(days=1)

    weekNo = 0

    while startDate != endDate:
        if startDate.weekday() == weekdays.index(weekDay):
            weekNo += 1
            if weekNo == x :
                return startDate.day
        startDate = startDate + deltaDay

    return -1
        
# * Solution 2
def holiday2(x, weekDay, month, yearNumber):
    from datetime import datetime
    from calendar import day_name

    try:
        d = datetime.strptime('{}-{}'.format(month, yearNumber), '%B-%Y')
        nd = (7 + list(day_name).index(weekDay) - d.weekday()) % 7 + 7 * x - 6
        datetime(d.year, d.month, nd)
        
        return nd
    except ValueError:
        return -1


x1 = 3
w1 = "Wednesday"
m1 = "November"
y1 = 2016
r1 = holiday(x1, w1, m1, y1)
print(r1)

x1 = 5
w1 = "Thursday"
m1 = "November"
y1 = 2016
r1 = holiday(x1, w1, m1, y1)
print(r1)

x1 = 3
w1 = "Thursday"
m1 = "January"
y1 = 2101
r1 = holiday(x1, w1, m1, y1)
print(r1)