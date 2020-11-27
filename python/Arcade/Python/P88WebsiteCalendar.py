#
# * Python 88. Website Calendar
# * Medium

# * You're creating your own website for Harry Potter fans. As you all believe in 
# * magic, you're waiting for your personal letter from Hogwarts, that will 
# * definitely arrive to you some day with a magnificent owl. To be prepared for 
# * this exciting moment you decided to embed a calendar to your website on which 
# * you will mark the days when Hogwarts owls can bring letters.

# * Given a month and a year, return an HTML table representing the desired calendar. 
# * Follow the same format as provided in the example but omit all whitespace 
# * characters (i.e. tabs, newlines and whitespaces) where it is possible, because 
# * you care about space efficiency.

# * Example

# For month = 11 and year = 2016, the output should be

# websiteCalendar(month, year) =
# "<table border="0" cellpadding="0" cellspacing="0" class="month">
#   <tr>
#     <th colspan="7" class="month">November 2016</th>
#   </tr>
#   <tr>
#     <th class="mon">Mon</th>
#     <th class="tue">Tue</th>
#     <th class="wed">Wed</th>
#     <th class="thu">Thu</th>
#     <th class="fri">Fri</th>
#     <th class="sat">Sat</th>
#     <th class="sun">Sun</th>
#   </tr>
#   <tr>
#     <td class="noday">&nbsp;</td>
#     <td class="tue">1</td>
#     <td class="wed">2</td>
#     <td class="thu">3</td>
#     <td class="fri">4</td>
#     <td class="sat">5</td>
#     <td class="sun">6</td>
#   </tr>
#   <tr>
#     <td class="mon">7</td>
#     <td class="tue">8</td>
#     <td class="wed">9</td>
#     <td class="thu">10</td>
#     <td class="fri">11</td>
#     <td class="sat">12</td>
#     <td class="sun">13</td>
#   </tr>
#   <tr>
#     <td class="mon">14</td>
#     <td class="tue">15</td>
#     <td class="wed">16</td>
#     <td class="thu">17</td>
#     <td class="fri">18</td>
#     <td class="sat">19</td>
#     <td class="sun">20</td>
#   </tr>
#   <tr>
#     <td class="mon">21</td>
#     <td class="tue">22</td>
#     <td class="wed">23</td>
#     <td class="thu">24</td>
#     <td class="fri">25</td>
#     <td class="sat">26</td>
#     <td class="sun">27</td>
#   </tr>
#   <tr>
#     <td class="mon">28</td>
#     <td class="tue">29</td>
#     <td class="wed">30</td>
#     <td class="noday">&nbsp;</td>
#     <td class="noday">&nbsp;</td>
#     <td class="noday">&nbsp;</td>
#     <td class="noday">&nbsp;</td>
#   </tr>
# </table>"

# Here is how this calendar would look on your website:
# November 2016
# Mon	Tue	Wed	Thu	Fri	Sat	Sun
#  	1	2	3	4	5	6
# 7	8	9	10	11	12	13
# 14	15	16	17	18	19	20
# 21	22	23	24	25	26	27
# 28	29	30	 	 	 	 

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] integer month

#     1-based number of a month (i.e. 1 stands for January, 2 stands for February, 
#       and so on).

#     Guaranteed constraints:
#     1 ≤ month ≤ 12.

#     [input] integer year

#     4-digit number of a year. Please don't forget that in leap years February 
#       has 29 days.

#     Guaranteed constraints:
#     1900 ≤ year ≤ 2100.

#     [output] string

#     An HTML table corresponding to the given month and the given year.

#%%

# * Solution 1
def websiteCalendar1(month, year):
    import datetime
    inputdate = datetime.date(year, month, 1)
    
    tableTagOpen = '<table border="0" cellpadding="0" cellspacing="0" class="month">'
    tableTagClose = '</table>'
    tableHead = '<tr><th colspan="7" class="month">{} {}</th></tr>'.format(inputdate.strftime('%B'), year)

    oneDay = datetime.timedelta(days=1)
    
    weekdays = [inputdate.weekday()]
    print(weekdays)
    
    curDate = datetime.date(year, month, 1)
    # TODO

    return tableTagOpen + tableHead + tableTagClose


# * Solution 2
def websiteCalendar2(month, year):
    import calendar

    text_cal = calendar.HTMLCalendar(firstweekday=0)

    return text_cal.formatmonth(year,month).replace('\n','')



month1= 11
year1 = 2016
r1 = websiteCalendar2(month1, year1)
print(r1)

# %%
