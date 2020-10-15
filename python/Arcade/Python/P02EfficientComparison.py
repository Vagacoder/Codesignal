#
# * Python 02, Efficient Comparison
# * Medium

# * You would like to write a function that takes integer numbers x, y, L and R 
# * as parameters, and returns True if xy lies within the interval (L, R] and 
# * False otherwise. You're considering several different ways to write the 
# * conditional statement inside this function:

#     if L < x ** y <= R:
#     if x ** y > L and x ** y <= R:
#     if x ** y in range(L + 1, R + 1):

# * Which option would be the most efficient in terms of execution time?

#%%
import time

s1 = time.time()
if 3<2**3<=9:
	e1 = time.time()
	print("First\t",e1-s1,"\n")

print("\n")

s2 = time.time()
if 2**3>3 and 2**3<=9:
	e2 = time.time()
	print("Second\t",e2-s2)

print ("\n")

s3 = time.time()
if 2**3 in range(4, 10):
	e3 = time.time()
	print("Third\t",e3-s3,"\n")



print("min:",min([e1-s1,e2-s2,e3-s3]))


print('if L < x**y <= R is fastest')

# %%
