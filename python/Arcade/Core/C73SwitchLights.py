#
# * Core 73, Switch Lights
# * Medium

# * N candles are placed in a row, some of them are initially lit. For each candle 
# * from the 1st to the Nth the following algorithm is applied: if the observed 
# * candle is lit then states of this candle and all candles before it are changed 
# * to the opposite. Which candles will remain lit after applying the algorithm 
# * to all candles in the order they are placed in the line?

# * Example

#     For a = [1, 1, 1, 1, 1], the output should be
#     switchLights(a) = [0, 1, 0, 1, 0].

#     Check out the image below for better understanding:



#     For a = [0, 0], the output should be
#     switchLights(a) = [0, 0].

#     The candles are not initially lit, so their states are not altered by the 
#       algorithm.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.integer a

#     Initial situation - array of zeros and ones of length N, 1 means that the 
#       corresponding candle is lit.

#     Guaranteed constraints:
#     2 ≤ a.length ≤ 5000.

#     [output] array.integer

#     Situation after applying the algorithm - array in the same format as input 
#       with the same length.

#%%

# * Solution 1
def switchLights(a: list) -> list:
    n = len(a)
    for i in range(n):
        if a[i] == 1:
            for j in range(i+1):
                a[j] = (a[j]+1)%2
    
    return a


a1 = [1, 1, 1, 1, 1]
r1 = switchLights(a1)
print(r1)

a1 = [0, 0]
r1 = switchLights(a1)
print(r1)

a1 = [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1]
r1 = switchLights(a1)
print(r1)