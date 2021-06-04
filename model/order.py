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
        self.x = x
        self.y = y
        self.deadline = deadline
        self.R = restaurantId
        self.deadline = deadline
