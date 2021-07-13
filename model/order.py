class Ds:
    def __init__(self, label, timeRequest, restaurantId, vehicle, L, x, y, deadline):
        # t is the request's time
        # R is the ordered restaurant
        # V is the assigned driver
        # L is the status

        self.label = label
        self.t = timeRequest
        self.V = vehicle
        self.L = L
        self.x: float = x
        self.y: float = y
        self.deadline = deadline
        self.R = restaurantId
        self.deadline = deadline
        self.arriveTime = 0

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

    def getRestaurant(self):
        return self.R

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
