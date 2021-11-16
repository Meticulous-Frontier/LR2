# override the default map_manager, to allow for one click location changes
# instead of clicking return after each choice

init -1 python:
    def create_tooltip_dictionary():
        start_time = time.time()
        result = {}
        for place in [x for x in list_of_places if x.hide_in_known_house_map and x.visible]:
            result[place.name] = [get_location_tooltip(place), get_location_on_enter_events(place)]

        if debug_log_enabled:
            add_to_debug_log("Map Buildup Time: {total_time:.3f}", start_time)
        return result

    def get_location_tooltip(location):
        known_people = sorted(known_people_at_location(location), key = lambda x: x.name)
        if __builtin__.len(known_people) == 0:
            return ""
        tooltip = "You know " + str(__builtin__.len(known_people)) + (" person here:\n" if __builtin__.len(known_people) == 1 else " people here:\n")
        for person in known_people:
            tooltip += person.name + " " + person.last_name + "\n"
        return tooltip

    def get_location_on_enter_events(location):
        for person in [x for x in location.people if x.on_room_enter_event_list]:
            if any(x for x in person.on_room_enter_event_list if x.is_action_enabled(person)):
                return True
        if any(x for x in location.on_room_enter_event_list if x.is_action_enabled()):
            return True
        return False

init 2:
    screen map_manager():
        add "Paper_Background.png"
        modal True
        zorder 100


        default tt_dict = create_tooltip_dictionary()
        default tt = Tooltip(None)

        $ x_size_percent = 0.07
        $ y_size_percent = 0.145

        for place in [x for x in list_of_places if x.hide_in_known_house_map and x.visible]: #Draw the text buttons over the background
            $ hex_x = x_size_percent * place.map_pos[0]
            $ hex_y = y_size_percent * place.map_pos[1]
            if place.map_pos[0] % 2 == 1:
                $ hex_y += y_size_percent/2
            if not place == mc.location:
                frame:
                    background None
                    xysize [171,150]
                    anchor [0.0,0.0]
                    align (hex_x,hex_y)
                    imagebutton:
                        anchor [0.5,0.5]
                        auto "gui/LR2_Hex_Button_%s.png"
                        focus_mask "gui/LR2_Hex_Button_idle.png"

                        action [Function(mc.change_location, place), Return(place)]
                        sensitive place.accessable #TODO: replace once we want limited travel again with: place in mc.location.connections
                        hovered tt.Action(tt_dict[place.name][0])
                    text (place.formal_name + "\n(" + str(place.get_person_count()) + ")").replace(" ", "\n", 2) + ("\n{color=#FFFF00}Event!{/color}" if tt_dict[place.name][1] else "") anchor [0.5,0.5] style "map_text_style"
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
                        action [Function(mc.change_location, place), Return(place)]
                        sensitive True
                        hovered tt.Action(tt_dict[place.name][0])
                    text (place.formal_name + "\n(" + str(place.get_person_count()) + ")").replace(" ", "\n", 2) + ("\n{color=#FFFF00}Event!{/color}" if tt_dict[place.name][1] else "") anchor [0.5,0.5] style "map_text_style"


            ##TODO: add a sub map to housing_map_manager() so we can go to people's homes

        $ xy_pos = [7,4]
        $ hex_x = x_size_percent * xy_pos[0]
        $ hex_y = y_size_percent * xy_pos[1]
        if xy_pos[0] % 2 == 1:
            $ hex_y += y_size_percent/2

        if mc.location in mc.known_home_locations:
            frame:
                background None
                xysize [171,150]
                anchor [0.0,0.0]
                align (hex_x,hex_y)
                imagebutton:
                    anchor [0.5,0.5]
                    idle "gui/LR2_Hex_Button_Alt_idle.png"
                    focus_mask "gui/LR2_Hex_Button_Alt_idle.png"
                    action Show("housing_map_manager")
                    sensitive __builtin__.len(mc.known_home_locations) > 0
                text "Visit Someone..." anchor [0.5,0.5] style "map_text_style"
        else:
            frame:
                background None
                xysize [171,150]
                anchor [0.0,0.0]
                align (hex_x, hex_y)
                imagebutton:
                    anchor [0.5,0.5]
                    auto "gui/LR2_Hex_Button_%s.png"
                    focus_mask "gui/LR2_Hex_Button_idle.png"
                    action Show("housing_map_manager")
                    sensitive __builtin__.len(mc.known_home_locations) > 0
                text "Visit Someone..." anchor [0.5,0.5] style "map_text_style"

        frame:
            background None
            anchor [0.5,0.5]
            align [0.5,0.88]
            xysize [500,125]
            imagebutton:
                align [0.5,0.5]
                auto "gui/button/choice_%s_background.png"
                focus_mask "gui/button/choice_idle_background.png"
                action Return(mc.location)
            textbutton "Return" align [0.5,0.5] style "transparent_style" text_style "return_button_style"


        if tt.value:
            text tt.value style "textbutton_text_style" size 18 xalign 0.02 yalign 0.02
