init -1 python:
    if "#ff2c2c" in readable_color_list:
        readable_color_list.remove("#ff2c2c") #Red
    if "#696eff" in readable_color_list:
        readable_color_list.remove("#696eff") #Blue

    if not "#cd5c5c" in readable_color_list:
        readable_color_list.append("#cd5c5c") #Indian Red
    if not "#87cefa" in readable_color_list:
        readable_color_list.append("#87cefa") #Light Sky Blue

