class restaurant:
    def __init__(self, restaurant_id, restaurant_x, restaurant_y):
        self.id: int = restaurant_id
        self.xPosition: float = restaurant_x
        self.yPosition: float = restaurant_y

    def getLongitude(self):
        return self.xPosition

    def getLatitude(self):
        return self.yPosition

    def getId(self):
        return self.id


