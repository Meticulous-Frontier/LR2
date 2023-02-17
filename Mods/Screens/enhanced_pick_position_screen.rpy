screen pick_position_screen(the_person, allow_none = True, ignore_taboo = False):
    default non_sex_options = {} # Add options that are not of the Position class. Key is display, [0] is return value
    python:
        if allow_none:
            non_sex_options["Nothing"] = "None"
    zorder 49 # Tooltip screen is zorder 50
    vbox:
        spacing -12
        xalign 0.3
        yalign 0.7
        ysize 675
        frame:
            vbox:
                xsize 500
                viewport:
                    mousewheel True
                    draggable True
                    if __builtin__.len(list_of_positions) + 1 > 6:
                        scrollbars "vertical"
                    vbox:
                        for position in list_of_positions:
                            if isinstance(position, Position):
                                $ position_info_list = position.build_position_willingness_string(the_person, ignore_taboo)
                                $ taboo_break_string = position_info_list[0]
                                $ position_opinion = position_info_list[2]
                                $ willingness_string = position_info_list[3]
                                $ tooltip_string = position_info_list[4]

                                textbutton taboo_break_string + position.name + position_opinion + willingness_string:
                                    tooltip tooltip_string
                                    if tooltip_string == "Disabled": #Visual indication that it is disabled
                                        background "#222222"
                                        action NullAction()

                                    else:
                                        action Return(position)
                                    style "textbutton_no_padding_highlight"
                                    text_style "serum_text_style"
                                    xfill True
                                    ysize 125
        if __builtin__.len(non_sex_options) != 0: # Collect any non- position options in a frame below.
            frame:
                #yalign 0.7
                vbox:
                    xsize 500
                    ysize 125
                    viewport:
                        mousewheel True
                        draggable True
                        if __builtin__.len(non_sex_options) > 1:
                            scrollbars "vertical"
                        vbox:
                            for option in non_sex_options:
                                textbutton option:
                                    style "textbutton_no_padding_highlight"
                                    text_style "serum_text_style"
                                    xfill True
                                    ysize 125

                                    action Return(non_sex_options[option])

screen pick_round_choice_screen(the_person, option_list, position_choice, ignore_taboo = False):

    # This screen gets passed a list in a format like this: [["Transition to" + Position.name, Position], ["Strip her down", "Strip"]] #NOTE Position objects or strings.
    zorder 49
    frame:
        xalign 0.3
        yalign 0.7
        ysize 800
        vbox:
            xsize 500
            viewport:
                mousewheel True
                draggable True
                if __builtin__.len(option_list) + 1 > 6:
                    scrollbars "vertical"
                vbox:
                    for position in option_list:
                        if isinstance(position[1], Position):
                            $ position_info_list = position[1].build_position_willingness_string(the_person, ignore_taboo) # Instead of doing too much formating in the function or in the sexmechanics file we take care of it here. #NOTE: Should revisit this for a better solution.
                            $ taboo_break_string = position_info_list[0]
                            $ position_opinion = position_info_list[2]
                            $ willingness_string = position_info_list[3]
                            $ tooltip_string = position_info_list[4]

                            textbutton taboo_break_string + position[0] + position_opinion + willingness_string:
                                tooltip tooltip_string
                                style "textbutton_no_padding_highlight"
                                text_style "serum_text_style"
                                xfill True
                                ysize 125
                                action Return(position[1])
                        else:
                            textbutton position[0]:
                                style "textbutton_no_padding_highlight"
                                text_style "serum_text_style"
                                xfill True
                                ysize 125

                                action Return(position[1])
