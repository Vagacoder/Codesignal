#
# * Intro 02, Century From Year
# * Given a year, return the century it is in. The first century spans from the 
# * year 1 up to and including the year 100, the second - from the year 101 up to 
# * and including the year 200, etc.
# * 
# * Example
# *
# *  For year = 1905, the output should be
# *  centuryFromYear(year) = 20;
# *  For year = 1700, the output should be
#  *  centuryFromYear(year) = 17.
#  * 
#  * Input/Output

#  *  [execution time limit] 3 seconds (java)

#  *  [input] integer year

#  *  A positive integer, designating the year.

#  *  Guaranteed constraints:
#  *  1 ≤ year ≤ 2005.

#  *  [output] integer

#  *  The number of the century the year is in.


#%%
import numpy as np

# * Solution #1
def centuryFromYear1(year:int) -> int:
    return np.ceil(year * 1.0/100)


# * Solution #2
def centuryFromYear2(year:int) -> int:
    return 1 + (year - 1)//100;


# * Solution #3
def centuryFromYear3(year: int) -> int:
    return (year + 99)//100;


years = np.array([1905, 1700, 1988, 2000, 2001, 200, 374, 45, 8, 1])
expected = np.array([20, 17, 20, 20, 21, 2, 4, 1, 1, 1])

result = []

for y in years:
    result.append(centuryFromYear3(y))


result = np.array(result)

print(result - expected)

# %%
