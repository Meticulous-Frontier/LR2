screen pick_position_screen(the_person, allow_none = True, ignore_taboo = False):

    zorder 49

    # default positon_option_list = []
    # python:
    #     for position in list_of_positions:
    #         if mc.location.has_object_with_trait(position.requires_location) and (the_person.has_large_tits() or not position.requires_large_tits):
    #             position_option_list.append([position.build_position_willingness_string(the_person, ignore_taboo = ignore_taboo), position])
    #     if allow_none:
    #         position_option_list.append([["Nothing"], "Nothing"])

    #test = [[["Nothing", "exciting"], "Nothing"]]
    $ tooltip = GetTooltip(renpy.current_screen().screen_name)
    frame:
        vbox:
            xalign 0.5
            yalign 0.5
            xsize 500
            ysize 900
            viewport:
                mousewheel True
                draggable True
                scrollbars "vertical"
                vbox:
                    for position in list_of_positions:
                        vbox:
                            textbutton position.build_position_willingness_string(the_person, ignore_taboo = ignore_taboo)[0] + position.build_position_willingness_string(the_person, ignore_taboo = ignore_taboo)[1] + "\n" + position.build_position_willingness_string(the_person, ignore_taboo = ignore_taboo)[2] + position.build_position_willingness_string(the_person, ignore_taboo = ignore_taboo)[3]:

                                tooltip position.build_position_willingness_string(the_person, ignore_taboo = ignore_taboo)[4]
                                if position.build_position_willingness_string(the_person, ignore_taboo = ignore_taboo)[4] == "Disabled": #Visual indication that it is disabled
                                    background "#222222"
                                    action NullAction()
                                else:
                                    action Return(position)

                                style "textbutton_no_padding_highlight"
                                text_style "serum_text_style"
                                xfill True

                    if allow_none:
                        textbutton "Nothing":
                            style "textbutton_no_padding_highlight"
                            text_style "serum_text_style"
                            xfill True

                            action Return("None")

screen pick_round_choice_screen(the_person, option_list, position_choice, ignore_taboo = False):

    $ tooltip = GetTooltip(renpy.current_screen().screen_name)
    zorder 49
    frame:
        vbox:
            xalign 0.5
            yalign 0.5
            xsize 500
            ysize 900
            viewport:
                mousewheel True
                draggable True
                scrollbars "vertical"
                vbox:
                    for option in option_list:
                        vbox:

                            if hasattr(option[1], "connections"): # Prevent errors when "None" is passed
                                textbutton option[1].build_position_willingness_string(the_person, ignore_taboo = ignore_taboo)[0] + option[0] + "\n" + option[1].build_position_willingness_string(the_person, ignore_taboo = ignore_taboo)[2] + option[1].build_position_willingness_string(the_person, ignore_taboo = ignore_taboo)[3]:
                                    tooltip option[1].build_position_willingness_string(the_person, ignore_taboo = ignore_taboo)[4]
                                    style "textbutton_no_padding_highlight"
                                    text_style "serum_text_style"
                                    xfill True

                                    action Return(option[1])
                            else:
                                textbutton option[0]:
                                    style "textbutton_no_padding_highlight"
                                    text_style "serum_text_style"
                                    xfill True

                                    action Return(option[1])
