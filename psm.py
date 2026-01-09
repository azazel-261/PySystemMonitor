import os
import time

import keyboard
import localtypes
import modules
import configmanager

def draw_widgets(widgets_to_draw: list[localtypes.Widget]):
    i = 0
    while i < len(widgets_to_draw):
        data = ["" for i in range(3)]
        wgt = modules.get(widgets_to_draw[i])
        for x in range(3):
            data[x] += wgt[x]
        i += 1
        while i < len(widgets_to_draw) and not widgets_to_draw[i-1].check_flag("break"):
            wgt = modules.get(widgets_to_draw[i])
            for x in range(3):
                data[x] += wgt[x]
            i += 1
        for t in data:
            print(t)

widgets = configmanager.parse_json("data/widgets.json")

while True:
    modules.update()
    os.system("cls")
    draw_widgets(widgets)
    time.sleep(1)
