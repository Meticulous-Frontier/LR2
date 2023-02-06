init 2:
    screen select_trait_research(the_traits): #You can now pass extra inventories, as well as names for all of the inventories you are passing. Returns nothing, but is used to view inventories.
        default decorated = sorted([(trait.exclude_tags or "zzz", trait.name, i, trait) for i, trait in enumerate(list_of_traits + mc.business.blueprinted_traits)])
        default sorted_traits = [trait for exclude_tags, name, i, trait in decorated]

        add "Science_Menu_Background.png"
        hbox:
            xalign 0.52
            yalign 0.05
            spacing 40
            frame:
                background "#000080"
                ysize 120
                xsize 600
                text "Select a trait to research" style "menu_text_title_style" xalign 0.5:
                    size 40
        hbox:
            $ count = 0
            xalign 0.05
            yalign 0.12
            yanchor 0.07
            spacing 40
            frame:
                background "#0a142688"
                xsize 600
                vbox:
                    xalign 0.02
                    yalign 0.02
                    frame:
                        background "#000080"
                        xsize 590
                        text "Serums Traits" style "menu_text_title_style" xalign 0.5

                    viewport:
                        xsize 600
                        ysize 800
                        scrollbars "vertical"
                        mousewheel True
                        spacing 1
                        xalign 0

                        vbox:
                            for dt in range(mc.business.research_tier, -1, -1):
                                if any([x for x in sorted_traits if x.tier == dt and not isinstance(x, SerumTraitBlueprint) and x.researched]):
                                    frame:
                                        background "#000000"
                                        xsize 365
                                        text "Tier [dt]" style "serum_text_style_header" xalign 0.5

                                    for trait in sorted_traits:
                                        if trait.tier == dt and not isinstance(trait, SerumTraitBlueprint) and trait.researched:
                                            $ trait_title = get_trait_display_title(trait)
                                            $ trait_side_effects_text = get_trait_side_effect_text(trait)
                                            $ trait_mastery_text = get_trait_mastery_text(trait)

                                            textbutton "[trait_title]\nMastery Level: [trait_mastery_text] | Side Effect Chance: [trait_side_effects_text]":
                                                text_xalign 0.5
                                                text_text_align 0.5
                                                style "textbutton_style"
                                                text_style "serum_text_style_traits"
                                                xsize 580
                                                action [Hide("select_trait_research"),Hide("select_trait_research_tooltip"),Return(trait)]
                                                hovered Show("select_trait_research_tooltip",None, trait, given_align = (0.97,0.07), given_anchor = (1.0,0.0))


init 2:
    screen select_trait_research_tooltip(the_trait, given_anchor = (0.0,0.0), given_align = (0.0,0.0), allow_edit = False):
        zorder 105

        frame:
            background "#0a142688"
            anchor given_anchor
            align given_align
            vbox:
                xsize 540
                ysize 900
                xalign 0.5
                spacing 10

                frame:
                    background "#000080"
                    xsize 520
                    text "[the_trait.name]" style "menu_text_title_style" xalign 0.5

                # use aspect_grid(the_trait)

                frame:
                    background "#0a142688"
                    xalign 0.5
                    xsize 520
                    ysize 150
                    vbox:
                        text "[the_trait.desc]":
                            size 16

                frame:
                    background "#0a142688"
                    xalign 0.5
                    xsize 520
                    ysize 150
                    vbox:
                        hbox:
                            spacing 5
                            vbox:
                                spacing 5
                                frame:
                                    background "#000080"
                                    xsize 245
                                    text "Mastery Level: {color=98fb98}[the_trait.mastery_level]{/color}" style "serum_text_style_traits"

                                if len(the_trait.exclude_tags) > 0:
                                    frame:
                                        background "#000080"
                                        xsize 245
                                        text "Trait Tag: {color=#cd5c5c}[the_trait.exclude_tags[0]]{/color}" style "serum_text_style_traits"

                            vbox:
                                spacing 5

                                frame:
                                    background "#000080"
                                    xsize 245
                                    text "Trait Tier: {color=#cd5c5c}[the_trait.tier]{/color}" style "serum_text_style_traits"

                frame:
                    background "#0a142688"
                    xalign 0.5
                    xsize 520
                    ysize 430
                    vbox:
                        spacing 5
                        hbox:
                            spacing 5
                            frame:
                                background "#43B197"
                                xsize 245
                                text "[the_trait.positive_slug]" style "serum_text_style_traits" size 16

                            frame:
                                background "#B14365"
                                xsize 245
                                text the_trait.build_negative_slug() style "serum_text_style_traits" size 16
