# override the default map_manager, to allow for one click location changes
# instead of clicking return after each choice

init -1 python:
    def create_tooltip_dictionary(locations):
        start_time = time.time()
        result = {}
        for place in locations:
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
            info = []
            #added girlfriend statuses to beginning
            if person.has_exact_role(affair_role):
                info.append(" {image=paramour_token_small}")
            if person.has_exact_role(harem_role):
                info.append(" {image=harem_token_small}")
            if person.has_exact_role(girlfriend_role):
                info.append(" {image=gf_token_small}")
            #dialog infront of name to catch eye faster
            if any(not isinstance(x, Limited_Time_Action) and x.is_action_enabled(person) for x in person.on_talk_event_list):
                info.append("{image=speech_bubble_exclamation_token_small}")
            elif any(x.name != "Ask new title" and x.is_action_enabled(person) for x in person.on_talk_event_list):
                info.append("{image=speech_bubble_token_small}")
            info.append(person.name)
            info.append(person.last_name)
            if person.knows_pregnant():
                info.append("{image=feeding_bottle_token_small}")
            if person.serum_effects:
                info.append("{image=vial_token_small}")
            if person.infractions:
                info.append("{image=infraction_token_small}")
            if person.has_role([trance_role, heavy_trance_role, very_heavy_trance_role]) and person.event_triggers_dict.get("trance_training_available", True):
                info.append("{image=lust_eye_token_small}")
            if person.arousal > 60:
                info.append("{image=arousal_token_small}")
            info.append("\n")
            tooltip += " ".join(info)
        return tooltip

    def get_location_on_enter_events(location):
        for person in [x for x in location.people if x.on_room_enter_event_list]:
            if any(x for x in person.on_room_enter_event_list if x.is_action_enabled(person) and not x.effect in ["work_spank_opportunity"]):
                return True
        if any(x for x in location.on_room_enter_event_list if x.is_action_enabled()):
            return True
        return False

    def get_location_tile_text(location, tt_dict):
        #added to show icons in tile text to bring attention that there is something there worth checking out etc
        known_people = known_people_at_location(location)
        #setting the catches
        extra_info = []
        if any(x for x in known_people if x.has_exact_role(harem_role)):
            extra_info.append("{image=harem_token_small}")
        if any(x for x in known_people if x.has_exact_role(affair_role)):
            extra_info.append("{image=paramour_token_small}")
        if any(x for x in known_people if x.has_exact_role(girlfriend_role)):
            extra_info.append("{image=gf_token_small}")
        if any(x for x in known_people if x.knows_pregnant()):
            extra_info.append("{image=feeding_bottle_token_small}")
        if any(x for x in known_people if x.has_role([trance_role, heavy_trance_role, very_heavy_trance_role]) and x.event_triggers_dict.get("trance_training_available", True)):
            extra_info.append("{image=lust_eye_token_small}")
        if any(y for y in known_people if any(not isinstance(x, Limited_Time_Action) and x.is_action_enabled(y) for x in y.on_talk_event_list)):
            extra_info.append("{image=speech_bubble_exclamation_token_small}")
        if any(y for y in known_people if any(x.name != "Ask new title" and x.is_action_enabled(y) for x in y.on_talk_event_list)):
            extra_info.append("{image=speech_bubble_token_small}")
        if any(x for x in known_people if x.arousal >= 60):
            extra_info.append("{image=arousal_token_small}")

        info = []
        if extra_info:
            info.append(" ".join(extra_info) + "\n")
        info.append(location.formal_name.replace(" ", "\n", 2))
        info.append("\n(")
        info.append(str(len(known_people_at_location(location))))
        info.append("/")
        info.append(str(location.get_person_count()))
        info.append(")")
        if tt_dict[location.name][1]:
            info.append("\n{color=#FFFF00}Event!{/color}")
        return "".join(info)

init 2:
    screen map_manager():
        add "Paper_Background.png"
        modal True
        zorder 100

        default locations = [x for x in list_of_places if x.hide_in_known_house_map and x.visible]
        default tt_dict = create_tooltip_dictionary(locations)
        default tt = Tooltip(None)

        default x_size_percent = 0.07
        default y_size_percent = 0.145

        for place in locations: #Draw the text buttons over the background
            $ hex_x = x_size_percent * place.map_pos[0]
            $ hex_y = y_size_percent * place.map_pos[1]
            $ tile_info = get_location_tile_text(place, tt_dict)
            if place.map_pos[0] % 2 == 1:
                $ hex_y += y_size_percent/2
            frame:
                background None
                xysize [171,150]
                anchor [0.0,0.0]
                align (hex_x,hex_y)
                imagebutton:
                    anchor [0.5,0.5]
                    if not place == mc.location:
                        auto "gui/LR2_Hex_Button_%s.png"
                        focus_mask "gui/LR2_Hex_Button_idle.png"
                    else:
                        idle "gui/LR2_Hex_Button_Alt_idle.png"
                        focus_mask "gui/LR2_Hex_Button_Alt_idle.png"

                    action [Function(mc.change_location, place), Return(place)]
                    sensitive True #TODO: replace once we want limited travel again with: place in mc.location.connections
                    hovered tt.Action(tt_dict[place.name][0])
                text "[tile_info]" anchor [0.5,0.5] style "map_text_style"

            ##TODO: add a sub map to housing_map_manager() so we can go to people's homes

        $ xy_pos = [7,4]
        $ hex_x = x_size_percent * xy_pos[0]
        $ hex_y = y_size_percent * xy_pos[1]
        if xy_pos[0] % 2 == 1:
            $ hex_y += y_size_percent/2

        frame:
            background None
            xysize [171,150]
            anchor [0.0,0.0]
            align (hex_x,hex_y)
            imagebutton:
                anchor [0.5,0.5]
                if mc.location in mc.known_home_locations:
                    idle "gui/LR2_Hex_Button_Alt_idle.png"
                    focus_mask "gui/LR2_Hex_Button_Alt_idle.png"
                else:
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
            text "[tt.value]" style "textbutton_text_style" text_align 0.0 size 18 xalign 0.95 yalign 0.98
