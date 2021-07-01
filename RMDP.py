import random
from math import factorial

import matplotlib.pyplot as plt

from Math.distance import distance
from assignOrder import AssignOrder
from findVehicle import FindVehicle
from generatingData import generateTestData
from model import order
from nextPermutation import nextPermutation
from postponement import Postponement
from remove import Remove
from slack import Slack


def RMDP(T, Theta,P_hat, delay: float, ):
    # Orders
    # parameters initialization
    t_ba = 40  # minutes
    p_max = 3  # number
    t_Pmax = 20  # minutes
    x = 0
    slack = 0
    D_0 = []  # Order
    R = []  # restaurant
    Order_num = 2
    Vehicle_num = 10
    horizon = 1000
    vertical = 1000

    Theta = []  # related plan

    # not understand parameters
    time_buffer = 1
    S = 0  # state(not sure)
    Delta_S = 0
    Theta_x = []
    P_x = 0

    R, x_R, y_R = generateTestData.importRestaurantValue()
    V, x_V, y_V = generateTestData.importVehicleValue()
    Ds_0, D_x, D_y = generateTestData.importOrderValue()

    # print(R)
    plt.scatter(x_R, y_R, c='red', s=25)
    plt.scatter(x_V, y_V, c='green', s=25)

    plt.show()

    Order_num = 2
    for i in range(T, T + 2):
        D_0.append(Ds_0[i])
    sequence = factorial(Order_num)  # counter for n! type sequences
    while sequence:
        nextPermutation(D_0)
        D_hat = D_0
        Theta_hat = Theta  # Candidate route plan
        P_hat = []  # Set of postponements
        for D in D_hat:
            currentDriver = FindVehicle(Theta_hat, D, time_buffer, V, R)
            Theta_hat = AssignOrder(Theta_hat, D, currentDriver, R)

            if Postponement(P_hat, D, p_max, t_Pmax):
                if D not in P_hat:
                    P_hat.append(D)
            x_hat = [Theta_hat, P_hat]
        if (S < delay) or ((S == delay) and (Slack(S, Theta_hat, time_buffer, t_ba) < slack)):
            x = x_hat
            delay = Delta_S
            slack = Slack(S, Theta_hat, time_buffer, t_ba)
        sequence -= 1
    Theta_x = Theta_hat
    Theta_x = Remove(Theta_x, P_x)
    return Theta_x, P_x
