import random
from math import factorial

import matplotlib.pyplot as plt

from assignOrder import AssignOrder
from findVehicle import FindVehicle
from generatingData import generateTestData
from model import order
from nextPermutation import nextPermutation
from postponement import Postponement
from remove import Remove
from slack import Slack

# Orders
# parameters initialization
t_ba = 40  # minutes
p_max = 3  # number
t_Pmax = 20  # minutes
x = []
slack = 0
delay = float('Inf')
D_0 = []  # Order
R = []  # restaurant
Order_num = 2
Vehicle_num = 10
horizon = 1000
vertical = 1000

x_R = []  # restaurant x position
y_R = []  # restaurant y position
x_V = []  # vehicle x position
y_V = []  # vehicle y position
V = []  # vehicle
Theta = []  # related plan
D_x: list = []
D_y: list = []

# not understand parameters
b = 1  # time buffer
S = 0  # state(not sure)
Delta_S = 0
Theta_x = []
P_x = 0

R, x_R, y_R = generateTestData.importRestaurantValue()

V, x_V, y_V = generateTestData.importVehicleValue()

# importOrderValue()
Restaurant_num = len(R)  # will be 110, is the same with the paper
Ds_0, D_x, D_y = generateTestData.importOrderValue()

# print(R)
plt.scatter(x_R, y_R, c='red', s=25)
plt.scatter(x_V, y_V, c='green', s=25)
# plt.scatter(D_x, D_y, c='blue', s=25)
plt.show()


# main function


def RMDP(T, Theta, P_x):
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
            V = FindVehicle(Theta_hat, D, b, V, R)
            Theta_hat = AssignOrder(Theta_hat, D, V)

            if Postponement(P_hat, D, p_max, t_Pmax):
                if D not in P_hat:
                    P_hat.append(D)
                    if len(P_hat) == p_max:
                        Pop_order = P_hat.pop(0)
                        V = FindVehicle(Theta_hat, Pop_order, b, V, R)
                        Theta_hat = AssignOrder(Theta_hat, Pop_order, V)
                    while D.t-P_hat[0].t>=t_Pmax:
                        Pop_order = P_hat.pop(0)
                        V = FindVehicle(Theta_hat, Pop_order, b, V, R)
                        Theta_hat = AssignOrder(Theta_hat, Pop_order, V)
            x_hat = [Theta_hat, P_hat]

        if (S < delay) or ((S == delay) and (Slack(S, Theta_hat) < slack)):
            x = x_hat
            delay = Delta_S
            slack = Slack(S, Theta_hat)
        sequence -= 1
    Theta_x = Theta_hat
    Theta_x = Remove(Theta_x, P_x)
    return Theta_x, P_x
