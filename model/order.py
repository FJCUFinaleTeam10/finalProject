class Ds:
    def __init__(self, label, timeRequest, restaurantId, V, L, x, y, deadline):
        # t is the request's time
        # R is the ordered restaurant
        # V is the assigned driver
        # L is the status
        self.label = label
        self.t = timeRequest
        self.V = V
        self.L = L
        self.x: float = x
        self.y: float = y
        self.deadline = deadline
        self.R = restaurantId
        self.deadline = deadline

    def get_timeRequest(self):
        return self.t

    def getVehicle(self):
        return self.V

    def getLongitude(self):
        return self.x

    def getAtitude(self):
        return self.y

    def getDeadLine(self):
        return self.deadline

    def getRestaurant(self):
        return self.R
