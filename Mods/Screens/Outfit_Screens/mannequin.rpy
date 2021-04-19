# Use display functions to draw the mannequin on layer '8' since it is above the screen layer (solo is below screen layer)
init 2 python:
    global mannequin_prediction
    mannequin_prediction = None

    def clear_prediction():
        global mannequin_prediction
        if mannequin_prediction:
            renpy.stop_predict(mannequin_prediction)
        mannequin_prediction = None
        return

    def draw_mannequin(mannequin, outfit, position = None, emotion = None, special_modifier = None, background_fill = "#0026a5", hide_list = []): # Small tweak of draw_person to allow for an outfit that is not theirs to be shown (NOTE: outfit.generate_draw_list)
        renpy.scene("8")
        clear_prediction()
        if position is None:
            position = mannequin.idle_pose

        if emotion is None:
            emotion = mannequin.get_emotion()

        mannequin.apply_outfit(outfit)

        mannequin_prediction = mannequin.build_person_displayable(position, emotion,special_modifier, [0.98,0.98,0.98], None, no_frame = True, hide_list = hide_list)

        renpy.show(mannequin.identifier, at_list=[character_right, scale_person(mannequin.height)],layer="8",what=mannequin_prediction,tag=mannequin.identifier)
        return

    def draw_average_mannequin(outfit, hide_list = []):
        renpy.scene("8")
        clear_prediction()
        displayable_list = []
        displayable_list.append(mannequin_average)
        displayable_list.extend(outfit.generate_draw_list(None, "stand3", hide_layers = hide_list))

        x_size, y_size = position_size_dict.get("stand3")

        composite_list = [(x_size,y_size)]
        for display in displayable_list:
            if isinstance(display, __builtin__.tuple):
                composite_list.extend(display)
            else:
                composite_list.append((0,0))
                composite_list.append(display)

        mannequin_prediction = Composite(*composite_list)

        renpy.show("mannequin_dummy", at_list=[character_right, scale_person(.9)],layer="8",what=mannequin_prediction,tag="mannequin_dummy")
        return
