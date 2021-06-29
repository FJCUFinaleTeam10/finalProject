from RMDP import RMDP

Theta = []

for i in range(0, 480):
    Theta, P_hat = RMDP(i, Theta, P_hat)
