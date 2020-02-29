init 2:
    screen housing_map_manager():
        add "Paper_Background.png"
        modal True
        zorder 101

        $ x_size_percent = 0.07
        $ y_size_percent = 0.145
        $ grid_size = [14.0, 6.0]

        $ total_places = len(mc.known_home_locations)
        $ places_so_far = 0
        $ n = grid_size[1] * grid_size[0]
        $ k = grid_size[1] / grid_size[0]
        $ height = math.ceil(math.sqrt(k * total_places))
        $ width = math.ceil(math.sqrt(total_places / k))

        $ start_row = int(math.floor((grid_size[1] - height)/2))
        $ start_col = int(math.floor((grid_size[0] - width)/2))
        $ current_row = start_row
        $ current_col = start_col

        for place in mc.known_home_locations:
            $ hex_x = x_size_percent * current_col
            $ hex_y = y_size_percent * current_row
            if current_col % 2 == 1:
                $ hex_y += y_size_percent/2

            if not place == mc.location and not place.hide_in_known_house_map:
                frame:
                    background None
                    xysize [171,150]
                    anchor [0.0,0.0]
                    align (hex_x,hex_y)
                    #align place.map_pos #TODO arange this properly
                    imagebutton:
                        anchor [0.5,0.5]
                        auto "gui/LR2_Hex_Button_%s.png"
                        focus_mask "gui/LR2_Hex_Button_idle.png"
                        action [Hide("housing_map_manager"), Return(place), Function(mc.change_location, place)]
                        sensitive place.accessable
                    text (place.formalName + " (" + str(len(place.people)) + ")").replace(" ", "\n", 2) anchor [0.5,0.5] style "map_text_style"

            else:
                frame:
                    background None
                    xysize [171,150]
                    anchor [0.0,0.0]
                    align (hex_x,hex_y)
                    imagebutton:
                        anchor [0.5,0.5]
                        idle "gui/LR2_Hex_Button_Alt_idle.png"
                        focus_mask "gui/LR2_Hex_Button_Alt_idle.png"
                        action [Hide("housing_map_manager"), Return(place), Function(mc.change_location, place)]
                        sensitive False
                    text place.formalName + "\n(" + str(len(place.people)) + ")" anchor [0.5,0.5] style "map_text_style"
            $ places_so_far += 1
            $ current_col += 1
            if places_so_far % width == 0:
                $ current_row += 1
                $ current_col = start_col


        frame:
            background None
            anchor [0.5,0.5]
            align [0.5,0.88]
            xysize [500,125]
            imagebutton:
                align [0.5,0.5]
                auto "gui/button/choice_%s_background.png"
                focus_mask "gui/button/choice_idle_background.png"
                action [Hide("housing_map_manager"), Return(mc.location)]
            textbutton "Return" align [0.5,0.5] text_style "return_button_style"

