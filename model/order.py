from pandocfilters import Null
from sqlalchemy import null


class Ds:
    def __init__(self, orderId, timeRequest, restaurantId, vehicle, L, x, y, deadline):
        # t is the request's time
        # R is the ordered restaurant
        # V is the assigned driver
        # L is the status

        self.orderId = orderId
        self.t = timeRequest
        self.V = vehicle
        self.L = L
        self.x: float = x
        self.y: float = y
        self.deadline = deadline
        self.restaurantId = restaurantId
        self.deadline = deadline
        self.arriveTime = 0
        self.driverId = Null

    def get_timeRequest(self):
        return self.t

    def getVehicle(self):
        return self.V

    def getLongitude(self):
        return self.x

    def getAtitude(self):
        return self.y

    def getLatitude(self):
        return self.y

    def getDeadLine(self):
        return self.deadline

    def getRestaurantId(self):
        return self.restaurantId

    def setRestautantId(self, restaurantId: int):
        self.restaurantId = restaurantId

    def setDriver(self, driverId: int):
        self.V = driverId

    def setArriveTime(self, arriveTime):
        self.arriveTime = arriveTime

    def getArriveTime(self):
        return self.arriveTime

    def setDeadline(self, time: int):
        self.time = time

    def setVelocity(self, velocity):
        self.velocity = velocity

    def getVelocity(self):
        return self.velocity

    def setOrderId(self, orderId: int):
        self.orderId = orderId

    def setDriverId(self, driverId: int):
        self.driverId = driverId

    def getDriverId(self):
        return self.driverId

    def getId(self):
        return self.orderId

    def setId(self, id: int):
        self.orderId = id
