init -1:
    $ array_to_change = None # Used to determine which line is passed to the serum_production_autosell function
    python:
        def serum_production_autosell(new_amount):
            if new_amount is "":
                new_amount = -1
            store.mc.business.serum_production_array[array_to_change][3] = new_amount


init 2:
    screen serum_production_select_ui:
        add "Science_Menu_Background.png"
        default line_selected = None
        default production_remaining = 100

        python:
            production_remaining = 100
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

                    xalign 0.5

                    textbutton "Production Lines":
                        xsize 550
                        xalign 0.5

                        style "serum_textbutton_style_header"
                        text_style "serum_text_style_header"

                        action NullAction()

                    textbutton "Capacity Remaining: [production_remaining]%":
                        xsize 550
                        xalign 0.5

                        style "textbutton_style"
                        text_style "serum_text_style"

                        action NullAction()

                    viewport:
                        draggable True
                        scrollbars "vertical"
                        mousewheel True
                        xsize 550
                        vbox:
                            spacing 20
                            for count in range(1,mc.business.production_lines+1): #For the non-programmers we index our lines to 1 through production_lines.
                                frame:
                                    background "#999999"
                                    vbox:
                                        $ name_string = ""
                                        if count in mc.business.serum_production_array:
                                            $ name_string = "Production Line " + str(count) + "\nCurrently Producing: " + mc.business.serum_production_array[count][0].name
                                        else:
                                            $ name_string = "Production Line " + str(count) + "\nCurrently Producing: Nothing"

                                        $ button_background = "#000080"
                                        if line_selected == count:
                                            $ button_background = "#666666"

                                        if count in mc.business.serum_production_array:
                                            $ the_serum = mc.business.serum_production_array[count][0]
                                            textbutton "[name_string]":

                                                action [
                                                ToggleScreenVariable("line_selected", count, None),
                                                Hide("serum_tooltip")
                                                ]

                                                style "textbutton_style"
                                                text_style "serum_text_style"

                                                hovered [
                                                Show("serum_tooltip",None,the_serum,0.94,0.072)
                                                ]


                                                xsize 500
                                        else:
                                            textbutton "[name_string]":

                                                action [
                                                ToggleScreenVariable("line_selected", count, None)
                                                ]

                                                style "textbutton_style"
                                                text_style "serum_text_style"

                                                xsize 500

                                        null height 20

                                        hbox:
                                            ysize 40
                                            xsize 500

                                            textbutton "Production Weight: ":
                                                style "textbutton_style"
                                                text_style "serum_text_style"

                                                action NullAction()

                                            if count in mc.business.serum_production_array:

                                                textbutton "-10%":

                                                    action [
                                                    Function(mc.business.change_line_weight,count,-10)
                                                    ]

                                                    style "textbutton_style"
                                                    text_style "serum_text_style"

                                                    tooltip "Work done by production employees will be split between active lines based on production weight."

                                                textbutton str(mc.business.serum_production_array[count][1]) + "%":

                                                    style "textbutton_style"
                                                    text_style "serum_text_style"

                                                    action NullAction()

                                                textbutton "+10%":

                                                    action [
                                                    Function(mc.business.change_line_weight,count,10)
                                                    ]

                                                    style "textbutton_style"
                                                    text_style "serum_text_style"

                                                    tooltip "Work done by production employees will be split between active lines based on production weight."

                                            else:
                                                textbutton "-10%":
                                                    action NullAction()
                                                    style "textbutton_style"
                                                    text_style "serum_text_style"
                                                    sensitive False

                                                    tooltip "Work done by production employees will be split between active lines based on production weight."

                                                textbutton "0%":
                                                    style "textbutton_style"
                                                    text_style "serum_text_style"
                                                    action NullAction()

                                                textbutton "+10%":
                                                    action NullAction()
                                                    style "textbutton_style"
                                                    text_style "serum_text_style"
                                                    sensitive False

                                                    tooltip "Work done by production employees will be split between active lines based on production weight."

                                        hbox:
                                            ysize 40
                                            xsize 500
                                            textbutton "Auto-sell Threshold: ":
                                                style "textbutton_style"
                                                text_style "serum_text_style"

                                                action NullAction()

                                            if count in mc.business.serum_production_array:
                                                textbutton "-1":
                                                    action [
                                                    Function(mc.business.change_line_autosell,count,-1)
                                                    ]
                                                    alternate [
                                                    Function(mc.business.change_line_autosell,count,-10)
                                                    ]
                                                    style "textbutton_style"
                                                    text_style "serum_text_style"
                                                    tooltip "Doses of serum above the auto-sell threshold will automatically be flagged for sale and moved to the marketing department."

                                                if mc.business.serum_production_array[count][3] < 0:
                                                    textbutton "None":
                                                        style "textbutton_style"
                                                        text_style "serum_text_style"
                                                        action NullAction()
                                                else:
                                                    button:
                                                        id "serum_production_autosell"
                                                        style "textbutton_style"
                                                        action NullAction()
                                                        hovered If(array_to_change is not count, SetVariable("array_to_change", count))
                                                        unhovered Function(renpy.restart_interaction) #TODO: Tweak this so it is less annoying  and fix any associated errors

                                                        add Input(
                                                        size =  20,
                                                        color = "#dddddd",
                                                        default = str(mc.business.serum_production_array[count][3]),
                                                        changed = serum_production_autosell, # TODO: This passes only the inputed text to the function, need the production line we have selected to also carry over
                                                        length = 7,
                                                        button = renpy.get_widget("serum_production_select_ui", "serum_production_autosell"),
                                                        allow = "0123456789"
                                                        )

                                                textbutton "+1":
                                                    action [
                                                    Function(mc.business.change_line_autosell,count,1)
                                                    ]
                                                    alternate [
                                                    Function(mc.business.change_line_autosell,count,+10)
                                                    ]
                                                    style "textbutton_style"
                                                    text_style "serum_text_style"

                                                    tooltip "Doses of serum above the auto-sell threshold will automatically be flagged for sale and moved to the marketing department."
                                            else:
                                                textbutton "-1":
                                                    action NullAction()
                                                    style "textbutton_style"
                                                    text_style "serum_text_style"
                                                    sensitive False

                                                    tooltip "Doses of serum above the auto-sell threshold will automatically be flagged for sale and moved to the marketing department."

                                                textbutton "None":

                                                    style "textbutton_style"
                                                    text_style "serum_text_style"

                                                    action NullAction()

                                                textbutton "+1":

                                                    style "textbutton_style"
                                                    text_style "serum_text_style"

                                                    sensitive False

                                                    action NullAction()
                                                    tooltip "Doses of serum above the auto-sell threshold will automatically be flagged for sale and moved to the marketing department."

            if line_selected:
                frame:
                    background "#888888"
                    xsize 300
                    ysize 450
                    vbox:
                        xalign 0.5
                        textbutton "Choose Production for Line [line_selected]":
                            style "serum_textbutton_style_header"
                            text_style "serum_text_style_header"
                            xalign 0.5
                            xsize 300
                            action SetScreenVariable("line_selected",None)

                        if len(mc.business.serum_designs) == 0:
                            textbutton "No designs researched! Create and research a design in the R&D department first!":
                                style "textbutton_style"
                                text_style "serum_text_style"
                                action NullAction()
                                xalign 0.5
                        else:
                            viewport:
                                draggable True
                                scrollbars "vertical"
                                mousewheel True

                                xsize 300
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
                                                xsize 300
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
