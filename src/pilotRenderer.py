import os
import sys
import json
from pprint import pp
import genUtilities
import pilotParser
from settings import *

#template = environment.get_template("pilot.tpl")
#session, csrf_token = genUtilities.create_wiki_session()

#busted, fix later
def render_pilot_entry(pilot):
    pilot_info = dict(pilot[1])
    firstname = pilot_info.get("firstname")
    print(firstname)


if __name__ == "__main__":
    results = pilotParser.process_pilot_files(pilot_dir_list)
    
    #pp(results)
    for pilot in results.items():
        render_pilot_entry(pilot)