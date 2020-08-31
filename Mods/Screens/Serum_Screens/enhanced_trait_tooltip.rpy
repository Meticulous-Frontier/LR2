init 2:
    screen trait_tooltip(the_trait,given_xalign=0.9,given_yalign=0.1):
        frame:
            background "#666666"

            xalign given_xalign
            yalign given_yalign

            vbox:
                spacing 5
                xalign 0.5
                frame:
                    background "#000080"
                    xsize 505
                    text "[the_trait.name]" style "serum_text_style"

                hbox:
                    spacing 5
                    frame:
                        background "#007000"
                        xsize 250
                        xfill True
                        text "[the_trait.positive_slug]" style "serum_text_style_traits"

                    frame:
                        background "#930000"
                        xsize 250
                        xfill True
                        $ negative_slug_text = the_trait.build_negative_slug()
                        text "[negative_slug_text]" style "serum_text_style_traits"
                frame:
                    background "#000080"
                    xsize 505
                    text "[the_trait.desc]" style "serum_text_style"

    screen trait_list_tooltip(the_traits, y_height = 0):
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
                        xsize 505
                        text trait.name style "menu_text_style" xalign 0.5 xanchor 0.5
                        text trait.positive_slug style "menu_text_style" size 14 color "#98fb98" xalign 0.5 xanchor 0.5
                        text trait.build_negative_slug() style "menu_text_style" size 14 color "#ff0000" xalign 0.5 xanchor 0.5
                        if trait.is_side_effect:
                            text trait.desc style "menu_text_style" xalign 0.5 xanchor 0.5
