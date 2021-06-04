from comtypes.automation import _

from Math.distance import distance
from model.driver import driver
from model.order import Ds
from model.restaurant import restaurant


def tripTime(driver: driver, res: restaurant, order: Ds):
    return distance(driver.x, driver.y, res.xPosition, res.yPosition) + \
           distance(res.xPosition, res.yPosition, order.x, order.y)


def FindVehicle(Theta_hat, Order, buffer, driverList,restaurantList):
    OrderRestaurant = restaurantList[Order.R + 1]
    minTimeDriver = driverList[0]

    for driver in driverList:
        if tripTime(driver, OrderRestaurant, Order) < tripTime(minTimeDriver, OrderRestaurant, Order):
            minTimeDriver = driver
    return minTimeDriver
