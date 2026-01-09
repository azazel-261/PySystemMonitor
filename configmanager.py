import localtypes
import configparser

# Config syntax:
# [widget_type]
# flag1
# param1 = value1

def parse_config(path: str) -> list[localtypes.Widget]:
    parser = configparser.ConfigParser(allow_no_value=True)
    parser.read(path)
    widgets = []
    for widget in parser.sections():
        params = dict(parser.items(widget))
        for k in localtypes.default_values:
            if k not in params:
                params[k] = localtypes.default_values[k]
        wgt = localtypes.Widget(widget, params)
        widgets.append(wgt)
    return widgets
# def parse_config(path: str) -> list[localtypes.Widget]:
#     with open(path, "r") as f:
#         widgets = []
#         data = f.read().removesuffix(";").split(";")
#         for entry in data:
#             entry_data = entry.split(":")
#             wg_type = entry_data.pop(0)
#             params = {}
#             for parameter in entry_data:
#                 param = parameter.split("=")
#                 if len(param) == 2 and param[0] in localtypes.config_types:
#                     try:
#                         params[param[0]] = localtypes.config_types[param[0]](param[1])
#                     except:
#                         pass
#             wgt = localtypes.Widget(wg_type, params)
#             widgets.append(wgt)
#         return widgets


