import os
import sys
import json
from pprint import pp
import genUtilities
import pilotParser
from settings import *

template = environment.get_template("pilot.tpl")
#session, csrf_token = genUtilities.create_wiki_session()

#busted, fix later
def render_pilot_entry(pilot):
    pilot_info = dict(pilot[1])
    pilottags = {key: value for key, value in pilot_info.items() if key.startswith('pilottag')}
    sorted_tags = dict(sorted(pilottags.items()))
    formatted_string = "".join(f"|{key} = {value}\n" for key, value in sorted_tags.items())
    pp(pilot_info)
    callsign = pilot_info.get("callsign")
    results_filename = "Pilot_" + callsign + ".wiki"

    context = {
        "availability": pilot_info.get("availability"),
        "callsign": pilot_info.get("callsign"), 
        "firstname": pilot_info.get("firstname"),
        "lastname": pilot_info.get("lastname"),
        "age": pilot_info.get("age"),
        "gender": pilot_info.get("gender"),
        "faction": pilot_info.get("faction"),
        "health": pilot_info.get("health"),
        "biography": pilot_info.get("biography"),
        "gunnery": pilot_info.get("gunnery"),
        "piloting": pilot_info.get("piloting"),
        "guts": pilot_info.get("guts"),
        "tactics": pilot_info.get("tactics"),
        "pilottags": formatted_string
    }

    if "GITHUB_ACTIONS" in os.environ or "LOCAL_OVERRIDE" in os.environ:
        # Wiki page writing
        page_title = "Template:Pilot_" + callsign
        genUtilities.post_to_wiki(session, csrf_token, page_title, template.render(context))
        #if not check_factory_page(session, planet_name):
            #print("Factory entry not found on Factory Worlds page and needs to be added: ", planet_name)
    else:
        # Local file writing
        with open(results_filename, mode="w", encoding="utf-8") as results:
            results.write(template.render(context))

if __name__ == "__main__":
    results = pilotParser.process_pilot_files(pilot_dir_list)
    
    #pp(results)
    for pilot in results.items():
        render_pilot_entry(pilot)