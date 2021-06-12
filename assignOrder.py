import copy

from model.restaurant import restaurant
from model.driver import driver
from model.order import Ds


def AssignOrder(Theta_hat, D: Ds, V: driver, RestaurantList: restaurant):
    if V.get_id() not in Theta_hat:
        sub_rout = []
        targetResttaurant: restaurant = RestaurantList[D.getRestaurant()]
        sub_rout.append([targetResttaurant.getLongitude(), targetResttaurant.getLatitude()])
        sub_rout.append([D.getLongitude(), D.getAtitude()])
        Theta_hat.append([V.get_id(), sub_rout])
    else:
        sub_rout = copy.copy(Theta_hat[V.get_id()])
        targetResttaurant: restaurant = RestaurantList[D.getRestaurant()]
        sub_rout.append([targetResttaurant.getLongitude(), targetResttaurant.getLatitude()])
        sub_rout.append([D.getLongitude, D.getAtitude()])
    return Theta_hat
# logic:the route will be divided into many sub_rout,  very subroute is the route for every driver, the key is driver
# id and the value is a list of the destination of restaurant and the delivery order destination, ijsut normally make the current destination is in the last of the list, this algorithm will have to dicuss with the professor
