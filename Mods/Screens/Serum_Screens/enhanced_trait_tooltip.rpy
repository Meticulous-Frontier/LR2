init 2:
    python:
        def get_unlockable_trait_names(trait):
            return [x.name for x in list_of_traits if trait in x.requires]

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
                    xsize 525
                    text "[the_trait.name]" + (" (C)" if isinstance(the_trait, SerumTraitBlueprint) else ""):
                        style "menu_text_title_style"
                        xalign 0.5

                use aspect_grid(the_trait)

                hbox:
                    spacing 5
                    frame:
                        background "#43B197"
                        xsize 260
                        xfill True
                        text "[the_trait.positive_slug]" style "serum_text_style_traits"

                    frame:
                        background "#B14365"
                        xsize 260
                        xfill True
                        text the_trait.build_negative_slug() style "serum_text_style_traits"
                frame:
                    background "#000080"
                    xsize 505
                    text "[the_trait.desc]" style "serum_text_style"

                $ unlockable_traits = get_unlockable_trait_names(the_trait)
                if len(unlockable_traits) > 0:
                    frame:
                        background "#000000"
                        xsize 525
                        text "Required for Traits" style "menu_text_title_style" xalign 0.5

                    frame:
                        background "#000080"
                        xsize 525
                        viewport:
                            xsize 505
                            ysize min(len(unlockable_traits) * 24, 580)
                            scrollbars "vertical"
                            mousewheel True
                            vbox:
                                for ut in get_unlockable_trait_names(the_trait):
                                    text "■ [ut]" style "serum_text_style" xalign 0.0


                transclude

    screen trait_list_tooltip(the_traits, given_align = (0.0,0.0), given_anchor = (0.0,0.0)):
        vbox:
            align given_align
            anchor given_anchor
            for trait in the_traits:
                frame:
                    background "#0a142688"
                    use trait_tooltip(trait)
