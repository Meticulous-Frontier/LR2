init 2:
    screen housing_map_manager():
        add "Paper_Background.png"
        modal True
        zorder 101

        default max_places_per_row = 5
        default x_offset_per_place = 0.145
        default y_offset_per_row = 0.07
        default locations = [x for x in mc.known_home_locations if not x.hide_in_known_house_map]
        default tt_dict = create_tooltip_dictionary(locations)
        default tt = Tooltip(None)

        $ x_pos = 0
        $ y_pos = 0
        for place in locations:
            $ tile_info = get_location_tile_text(place, tt_dict)

            frame:
                background None
                xysize [171,150]
                anchor [0.0,0.0]
                align [0.1 + (x_offset_per_place * x_pos), 0.1 + (y_offset_per_row * y_pos)]
                imagebutton:
                    anchor [0.5,0.5]
                    if not place == mc.location:
                        auto "gui/LR2_Hex_Button_%s.png"
                        focus_mask "gui/LR2_Hex_Button_idle.png"
                        sensitive place.accessable
                    else:
                        idle "gui/LR2_Hex_Button_Alt_idle.png"
                        focus_mask "gui/LR2_Hex_Button_Alt_idle.png"
                        sensitive False
                    action [Hide("housing_map_manager"), Return(place), Function(mc.change_location, place)]
                    hovered tt.Action(tt_dict[place.name][0])
                text "[tile_info]" anchor [0.5,0.5] style "map_text_style"

            $ x_pos += 1
            if x_pos >= max_places_per_row + 0.5:
                $ x_pos = 0
                $ y_pos += 1
                $ x_pos += .5 if y_pos % 2 == 1 else 0

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

        if tt.value:
            text "[tt.value]" style "textbutton_text_style" text_align 0.0 size 18 xalign 0.95 yalign 0.98
