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
x = 0
slack = 0
delay = float('Inf')
D_0 = []  # Order
R = []  # restaurant
T = 60  # time=5hr
Order_num = 10
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
Theta_x = 0
P_x = 0
# create restaurant& D_0& vehicle start place
# for _ in range(Resturant_num):
#     R.append([random.randint(0, (horizon+1)), random.randint(0, (vertical+1))])
#     x_R.append(R[_][0])
#     y_R.append(R[_][1])
R, x_R, y_R = generateTestData.importRestaurantValue()

# for _ in range(Vehicle_num):
#     V.append([random.randint(0, (horizon + 1)), random.randint(0, (vertical + 1))])
#     x_V.append(V[_][0])
#     y_V.append(V[_][1])
V, x_V, y_V = generateTestData.importVehicleValue()

# importOrderValue()
Restaurant_num = len(R)  # will be 110, is the same with the paper
D_0, D_x, D_y = generateTestData.importOrderValue()
# for _ in range(Order_num):
#     D_0.append(order.Ds(_, random.randint(0, T + 1), random.randint(0, Restaurant_num), 0, 0))

# print(R)
plt.scatter(x_R, y_R, c='red', s=25)
plt.scatter(x_V, y_V, c='green', s=25)
# plt.scatter(D_x, D_y, c='blue', s=25)
plt.show()
# main function
sequence = factorial(Order_num)  # counter for n! type sequences
while sequence:
    nextPermutation(D_0)
    D_hat = D_0
    Theta_hat = Theta  # Candidate route plan
    P_hat = set()  # Set of postponements
    for D in D_hat:
        pairedVehicle = FindVehicle(Theta_hat, D, b, V, R)
        Theta_hat = AssignOrder(Theta_hat, D, pairedVehicle, R)

        if Postponement(P_hat, D, p_max, t_Pmax):
            P_hat = P_hat.add(D)  # Union D
        x_hat = [Theta_hat, P_hat]
    if (S < delay) or ((S == delay) and (Slack(S, Theta_hat) < slack)):
        x = x_hat
        delay = Delta_S
        slack = Slack(S, Theta_hat)
    sequence -= 1

Theta_x = Remove(Theta_x, P_x)


