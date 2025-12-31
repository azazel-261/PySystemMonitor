from typing import Any

default_values = {
    "notitle" : 0,
    "nobreak" : 0,
    "nocolor" : 0,
    "width" : 20
}

config_types = {
    "notitle" : int,
    "nobreak" : int,
    "nocolor" : int,
    "width" : int,
}

class ConfigWidget:
    def __init__(self, wg_type: str = "", args : dict[str, Any] | None = None):
        if args is None:
            args = {}
        self.wg_type = wg_type
        self.args = args
        for k in default_values:
            if k not in args:
                args[k] = default_values[k]