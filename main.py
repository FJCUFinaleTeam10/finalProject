from RMDP import RMDP

Theta = []

for i in range(0, 480):
    #testing
    Theta, P_hat = RMDP(i, Theta, P_hat)
