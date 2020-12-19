init 2 python:
    def draw_mannequin(mannequin, outfit, position = None, emotion = None, special_modifier = None, background_fill = "#0026a5", hide_list = []): # Small tweak of draw_person to allow for an outfit that is not theirs to be shown (NOTE: outfit.generate_draw_list)
        clear_scene()

        if position is None:
            position = mannequin.idle_pose

        if emotion is None:
            emotion = mannequin.get_emotion()

        mannequin.apply_outfit(outfit)

        final_image = Flatten(mannequin.build_person_displayable(position, emotion,special_modifier, [0.98,0.98,0.98], None, no_frame = True, hide_list = hide_list))

        renpy.show(mannequin.name + mannequin.last_name,at_list=[character_right, scale_person(mannequin.height)],layer="solo",what=final_image,tag=mannequin.name + mannequin.last_name)
        renpy.restart_interaction()

init 2: # Moved to screen so that it can be refreshed upon changes made in outfit_creator
    screen mannequin(outfit, model = "mannequin", hide_list = []):
        $ clear_scene()
        zorder 102
        fixed: #TODO: Move this to it's own screen so it can be shown anywhere
            pos (1600,200)
            add mannequin_average zoom .6
            if outfit is not None:
                for cloth in outfit.generate_draw_list(None,"stand3", hide_layers = hide_list):
                    add cloth zoom .6
