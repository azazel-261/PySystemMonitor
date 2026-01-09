import localtypes
import json

# Config syntax:
# [
#   {
#     "type" : "type",
#     "parameters" : {
#       "param1" : somevalue
#     },
#     "flags" : ["someflag"]
#   }
# ]

def parse_json(filename):
    with open(filename, "r") as f:
        raw_data = f.read()
        data = json.loads(raw_data)
    if type(data) != list:
        raise TypeError("Invalid data in JSON! Items should be in a list")
    widgets = []
    for index, item in  enumerate(data):
        if type(item) != dict:
            raise TypeError(f"Error at item {index}: invalid data in JSON! Every item should be in a dict")
        wg_type = item["type"]
        flags = {flag : None for flag in item["flags"]}
        wg_args = item["parameters"] | flags
        widgets.append(localtypes.Widget(wg_type, wg_args))
    return widgets

