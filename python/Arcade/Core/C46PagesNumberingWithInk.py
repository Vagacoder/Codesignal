#
# * Core 46, Pages Numbering with Ink
# * Medium

# * You work in a company that prints and publishes books. You are responsible for 
# * designing the page numbering mechanism in the printer. You know how many digits 
# * a printer can print with the leftover ink. Now you want to write a function 
# * to determine what the last page of the book is that you can number given the 
# * current page and numberOfDigits left. A page is considered numbered if it has 
# * the full number printed on it (e.g. if we are working with page 102 but have 
# * ink only for two digits then this page will not be considered numbered).

# It's guaranteed that you can number the current page, and that you can't number 
# the last one in the book.

# * Example

#     For current = 1 and numberOfDigits = 5, the output should be
#     pagesNumberingWithInk(current, numberOfDigits) = 5.

#     The following numbers will be printed: 1, 2, 3, 4, 5.

#     For current = 21 and numberOfDigits = 5, the output should be
#     pagesNumberingWithInk(current, numberOfDigits) = 22.

#     The following numbers will be printed: 21, 22.

#     For current = 8 and numberOfDigits = 4, the output should be
#     pagesNumberingWithInk(current, numberOfDigits) = 10.

#     The following numbers will be printed: 8, 9, 10.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

    # [input] integer current

    # A positive integer, the number on the current page which is not yet printed.

    # Guaranteed constraints:
    # 1 ≤ current ≤ 1000.

    # [input] integer numberOfDigits

    # A positive integer, the number of digits which your printer can print.

    # Guaranteed constraints:
    # 1 ≤ numberOfDigits ≤ 1000.

    # [output] integer

    # The last printed page number.

#%%

# * Solution 1
def pagesNumberingWithInk(current:int, numberOfDigits:int)-> int:
    sumOfDigit = 0
    while sumOfDigit < numberOfDigits:
        curString = str(current)
        sumOfDigit += len(curString)
        if sumOfDigit > numberOfDigits:
            current -= 1
            break
        elif sumOfDigit == numberOfDigits:
            break
        current += 1
    
    return current


# * Solution 2
def pagesNumberingWithInk2(current:int, numberOfDigits:int)-> int:
    while numberOfDigits >= 0:
        numberOfDigits -= len(str(current))
        current -= 1

    return current - 2


# * Solution 3
def pagesNumberingWithInk3(current:int, numberOfDigits:int)-> int:
    if numberOfDigits < 0:
        return current - 2
    return pagesNumberingWithInk3(current+1, numberOfDigits-len(str(current)))



c1 = 8
n1 = 4
r1 = pagesNumberingWithInk(c1, n1)
print(r1)

c1 = 1
n1 = 5
r1 = pagesNumberingWithInk(c1, n1)
print(r1)

c1 = 21
n1 = 5
r1 = pagesNumberingWithInk(c1, n1)
print(r1)