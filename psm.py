import os
import time

import keyboard
import localtypes
import modules
import configmanager

def print_module(data: list[str]):
    for t in data:
        print(t)

def draw_widgets(widgets_to_draw: list[localtypes.ConfigWidget]):
    i = 0
    while i < len(widgets_to_draw):
        to_draw = ["" for i in range(3)]
        wgt = modules.get(widgets_to_draw[i].wg_type, **widgets_to_draw[i].args)
        for x in range(3):
            to_draw[x] += wgt[x]
        i += 1
        while i < len(widgets_to_draw) and widgets_to_draw[i-1].args["nobreak"]:
            wgt = modules.get(widgets_to_draw[i].wg_type, **widgets_to_draw[i].args)
            for x in range(3):
                to_draw[x] += wgt[x]
            i += 1
        print_module(to_draw)

widgets = configmanager.parse_config("data/psm.config")

while True:
    os.system("cls")
    modules.update()
    draw_widgets(widgets)
    time.sleep(1)
