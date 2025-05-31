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
        genUtilities.post_to_wiki(session, csrf_token, page_title, template.render(context))
        #if not check_factory_page(session, planet_name):
            #print("Factory entry not found on Factory Worlds page and needs to be added: ", planet_name)
    else:
        # Local file writing
        with open(results_filename, mode="w", encoding="utf-8") as results:
            results.write(template.render(context))
            #print(f"... wrote {results_filename}")


if __name__ == "__main__":
    results = vehicleParser.process_vehicle_files(bta_dir + "/VIPAdvanced")
    #pp(results)
    for vehicle,items in results.items():
        #print("The planet ", planet, " is owned by ", items.get('owner'), "and with reputation ", items.get('rep'), " you can buy ", items.get('items'))
        render_vehicleentry(vehicle, items.get("Components"), items.get("Tonnage"), items.get("Propulsion"), items.get("ArmorValues"), items.get("TotalArmor"), items.get("TotalStructure"), items.get("CoreSize"), items.get("CoreType"), items.get("Speed"), items.get("Icon"))   