class driver:
    def __init__(self, driver_id, driver_x, driver_y, velocity: float = 0.0):
        self.id: int = driver_id
        self.x: float = driver_x
        self.y: float = driver_y
        self.velocity: float = velocity

    def get_id(self):
        return self.id

    def get_Longitude(self):
        return self.x

    def get_id(self):
        return self.id

    def getLatitude(self):
        return self.y

    def setVelocity(self, velocity):
        self.velocity = velocity

    def getVelocity(self):
        return self.velocity
