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

                        textbutton "[the_trait.negative_slug]":
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
