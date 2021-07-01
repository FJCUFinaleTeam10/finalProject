from RMDP import RMDP


def main():
    instance = RMDP()
    instance.generatingData()
    delay = float('inf')
    for i in range(0, 480):
        # Input: State S, time t, route plan Θ, unassigned orders $o
        # , buffer b, maximal number of postonements pmax,
        # maximum time allowed for postponement tpmax）
        Theta, P_hat = instance.runRMDP(i, Theta, P_hat, delay)


main()
