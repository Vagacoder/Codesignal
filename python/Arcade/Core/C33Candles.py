#
# * Core 33. Candles
# * Easy

# * When a candle finishes burning it leaves a leftover. makeNew leftovers can be 
# * combined to make a new candle, which, when burning down, will in turn leave 
# * another leftover.

# * You have candlesNumber candles in your possession. What's the total number of 
# * candles you can burn, assuming that you create new candles as soon as you have 
# * enough leftovers?

# * Example

# For candlesNumber = 5 and makeNew = 2, the output should be
# candles(candlesNumber, makeNew) = 9.

# Here is what you can do to burn 9 candles:

#     burn 5 candles, obtain 5 leftovers;
#     create 2 more candles, using 4 leftovers (1 leftover remains);
#     burn 2 candles, end up with 3 leftovers;
#     create another candle using 2 leftovers (1 leftover remains);
#     burn the created candle, which gives another leftover (2 leftovers in total);
#     create a candle from the remaining leftovers;
#     burn the last candle.

# Thus, you can burn 5 + 2 + 1 + 1 = 9 candles, which is the answer.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] integer candlesNumber

#     The number of candles you have in your possession.

#     Guaranteed constraints:
#     1 ≤ candlesNumber ≤ 15.

#     [input] integer makeNew

#     The number of leftovers that you can use up to create a new candle.

#     Guaranteed constraints:
#     2 ≤ makeNew ≤ 5.

#     [output] integer


#%%

# * Solution 1
# ! Recursive
def candles1(candlesNumber:int, makeNew:int)-> int:
    def makeCandle(ruin:int):
        if ruin < makeNew:
            return 0
        return ruin//makeNew + makeCandle(ruin//makeNew +ruin%makeNew)

    return candlesNumber + makeCandle(candlesNumber)
    


# * Solution 2
# ! Iteration
def candles2(candlesNumber:int, makeNew:int)-> int:
    result = candlesNumber
    ruins = candlesNumber
    while ruins >= makeNew:
        result += ruins//makeNew
        ruins = ruins//makeNew + ruins%makeNew
    
    return result


# * Solution 3
# ! Mathematics
def candles3(candlesNumber, makeNew):
    return candlesNumber + (candlesNumber - 1) // (makeNew - 1)



c1 = 5
m1 = 2
r1 = candles1(c1, m1)
print('exp: {}, re: {}'.format(9, r1))

c1 = 1
m1 = 2
r1 = candles1(c1, m1)
print('exp: {}, re: {}'.format(1, r1))

c1 = 3
m1 = 3
r1 = candles1(c1, m1)
print('exp: {}, re: {}'.format(4, r1))

c1 = 6
m1 = 4
r1 = candles1(c1, m1)
print('exp: {}, re: {}'.format(7, r1))
