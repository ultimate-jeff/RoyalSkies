


from scripts.imports import *
from scripts.defs import (
    Vector,
    Plane
)



dm.running = True
dm.target_fps = 60
while dm.running:

    dm.event_handler()
    dm.update_window()
    dm.tick(dm.target_fps)

