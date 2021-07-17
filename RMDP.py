import copy
from math import factorial

import matplotlib.pyplot as plt

from Math.Geometry import interSectionCircleAndLine
from Math.distance import distance
from generatingData import generateTestData
from model.driver import driver
from model.order import Ds
from model.restaurant import restaurant
from nextPermutation import nextPermutation
from postponement import Postponement
import itertools


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
        self.vertical = 1000  # related plan
        self.Theta_x = [{"driverId": driver.get_id(), "route": []} for driver in self.vehiceList]
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

        for currentDelay in self.vehiceList:
            currentDelay.setVelocity(40)

        for vehicle in self.vehiceList:
            vehicle.setVelocity(self.velocity)
            vehicle.setCurrentCapacity(100000000000)

        for restaurant in self.restaurantList:
            restaurant.setPrepareTime(self.restaurantPrepareTime)

    def runRMDP(self, state: int, T: int, delay: int):

        Order_num = 5
        T = Order_num * T
        for i in range(T, T + Order_num):
            self.D_0.append(self.Ds_0[i])
        sequence = factorial(Order_num)
        # counter for n! type sequences
        unassignedOrderPermutation = list(itertools.permutations(self.D_0))
        for permutation in unassignedOrderPermutation:
            # while sequence:
            # print(sequence)
            # nextPermutation(self.D_0)
            # D_hat = self.
            Theta_hat = copy.copy(self.Theta_x)  # Candidate route plan
            P_hat = copy.copy(self.P_x)

            for D in permutation:

                currentPairdDriver: driver = self.FindVehicle(D)
                D.setDriverId(currentPairdDriver.get_id())
                currentPairdRestaurent: restaurant = copy.copy(self.restaurantList[D.getRestaurantId() - 1])
                currentPairdRestaurent.setOrderId(D.getId())

                Theta_hat = self.AssignOrder(Theta_hat, D, currentPairdDriver, currentPairdRestaurent)

                if Postponement(P_hat, D, self.p_max, self.t_Pmax):
                    if D not in P_hat:
                        P_hat.append(D)
                else:
                    while (D.t - P_hat[0].t) >= self.t_Pmax:
                        pairedDriver = self.FindVehicle(
                            P_hat[0], self.time_buffer, self.V, self.R)
                        Theta_hat = self.AssignOrder(
                            Theta_hat, D, pairedDriver, self.R)
                        P_hat.pop(0)
                    if len(P_hat) >= self.p_max:
                        for i in range(0, len(P_hat)):
                            pairedDriver = self.FindVehicle(P_hat[i])
                            Theta_hat = self.AssignOrder(
                                Theta_hat, D, pairedDriver, currentPairdRestaurent)
                        P_hat.clear()
                    P_hat.append(D)
            # if sequence == 50:
            #     print(Theta_hat)
            self.S = self.TotalDelay()
            if (self.S < self.delay) or ((self.S == self.delay) and (self.Slack() < self.slack)):
                self.slack = self.Slack()
                self.delay = self.S
                self.Theta_x = Theta_hat
                self.P_x = P_hat
            # sequence -= 1

        print(self.Theta_x)
        self.Remove()

    def deltaSDelay(self, route: list):
        delay: float = 0.0
        tripTime: float = 0.0
        for i in range(1, len(route['route']), 1):
            previousNode = route['route'][i - 1]
            currentNode = route['route'][i]
            currentDistance = distance(previousNode.getLatitude(), previousNode.getLongitude(),
                                       currentNode.getLatitude(), currentNode.getLongitude())
            tripTime += currentDistance / self.velocity
            if isinstance(currentNode, Ds):
                delay += max(0, (tripTime + self.time_buffer) -
                             (currentNode.getDeadLine() + currentNode.get_timeRequest()))
        return delay

    def AssignOrder(self, Theta_hat, D: Ds, V: driver, currentParedRestaurent: restaurant):
        currentRoute: list = next((route for route in Theta_hat if route.get("driverId") == V.get_id()), [])

        if not currentRoute['route']:
            currentRoute['route'].append(currentParedRestaurent)
            currentRoute['route'].append(D)

        else:
            first: int = 0
            second: int = 1
            minDelayTime = float('inf')
            for i in range(0, len(currentRoute), 1):  # control Restaurant
                for j in range(i + 1, len(currentRoute) + 2, 1):  # find all the possible positioins of new order
                    tempList = copy.deepcopy(currentRoute)
                    tempList["route"].insert(i, currentParedRestaurent)
                    tempList["route"].insert(j, D)
                    delayTime = self.deltaSDelay(tempList)

                    if minDelayTime > delayTime:
                        minDelayTime = delayTime
                        first = i
                        second = j

            currentRoute['route'].insert(first, currentParedRestaurent)
            currentRoute['route'].insert(second, D)

        return Theta_hat

    # main function

    def Slack(self):
        totalSlack: int = 0
        for routePerVehicle in self.Theta_x:
            totalSlack += self.slackDelay(routePerVehicle)
        return totalSlack

    def showPosition(self):
        plt.scatter(self.x_R, self.y_R, c='red', s=25)
        plt.scatter(self.x_V, self.y_V, c='green', s=25)
        plt.show()

    def updateDriverLocation(self, time):
        for route in self.Theta_x:
            currentDriver = self.vehiceList[route.get("driverId") - 1]
            targetDestination = route['route'][0]
            travledDistance = currentDriver.getVelocity() * time
            updatedLocation = interSectionCircleAndLine(currentDriver.getLongitude(),
                                                        currentDriver.getLatitude(),
                                                        travledDistance, currentDriver.getLongitude(),
                                                        currentDriver.getLatitude(), targetDestination.getLongitude(),
                                                        targetDestination.getLatitude())
            if distance(updatedLocation.getLatitude(), updatedLocation.getLongitude(),
                        targetDestination.getLatitude(), targetDestination.getLongitude()):
                currentDriver.route.pop(0)
            currentDriver.setLongitude(updatedLocation.x)
            currentDriver.setLatitude(updatedLocation.y)

    def tripTime(self, driv: driver, res: restaurant, order: Ds):
        return (distance(driv.x, driv.y, res.xPosition, res.yPosition) +
                distance(res.xPosition, res.yPosition, order.x, order.y)) / self.velocity

    def FindVehicle(self, Order: Ds):
        OrderRestaurant = self.restaurantList[Order.getRestaurantId() - 1]
        minTimeDriver = self.vehiceList[0]
        minTimeTolTal = float('inf')
        handleDriver = [driver for driver in self.vehiceList if driver.getCurrentCapacity() < self.capacity]
        for currentDriver in handleDriver:
            currenTripTime: float = self.tripTime(currentDriver, OrderRestaurant, Order)
            if currenTripTime < minTimeTolTal:
                minTimeDriver = copy.copy(currentDriver)
                minTimeTolTal = currenTripTime
        return minTimeDriver

    def slackDelay(self, route):
        delay: int = 0
        tripTime: int = 0
        currentDriver = self.vehiceList[route["driverId"] - 1]
        currentRoute: list = copy.copy(route['route'])
        currentRoute.append(currentDriver)
        for i in range(1, len(currentRoute), 1):
            currentDistance = distance(currentRoute[i - 1].getLatitude(), currentRoute[i - 1].getLongitude(),
                                       currentRoute[i].getLatitude(),
                                       currentRoute[i].getLongitude())
            tripTime += currentDistance / self.velocity
            if isinstance(currentRoute[i], Ds):
                delay += max(0, currentRoute[i].getDeadLine() -
                             tripTime - self.time_buffer)
        return delay

    def TotalDelay(self):
        totalSlack: int = 0
        for routePerVehicle in self.Theta_x:
            totalSlack += self.deltaSDelay(routePerVehicle)
        return totalSlack

    def Remove(self):
        # out_index = []
        # for i in range(len(self.Theta_x)):
        #     for k in self.P_x:
        #         if self.Theta_x[i]['route'].label == k.label:
        #             out_index.append(i)
        # out_index.reverse()
        # print(out_index)
        #
        # for i in out_index:
        #     self.Theta_x.pop(i)
        for pospondedOrder in self.P_x:
            currentPairedDriver: driver = self.vehiceList[pospondedOrder.getDriverId() - 1]
            targetRoute: list = next(
                (route for route in self.Theta_x if route.get("driverId") == currentPairedDriver.get_id()), [])
            ans = [node for node in targetRoute['route'] if
                   ((isinstance(node, Ds) and node.getId() != pospondedOrder.getId()) or
                    (isinstance(node, restaurant) and node.getOrderId() != pospondedOrder.getId()))]
            targetRoute['route'] = ans[:]
            print('done')
