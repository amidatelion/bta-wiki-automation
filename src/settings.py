import os
from jinja2 import Environment, FileSystemLoader

if "GITHUB_ACTIONS" in os.environ:
    bta_dir = "/home/runner/work/BattleTech-Advanced/BattleTech-Advanced/bta/"
    jinja_dir = "/home/runner/work/BattleTech-Advanced/BattleTech-Advanced/wiki-gen/templates/"
else:
    bta_dir = "../../BattleTech-Advanced/"
    jinja_dir = "../templates/"

environment = Environment(loader=FileSystemLoader(jinja_dir))

csv_dir_list = [bta_dir + "DynamicShops/", bta_dir + "Community Content/", bta_dir + "Flashpoint Unit Module/",
    bta_dir + "Heavy Metal Unit Module/", bta_dir + "Urban Warfare Unit Module"]