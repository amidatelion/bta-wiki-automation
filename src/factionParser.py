import os
import sys
import json
from pprint import pp
import genUtilities

def process_Faction_Collection(file_path):
    with open(file_path, "r") as json_file:
        data = json.load(json_file)
        item_name = data[0].get("items")
        return item_name

def process_files(primary_path, prefix):
    file_dict = {}
    csv_files_index = genUtilities.index_csv_files("/home/runner/work/wiki-actions-poc/wiki-actions-poc/bta/DynamicShops/")
    #csv_files_index = genUtilities.index_csv_files(["../DynamicShops/"])
    # Iterate through files in primary path and process each
    for file_name in os.listdir(primary_path):
        full_path = os.path.join(primary_path, file_name)
        if os.path.isfile(full_path):
            file_dict[file_name] = []
            if file_name.endswith(".json"):
                collection_name = process_Faction_Collection(full_path)
                add_file_contents(collection_name, csv_files_index, file_dict, file_dict[file_name], prefix)
    return file_dict

def add_file_contents(collection_name, csv_files_index, file_dict, current_file_lines, prefix):
        # Read file and get its contents
        csv_files_index[collection_name]
        with open(csv_files_index[collection_name], 'r') as file:
            lines = file.readlines()
        # Skip the first line
        lines = lines[1:]
        # Iterate over the lines in the file
        for line in lines:
            line = line.split(",")
            if line[0].startswith(prefix):
                add_file_contents(line[0], csv_files_index, file_dict, current_file_lines, prefix)
            else: 
                current_file_lines.append(line[0])


def index_csv_files(directory):
    csv_files = {}
    
    # Walk through directory recursively
    for root, _, files in os.walk(directory):
        for file in files:
            # Check if the file ends with .csv
            if file.endswith('.csv'):
                # Append the full file path to the list
                csv_files[file[:-4]]=os.path.join(root, file)
    
    return csv_files

if __name__ == "__main__":
    result = process_files(sys.argv[1], sys.argv[2])

    """get rid of this for now   
    for item_name, entries in matched_entries.items():
        print(f"Processing {item_name} list:")
        for entry in entries:
            print(entry) """

