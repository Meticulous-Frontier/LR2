# override the default map_manager, to allow for one click location changes
# instead of clicking return after each choice
init 2:
    screen map_manager():
        add "Paper_Background.png"
        zorder 100
        #TODO: figure out why the line drawing is SO SLOW!
        #UPDATE: Directly drawing to canvases requires software rendering instead of hardware, which makes it much slower. Possible solutions include:
        # A) Just creating a static map. Boring.
        # B) Passing the list of places and having Vren_Line do all of the lines at the same time. Batch processing them may be significantly faster.
        # C) Processing the map image one on initialization and saving it, then just calling it as an image when the map is shown. This doesn't play well with live updating the map.
        # D) Create a "line" graphic and simply place and stretch it to go between location A and B on the map. Alternatively, take a short line segment and tile it as needed.
        # D seems to be the option suggested by PyTom, so that's likely what I'll do. (Hello intrepid code reader who has discovered these notes!)
        # for place in list_of_places: #Draw the background
        #     for connected in place.connections:
        #         if mc.location == place and place.visible and connected.visible: #This is an acceptable hack to get reasonable performance.
        #             add Vren_Line([int(place.map_pos[0]*1920),int(place.map_pos[1]*1080)],[int(connected.map_pos[0]*1920),int(connected.map_pos[1]*1080)],4,"#117bff") #Draw a white line between each location

        for place in list_of_places: #Draw the text buttons over the background
            if place.visible:
                if not place == mc.location:
                    frame:
                        background None
                        xysize [171,150]
                        anchor [0.0,0.0]
                        align place.map_pos
                        imagebutton:
                            anchor [0.5,0.5]
                            auto "gui/LR2_Hex_Button_%s.png"
                            focus_mask "gui/LR2_Hex_Button_idle.png"
                            action [Function(mc.change_location, place), Return(place)]
                            sensitive place.accessable #TODO: replace once we want limited travel again with: place in mc.location.connections
                        text place.formalName + "\n(" + str(len(place.people)) + ")" anchor [0.5,0.5] style "map_text_style"

                else:
                    frame:
                        background None
                        xysize [171,150]
                        anchor [0.0,0.0]
                        align place.map_pos
                        imagebutton:
                            anchor [0.5,0.5]
                            idle "gui/LR2_Hex_Button_Alt_idle.png"
                            focus_mask "gui/LR2_Hex_Button_Alt_idle.png"
                            action Function(mc.change_location,place)
                            sensitive False
                        text place.formalName + "\n(" + str(len(place.people)) + ")" anchor [0.5,0.5] style "map_text_style"

            ##TODO: add a sub map to housing_map_manager() so we can go to people's homes

        if mc.location in mc.known_home_locations:
            frame:
                background None
                xysize [171,150]
                anchor [0.0,0.0]
                align [0.6,0.45]
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
                align [0.6,0.45]
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