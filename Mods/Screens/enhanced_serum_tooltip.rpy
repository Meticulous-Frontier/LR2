init -2 style serum_text_style_traits: # Cheat Text Style
    size 20
    color "#dddddd"
    outlines [(2,"#222222",0,0)]
    xalign 0.5


init -1:
    python:
        def serum_rename_func(new_name):
            the_serum.name = new_name

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

                    style "textbutton_style"
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
                    hbox:
                        vbox:
                            textbutton "Research Required: [the_serum.research_needed]":
                                style "textbutton_style"
                                text_style "serum_text_style"
                                xsize 225
                                action NullAction()

                            textbutton "Production Cost: [the_serum.production_cost]":
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
                                textbutton "Expected Profit:{color=#ff0000} -$[calculated_profit]{/color}":
                                    style "textbutton_style"
                                    text_style "serum_text_style"
                                    xsize 225
                                    action NullAction()

                            textbutton "Duration: [the_serum.duration] Turns":
                                style "textbutton_style"
                                text_style "serum_text_style"
                                xsize 225
                                action NullAction()
                frame:
                    background "#777777"
                    xalign 0.5
                    xsize 450
                    ysize 600
                    viewport:
                        scrollbars "vertical"
                        xsize 450
                        ysize 650
                        mousewheel True
                        vbox:
                            for trait in the_serum.traits:
                                textbutton trait.name:
                                    style "textbutton_style"
                                    text_style "serum_text_style_traits"
                                    xsize 450

                                    action NullAction()

                                    alternate [
                                    SensitiveIf(trait in the_serum.traits),
                                    Function(the_serum.remove_trait, trait)
                                    ]

                                hbox:
                                    xsize 225

                                    vbox:
                                        textbutton "{color=#98fb98}[trait.positive_slug]{/color}":
                                             style "textbutton_style"
                                             text_style "serum_text_style_traits"
                                             xalign 0.5
                                             xsize 225

                                             action NullAction()


                                    vbox:
                                        textbutton "{color=#cd5c5c}[trait.negative_slug]{/color}":
                                            style "textbutton_style"
                                            text_style "serum_text_style_traits"
                                            xalign 0.5
                                            xsize 225

                                            action NullAction()

                            if the_serum.side_effects:
                                for side_effect in the_serum.side_effects:
                                    textbutton side_effect.name:
                                        style "textbutton_style"
                                        text_style "serum_text_style_traits"
                                        xsize 450

                                        action NullAction()

                                    hbox:
                                        xsize 225
                                        vbox:
                                            textbutton "{color=#cd5c5c}[side_effect.negative_slug]{/color}":
                                                style "textbutton_style"
                                                text_style "serum_text_style_traits"
                                                xalign 0.5
                                                xsize 225

                                                action NullAction()
                                        vbox:
                                            pass
