init -1 python:
        def get_trait_side_effect_text(trait):
            trait_side_effects = trait.get_effective_side_effect_chance()

            if trait.research_needed > 10000:
                return "{color=#cd5c5c}Always Guaranteed{/color}"
            if trait_side_effects > 100:
                return "{color=#cd5c5c}100%{/color}"
            if trait_side_effects >= 60: # Red (Color code the side effect risk for quicker identification)
                return "{color=#cd5c5c}" + str(trait_side_effects) + "%{/color}"
            elif trait_side_effects >= 20: # Yellow
                return "{color=#eee000}" + str(trait_side_effects) + "%{/color}"
            else: # Green
                return "{color=#98fb98}" + str(trait_side_effects) + "%{/color}"

        def get_trait_mastery_text(trait):
            if trait.mastery_level <= 10: # Red
                return "{color=#cd5c5c}" + str(trait.mastery_level) + "{/color}"
            elif trait.mastery_level <= 50: # Yellow
                return "{color=#eee000}" + str(trait.mastery_level) + "{/color}"
            else: # Green
                return "{color=#98fb98}" + str(trait.mastery_level) + "{/color}"

        def get_trait_display_title(trait):
            trait_tags = ""
            if trait.exclude_tags:
                trait_tags = "\nExcludes Other: "
                for a_tag in trait.exclude_tags:
                    trait_tags += "[" + a_tag + "]"

            if trait.research_needed > 10000: #Assume very high values are impossible #TODO: Just make this a boolean we can toggle on each trait.
                research_needed_string = "\nResearch Impossible"
            else:
                research_needed_string = "(" +str(trait.current_research)+"/"+ str(trait.research_needed) + ")"

            return trait.name + " " + research_needed_string + trait_tags

init 2:
    screen research_select_ui: #How you select serum and trait research
        add "Science_Menu_Background.png"

        default decorated = sorted([(trait.exclude_tags or "zzz", trait.name, i, trait) for i, trait in enumerate(list_of_traits + mc.business.blueprinted_traits)])
        default sorted_traits = [trait for exclude_tags, name, i, trait in decorated]
        default selected_research = None #If not None a screen is shown, including a "begin research" button or an "unlock and research" button.

        vbox:
            xalign 0.08
            yalign 0.4
            frame:
                background "#0a142688"
                xsize 1200
                ymaximum 55
                frame:
                    background "#000080"
                    xsize 1190
                    if not mc.business.active_research_design is None:
                        if isinstance(mc.business.active_research_design, SerumTrait):
                            $ trait_side_effects_text = get_trait_side_effect_text(mc.business.active_research_design)
                            $ trait_mastery_text = get_trait_mastery_text(mc.business.active_research_design)
                            text "Current: [mc.business.active_research_design.name] ([mc.business.active_research_design.current_research]/[mc.business.active_research_design.research_needed])" + "{size=14} Mastery Level: [trait_mastery_text] | Side Effect Chance: [trait_side_effects_text]":
                                style "serum_text_style"
                                size 22
                                xalign 0.0
                        else:
                            $ change_amount = str(__builtin__.round((mc.business.active_research_design.current_research/mc.business.active_research_design.research_needed) * 100, 1))
                            text "Current: [mc.business.active_research_design.name] {size=14} Completion: [change_amount]%":
                                style "serum_text_style"
                                size 22
                                xalign 0.0
                    else:
                        text "Current: None!":
                            style "serum_text_style"
                            size 22
                            xalign 0.0

                    text "{size=14}Available Clarity:{/size} [mc.free_clarity]":
                        style "serum_text_style"
                        size 22
                        xalign 1.0

            null height 20

            frame:
                background "#0a142688"
                xsize 1200
                ysize 900
                hbox:
                    spacing 5
                    vbox:
                        frame:
                            background "#000080"
                            xsize 380
                            text "Research New Traits" style "menu_text_title_style" xalign 0.5

                        viewport:
                            xsize 380
                            ysize 780
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
                                                    action SetScreenVariable("selected_research", trait)
                                                    if selected_research == trait:
                                                        if mc.business.active_research_design == trait:
                                                            background "#593f85"
                                                        else:
                                                            background "#59853f"
                                                        hover_background "#a9d59f"
                                                    else:
                                                        if mc.business.active_research_design == trait:
                                                            background "#008000"
                                                        else:
                                                            background "#000080"
                                                        hover_background "#1a45a1"
                                                    xsize 365

                    vbox:
                        frame:
                            background "#000080"
                            xsize 410
                            text "Master Existing Traits:" style "menu_text_title_style" xalign 0.5

                        viewport:
                            xsize 410
                            ysize 780
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

                                                    action SetScreenVariable("selected_research", trait)
                                                    style "textbutton_style"
                                                    text_style "serum_text_style_traits"
                                                    if selected_research == trait:
                                                        if mc.business.active_research_design == trait:
                                                            background "#593f85"
                                                        else:
                                                            background "#59853f"
                                                        hover_background "#a9d59f"
                                                    else:
                                                        if mc.business.active_research_design == trait:
                                                            background "#008000"
                                                        else:
                                                            background "#000080"
                                                        hover_background "#1a45a1"
                                                    xsize 395

                    vbox:
                        frame:
                            background "#000080"
                            xsize 380
                            text "Research New Designs:" style "menu_text_title_style" xalign 0.5

                        viewport:
                            xsize 380
                            ysize 780
                            scrollbars "vertical"
                            mousewheel True
                            vbox:
                                xsize 370

                                for serum in mc.business.serum_designs:
                                    if not serum.researched:
                                        textbutton "[serum.name] ([serum.current_research]/[serum.research_needed])":
                                            text_xalign 0.5
                                            text_text_align 0.5

                                            action SetScreenVariable("selected_research", serum)
                                            style "textbutton_style"
                                            text_style "serum_text_style_traits"
                                            if selected_research == trait:
                                                if mc.business.active_research_design == trait:
                                                    background "#593f85"
                                                else:
                                                    background "#59853f"
                                                hover_background "#a9d59f"
                                            else:
                                                if mc.business.active_research_design == trait:
                                                    background "#008000"
                                                else:
                                                    background "#000080"
                                                hover_background "#1a45a1"
                                            xsize 365

                textbutton "Return" action [Return("None")] style "textbutton_style" text_style "textbutton_text_style" text_align (0.5, 0.5) yalign 0.995 xanchor 0.5 xalign 0.5 xsize 360

        if selected_research is not None:
            frame: #Frame that displays the info on the currently selected screen.
                xsize 540
                ysize 974
                background "#0a142688"
                xalign 0.95
                yalign 0.5
                $ button_name = ""
                $ button_actions = []
                $ button_sensitive = True

                if isinstance(selected_research, SerumTrait):
                    use trait_tooltip(selected_research, given_align = (0.5,0.0), given_anchor = (0.5,0.0))
                elif isinstance(selected_research, SerumDesign):
                    use serum_tooltip(selected_research, given_align = (0.5,0.0), given_anchor = (0.5,0.0))

                if selected_research == mc.business.active_research_design:
                    $ button_name = "Halt Research"
                    $ button_actions.append(Function(mc.business.set_serum_research,None))

                elif isinstance(selected_research, SerumTrait): #
                    if not selected_research.unlocked:
                        if isinstance(selected_research, SerumTraitBlueprint):
                            $ button_name = "Design and Unlock Trait"
                        else:
                            $ button_name = "Unlock and Begin Research"
                        $ button_name += "\nCosts: " + str(selected_research.clarity_cost) + " Clarity"
                        if selected_research.clarity_cost > mc.free_clarity:
                            $ button_sensitive = False
                        else:
                            $ button_actions.append(Function(selected_research.unlock_trait))
                            $ button_actions.append(Function(mc.business.set_serum_research,selected_research))

                    elif not selected_research.researched:
                        $ button_name = "Continue Unlocked Research"
                        $ button_actions.append(Function(mc.business.set_serum_research,selected_research))

                    else:
                        $ button_name = "Continue Mastery Research"
                        $ button_actions.append(Function(mc.business.set_serum_research,selected_research))

                elif isinstance(selected_research, SerumDesign):
                    use serum_tooltip(selected_research, given_align = (0.5,0.0), given_anchor = (0.5,0.0))
                    if not selected_research.unlocked:
                        $ button_name = "Unlock and Begin Research"
                        $ button_name += "\nCosts: " + str(selected_research.clarity_needed)
                        if selected_research.clarity_needed > mc.free_clarity:
                            $ button_sensitive = False
                        else:
                            $ button_actions.append(Function(selected_research.unlock_design))
                            $ button_actions.append(Function(mc.business.set_serum_research,selected_research))
                    elif not selected_research.researched:
                        $ button_name = "Continue Unlocked Research"
                        $ button_actions.append(Function(mc.business.set_serum_research,selected_research))
                    else:
                        pass #Serum designs that are unlocked and researched shouldn't get here anyways.

                textbutton button_name:
                    text_align (0.5, 0.5)
                    text_style "textbutton_text_style"
                    style "textbutton_style"
                    action button_actions
                    sensitive button_sensitive
                    xsize 300
                    anchor (0.5,1.0)
                    align (0.5,1.0)

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
