init 2:
    screen trait_tooltip(the_trait,given_xalign=0.9,given_yalign=0.1):

        frame:
            background "#666666"

            xalign given_xalign
            yalign given_yalign

            vbox:
                xalign 0.5
                textbutton "[the_trait.name]":
                    style "textbutton_style"
                    text_style "serum_text_style"
                    xalign 0.5
                    xsize 500
                    action NullAction()

                hbox:

                    vbox:

                        textbutton "[the_trait.positive_slug]":
                            style "serum_textbutton_style_positive"
                            text_style "serum_text_style_traits"
                            xalign 0.5

                            xsize 225

                            action NullAction()

                    vbox:
                        $ negative_slug_text = the_trait.build_negative_slug()
                        textbutton "[negative_slug_text]":
                            style "serum_textbutton_style_negative"
                            text_style "serum_text_style_traits"
                            xalign 0.5

                            xsize 225

                            action NullAction()

                textbutton "[the_trait.desc]":
                    style "textbutton_style"
                    text_style "serum_text_style"
                    xalign 0.5

                    xsize 500

                    action NullAction()


    screen trait_list_tooltip(the_traits):
        vbox:
            xalign 0.9
            yalign 0.1
            for trait in the_traits:
                frame:
                    background "#888888"

                    xalign 0
                    yalign 0
                    xanchor 1.0
                    yanchor 0.0
                    vbox:
                        xsize 500
                        text trait.name style "menu_text_style" xalign 0.5 xanchor 0.5
                        text trait.positive_slug style "menu_text_style" size 14 color "#98fb98" xalign 0.5 xanchor 0.5
                        text trait.build_negative_slug() style "menu_text_style" size 14 color "#ff0000" xalign 0.5 xanchor 0.5
                        if trait.is_side_effect:
                            text trait.desc style "menu_text_style" xalign 0.5 xanchor 0.5
