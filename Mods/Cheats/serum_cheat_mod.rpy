# Since a lot of players complain about a new game restart is due almost at every game
# update, I made this cheat screen for serums to be quickly researched and mastered.

init python:
    if "serum_cheat_menu_keybind" not in config.overlay_screens:
        config.overlay_screens.append("serum_cheat_menu_keybind")

screen serum_cheat_menu_keybind():
    key "t" action ToggleScreen("serum_cheat_menu")
    key "T" action ToggleScreen("serum_cheat_menu")

screen serum_cheat_menu():
    add "Science_Menu_Background.png"

    default decorated = sorted([(trait.exclude_tags or "zzz", trait.name, i, trait) for i, trait in enumerate(list_of_traits + mc.business.blueprinted_traits)])
    default sorted_traits = [trait for exclude_tags, name, i, trait in decorated]

    vbox:
        xalign 0.04
        yalign 0.3
        frame:
            background "#0a142688"
            xsize 1200
            ysize 1000
            hbox:
                spacing 5
                vbox:
                    frame:
                        background "#000080"
                        xsize 380
                        vbox:
                            text "Available New Traits" style "menu_text_title_style"
                            text "{color=#B14365}{size=14}Click the Trait to have it researched{/size}{/color}" style "serum_text_style"

                    viewport:
                        xsize 380
                        ysize 980
                        scrollbars "vertical"
                        mousewheel True
                        vbox:
                            xsize 370
                            for dt in range(mc.business.research_tier, -1, -1):
                                if any([x for x in list_of_traits + mc.business.blueprinted_traits if x.tier == dt and not x.researched and x.has_required()]):
                                    frame:
                                        background "#000000"
                                        xsize 365
                                        text "Tier " + str(dt) style "serum_text_style_header" xalign 0.5

                                    for trait in sorted_traits:
                                        if trait.tier == dt and not trait.researched and trait.has_required():
                                            $ trait_title = get_trait_display_title(trait)
                                            textbutton "[trait_title]":
                                                style "textbutton_style"
                                                text_style "serum_text_style_traits"
                                                sensitive not isinstance(trait, SerumTraitBlueprint)
                                                action [Hide("trait_tooltip"), SetField(trait, "researched", True), SetField(trait, "unlocked", True)]
                                                hovered Show("trait_tooltip",None,trait, given_align = (0.97,0.07), given_anchor = (1.0,0.0))
                                                unhovered Hide("trait_tooltip")
                                                xsize 365
                vbox:
                    frame:
                        background "#000080"
                        xsize 410
                        vbox:
                            text "Master Existing Traits" style "menu_text_title_style"
                            text "{color=#B14365}{size=14}Click the Trait to add mastery levels{/size}{/color}" style "serum_text_style"

                    viewport:
                        xsize 410
                        ysize 980
                        scrollbars "vertical"
                        mousewheel True
                        vbox:
                            xsize 400

                            for dt in range(mc.business.research_tier, -1, -1):
                                if any([x for x in list_of_traits + mc.business.blueprinted_traits if x.tier == dt and x.researched]):
                                    frame:
                                        background "#000000"
                                        xsize 395
                                        text "Tier " + str(dt) style "serum_text_style_header" xalign 0.5

                                for trait in sorted_traits:
                                    if trait.tier == dt and trait.researched:
                                        $ trait_title = get_trait_display_title(trait)
                                        $ trait_side_effects_text = get_trait_side_effect_text(trait)
                                        $ trait_mastery_text = get_trait_mastery_text(trait)

                                        textbutton "[trait_title]\nMastery Level: [trait_mastery_text] | Side Effect Chance: [trait_side_effects_text]":
                                            text_xalign 0.5
                                            text_text_align 0.5
                                            action [
                                                Hide("trait_tooltip"),
                                                SetField(trait, "mastery_level", trait.mastery_level + 1)
                                            ]
                                            alternate [
                                                Hide("trait_tooltip"),
                                                SetField(trait, "mastery_level", (trait.mastery_level - 1) if trait.mastery_level > 2 else 1.0),
                                            ]
                                            style "textbutton_style"
                                            text_style "serum_text_style_traits"
                                            hovered Show("trait_tooltip",None,trait, given_align = (0.97,0.07), given_anchor = (1.0,0.0))
                                            unhovered Hide("trait_tooltip")
                                            xsize 395

                vbox:
                    frame:
                        background "#000080"
                        xsize 390
                        vbox:
                            text "Research New Designs" style "menu_text_title_style"
                            text "{color=#B14365}{size=14}Click the Design to have it researched{/size}{/color}" style "serum_text_style"

                    viewport:
                        xsize 390
                        ysize 980
                        scrollbars "vertical"
                        mousewheel True
                        vbox:
                            xsize 370

                            for serum in mc.business.serum_designs:
                                if not serum.researched:
                                    textbutton "[serum.name] ([serum.current_research]/[serum.research_needed])":
                                        text_xalign 0.5
                                        text_text_align 0.5
                                        action [Hide("serum_tooltip"), SetField(serum, "researched", True)]
                                        style "textbutton_style"
                                        text_style "serum_text_style_traits"
                                        hovered Show("serum_tooltip",None,serum, given_align = (0.97,0.07), given_anchor = (1.0,0.0))
                                        unhovered Hide("serum_tooltip")
                                        xsize 370
                                        xalign 0.5
