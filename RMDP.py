import random
from math import factorial

import matplotlib.pyplot as plt

from Math.Geometry import interSectionCircleAndLine
from Math.distance import distance
from assignOrder import AssignOrder
from findVehicle import FindVehicle
from generatingData import generateTestData
from model import order
from nextPermutation import nextPermutation
from postponement import Postponement
from remove import Remove
from slack import Slack


class RMDP:
    def __init__(self):
        self.x = 0
        self.slack = 0
        self.D_0 = []  # Order
        self.R = []  # restaurant
        self.Order_num = 2
        self.Vehicle_num = 10
        self.horizon = 1000
        self.vertical = 1000
        self.Theta = []  # related plan
        self.S = 0  # state(not sure)
        self.Delta_S = 0
        self.P_x = 0
        self.time_buffer=0
        self.p_max=3
        self.t_Pmax=40

    def runRMDP(self, T, Theta, delay: float):

        # Orders
        # parameters initialization
        # print(R)

        Order_num = 5
        T = Order_num * T
        for i in range(T, T + Order_num):
            self.D_0.append(self.Ds_0[i])
        sequence = factorial(Order_num)  # counter for n! type sequences

        while sequence:
            nextPermutation(self.D_0)
            D_hat = self.D_0
            Theta_hat = self.Theta  # Candidate route plan
            P_hat = []  # Set of postponements
            for D in D_hat:
                currentDriver = FindVehicle(Theta_hat, D, self.time_buffer, self.V, self.R)
                Theta_hat = AssignOrder(Theta_hat, D, currentDriver, self.R)

                if Postponement(P_hat, D, self.p_max, self.t_Pmax):
                    if D not in P_hat:
                        P_hat.append(D)
                else:
                    TMP: list = []
                    while D.t - P_hat[0].t < self.t_Pmax:
                        TMP.append(P_hat[0])
                        P_hat.pop()
                    if len(P_hat) >= self.p_max:
                        TMP.add()
                x_hat = [Theta_hat, P_hat]
            delay = Slack(self.S, Theta_hat, self.time_buffer,
                          self.t_ba)  # delay with no postponement
            # plan with postpnement
            Theta_hat_postpone = Remove(Theta_hat, P_hat)
            delay_postpone = Slack(self.S, Theta_hat_postpone, self.time_buffer, self.t_ba)  # delay with postponement
            if delay_postpone < delay:
                Theta_hat = Theta_hat_postpone
            else:
                P_hat = P_hat.pop()
            sequence -= 1
        Theta_x = Theta_hat
        self.P_x = P_hat
        # Theta_x = Remove(Theta_x, self.P_x)
        return Theta_x, self.P_x

    def showPosition(self):
        plt.scatter(self.x_R, self.y_R, c='red', s=25)
        plt.scatter(self.x_V, self.y_V, c='green', s=25)
        plt.show()

    def generatingData(self):
        self.R, self.x_R, self.y_R = generateTestData.importRestaurantValue()
        self.V, self.x_V, self.y_V = generateTestData.importVehicleValue()
        self.Ds_0, self.D_x, self.D_y = generateTestData.importOrderValue()

        for vehicle in self.V:
            vehicle.setVelocity(10)

        for restaurant in self.R:
            restaurant.setPrepareTime(10 * 60)

    def updateDriverLocation(self, time):
        for route in self.Theta:
            currentDriver = self.D[route.get("driverid")]
            targetDestination = currentDriver.route[0]
            travledDistance = currentDriver.getVelocity * time
            updatedLocation = interSectionCircleAndLine(currentDriver.getLongitude,
                                                        currentDriver.getLatitude,
                                                        travledDistance, currentDriver.getLongitude,
                                                        currentDriver.getLatitude, targetDestination.getLongitude,
                                                        targetDestination.getLatitude)
            if distance(updatedLocation.y, updatedLocation.x, targetDestination.y, targetDestination.x):
                currentDriver.route.pop(0)
            currentDriver.setLongitude(updatedLocation.x)
            currentDriver.setLatitude(updatedLocation.y)
