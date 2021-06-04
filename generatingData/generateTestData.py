import math
import os

from model import driver
from model import order
from model import restaurant
from data import rawData
import setting


def importRestaurantValue():
    R: list = []
    x_R: list = []
    y_R: list = []
    with open(setting.restaurant_dir) as openfileobject:
        for line in openfileobject:
            if line.__contains__("\n"):
                line = line.replace('\n', '')
            value = line.split('\t')
            restaurantInfo = restaurant.restaurant(int(value[0]), float(value[1]), float(value[2]))
            R.append(restaurantInfo)
            x_R.append(restaurantInfo.xPosition)
            y_R.append(restaurantInfo.yPosition)
    return R, x_R, y_R
    # for _ in range(Restaurant_num):
    #     R.append([random.randint(0, (horizon+1)), random.randint(0, (vertical+1))])
    #     x_R.append(R[_][0])
    #     y_R.append(R[_][1])


def importVehicleValue():
    V: list = []
    x_V: list = []
    y_V: list = []

    with open(setting.vehicles_dir) as openfileObject:
        for line in openfileObject:
            if line.__contains__("\n"):
                line = line.replace('\n', '')
            value = line.split('\t')
            vehicleInfo = driver.driver(int(value[0]), float(value[1]), float(value[2]))
            V.append(vehicleInfo)
            x_V.append(vehicleInfo.x)
            y_V.append(vehicleInfo.y)
    return V, x_V, y_V
    # for _ in range(Vehicle_num):
    #     V.append([random.randint(0, (horizon + 1)), random.randint(0, (vertical + 1))])
    #     x_V.append(V[_][0])
    #     y_V.append(V[_][1])


def importOrderValue():
    # value1: int = -1
    # value2: int = -1
    # value3: int = -1
    # value4: float = -1
    # value5: float = -1
    # value6: int = -1
    # value7: int = -1

    D_0: list = []
    D_x: list = []
    D_y: list = []
    with open(setting.order_dir) as openFileObject:
        for line in openFileObject:
            if line.__contains__("\n"):
                line = line.replace('\n', '')
            value = line.split('_')

            # value1 = max(value1, int(value[0]))
            # value2 = max(value2, int(value[1]))
            # value3 = max(value3, int(value[2]))
            # value4 = max(value4, float(value[3]))
            # value5 = max(value5, float(value[4]))
            # value6 = max(value6, int(value[5]))
            # value7 = max(value7, int(value[6]))

            orderInfo = order.Ds(int(value[0]), int(value[1]), int(value[5]), 0, 0,
                                 float(value[3]), float(value[4]),
                                 int(value[6]))
            D_0.append(orderInfo)
            D_x.append(orderInfo.x)
            D_y.append(orderInfo.y)

    # print(value1, " ", value2, " ", value3, " ", value4, " ", value5, " ", value6, " ", value7)
    return D_0, D_x, D_y


# for _ in range(Order_num):
#     D_0.append(order.Ds(_, random.randint(0, T + 1), random.randint(0, Restaurant_num), 0, 0))
importOrderValue()
