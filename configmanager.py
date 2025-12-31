import localtypes

# Config syntax: widget_type:param1=1:param2=0;

def parse_config(path: str) -> list[localtypes.ConfigWidget]:
    with open(path, "r") as f:
        widgets = []
        data = f.read().removesuffix(";").split(";")
        for entry in data:
            entry_data = entry.split(":")
            wg_type = entry_data.pop(0)
            params = {}
            for parameter in entry_data:
                param = parameter.split("=")
                if len(param) == 2 and param[0] in localtypes.config_types:
                    try:
                        params[param[0]] = localtypes.config_types[param[0]](param[1])
                    except:
                        pass
            wgt = localtypes.ConfigWidget(wg_type, params)
            widgets.append(wgt)
        return widgets


