#
# * Core 76, Integer to String of Fixed Width
# * Easy

# * Given a positive integer number and a certain length, we need to modify the 
# * given number to have a specified length. We are allowed to do that either by 
# * cutting out leading digits (if the number needs to be shortened) or by adding 
# * 0s in front of the original number.

# * Example

#     For number = 1234 and width = 2, the output should be
#     integerToStringOfFixedWidth(number, width) = "34";
#     For number = 1234 and width = 4, the output should be
#     integerToStringOfFixedWidth(number, width) = "1234";
#     For number = 1234 and width = 5, the output should be
#     integerToStringOfFixedWidth(number, width) = "01234".

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] integer number

#     A non-negative integer.

#     Guaranteed constraints:
#     0 ≤ number ≤ 109.

#     [input] integer width

#     A positive integer representing the desired length.

#     Guaranteed constraints:
#     1 ≤ width ≤ 50.

#     [output] string

#     The modified version of number as described above.

#%%

# * Solution 1
def integerToStringOfFixedWidth(number:int, width:int)-> str:
    result = str(number)
    n = len(result)
    if n > width:
        result = result[(n-width):]
    elif n < width:
        result = '0' * (width - n) + result
    return result


# * Solution 2
# ! String fill with leading zeros: str.zfill()
def integerToStringOfFixedWidth2(number:int, width:int)-> str:
    return str(number).zfill(width)[-width:]

a1 = 1234
a2 = 5
r1 = integerToStringOfFixedWidth2(a1, a2)
print(r1)

a2 = 2
r1 = integerToStringOfFixedWidth2(a1, a2)
print(r1)