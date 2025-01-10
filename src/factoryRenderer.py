from jinja2 import Environment, FileSystemLoader
import os
import json
import requests
import factoryParser
import genUtilities
from pprint import pp
from settings import *

template = environment.get_template("factory.tpl")

def render_factoryentry(planet, owner, rep, collection): 
    
    planet_name = planet
    results_filename = planet_name+"_store_Table.wiki"
    owner_name = owner
    reputation = rep
    weapons = []
    ammunitions = []
    gears = []
    mechs = []
    vehicles = []
    battlearmors = []
    contracts = []
    for item in collection:
        if item.startswith("Weapon_"):
            weapons.append(item)
        elif item.startswith("Ammo_"):
            ammunitions.append(item)
        elif item.startswith(("Gear_", "emod_")) and not item.startswith("Gear_Contract_"):
            gears.append(item)
        elif item.startswith("mechdef_") and not item.startswith("mechdef_ba_"):
            mechs.append(item)
        elif item.startswith("vehicledef_"):
            vehicles.append(item)
        elif item.startswith("mechdef_ba_"):
            battlearmors.append(item)
        elif item.startswith("Gear_Contract_"):
            contracts.append(item)
    
    for index, item in enumerate(weapons):
        weapons[index] = genUtilities.get_display_name(item)
    for index, item in enumerate(ammunitions):
        ammunitions[index] = genUtilities.get_display_name(item)
    for index, item in enumerate(gears):
        gears[index] = genUtilities.get_display_name(item)
    for index, item in enumerate(mechs):
        mechs[index] = genUtilities.get_display_name(item)
    for index, item in enumerate(vehicles):
        vehicles[index] = genUtilities.get_display_name(item)
    for index, item in enumerate(battlearmors):
        battlearmors[index] = genUtilities.get_display_name(item)
    for index, item in enumerate(contracts):
        contracts[index] = genUtilities.get_display_name(item)
    
    for index, item in enumerate(mechs):
        mechs[index] = '#'.join(item.rsplit(' ', 1)) + '|' + item
    for index, item in enumerate(vehicles):
        vehicles[index] = '#'.join(item.rsplit(' ', 1)) + '|' + item

    context = {
        "planet_name": planet_name,
        "owner_name": owner_name,
        "reputation": reputation,
        "weapons": weapons,
        "ammunitions": ammunitions,
        "gears": gears,
        "mechs": mechs,
        "vehicles": vehicles, 
        "battlearmors": battlearmors,
        "contracts": contracts,
    }

    
    if "GITHUB_ACTIONS" in os.environ:
        # Wiki page writing
        page_title = "Template:Factory_" + planet_name
        genUtilities.post_to_wiki(page_title, template.render(context))
    else:
        # Local file writing
        with open(results_filename, mode="w", encoding="utf-8") as results:
            results.write(template.render(context))
            print(f"... wrote {results_filename}")

if __name__ == "__main__":
    #results = factoryParser.process_files("../DynamicShops/sshops")
    results = factoryParser.process_files(bta_dir + "DynamicShops/sshops")
    pp(results)
    for planet,items in results.items():
        #print("The planet ", planet, " is owned by ", items.get('owner'), "and with reputation ", items.get('rep'), " you can buy ", items.get('items'))
        render_factoryentry(planet, items.get("owner"), items.get("rep"), items.get("items"))   