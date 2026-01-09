import psutil
import colorama

import localtypes
from typing import Any

colorama.init()

min_widget_width = 12

# ╭──────────╮
# |CPU : 100%|
# ╰──────────╯

cpu_percentage = 0
cpu_frequency = 0

def update():
    global cpu_percentage, cpu_frequency
    cpu_percentage = psutil.cpu_percent()
    cpu_frequency = psutil.cpu_freq().current

def cpu_perc(widget: localtypes.Widget) -> list[str]:
    out = ["" for i in range(3)]
    if widget.get_parameter("width") < min_widget_width:
        return out

    perc = cpu_percentage

    out[0] = f"╭{"─" * widget.get_parameter("width")}╮"
    out[2] = f"╰{"─" * widget.get_parameter("width")}╯"

    color = colorama.Fore.RESET if perc < 10 or widget.check_flag("nocolor") else colorama.Fore.GREEN if perc < 40 else colorama.Fore.YELLOW if perc < 70 else colorama.Fore.RED
    color_escape_len = len(color) + len(colorama.Fore.RESET)

    perc_string = f"{"CPU : " if not widget.check_flag("notitle") else ""}{color + str(perc).removesuffix(".0") + colorama.Fore.RESET}%"
    space = widget.get_parameter("width") - len(perc_string) + color_escape_len
    left_margin = space // 2
    right_margin = space - left_margin

    out[1] = f"|{" " * left_margin}{perc_string}{" " * right_margin}|"

    return out

def cpu_vis(widget: localtypes.Widget) -> list[str]:
    out = ["" for i in range(3)]
    if widget.get_parameter("width") < min_widget_width:
        return out

    perc = cpu_percentage

    width = widget.get_parameter("width")

    filled = round(perc * (width - 2) / 100)
    empty = width - filled

    space = widget.get_parameter("width") - 3
    left_margin = space // 2
    right_margin = space - left_margin

    out[0] = f"╭{"─" * left_margin + ("───" if widget.check_flag("notitle") else "CPU") + "─" * right_margin}╮"
    out[2] = f"╰{"─" * abs(widget.get_parameter("width"))}╯"

    color = colorama.Fore.RESET if perc < 10 or widget.check_flag("nocolor") else colorama.Fore.GREEN if perc < 40 else colorama.Fore.YELLOW if perc < 70 else colorama.Fore.RED
    out[1] = f"|{color + "█" * filled + colorama.Fore.RESET + "░" * empty}|"

    return out

def cpu_freq(widget: localtypes.Widget) -> list[str]:
    out = ["" for i in range(3)]
    if widget.get_parameter("width") < min_widget_width:
        return out

    freq = cpu_frequency

    out[1] = str(freq)

    out[0] = f"╭{"─" * widget.get_parameter("width")}╮"
    out[2] = f"╰{"─" * widget.get_parameter("width")}╯"

    return out

modules = {
    "cpu-perc": cpu_perc,
    "cpu-vis": cpu_vis,
    "cpu-freq": cpu_freq,
}

def get(widget: localtypes.Widget) -> list[str]:
    return modules[widget.type](widget)