import copy

from model.restaurant import restaurant
from model.driver import driver
from model.order import Ds


def AssignOrder(Theta_hat, D: Ds, V: driver, RestaurantList: list):
    currentRoute = next((route for route in Theta_hat if route.get("driverId") == V.get_id()), None)

    if currentRoute is None:
        sub_rout = [RestaurantList[D.getRestaurant()], D]
        Theta_hat.append({"driverId": V.get_id(), "route": sub_rout})
    else:
        currentRoute["route"].append(RestaurantList[D.getRestaurant()])
        currentRoute["route"].append(D)

        # currentRoute = next((route for route in Theta_hat if route.get("driverId") == V.get_id()), None)
        # currRlist = [node for node in currentRoute if isinstance(node, driver) == True]
        # currOlist = [node for node in currentRoute if isinstance(node, Ds) == True]

        newList = currentRoute
        i = 0

        for i in range(len(currentRoute)):
            delayTime = 0
            j = i+1
            for j in range(len(currentRoute)+2):
                newList["route"].insert(i, RestaurantList[D.getRestaurant()])
                newList["route"].insert(j, D)


    return Theta_hat
# logic:the route will be divided into many sub_rout,  very subroute is the route for every driver, the key is driver
# id and the value is a list of the destination of restaurant and the delivery order destination, ijsut normally make
# the current destination is in the last of the list, this algorithm will have to dicuss with the professor
