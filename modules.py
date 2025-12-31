import psutil
import colorama

colorama.init()

min_widget_width = 12

# ╭──────────╮
# |CPU : 100%|
# ╰──────────╯

cpu_percentage = 0

def update():
    global cpu_percentage
    cpu_percentage = psutil.cpu_percent()

def cpu_perc(**kwargs) -> list[str]:
    out = ["" for i in range(3)]
    if kwargs["width"] < min_widget_width:
        return out

    perc = cpu_percentage

    out[0] = f"╭{"─" * kwargs["width"]}╮"
    out[2] = f"╰{"─" * kwargs["width"]}╯"

    color = colorama.Fore.RESET if perc < 10 or kwargs["nocolor"] else colorama.Fore.GREEN if perc < 40 else colorama.Fore.YELLOW if perc < 70 else colorama.Fore.RED
    color_escape_len = len(color) + len(colorama.Fore.RESET)

    perc_string = f"CPU : {color + str(perc).removesuffix(".0") + colorama.Fore.RESET}%"
    space = kwargs["width"] - len(perc_string) + color_escape_len
    left_margin = space // 2
    right_margin = space - left_margin

    out[1] = f"|{" " * left_margin}{perc_string}{" " * right_margin}|"

    return out

def cpu_vis(**kwargs) -> list[str]:
    out = ["" for i in range(3)]
    if kwargs["width"] < min_widget_width:
        return out

    perc = cpu_percentage

    width = kwargs["width"]

    filled = round(perc * (width - 2) / 100)
    empty = width - filled

    space = kwargs["width"] - 3
    left_margin = space // 2
    right_margin = space - left_margin

    out[0] = f"╭{"─" * left_margin + ("───" if kwargs["notitle"] else "CPU") + "─" * right_margin}╮"
    out[2] = f"╰{"─" * abs(kwargs["width"])}╯"

    color = colorama.Fore.RESET if perc < 10 or kwargs["nocolor"] else colorama.Fore.GREEN if perc < 40 else colorama.Fore.YELLOW if perc < 70 else colorama.Fore.RED
    out[1] = f"|{color + "█" * filled + colorama.Fore.RESET + "░" * empty}|"

    return out

modules = {
    "cpu-perc": cpu_perc,
    "cpu-vis": cpu_vis
}

def get(name: str, **kwargs) -> list[str]:
    return modules[name](**kwargs)