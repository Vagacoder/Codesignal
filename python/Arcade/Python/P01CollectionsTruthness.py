#
# * Python 01, Collections Truthness
# * Easy

#%%
xs = [()]
res = [False]*2
if xs:
    res[0] = True
if xs[0]:
    res[1] = True

print(res)
# %%
