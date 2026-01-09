from typing import Any

flags = {
    'notitle',
    'break',
    'nocolor'
}

default_values = {
    "width" : 20
}

config_types = {
    "width" : int,
}

class Widget:
    def __init__(self, type: str = "", args : dict[str, Any] | None = None):
        self.type = type
        self.args = args

    def check_flag(self, flag: str) -> bool:
        return flag in self.args

    def get_parameter(self, param: str) -> Any:
        return config_types[param](self.args[param])