import pandas as pd
import numpy as np
import pickle
import json
import warnings
warnings.filterwarnings("ignore")

class BangaluruHouse():
    def __init__(self,total_sqft,bath,balcony,area_type,availability,size,location):
        self.total_sqft = total_sqft
        self.bath = bath
        self.balcony = balcony
        self.area_type = area_type
        self.availability = availability
        self.size = size
        self.location = location

    def get_models(self):

        with open("bangluru_json_data.json","r") as j :
            self.json_data = json.load(j)

        with open("benguluru_data_linear_model.pkl","rb") as m :
            self.model = pickle.load(m)

    def get_prediction(self):

        self.get_models()

        test_array = np.zeros(len(self.json_data["columns"]),int)

        test_array[0] = self.total_sqft
        test_array[1] = self.bath
        test_array[2] = self.balcony

        area_type_index = self.json_data["columns"].index("area_type_"+self.area_type)

        test_array[area_type_index] = 1

        availability_index = self.json_data["columns"].index("availability_"+self.availability)

        test_array[availability_index] = 1

        if "size_"+self.size in self.json_data["columns"] :
            size_index = self.json_data["columns"].index("size_"+self.size)

        else :
            self.size = "size_uncommon_size"
            size_index = self.json_data["columns"].index(self.size)

        test_array[size_index] = 1

        if "location_"+self.location in self.json_data["columns"]:
            location_index = self.json_data["columns"].index("location_"+self.location)

        else :
            self.location = "location_uncommon_location"
            location_index = self.json_data["columns"].index(self.location)

        test_array[location_index] = 1


        return np.around(self.model.predict([test_array])[0],2)
    
if __name__ == "__main__":

    area_type="Super built-up  Area"
    availability="Ready To Move"
    size="2 BHK"
    total_sqft=1056
    bath=2.0
    balcony=1.0
    location="Alandi Road"

    obj = BangaluruHouse(total_sqft,bath,balcony,area_type,availability,size,location)
    price = obj.get_prediction()
    print("Your House Price is :Rs",price,"lac")
