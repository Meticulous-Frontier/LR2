init -1:
    python:
        def serum_rename_func(new_name):
            store.the_serum.name = new_name


init 2:
    screen serum_tooltip(the_serum, set_x_align = 0.9, set_y_align = 0.1):
        frame:
            background "#888888"
            xalign set_x_align
            yalign set_y_align
            yanchor 0.0
            xsize 500
            ysize 900
            vbox:
                xalign 0.5
                spacing 10
                button:
                    id "serum_rename_id"
                    selected

                    style "serum_textbutton_style_header"
                    xalign 0.5
                    xsize 450

                    action NullAction()

                    add Input(
                    size =  24,
                    color = "#dddddd",
                    default = the_serum.name,
                    changed = serum_rename_func,
                    length = 25,
                    button = renpy.get_widget("serum_tooltip", "serum_rename_id")
                    ) xalign 0.5

                    unhovered Function(renpy.restart_interaction) #TODO: Tweak this so it is less annoying  and fix any associated errors

                frame:
                    background "#777777"
                    xalign 0.5
                    xsize 450
                    ysize 200
                    vbox:
                        hbox:
                            vbox:
                                textbutton "Research Required: {color=98fb98}[the_serum.research_needed]{/color}":
                                    style "textbutton_style"
                                    text_style "serum_text_style"
                                    xsize 225
                                    action NullAction()

                                textbutton "Production Cost: {color=#cd5c5c}[the_serum.production_cost]{/color}":
                                    style "textbutton_style"
                                    text_style "serum_text_style"
                                    xsize 225
                                    action NullAction()

                                textbutton "Value: $[the_serum.value]":
                                    style "textbutton_style"
                                    text_style "serum_text_style"
                                    xsize 225
                                    action NullAction()


                            vbox:
                                $ calculated_profit = (the_serum.value*mc.business.batch_size)-the_serum.production_cost
                                if calculated_profit > 0:
                                    textbutton "Expected Profit:{color=#98fb98} $[calculated_profit]{/color}":
                                        style "textbutton_style"
                                        text_style "serum_text_style"
                                        xsize 225
                                        action NullAction()
                                else:
                                    $ calculated_profit = 0 - calculated_profit
                                    textbutton "Expected Profit:{color=#cd5c5c} -$[calculated_profit]{/color}":
                                        style "textbutton_style"
                                        text_style "serum_text_style"
                                        xsize 225
                                        action NullAction()

                                textbutton "Duration: [the_serum.duration] Turns":
                                    style "textbutton_style"
                                    text_style "serum_text_style"
                                    xsize 225
                                    action NullAction()
                                if renpy.get_screen("review_designs_screen"): #Make it so you have to be in the review screen to edit things (still need to protect already created serum somehow)
                                    textbutton "Edit Serum":
                                        style "textbutton_style"
                                        text_style "serum_text_style"
                                        xsize 225
                                        action Show("serum_design_ui", None, the_serum, the_serum.traits)

                frame:
                    background "#777777"
                    xalign 0.5
                    xsize 450
                    if the_serum.side_effects:
                        ysize 400
                    viewport:
                        scrollbars "vertical"
                        xsize 450
                        mousewheel True
                        vbox:
                            for trait in the_serum.traits:
                                textbutton trait.name:
                                    style "textbutton_style"
                                    text_style "serum_text_style"
                                    xsize 450

                                    action NullAction()

                                    alternate [
                                    SensitiveIf(trait in the_serum.traits),
                                    ]

                                hbox:
                                    xsize 225

                                    vbox:
                                        textbutton "[trait.positive_slug]":
                                             style "serum_textbutton_style_positive"
                                             text_style "serum_text_style_traits"
                                             xalign 0.5
                                             xsize 225

                                             action NullAction()


                                    vbox:
                                        textbutton "[trait.negative_slug]":
                                            style "serum_textbutton_style_negative"
                                            text_style "serum_text_style_traits"
                                            xalign 0.5
                                            xsize 225

                                            action NullAction()
                if the_serum.side_effects:
                    textbutton "Side Effects:":
                        style "serum_textbutton_style_header"
                        text_style "serum_text_style_header"
                        xsize 450

                        action NullAction()
                    frame:
                        background "#777777"
                        xalign 0.5
                        xsize 450
                        viewport:
                            scrollbars "vertical"
                            xsize 450
                            mousewheel True
                            vbox:

                                for side_effect in the_serum.side_effects:
                                    textbutton side_effect.name:
                                        style "textbutton_style"
                                        text_style "serum_text_style"
                                        xsize 450

                                        action NullAction()

                                    hbox:
                                        xsize 225
                                        vbox:
                                            pass
                                        vbox:
                                            textbutton "[side_effect.negative_slug]":
                                                style "serum_textbutton_style_negative"
                                                text_style "serum_text_style_traits"
                                                xalign 0.5
                                                xsize 225

                                                action NullAction()
