#
# * Python 72, Super Prize
# * Meduim

# * In a large and famous supermarket a new major campaign was launched. From now 
# * on, each nth customer has a chance to win a prize: a brand new luxury car! 
# * However, it's not that simple. A customer wins a prize only if the total price 
# * of their purchase is divisible by d. This number is kept as a secret, so the 
# * customers don't know in advance how much they should spend on their purchases. 
# * The winners will be announced once the campaign is over.

# Your task is to implement a function that will determine the winners. Given the 
# purchases of some customers over time, return the 1-based indices of all the 
# customers who won the prize, i.e. each nth who spend on their purchases amount 
# of money divisible by d.

# * Example

# For purchases = [12, 43, 13, 465, 1, 13], n = 2, and d = 3,
# the output should be
# superPrize(purchases, n, d) = [4].

# Each second customer has a chance to win a car, which makes customers 2, 4 and 
# 6 potential winners. Customer number 2 spent 43 on his purchase, which is not 
# divisible by 3. 13 also is not divisible by 3, so the sixth customer also doesn't 
# get the price. Customer 4, however, spent 465, which is divisible by 3, so he 
# is the only lucky guy.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.integer purchases

#     A list that represents the cost of the purchases some customers made.

#     Guaranteed constraints:
#     0 ≤ purchases.length ≤ 100,
#     1 ≤ purchases[i] ≤ 1000.

#     [input] integer n

#     Guaranteed constraints:
#     2 ≤ n ≤ 20.

#     [input] integer d

#     Guaranteed constraints:
#     2 ≤ d ≤ 20.

#     [output] array.integer

#     A sorted list of 1-based customers who won the prize.

#%%

# * Solution 1
class Prizes1(object):
    
    def __init__(self, purchases, n, d):
        self.i = 0
        self.purchase = purchases
        self.n = n
        self.d = d


    def __iter__(self):
        return self


    def __next__(self):
        # ! wrap with while loop, or __next__(self) will return None.
        # ! since __next__() always returns something
        while True:
            if self.i < len(self.purchase):
                self.i += 1
                if self.i%self.n == 0 and self.purchase[self.i-1]%self.d ==0:
                    return self.i
            else:
                raise StopIteration


# * Solution 2
class Prizes2(object):
    
    def __init__(self, purchases, n, d):
        self.p = purchases
        self.n = n
        self.d = d


    def __iter__(self):
        for i, x in enumerate(self.p):
            if (i+1)% self.n == 0 and self.p[i]%self.d == 0:
                yield i+1


# * Solution 3
class Prizes3(object):
    def __init__(self, p, n, d):
        self.p = p
        self.n = n
        self.d = d

    
    def __iter__(self):
        return iter([i+1 for i,x in enumerate(self.p) if (i+1)%self.n == 0 and x%self.d==0])




def superPrize(purchases, n, d):
    return list(Prizes3(purchases, n, d))


p1 = [12, 43, 13, 465, 1, 13]
n1 = 2
d1 = 3
r1 = superPrize(p1, n1, d1)
print(r1)



# %%

# %%
