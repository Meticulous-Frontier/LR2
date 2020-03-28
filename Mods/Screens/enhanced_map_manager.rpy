# override the default map_manager, to allow for one click location changes
# instead of clicking return after each choice

init -1 python:
    def get_location_tooltip(location):
        known_people = sorted(known_people_at_location(location), key = lambda x: x.name)
        if len(known_people) == 0:
            return ""
        tooltip = "You know " + str(len(known_people))
        if len(known_people) == 1:
            tooltip += " person here:\n"
        else:
            tooltip += " people here:\n"
        for person in known_people:
            tooltip += person.name + " " + person.last_name + "\n"
        return tooltip

    def get_location_on_enter_events(location):
        for person in [x for x in location.people if x.on_room_enter_event_list]:
            for an_action in person.on_room_enter_event_list:
                if an_action.is_action_enabled(person):
                    return True
        return False

init 2:
    screen map_manager():
        add "Paper_Background.png"
        modal True
        zorder 100

        $ x_size_percent = 0.07
        $ y_size_percent = 0.145

        for place in list_of_places: #Draw the text buttons over the background
            if place.visible:
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
                            tooltip get_location_tooltip(place)
                        text place.formalName + "\n(" + str(len(place.people)) + ")" + ("\n{color=#FFFF00}Event!{/color}" if get_location_on_enter_events(place) else "") anchor [0.5,0.5] style "map_text_style"
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
                            tooltip get_location_tooltip(place)
                        text place.formalName + "\n(" + str(len(place.people)) + ")" + ("\n{color=#FFFF00}Event!{/color}" if get_location_on_enter_events(place) else "") anchor [0.5,0.5] style "map_text_style"


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
                    sensitive len(mc.known_home_locations) > 0
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
                    sensitive len(mc.known_home_locations) > 0
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
            textbutton "Return" align [0.5,0.5] text_style "return_button_style"


        $ tooltip = GetTooltip()
        if tooltip:
            text "[tooltip]" style "textbutton_text_style" size 18
