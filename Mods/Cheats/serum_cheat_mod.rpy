# Since a lot of players complain about a new game restart is due almost at every game
# update, I made this cheat screen for serums to be quickly researched and mastered.

init -2 style serum_cheat_text_style: # cheat_text_style already defined in cheat_mod
    text_align 0.5
    size 20
    color "#dddddd"
    outlines [(2,"#222222",0,0)]
    xalign 0.5

init -1 python:
    if "keybindS" not in config.overlay_screens:
        config.overlay_screens.append("keybindT")

screen keybindT():
    key "t" action ToggleScreen("serum_cheat_menu")
    key "T" action ToggleScreen("serum_cheat_menu")

screen serum_cheat_menu:
    add "Science_Menu_Background.png"
    vbox:
        xalign 0.04
        yalign 0.3
        frame:
            background "#666666"
            xsize 1200
            ysize 1000
            hbox:
                spacing 5
                vbox:
                    frame:
                        background "#000080"
                        xsize 380
                        text "Available New Traits\n{color=#ff0000}{size=14}Click the Trait to have it researched{/size}{/color}" style "serum_cheat_text_style"

                    viewport:
                        xsize 380
                        ysize 980
                        scrollbars "vertical"
                        mousewheel True
                        vbox:
                            xsize 370
                            for trait in sorted(sorted(list_of_traits, key = lambda trait: trait.exclude_tags, reverse = True), key=lambda trait: trait.tier, reverse = True): # Sort traits by exclude tags (So all production traits are grouped, for example), then by tier (so the highest tier production tag ends up at the top
                                if not trait.researched and trait.has_required() and "Production" in trait.exclude_tags:
                                    $ trait_title = get_trait_display_title(trait)
                                    textbutton "[trait_title]":
                                        style "textbutton_style"
                                        text_style "serum_text_style_traits"
                                        action [Hide("trait_tooltip"), SetField(trait, "researched", True)]
                                        hovered Show("trait_tooltip",None,trait)
                                        unhovered Hide("trait_tooltip")
                                        xsize 365

                            for trait in sorted(sorted(list_of_traits, key = lambda trait: trait.exclude_tags, reverse = True), key=lambda trait: trait.tier, reverse = True): # Sort traits by exclude tags (So all production traits are grouped, for example), then by tier (so the highest tier production tag ends up at the top
                                if not trait.researched and trait.has_required() and "Suggest" in trait.exclude_tags:
                                    $ trait_title = get_trait_display_title(trait)
                                    textbutton "[trait_title]":
                                        style "textbutton_style"
                                        text_style "serum_text_style_traits"
                                        action [Hide("trait_tooltip"), SetField(trait, "researched", True)]
                                        hovered Show("trait_tooltip",None,trait)
                                        unhovered Hide("trait_tooltip")
                                        xsize 365

                            for trait in sorted(sorted(list_of_traits, key = lambda trait: trait.exclude_tags, reverse = True), key=lambda trait: trait.name, reverse = False): # Sort traits by exclude tags (So all production traits are grouped, for example), then by name since tier does not matter.
                                if not trait.researched and trait.has_required() and "Production" not in trait.exclude_tags and "Suggest" not in trait.exclude_tags:
                                    $ trait_title = get_trait_display_title(trait)
                                    textbutton "[trait_title]":
                                        style "textbutton_style"
                                        text_style "serum_text_style_traits"
                                        action [Hide("trait_tooltip"), SetField(trait, "researched", True)]
                                        hovered Show("trait_tooltip",None,trait)
                                        unhovered Hide("trait_tooltip")
                                        xsize 365
                vbox:
                    frame:
                        background "#000080"
                        xsize 410
                        text "Master Existing Traits:\n{color=#ff0000}{size=14}Click the Trait to add 10 Mastery levels{/size}{/color}" style "serum_cheat_text_style"

                    viewport:
                        xsize 410
                        ysize 980
                        scrollbars "vertical"
                        mousewheel True
                        vbox:
                            xsize 400
                            for trait in sorted(sorted(list_of_traits, key = lambda trait: trait.exclude_tags, reverse = True), key=lambda trait: trait.tier, reverse = True): # Sort traits by exclude tags (So all production traits are grouped, for example), then by tier (so the highest tier production tag ends up at the top
                                if trait.researched and "Production" in trait.exclude_tags:
                                    $ trait_title = get_trait_display_title(trait)
                                    $ trait_side_effects_text = get_trait_side_effect_text(trait)
                                    $ trait_mastery_text = get_trait_mastery_text(trait)

                                    textbutton "[trait_title]\nMastery Level: [trait_mastery_text] | Side Effect Chance: [trait_side_effects_text] %":
                                        text_xalign 0.5
                                        text_text_align 0.5
                                        action [Hide("trait_tooltip"), SetField(trait, "mastery_level", trait.mastery_level+10)] style "textbutton_style"
                                        text_style "serum_text_style_traits"
                                        hovered Show("trait_tooltip",None,trait)
                                        unhovered Hide("trait_tooltip")
                                        xsize 395

                            for trait in sorted(sorted(list_of_traits, key = lambda trait: trait.exclude_tags, reverse = True), key=lambda trait: trait.tier, reverse = True): # Sort traits by exclude tags (So all production traits are grouped, for example), then by tier (so the highest tier production tag ends up at the top
                                if trait.researched and "Suggest" in trait.exclude_tags:
                                    $ trait_title = get_trait_display_title(trait)
                                    $ trait_side_effects_text = get_trait_side_effect_text(trait)
                                    $ trait_mastery_text = get_trait_mastery_text(trait)

                                    textbutton "[trait_title]\nMastery Level: [trait_mastery_text] | Side Effect Chance: [trait_side_effects_text] %":
                                        text_xalign 0.5
                                        text_text_align 0.5
                                        action [Hide("trait_tooltip"), SetField(trait, "mastery_level", trait.mastery_level+10)] style "textbutton_style"
                                        text_style "serum_text_style_traits"
                                        hovered Show("trait_tooltip",None,trait)
                                        unhovered Hide("trait_tooltip")
                                        xsize 395

                            for trait in sorted(sorted(list_of_traits, key = lambda trait: trait.exclude_tags, reverse = True), key=lambda trait: trait.name, reverse = False): # Sort traits by exclude tags (So all production traits are grouped, for example), then by name since tier does not matter.
                                if trait.researched and "Production" not in trait.exclude_tags and "Suggest" not in trait.exclude_tags:
                                    $ trait_title = get_trait_display_title(trait)
                                    $ trait_side_effects_text = get_trait_side_effect_text(trait)
                                    $ trait_mastery_text = get_trait_mastery_text(trait)

                                    textbutton "[trait_title]\nMastery Level: [trait_mastery_text] | Side Effect Chance: [trait_side_effects_text] %":
                                        text_xalign 0.5
                                        text_text_align 0.5
                                        action [Hide("trait_tooltip"), SetField(trait, "mastery_level", trait.mastery_level+10)] style "textbutton_style"
                                        text_style "serum_text_style_traits"
                                        hovered Show("trait_tooltip",None,trait)
                                        unhovered Hide("trait_tooltip")
                                        xsize 395

                vbox:
                    frame:
                        background "#000080"
                        xsize 390
                        text "Research New Designs:\n{color=#ff0000}{size=14}Click the Design to have it researched{/size}{/color}" style "serum_cheat_text_style"

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
                                        action [Hide("serum_tooltip"), SetField(serum, "researched", True)] style "textbutton_style"
                                        text_style "serum_text_style_traits"
                                        hovered Show("serum_tooltip",None,serum)
                                        unhovered Hide("serum_tooltip")
                                        xsize 365
