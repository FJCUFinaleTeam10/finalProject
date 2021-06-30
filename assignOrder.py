import copy

from model.restaurant import restaurant
from model.driver import driver
from model.order import Ds


def AssignOrder(Theta_hat, D: Ds, V: driver, RestaurantList: restaurant):
    currentRoute = next((route for route in Theta_hat if route.get("driverId") == V.get_id()), None)
    if currentRoute is None:
        sub_rout = []
        targetRestaurant: restaurant = RestaurantList[D.getRestaurant()]
        sub_rout.append({'timeAssign': D.get_timeRequest(),
                         'timeDeadline': D.getDeadLine(),
                         'restaurantLongitude': targetRestaurant.getLongitude(),
                         'restaurantLatitude': targetRestaurant.getLatitude(),
                         'orderLongitude': D.getLongitude(),
                         'orderLatitude': D.getAtitude(),
                         'arriveTime': D.getArriveTime()})
        Theta_hat.append({"driverId": V.get_id(), "route": sub_rout})
    else:
        targetRestaurant: restaurant = RestaurantList[D.getRestaurant()]
        currentRoute["route"].append({'timeAssign': D.get_timeRequest,
                                      'timeDeadline': D.getDeadLine(),
                                      'restaurantLongitude': targetRestaurant.getLongitude(),
                                      'restaurantLatitude': targetRestaurant.getLatitude(),
                                      'orderLongitude': D.getLongitude(),
                                      'orderLatitude': D.getAtitude(),
                                      'arriveTime': D.getArriveTime()})
    return Theta_hat
# logic:the route will be divided into many sub_rout,  very subroute is the route for every driver, the key is driver
# id and the value is a list of the destination of restaurant and the delivery order destination, ijsut normally make
# the current destination is in the last of the list, this algorithm will have to dicuss with the professor
