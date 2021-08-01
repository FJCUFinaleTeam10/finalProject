from pymongo import MongoClient
from generatingData import generateTestData
from model.driver import driver
from model.order import Ds
from model.restaurant import restaurant


def get_database(database):
    client = MongoClient('60.251.157.47', 27017)
    # Create the database for our example (we will use the same database throughout the tutorial
    return client[database]


def insert_database(model, database):
    if isinstance(model, restaurant):
        post = {"latitude": model.getLatitude(),
                "longitude": model.getLongitude()
                }
        collectionIndex = database.restaurant
        index_id = collectionIndex.insert_one(post).inserted_id
        print(index_id)
    if isinstance(model, Ds):
        post = {"latitude": model.getLatitude(),
                "longitude": model.getLongitude()
                }
        collectionIndex = database.order
        index_id = collectionIndex.insert_one(post).inserted_id
        print(index_id)
    if isinstance(model, driver):
        post = {"latitude": model.getLatitude(),
                "longitude": model.getLongitude(),
                "velocity":  0,
                "capacity":  0
                }
        collectionIndex = database.driver
        index_id = collectionIndex.insert_one(post).inserted_id
        print(index_id)


if __name__ == "__main__":
    Ds_0, D_x, D_y = generateTestData.importOrderValue()
    vehiceList, vehiclelist_x, vehiclelist_y = generateTestData.importVehicleValue()
    restaurantList, restauranList_x, restauranList_y = generateTestData.importRestaurantValue()

    db = get_database('RMDP')

    for index in restaurantList:
        insert_database(index, db)
    for index in vehiceList:
        insert_database(index, db)
