import copy

from comtypes.automation import _

from Math.distance import distance
from model.driver import driver
from model.order import Ds
from model.restaurant import restaurant


def tripTime(driv: driver, res: restaurant, order: Ds):
    try:
        return distance(driv.x, driv.y, res.xPosition, res.yPosition) + \
               distance(res.xPosition, res.yPosition, order.x, order.y)
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")


def FindVehicle(Theta_hat, Order, buffer, driverList, restaurantList):
    OrderRestaurant = restaurantList[Order.R + 1]
    minTimeDriver = driverList[0]

    for currentDriver in driverList:
        if tripTime(currentDriver, OrderRestaurant, Order) < tripTime(minTimeDriver, OrderRestaurant, Order):
            minTimeDriver = copy.copy(currentDriver)
    return minTimeDriver
