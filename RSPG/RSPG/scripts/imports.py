import skyport as sp

pygame = sp.pygame
np = sp.imports.np
math = sp.imports.math
shapely = sp.imports.shapely
logger = sp.logger

import json
import os
import sys


import core

util = sp.Util()
delta_timer = sp.Delta_timer()
loader = sp.Loader(core.__file__)


game_config = loader.read("configs/game_config.json")
if( game_config == None ):
    logger.output_print_data()
    exit(1)


dm = sp.Display_Manager(
    window_size=game_config["start_up"]["window_size"],
    display_size=game_config["start_up"]["game_resolution"],
    window_name="Royal-Skies",
    window_ico=loader.image("pt-17.png")
)




