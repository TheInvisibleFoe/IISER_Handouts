import numpy as np

rl = np.array([5e1, 5e2, 5e3, 5e4, 5e5])

vab = 25*rl/(5000+rl)
iab=25/(5000+rl)*1000
pab = vab*iab

print("vab : ")
print(vab)
print("iab : ")
print(iab)
print("pab : ")
print(pab)



