from RMDP import RMDP
from generatingData import generateTestData


def main():
    instance = RMDP()
    instance.generatingData()

    delay = float('inf')
    buffer: int = 1
    maxLengthPost: int = 3  # p_max
    maxTimePost: int = 20  # minutes     #t_pmax

    potentialOrders: list = generateTestData.importOrderValue()

    # for order in potentialOrders:
    #     order.setDeadline(60 * 40)

    for time in range(0, 480):
        s: int = 0  # state
        currentTime = time
        routePlan = []
        UnassignedOrder = []

        # Input: State S, time t, route plan Θ, unassigned orders $o
        # , buffer b, maximal number of postonements pmax,
        # maximum time allowed for postponement tpmax)

        # instance.runRMDP(s, currentTime, routePlan, UnassignedOrder,
        #                  buffer, maxLengthPost, maxTimePost)
        instance.runRMDP( currentTime, routePlan, 0)

        # every time new order comming we will call RMDP mocdel
        # to generate Decision and update the Driver location
        # for next order coming

        instance.updateDriverLocation(currentTime)


main()
