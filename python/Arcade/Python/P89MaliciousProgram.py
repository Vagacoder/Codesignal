#
# * Python 89. Malicious Program
# * Meidum

# *You decided to create a malicious program to play a joke on your friend. He's 
# * now struggling with a report for his work, and you want to scare him by spoiling 
# * some dates in it (of course you will change them back after you have your 
# * moment of joy). However, you don't want him to discover the errors until he 
# * starts double-checking the report, so all spoiled dates should be valid.

# Now your goal is to write a program that modifies the curDate according to the 
# rules that specify the changes that should be made. However, if the changes 
# result in an incorrect date, the program should leave the date as is.

# Given the changes and the curDate, return the spoiled date or don't change it 
# if the result appears to be invalid.

# Example

#     For curDate = "01 Jul 2016 16:53:24" and
#     changes = [2, 3, -1, 0, 5, 4], the output should be
#     maliciousProgram(curDate, changes) = "03 Oct 2015 16:58:28";

#     For curDate = "15 Mar 1998 12:09:59" and
#     changes = [-2, 0, 9, 1, 3, 1], the output should be
#     maliciousProgram(curDate, changes) = "15 Mar 1998 12:09:59".

#     After changing the date will look like "13 Mar 2007 13:12:60", which is 
#       incorrect, because the number of seconds cannot be equal to 60.

# Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string curDate

#     The current date in the format "DD MMM YYYY HH:MM:SS", where DD stands for 
#       day of the month (1-based), MMM stands for the name of month cut to 3 
#       letters (i.e. "Jan" for January, "Feb" for February and so on), YYYY - 
#       for the year, HH - for hour (your friend uses 24-hour clock), MM - for 
#       minutes and SS - for seconds. It's guaranteed that given date is correct.

#     Guaranteed constraints:
#     01 ≤ DD ≤ 31,
#     MMM ∈ ["Jan", "Feb", ..., "Dec"],
#     1900 ≤ YYYY ≤ 2100,
#     00 ≤ HH ≤ 23,
#     00 ≤ MM ≤ 59,
#     00 ≤ SS ≤ 59.

#     [input] array.integer changes

#     An array that describes how each component of curDate should be updated. 
#       changes[i] is equal to the value that should be added to the ith component, 
#       where i stands for:
#         0: for the day;
#         1: for the month;
#         2: for the year;
#         3: for the hour;
#         4: for the minute;
#         5: for the second.

#     Guaranteed constraints:
#     -30 ≤ changes[0] ≤ 30,
#     -11 ≤ changes[1] ≤ 12,
#     -100 ≤ changes[2] ≤ 100,
#     -23 ≤ changes[3] ≤ 23,
#     -59 ≤ changes[4] ≤ 59,
#     -59 ≤ changes[5] ≤ 59.

#     [output] string

#     The modified date if it's correct and the given date otherwise (the output 
#       should follow the same format as the input). The date is considered to be 
#       incorrect if at least one of its components is invalid.

#%%

# * Solution 1
def maliciousProgram1(curDate, changes):
    import datetime

    stamp = datetime.datetime.strptime(curDate, '%d %b %Y %H:%M:%S')
    # day = stamp.day+changes[0]
    # month = stamp.month+changes[1]
    # year = stamp.year+changes[2]
    # hour = stamp.hour+changes[3]
    # minute = stamp.minute+changes[4]
    # second = stamp.second+changes[5]
    # if second > 59:
    #     second -= 60
    #     minute += 1
    # if minute > 59:
    #     minute -= 60
    #     hour +=1
    # if hour > 23:
    #     hour -= 1
    #     day += 1
    
    # newStamp = datetime.datetime(year=year, month=month, day=day, hour=hour,
    #                                 minute=minute,second=second)
    # return newStamp.strftime('%d %b %Y %H:%M:%S')
    try:
        newStamp = stamp.replace(day=stamp.day+changes[0], 
                        month=stamp.month+changes[1],
                        year=stamp.year+changes[2],
                        hour=stamp.hour+changes[3],
                        minute=stamp.minute+changes[4],
                        second=stamp.second+changes[5]
                        )
        return newStamp.strftime('%d %b %Y %H:%M:%S')
    except:
        return curDate


curDate = '01 Jul 2016 16:53:24'
changes = [2, 3, -1, 0, 5, 4]
r1 = maliciousProgram1(curDate, changes)
print(r1)
