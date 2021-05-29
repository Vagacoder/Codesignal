#
# * Core 131. Video Part

# * You have been watching a video for some time. Knowing the total video duration 
# * find out what portion of the video you have already watched.

# * Example

# For part = "02:20:00" and total = "07:00:00", the output should be
# videoPart(part, total) = [1, 3].

# You have watched 1 / 3 of the whole video.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string part

#     A string of the following format "hh:mm:ss" representing the time you have been watching the video.

#     [input] string total

#     A string of the following format "hh:mm:ss" representing the total video duration.

#     [output] array.integer

#     An array of the following format [a, b] (where a / b is a reduced fraction).

#%%

# * Solution 1
def videoPart(part: str, total: str)-> list:
    from fractions import Fraction
    pParts = part.split(':')
    pTime = int(pParts[0])*3600 + int(pParts[1])*60 + int(pParts[2])
    tParts = total.split(':')
    tTime = int(tParts[0])*3600 + int(tParts[1])*60 + int(tParts[2])

    # print(pTime)
    # print(tTime)
    # print(pTime/tTime)

    return [Fraction(pTime, tTime).numerator, Fraction(pTime, tTime).denominator]


# * Solution 2
# ! using gcd
def videoPart2(part, total):
    s = lambda x: int(x[:2])*60**2 + int(x[3:5])*60 + int(x[6:])
    p, t = s(part), s(total)
    gcd = lambda m, n : m if not n else gcd(n, m%n)
    g = gcd(p, t)
    return [p/g, t/g]


a1 = "02:20:00"
b1 = "07:00:00"
r1 = videoPart(a1, b1)
print(r1)
