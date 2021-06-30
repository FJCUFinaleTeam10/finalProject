import copy

from comtypes.automation import _
from Math.distance import distance
from model.driver import driver
from model.order import Ds
from model.restaurant import restaurant


def tripTime(driv: driver, res: restaurant, order: Ds):
    return (distance(driv.x, driv.y, res.xPosition, res.yPosition) + distance(res.xPosition, res.yPosition, order.x,
                                                                              order.y)) * 1.4


def FindVehicle(Theta_hat, Order, buffer, driverList, restaurantList):
    OrderRestaurant = restaurantList[Order.R + 1]
    minTimeDriver = driverList[0]
    minTimeTolTal = float('inf')

    for currentDriver in driverList:
        if tripTime(currentDriver, OrderRestaurant, Order) < tripTime(minTimeDriver, OrderRestaurant, Order):
            minTimeDriver = copy.copy(currentDriver)
            minTimeTolTal = tripTime(currentDriver, OrderRestaurant, Order)
    Order.setDriver(currentDriver)
    Order.setArriveTime(minTimeTolTal)
    return minTimeDriver
