#
# * Core 95, Runners Meetings
# * Medium

# * Some people run along a straight line in the same direction. They start 
# * simultaneously at pairwise distinct positions and run with constant speed 
# * (which may differ from person to person).

# If two or more people are at the same point at some moment we call that a meeting. 
# The number of people gathered at the same point is called meeting cardinality.

# For the given starting positions and speeds of runners find the maximum meeting 
# cardinality assuming that people run infinitely long. If there will be no meetings, 
# return -1 instead.

# Example

# For startPosition = [1, 4, 2] and speed = [27, 18, 24], the output should be
# runnersMeetings(startPosition, speed) = 3.

# In 20 seconds after the runners start running, they end up at the same point. 
# Check out the gif below for better understanding:

# Input/Output

    # [execution time limit] 4 seconds (py3)

    # [input] array.integer startPosition

    # A non-empty array of integers representing starting positions of runners 
    # (in meters).

    # Guaranteed constraints:
    # 2 ≤ startPosition.length ≤ 100,
    # -104 ≤ startPosition[i] ≤ 104.

    # [input] array.integer speed

    # Array of positive integers of the same length as startPosition representing 
    # speeds of the runners (in meters per minute).

    # Guaranteed constraints:
    # speed.length = startPosition.length,
    # 1 ≤ speed[i] ≤ 100.

    # [output] integer

    # The maximum meeting cardinality or -1 if there will be no meetings.

#%%

# * Solution 1
# ! TLE
def runnersMeetings(startPosition: list, speed: list) -> int:
    n = len(startPosition)
    startPosition = [p*60 for p in startPosition]
    maxTime = 1200000
    t = 0
    count = 0
    while t < maxTime:
        startPosition = [p+speed[i] for i, p in enumerate(startPosition)]
        curCount = n - len(set(startPosition)) + 1
        count = max(count, curCount)
        t += 1
    
    if count == 1:
        return -1
    else:
        return count

# * Solution 2
# ! find LCM using GCD
def runnersMeetings2(startPosition: list, speed: list) -> int:

    def gcd(a: int, b:int)-> int:
        while b > 0:
            a, b = b, a % b
        return a

    def lcm(a:int, b:int)-> int:
        return (a*b)//gcd(a,b)

    lcms = []

    return lcm(24, 54)
    

a1 = [1, 4, 2]
s1 = [27, 18, 24]
r1 = runnersMeetings2(a1, s1)
print('ex: {}, ar: {}'.format(3, r1))

a1 = [1, 1000]
s1 = [23, 22]
r1 = runnersMeetings2(a1, s1)
print('ex: {}, ar: {}'.format(2, r1))