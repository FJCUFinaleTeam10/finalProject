import copy
from math import factorial

import matplotlib.pyplot as plt

from Math.Geometry import interSectionCircleAndLine
from Math.distance import distance
from assignOrder import AssignOrder
from generatingData import generateTestData
from model.driver import driver
from model.order import Ds
from model.restaurant import restaurant
from nextPermutation import nextPermutation
from postponement import Postponement
from remove import Remove


class RMDP:
    def __init__(self, delay: int, maxLengthPost: int, maxTimePost: int,
                 capacity: int, velocity: int, restaurantPrepareTime: int):
        self.Ds_0, self.D_x, self.D_y = generateTestData.importOrderValue()
        self.vehiceList, self.vehiclelist_x, self.vehiclelist_y = generateTestData.importVehicleValue()
        self.restaurantList, self.restauranList_x, self.restauranList_y = generateTestData.importRestaurantValue()
        self.x = 0
        self.slack = 0
        self.D_0 = []  # Order
        self.R = []  # restaurant
        self.Order_num = 2
        self.Vehicle_num = 10
        self.horizon = 1000
        self.vertical = 1000
        self.Theta = [{"driverId": driver.get_id(), "route": []}
                      for driver in self.vehiceList]  # related plan
        self.S = 0  # state(not sure)
        self.Delta_S = 0
        self.P_x = []
        self.time_buffer = 0
        self.p_max = 3
        self.t_Pmax = 40
        self.distanceEpsilon = 10
        self.t_ba = 10
        self.delay = delay
        self.maxLengthPost = maxLengthPost
        self.maxTimePost = maxTimePost
        self.capacity = capacity
        self.velocity = velocity
        self.restaurantPrepareTime = restaurantPrepareTime

    def runRMDP(self, state: int, T: int, delay: int):

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
            P_hat = self.P_x
            for D in D_hat:
                currentPairdDriver = self.FindVehicle(Theta_hat, D)
                Theta_hat = AssignOrder(
                    Theta_hat, D, currentPairdDriver, self.restaurantList)

                if Postponement(P_hat, D, self.p_max, self.t_Pmax):
                    if D not in P_hat:
                        P_hat.append(D)
                else:
                    while D.t - P_hat[0].t > self.t_Pmax:
                        pairedDriver = self.FindVehicle(
                            Theta_hat, P_hat[0], self.time_buffer, self.V, self.R)
                        Theta_hat = AssignOrder(
                            Theta_hat, D, pairedDriver, self.R)
                        P_hat.pop(0)
                    if len(P_hat) >= self.p_max:
                        for i in range(0, len(P_hat)):
                            pairedDriver = self.FindVehicle(
                                Theta_hat, P_hat[i])
                            Theta_hat = AssignOrder(
                                Theta_hat, D, pairedDriver, self.restaurantList)
                        P_hat.clear
                    P_hat.append(D)

            if (self.S < self.delay) or ((self.S == self.delay) and (self.Slack() < self.slack)):
                self.slack = self.Slack()
                self.delay = self.S
                self.Theta_x = Theta_hat
                self.P_x = P_hat
            sequence -= 1
        self.Theta_x = Remove(self.Theta_x, self.P_x)

    # main function
    def Slack(self):
        totalSlack: int = 0
        for routePerVehicle in self.Theta:
            currentRoute: list = routePerVehicle['route']
            currentVehicle: driver = self.vehiceList[routePerVehicle['driverId']]
            totalSlack += self.delayTotal(currentRoute)
        return totalSlack

        # For every route plan Θ̂, the function calculates
        # the sum of differences between arrival time aD and deadline over
        # all orders: max{0, (tD + ¯t)−(aD + b)}.

    def showPosition(self):
        plt.scatter(self.x_R, self.y_R, c='red', s=25)
        plt.scatter(self.x_V, self.y_V, c='green', s=25)
        plt.show()

        for vehicle in self.vehiceList:
            vehicle.setVelocity(self.velocity)
            vehicle.setCurrentCapacity(0)

        for restaurant in self.restaurantList:
            restaurant.setPrepareTime(self.restaurantPrepareTime)

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

    def tripTime(self, driv: driver, res: restaurant, order: Ds):
        return (distance(driv.x, driv.y, res.xPosition, res.yPosition) +
                distance(res.xPosition, res.yPosition, order.x, order.y)) / self.velocity

    def FindVehicle(self, Theta_hat, Order):
        OrderRestaurant = self.restaurantList[Order.R - 1]
        minTimeDriver = self.vehiceList[0]
        minTimeTolTal = float('inf')
        handleDriver = [
            driver for driver in self.vehiceList if driver.getCurrentCapacity() < self.capacity]
        for currentDriver in handleDriver:
            if self.tripTime(currentDriver, OrderRestaurant, Order) < self.tripTime(minTimeDriver, OrderRestaurant,
                                                                                    Order):
                minTimeDriver = copy.copy(currentDriver)
                minTimeTolTal = self.tripTime(
                    currentDriver, OrderRestaurant, Order)
            Order.setDriver(currentDriver)
            Order.setArriveTime(minTimeTolTal)
            return minTimeDriver

    def deltaSDelay(self, route: list):
        delay: int = 0
        tripTime: int = 0
        for i in range(1, len(route), 1):
            currentDistance = distance(route[i - 1].getLatitude(), route[i - 1].getLongitude(), route[i].getLatitude(),
                                       route[i].getLongitude())
            tripTime += currentDistance / self.velocity
            if isinstance(route[i], Ds):
                delay += max(0, tripTime+self.time -route[i].getDeadLine())
        return delay

    def slackDelay(self, route: list):
        delay: int = 0
        tripTime: int = 0
        for i in range(1, len(route), 1):
            currentDistance = distance(route[i - 1].getLatitude(), route[i - 1].getLongitude(), route[i].getLatitude(),
                                       route[i].getLongitude())
            tripTime += currentDistance / self.velocity
            if isinstance(route[i], Ds):
                delay += max(0, route[i].getDeadLine() - tripTime - self.time_buffer)
        return delay
