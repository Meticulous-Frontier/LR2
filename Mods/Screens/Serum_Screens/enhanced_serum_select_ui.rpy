init 2:
    screen serum_select_ui: #How you select serum and trait research
        add "Science_Menu_Background.png"
        vbox:
            xalign 0.1
            yalign 0.4
            frame:
                background "#888888"
                xsize 1000
                if not mc.business.active_research_design == None:
                    textbutton "Current Research: [mc.business.active_research_design.name] ([mc.business.active_research_design.current_research]/[mc.business.active_research_design.research_needed])":
                        style "textbutton_style"
                        text_style "serum_text_style"
                        xsize 1000
                        xanchor 0.5
                        xalign 0.5

                        action NullAction()
                else:
                    textbutton "Current Research: None!":
                        style "textbutton_style"
                        text_style "serum_text_style"
                        xsize 1000
                        xanchor 0.5
                        xalign 0.5

                        action NullAction()

            null height 20

            frame:
                background "#888888"
                xsize 1000
                ysize 900
                hbox:
                    viewport:
                        xsize 320
                        ysize 800
                        scrollbars "vertical"
                        mousewheel True
                        vbox:
                            xsize 320
                            textbutton "Research New Traits":
                                style "textbutton_style"
                                text_style "serum_text_style"
                                xsize 320
                                xanchor 0.5
                                xalign 0.5

                                action NullAction()

                            for trait in sorted(sorted(list_of_traits, key = lambda trait: trait.exclude_tags, reverse = True), key=lambda trait: trait.tier, reverse = True):
                                if not trait.researched and trait.has_required():
                                    $ trait_tags = ""
                                    if trait.exclude_tags:
                                        $ trait_tags = "\nExcludes Other: "
                                        for a_tag in trait.exclude_tags:
                                            $ trait_tags += "[[" + a_tag + "]"
                                    $ trait_title = trait.name + " " + "(" +str(trait.current_research)+"/"+ str(trait.research_needed) + ")" + trait_tags

                                    textbutton "[trait_title]":
                                        style "textbutton_style"
                                        text_style "serum_text_style"
                                        action [Hide("trait_tooltip"),Return(trait)]
                                        text_size 14
                                        hovered Show("trait_tooltip",None,trait)
                                        unhovered Hide("trait_tooltip")
                                        xsize 320

                    viewport:
                        xsize 320
                        ysize 800
                        scrollbars "vertical"
                        mousewheel True
                        vbox:
                            xsize 320
                            textbutton "Master Existing Traits:":
                                style "textbutton_style"
                                text_style "serum_text_style"
                                xsize 320
                                xanchor 0.5
                                xalign 0.5

                                action NullAction()

                            for trait in sorted(sorted(list_of_traits, key = lambda trait: trait.exclude_tags, reverse = True), key=lambda trait: trait.tier, reverse = True):
                                if trait.researched:
                                    $ trait_tags = ""
                                    if trait.exclude_tags:
                                        $ trait_tags = "\nExcludes Other: "
                                        for a_tag in trait.exclude_tags:
                                            $ trait_tags += "[[" + a_tag + "]"

                                    $ trait_title = trait.name + " " + "(" +str(trait.current_research)+"/"+ str(trait.research_needed) + ")" + trait_tags

                                    $ trait_side_effects = str(trait.get_effective_side_effect_chance()) # Put this section into a function?

                                    if trait.get_effective_side_effect_chance() >= 60: # Red (Color code the side effect risk for quicker identification)
                                        $ trait_side_effects_text = "{color=#cd5c5c}[trait_side_effects]{/color}"

                                    elif trait.get_effective_side_effect_chance() >= 20: # Yellow
                                        $ trait_side_effects_text = "{color=#eee000}[trait_side_effects]{/color}"

                                    else: # Green
                                        $ trait_side_effects_text = "{color=#98fb98}[trait_side_effects]{/color}"


                                    $ trait_mastery_level = str(trait.mastery_level)

                                    if trait.mastery_level <= 10: # Red
                                        $ trait_mastery_text = "{color=#cd5c5c}[trait_mastery_level]{/color}"
                                    elif trait.mastery_level <= 50: # Yellow
                                        $ trait_mastery_text = "{color=#eee000}[trait_mastery_level]{/color}"
                                    else: # Green
                                        $ trait_mastery_text = "{color=#98fb98}[trait_mastery_level]{/color}"

                                    textbutton "[trait_title]" + "\n Mastery Level: " + trait_mastery_text + " | " + "Side Effect Chance: " + trait_side_effects_text + " %":
                                        text_xalign 0.5
                                        text_text_align 0.5
                                        text_size 14
                                        action [Hide("trait_tooltip"),Return(trait)] style "textbutton_style"
                                        text_style "serum_text_style"
                                        hovered Show("trait_tooltip",None,trait)
                                        unhovered Hide("trait_tooltip")
                                        xsize 320


                    viewport:
                        xsize 320
                        ysize 800
                        scrollbars "vertical"
                        mousewheel True
                        vbox:
                            xsize 320
                            textbutton "Research New Designs:":
                                style "textbutton_style"
                                text_style "serum_text_style"
                                xsize 320
                                xanchor 0.5
                                xalign 0.5

                                action NullAction()

                            for serum in mc.business.serum_designs:
                                if not serum.researched:
                                    textbutton "[serum.name] ([serum.current_research]/[serum.research_needed])":
                                        text_xalign 0.5
                                        text_text_align 0.5
                                        text_size 14
                                        action [Hide("serum_tooltip"),Return(serum)] style "textbutton_style"
                                        text_style "serum_text_style"
                                        hovered Show("serum_tooltip",None,serum)
                                        unhovered Hide("serum_tooltip")
                                        xsize 320

                textbutton "Do not change research." action Return("None") style "textbutton_style" text_style "serum_text_style" yalign 0.995 xanchor 0.5 xalign 0.5

        imagebutton:
            auto "/tutorial_images/restart_tutorial_%s.png"
            xsize 54
            ysize 54
            yanchor 1.0
            xalign 0.0
            yalign 1.0
            action Function(mc.business.reset_tutorial,"research_tutorial")

        $ research_tutorial_length = 5 #The number of  tutorial screens we have.
        if mc.business.event_triggers_dict["research_tutorial"] > 0 and mc.business.event_triggers_dict["research_tutorial"] <= research_tutorial_length: #We use negative numbers to symbolize the tutorial not being enabled
            imagebutton:
                auto
                sensitive True
                xsize 1920
                ysize 1080
                idle "/tutorial_images/research_tutorial_"+__builtin__.str(mc.business.event_triggers_dict["research_tutorial"])+".png"
                hover "/tutorial_images/research_tutorial_"+__builtin__.str(mc.business.event_triggers_dict["research_tutorial"])+".png"
                action Function(mc.business.advance_tutorial,"research_tutorial")
