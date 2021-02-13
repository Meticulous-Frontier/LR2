init -1:
    $ production_max = 100
    $ array_to_change = None # Used to determine which line is passed to the serum_production_autosell function
    python:
        def serum_production_autosell(new_amount):
            if new_amount is "":
                new_amount = 0
            if new_amount == "-":
                new_amount = -1
            store.mc.business.serum_production_array[array_to_change][3] = __builtin__.int(new_amount)
            renpy.restart_interaction()

        def color_indicator(variable, max_value = 100): # Gives color indication to a value range split into 5.
            if variable >= max_value / 1.25: # 80%
                return "{color=#24ed27}" + str(variable) +"{/color}"
            if variable >= max_value / 1.67: # 60%
                return "{color=#8edb21}" + str(variable) +"{/color}"
            if variable >= max_value / 2.5: # 40%
                return "{color=#ffec6e}" + str(variable) +"{/color}"
            if variable >= max_value / 5: # 20%
                return "{color=#ed9d4c}" + str(variable) +"{/color}"
            else: # less than 20%
                return "{color=#ff6347}" + str(variable) +"{/color}"

init 2:
    screen serum_production_select_ui:
        add "Science_Menu_Background.png"
        default line_selected = None

        default production_line_weight_tooltip = "Work done by production employees will be split between active lines based on production weight."
        default production_line_autosell_tooltip = "Doses of serum above the auto-sell threshold will automatically be flagged for sale and moved to the marketing department."

        $ renpy.block_rollback()

        python:
            production_max_use = production_max
            production_remaining = production_max_use
            for key in mc.business.serum_production_array:
                production_remaining -= mc.business.serum_production_array[key][1] # How much of the 100% capability are we using?
        hbox:
            xalign 0.04
            yalign 0.4
            ysize 900
            spacing 20
            frame:
                background "#888888"
                xsize 600
                ysize 900
                vbox:
                    spacing 5
                    xalign 0.5
                    frame:
                        background "#000080"
                        xfill True

                        text "Production Lines" style "serum_text_style_header"

                    frame:
                        background "#000080"
                        xfill True

                        text "Capacity Remaining: " + str(color_indicator(production_remaining)) + "%" style "serum_text_style"

                    viewport:
                        draggable True
                        if mc.business.production_lines > 3: # Have the scrollbar only exist if it is nescessary
                            scrollbars "vertical"
                        mousewheel True
                        xfill True

                        vbox:
                            spacing 20
                            xfill True

                            for count in __builtin__.range(1,mc.business.production_lines+1): #For the non-programmers we index our lines to 1 through production_lines.
                                vbox:
                                    xfill True
                                    frame:
                                        background "#999999"


                                        vbox:
                                            xfill True

                                            $ name_string = ""
                                            if count in mc.business.serum_production_array:
                                                $ name_string = "Production Line " + str(count) + "\nCurrently Producing: " + mc.business.serum_production_array[count][0].name
                                            else:
                                                $ name_string = "Production Line " + str(count) + "\nCurrently Producing: {color=#ff6347}Nothing{/color}"

                                            # $ button_background = "#000080"
                                            # if line_selected == count:
                                            #     $ button_background = "#666666"

                                            if count in mc.business.serum_production_array:
                                                $ the_serum = mc.business.serum_production_array[count][0]
                                                textbutton "[name_string]":
                                                    xfill True
                                                    style "textbutton_style"
                                                    text_style "serum_text_style"

                                                    action [
                                                    ToggleScreenVariable("line_selected", count, None),
                                                    ToggleScreen("serum_tooltip", None, the_serum, 0.94, 0.072)
                                                    ]

                                                    # hovered [
                                                    # Show("serum_tooltip", None, the_serum, 0.94, 0.072)
                                                    # ]

                                            else:
                                                textbutton "[name_string]":
                                                    xfill True
                                                    style "textbutton_style"
                                                    text_style "serum_text_style"

                                                    action [
                                                    ToggleScreenVariable("line_selected", count, None)
                                                    ]




                                        #null height 20
                                            frame:
                                                background "#000080"
                                                grid 1 2:
                                                    xfill True
                                                    hbox:

                                                        xfill True

                                                        frame:
                                                            background None

                                                            text "Production Weight:   " style "serum_text_style"

                                                        if count in mc.business.serum_production_array:
                                                            textbutton "-10%":
                                                                xsize 40
                                                                style "textbutton_style"
                                                                text_style "serum_text_style"


                                                                action [
                                                                Function(mc.business.change_line_weight,count,-10)
                                                                ]

                                                                tooltip production_line_weight_tooltip

                                                            frame:
                                                                xsize 140
                                                                background None

                                                                text str(color_indicator(mc.business.serum_production_array[count][1])) + "%" style "serum_text_style"

                                                            textbutton "+10%":
                                                                xsize 40
                                                                style "textbutton_style"
                                                                text_style "serum_text_style"

                                                                action [
                                                                Function(mc.business.change_line_weight,count,10)
                                                                ]

                                                                tooltip production_line_weight_tooltip

                                                        else:
                                                            frame:
                                                                background None
                                                                xsize 40
                                                                text "-10%" style "serum_text_style"
                                                                tooltip production_line_weight_tooltip

                                                            frame:
                                                                background None
                                                                xsize 140
                                                                text "0%" style "serum_text_style"

                                                            frame:
                                                                background None
                                                                xsize 40
                                                                text "+10%" style "serum_text_style"
                                                                tooltip production_line_weight_tooltip

                                                    hbox:

                                                        xfill True
                                                        frame:
                                                            background None
                                                            text "Auto-sell Threshold: " style "serum_text_style"

                                                        if count in mc.business.serum_production_array:
                                                            hbox:
                                                                xsize 40
                                                                yoffset 8
                                                                textbutton "<<":
                                                                    action [Function(mc.business.change_line_autosell,count, (-10 if mc.business.serum_production_array[count][3] != 10 else -11))]
                                                                    style "textbutton_no_padding_highlight"
                                                                    text_style "serum_text_style"
                                                                    tooltip production_line_autosell_tooltip
                                                                textbutton "<":
                                                                    action [Function(mc.business.change_line_autosell,count, -1)]
                                                                    style "textbutton_no_padding_highlight"
                                                                    text_style "serum_text_style"
                                                                    tooltip production_line_autosell_tooltip

                                                            # frame:
                                                            #     background None
                                                            #     xfill True
                                                            button:
                                                                xsize 140
                                                                action ToggleVariable("array_to_change", count, None)

                                                                if array_to_change == count:
                                                                    input default str(mc.business.serum_production_array[count][3]) length 7 allow "0123456789" changed serum_production_autosell style "serum_text_style"
                                                                else:
                                                                    if mc.business.serum_production_array[count][3] > 0:
                                                                        text str(mc.business.serum_production_array[count][3]) style "serum_text_style" yalign 0.5

                                                                    if mc.business.serum_production_array[count][3] < 0:
                                                                        text "None" style "serum_text_style" yalign 0.5

                                                                    if mc.business.serum_production_array[count][3] == 0:
                                                                        text "All" style "serum_text_style" yalign 0.5

                                                            hbox:
                                                                xalign 1
                                                                xsize 40
                                                                yoffset 8
                                                                textbutton ">":
                                                                    action [Function(mc.business.change_line_autosell, count, 1)]
                                                                    style "textbutton_no_padding_highlight"
                                                                    text_style "serum_text_style"
                                                                    tooltip production_line_autosell_tooltip
                                                                textbutton ">>":
                                                                    action [Function(mc.business.change_line_autosell,count, (11 if mc.business.serum_production_array[count][3] <= 0 else 10))]
                                                                    style "textbutton_no_padding_highlight"
                                                                    text_style "serum_text_style"
                                                                    tooltip production_line_autosell_tooltip


                                                        else:
                                                            frame:
                                                                background None
                                                                xsize 60
                                                                text "<< <" style "serum_text_style"

                                                                tooltip production_line_autosell_tooltip

                                                            frame:
                                                                background None
                                                                xsize 100
                                                                text "None" style "serum_text_style"

                                                            frame:
                                                                background None
                                                                xsize 60
                                                                text "> >>" style "serum_text_style"
                                                                tooltip production_line_autosell_tooltip
            if line_selected:
                frame:
                    background "#888888"
                    xsize 400
                    ysize 650
                    xalign 0.5
                    vbox:
                        textbutton "Choose Production for Line [line_selected]":
                            style "serum_textbutton_style_header"
                            text_style "serum_text_style_header"
                            xsize 375
                            action SetScreenVariable("line_selected",None)

                        if __builtin__.len(mc.business.serum_designs) == 0:
                            textbutton "No designs researched! Create and research a design in the R&D department first!":
                                style "textbutton_style"
                                text_style "serum_text_style"
                                action NullAction()
                        else:
                            viewport:
                                draggable True
                                scrollbars "vertical"
                                mousewheel True
                                xsize 400
                                vbox:
                                    for a_serum in mc.business.serum_designs:
                                        if a_serum.researched:
                                            textbutton "[a_serum.name]":
                                                action [
                                                Hide("serum_tooltip"),
                                                Function(mc.business.change_production,a_serum,line_selected),
                                                SetScreenVariable("line_selected",None)
                                                ]
                                                hovered [
                                                Show("serum_tooltip",None,a_serum,0.94,0.072)
                                                ]
                                                style "textbutton_style"
                                                text_style "serum_text_style"
                                                xsize 400
                                                xalign 0.5

        frame:
            background None
            anchor [0.5,0.5]
            align [0.5,0.88]
            xysize [500,125]
            imagebutton:
                align [0.5,0.5]
                auto "gui/button/choice_%s_background.png"
                focus_mask "gui/button/choice_idle_background.png"
                action [Return(), Hide("serum_tooltip")]
            textbutton "Return" align [0.5,0.5] text_style "return_button_style"

        imagebutton:
            auto "/tutorial_images/restart_tutorial_%s.png"
            xsize 54
            ysize 54
            yanchor 1.0
            xalign 0.0
            yalign 1.0
            action Function(mc.business.reset_tutorial,"production_tutorial")


        $ production_tutorial_length = 5 #The number of  tutorial screens we have.
        if mc.business.event_triggers_dict["production_tutorial"] > 0 and mc.business.event_triggers_dict["production_tutorial"] <= production_tutorial_length: #We use negative numbers to symbolize the tutorial not being enabled
            imagebutton:
                auto
                sensitive True
                xsize 1920
                ysize 1080
                idle "/tutorial_images/production_tutorial_"+__builtin__.str(mc.business.event_triggers_dict["production_tutorial"])+".png"
                hover "/tutorial_images/production_tutorial_"+__builtin__.str(mc.business.event_triggers_dict["production_tutorial"])+".png"
                action Function(mc.business.advance_tutorial,"production_tutorial")
