from pymongo import MongoClient
from bson.objectid import ObjectId
from pprint import pprint

print('Hello, Welcome to the Animal Application!')

class AnimalShelter(object):
    """CRUD operations for Animal collection in MongoDB"""

    def __init__(self, username, password):  
        # provide default values for object
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.

            self.client = MongoClient('mongodb://%s:%s@localhost:54917/AAC' % (username, password))
            
            # self.client = MongoClient('mongodb://127.0.0.1:54917')
            self.database = self.client['AAC']

    # Create this method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            insert = self.database.animals.insert_one(data)
            if insert != 0:
                return True
            else:
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    # Create this method to implement the R in CRUD.
    def read(self, searchData=None):
        if searchData:
            data = self.database.animals.find(searchData, {"_id": False})  
        else:
            data = self.database.animals.find({}, {"_id": False})
        return data

    # Create this method to implement the U in CRUD
    def update(self, updateData):
        if updateData is not None:
            if updateData:
                result = self.database.animals.insert_one(updateData)
            return result;
        else:
            raise Exception("Nothing to update, save is empty")

    # Create this method to implement the D in CRUD
    def delete(self, deleteData):
        if deleteData is not None:
            if deleteData:
                result = self.database.animals.delete_one(deleteData)
        else:
            raise Exception("Nothing to delete, remove is empty")