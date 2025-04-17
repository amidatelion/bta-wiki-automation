import os
import sys
import json
from pprint import pp
import genUtilities
from settings import *

def process_vehicle_files(directory):
    vehicle_dict = {}
    for root, _, files in os.walk(directory):
        for file in files:
            if file.startswith("vehicledef_") and file.endswith(".json"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    data = json.load(f)
                    if "unit_controllableTank" in data["VehicleTags"]["items"]:
                        print(f"Vehicle is {file_path} and is controllable")
                        #vehicle_entry = parse_vehicle_json(file_path)
                        #vehicle_dict.update(vehicle_entry)

    return vehicle_dict

if __name__ == "__main__":
    #result = process_vehicle_files(vehicle_dir_list)
    result = process_vehicle_files("/Users/amidatelion/git/amids-vers/BattleTech-Advanced/VIPAdvanced")
    #pp(result)