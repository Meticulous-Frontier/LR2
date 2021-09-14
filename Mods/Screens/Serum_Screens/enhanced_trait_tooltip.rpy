init 2:
    screen trait_tooltip(the_trait, given_align = (0.0,0.0), given_anchor = (0.0,0.0)):
        frame:
            background "#0a142688"

            align given_align
            anchor given_anchor

            vbox:
                spacing 5
                xalign 0.5
                frame:
                    background "#000080"
                    xsize 505
                    text the_trait.name + (" (C)" if isinstance(the_trait, SerumTraitBlueprint) else ""):
                        style "menu_text_title_style"
                        xalign 0.5

                hbox:
                    spacing 5
                    frame:
                        background "#43B197"
                        xsize 250
                        xfill True
                        text the_trait.positive_slug style "serum_text_style_traits"

                    frame:
                        background "#B14365"
                        xsize 250
                        xfill True
                        text the_trait.build_negative_slug() style "serum_text_style_traits"
                frame:
                    background "#000080"
                    xsize 505
                    text the_trait.desc style "serum_text_style"

                transclude

    screen trait_list_tooltip(the_traits, given_align = (0.0,0.0), given_anchor = (0.0,0.0)):
        vbox:
            align given_align
            anchor given_anchor
            for trait in the_traits:
                frame:
                    background "#0a142688"
                    use trait_tooltip(trait)
