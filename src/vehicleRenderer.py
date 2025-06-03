from jinja2 import Environment, FileSystemLoader
import os
import json
import requests
import vehicleParser
import genUtilities
from pprint import pp
from settings import *

template = environment.get_template("vehicle.tpl")

if os.getenv("WIKI_USER") and os.getenv("WIKI_PASS"):
    session, csrf_token = genUtilities.create_wiki_session()

def check_vehicle_page(session, vehicle):
    #planet_url = planet.replace(" ", "_")
    vehicle_check = vehicle
    check_resp = session.post(api_url, data={
	"action": "query",
	"format": "json",
	"prop": "revisions",
	"titles": "Full_List_of_Vehicles",
	"formatversion": "2",
	"rvprop": "content",
	"rvslots": "*"
    })
    data = check_resp.json()
    data = json.dumps(data)
    return vehicle_check in data

def render_vehicleentry(vehicle, components, tonnage, propulsion, armorvalues, totalarmor, totalstructure, coresize, coretype, speed, icon):
    
    vehicle_name = vehicle
    vehicle_file = vehicle_name.replace("/", "_")
    results_filename = vehicle_file+"_entry_Table.wiki"
    weapons = []
    ammunitions = []
    gears = []
    
    for item in components:
        if item.startswith("Weapon_"):
            weapons.append(item)
        elif item.startswith("Ammo_"):
            ammunitions.append(item)
        elif item.startswith(("Gear_")) and not item.startswith("emod_"):
            gears.append(item)

    for index, item in enumerate(weapons):
        weapons[index] = genUtilities.get_display_name(item)
    for index, item in enumerate(ammunitions):
        ammunitions[index] = genUtilities.get_display_name(item)
    for index, item in enumerate(gears):
        gears[index] = genUtilities.get_display_name(item)

    
    frontarmor = armorvalues.get("FrontArmor", "None")
    leftarmor = armorvalues.get("LeftArmor", "None")
    rightarmor = armorvalues.get("RightArmor", "None")
    reararmor = armorvalues.get("RearArmor", "None")
    turretarmor = armorvalues.get("TurretArmor", "None")
    

    context = {
        "icon": icon,
        "name": vehicle_name,
        "uiname": vehicle_name,
        "tonnage": tonnage,
        "propulsion": propulsion,
        "speed": speed,
        "enginetype": coretype,
        "enginecore": coresize,
        "armortotal": totalarmor,
        "structuretotal": totalstructure,
        "frontarmor": frontarmor,
        "leftarmor": leftarmor,
        "rightarmor": rightarmor,
        "reararmor": reararmor,
        "turretarmor": turretarmor,
        "gears": gears,
        "weapons": weapons,
        "ammunitions": ammunitions,
    }
    
    if "GITHUB_ACTIONS" in os.environ or "LOCAL_OVERRIDE" in os.environ:
        # Wiki page writing
        page_title = "Template:Vehicle_" + vehicle_name
        print("Posting to Template:Vehicle_", vehicle_name)
        genUtilities.post_to_wiki(session, csrf_token, page_title, template.render(context))
        if not check_vehicle_page(session, vehicle_name):
            print("Vehicle entry not found on List of Vehicles page and needs to be added: ", vehicle_name)
    else:
        # Local file writing
        with open(results_filename, mode="w", encoding="utf-8") as results:
            results.write(template.render(context))
            #print(f"... wrote {results_filename}")

#def assemble_list_of_vehicles()
def output_vehicles_by_tonnage(results):
    categories = {
        "Light": [],
        "Medium": [],
        "Heavy": [],
        "Assault": []
    }

    for name, info in results.items():
        tonnage = info.get("Tonnage", 0)
        if 0 <= tonnage <= 39:
            categories["Light"].append(name)
        elif 40 <= tonnage <= 59:
            categories["Medium"].append(name)
        elif 60 <= tonnage <= 79:
            categories["Heavy"].append(name)
        elif 80 <= tonnage <= 100:
            categories["Assault"].append(name)

    # Sort each category by tonnage
    for cat in categories:
        categories[cat].sort()

    # Output the result
    for cat in ["Light", "Medium", "Heavy", "Assault"]:
        print(f"{cat}:")
        for name in categories[cat]:
            print(f"{{{{Vehicle_{name}}}}}")
        print()  # Add a newline between categories


if __name__ == "__main__":
    results = vehicleParser.process_vehicle_files(bta_dir + "/VIPAdvanced")
    #pp(results)
    for vehicle,items in results.items():
        render_vehicleentry(vehicle, items.get("Components"), items.get("Tonnage"), items.get("Propulsion"), items.get("ArmorValues"), items.get("TotalArmor"), items.get("TotalStructure"), items.get("CoreSize"), items.get("CoreType"), items.get("Speed"), items.get("Icon"))   
    print("To add to List of Vehicles page if necessary:")
    output_vehicles_by_tonnage(results)


