#
# * Intro 56, Digits Products
# * Medium

# * Given an integer product, find the smallest positive (i.e. greater than 0) 
# * integer the product of whose digits is equal to product. If there is no such 
# * integer, return -1 instead.

# * Example

#     For product = 12, the output should be
#     digitsProduct(product) = 26;
#     For product = 19, the output should be
#     digitsProduct(product) = -1.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] integer product

#     Guaranteed constraints:
#     0 ≤ product ≤ 600.

#     [output] integer

#%%

# * Solution 1
# ! Note: max product = 600, 600 = 2*2*2*3*5*5, result = 222,355<1,000,000
def digitsProduct1(product: int)->int:
    for i in range(1,1000000):
        temp = getProduct(i)
        if temp == product:
            return i
    return -1


# * helper 
def getProduct(n: int)->int:
    product = 1
    while n > 0:
        product *= n%10
        n = n//10
    return product


# * Solution 2
def digitsProduct2(product:int)->int:
    if product == 1:
        return 1
    elif product == 0:
        return 10
    
    products = []

    while product > 1:
        # ! Note: for/break/else loop !
        for i in range(9,1,-1):
            if product % i == 0:
                product //= i
                products.append(i)
                break
        else:
            return -1

    print(products)
    if len(products) == 0:
        return -1
    else:
        return int(''.join([str(p) for p in sorted(products)]))


a1 = 12
e1 = 26
# print(getProduct(e1))
r1 = digitsProduct2(a1)
print('For {}, expected: {}, result: {}'.format(a1, e1, r1))

a1 = 1
e1 = 1
r1 = digitsProduct2(a1)
print('For {}, expected: {}, result: {}'.format(a1, e1, r1))

a1 = 19
e1 = -1
r1 = digitsProduct2(a1)
print('For {}, expected: {}, result: {}'.format(a1, e1, r1))

a1 = 0
e1 = 10
r1 = digitsProduct2(a1)
print('For {}, expected: {}, result: {}'.format(a1, e1, r1))
# %%
