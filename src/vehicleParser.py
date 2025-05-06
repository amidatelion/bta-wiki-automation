import os
import sys
import json
from pprint import pp
import genUtilities
from settings import *

def add_vehicle_inventory(file_path):
    with open(file_path, "r") as json_file:
        data = json.load(json_file)
        item_name = data[0].get("items")
        print("item_name")
        #if not "" in item_name 

def remove_unwanted_components(data):
    keywords = ['slots', 'HeatSink', 'Tank', 'Tracked', 'Hover']
    filtered_data = {}
    for filename, components in data.items():
        filtered_components = [
            comp for comp in components
            if 'ComponentDefID' in comp and not any(keyword in comp['ComponentDefID'] for keyword in keywords)
        ]
        filtered_data[filename] = filtered_components
    return filtered_data

def process_vehicle_files(directory):
    vehicle_dict = {}
    for root, _, files in os.walk(directory):
        for file in files:
            if file.startswith("vehicledef_") and file.endswith(".json"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    data = json.load(f)
                    if "unit_controllableTank" in data["VehicleTags"]["items"]:
                        # Key by UIName, not file_path?
                        vehicle_dict[file_path] = data["inventory"]
                        vehicle_dict = remove_unwanted_components(vehicle_dict)
    return vehicle_dict

if __name__ == "__main__":
    #result = process_vehicle_files(vehicle_dir_list)
    result = process_vehicle_files(bta_dir + "/VIPAdvanced")
    #pp(result)