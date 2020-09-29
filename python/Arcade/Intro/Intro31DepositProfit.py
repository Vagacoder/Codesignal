#
# * Intro 31. Deposit Profit
# * Medium

# * You have deposited a specific amount of money into your bank account. Each 
# * year your balance increases at the same growth rate. With the assumption that 
# * you don't make any additional deposits, find out how long it would take for 
# * your balance to pass a specific threshold.

# * Example

# For deposit = 100, rate = 20, and threshold = 170, the output should be
# depositProfit(deposit, rate, threshold) = 3.

# Each year the amount of money in your account increases by 20%. So throughout 
# the years, your balance would be:

#     year 0: 100;
#     year 1: 120;
#     year 2: 144;
#     year 3: 172.8.

# Thus, it will take 3 years for your balance to pass the threshold, so the answer is 3.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] integer deposit

#     The initial deposit, guaranteed to be a positive integer.

#     Guaranteed constraints:
#     1 ≤ deposit ≤ 100.

#     [input] integer rate

#     The rate of increase. Each year the balance increases by the rate percent of the current sum.

#     Guaranteed constraints:
#     1 ≤ rate ≤ 100.

#     [input] integer threshold

#     The target balance.

#     Guaranteed constraints:
#     deposit < threshold ≤ 200.

#     [output] integer

#     The number of years it would take to hit the threshold.

#%%

# * Solution 1
def depositProfit1(deposit:int, rate:int, threshold:int)->int:
    year = 0
    while deposit < threshold:
        deposit += (deposit * (rate)/100)
        year += 1
        print(year, deposit)

    return year


# * Solution 2
import math
def depositProfit2(deposit:int, rate:int, threshold:int)->int:
    return math.ceil(math.log(threshold/deposit, 1+rate/100))


a1 = 100
a2 = 20
a3 = 170
e1 = 3
r1 = depositProfit2(a1, a2, a3)
print('For {} {} {}, expected: {}, result:{}'.format(a1, a2, a3, e1, r1))


# %%
