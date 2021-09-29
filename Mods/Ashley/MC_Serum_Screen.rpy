init 2:

    screen MC_serum_design_ui(starting_serum,current_traits):
        $ renpy.block_rollback()

        add "Science_Menu_Background.png"
        default trait_tooltip = primitive_serum_prod
        python:
            effective_traits = 0
            for trait_count in starting_serum.traits:
                if not "Production" in trait_count.exclude_tags:
                    effective_traits += 1
        hbox:
            yalign 0.15
            xanchor 0.5
            xalign 0.5
            xsize 1180
            spacing 10
            frame:
                background "#888888"
                ysize 850


                vbox:
                    xsize 530
                    frame:
                        background "#000080"
                        xsize 530
                        text "Available Serum Effects" style "serum_text_style_header"
                    frame:
                        background "#666666"
                        xalign 0.5
                        xsize 530
                        ysize 175

                        viewport:
                            xsize 530
                            scrollbars "vertical"
                            mousewheel True
                            vbox:
                                for trait in get_avail_MC_serums():
                                    textbutton trait.name:
                                        style "textbutton_style"
                                        text_style "serum_text_style"
                                        xsize 530
                                        sensitive trait_allowed
                                        action [
                                            Function(starting_serum.add_trait,trait)
                                        ]
                                        hovered [
                                            SetScreenVariable("trait_tooltip", trait)
                                        ]

                                        #unhovered [
                                        #Hide("trait_tooltip")
                                        #]
                    frame:
                        background "#000080"
                        xsize 530
                        text "Add Suggestion Trait" style "serum_text_style_header"
                    frame:
                        background "#666666"
                        xalign 0.5
                        xsize 530
                        ysize 175

                        viewport:
                            xsize 530
                            scrollbars "vertical"
                            mousewheel True
                            vbox:
                                for trait in sorted(sorted(list_of_traits + mc.business.blueprinted_traits, key = lambda trait: trait.exclude_tags, reverse = True), key=lambda trait: trait.tier, reverse = True): # Sort traits by exclude tags (So all production traits are grouped, for example), then by tier (so the highest tier production tag ends up at the top)
                                    if trait not in starting_serum.traits and trait.researched and "Suggest" in trait.exclude_tags:
                                        $ trait_tags = get_exclude_tags(trait)
                                        $ trait_allowed = get_trait_allowed(starting_serum, trait)

                                        #$ trait_side_effects_text = get_trait_side_effect_text(trait)
                                        #$ trait_mastery_text = get_trait_mastery_text(trait)
                                                        # + "\nMastery Level: [trait_mastery_text] | Side Effect Chance: [trait_side_effects_text] %":
                                        textbutton trait.name + trait_tags:
                                            style "textbutton_style"
                                            text_style "serum_text_style"
                                            xsize 530
                                            sensitive trait_allowed
                                            action [
                                                Function(starting_serum.add_trait,trait)
                                            ]
                                            hovered [
                                                SetScreenVariable("trait_tooltip", trait)
                                            ]

                    frame:
                        background "#000080"
                        xsize 530
                        text "Add Serum Traits" style "serum_text_style_header"
                    frame:
                        background "#666666"
                        xalign 0.5
                        xsize 530
                        ysize 350

                        viewport:
                            xsize 530
                            scrollbars "vertical"
                            mousewheel True

                            vbox:
                                for trait in sorted(sorted(list_of_traits + mc.business.blueprinted_traits, key = lambda trait: trait.exclude_tags, reverse = True), key=lambda trait: trait.name, reverse = False): # Sort traits by exclude tags (So all production traits are grouped, for example), then by name since tier does not matter.
                                    if trait not in starting_serum.traits and trait.researched and "Production" not in trait.exclude_tags and "Suggest" not in trait.exclude_tags:
                                        $ trait_tags = get_exclude_tags(trait)
                                        $ trait_allowed = get_trait_allowed(starting_serum, trait)

                                        #$ trait_side_effects_text = get_trait_side_effect_text(trait)
                                        #$ trait_mastery_text = get_trait_mastery_text(trait)
                                                        #+ "\nMastery Level: [trait_mastery_text] | Side Effect Chance: [trait_side_effects_text] %":
                                        textbutton trait.name + trait_tags:
                                            style "textbutton_style"
                                            text_style "serum_text_style"
                                            xsize 530
                                            sensitive trait_allowed
                                            action [
                                                Function(starting_serum.add_trait,trait)
                                            ]
                                            hovered [
                                                SetScreenVariable("trait_tooltip", trait)
                                            ]

                                            #unhovered [
                                            #Hide("trait_tooltip")
                                            #]
            frame:
                background "#888888"
                ysize 850
                vbox:
                    frame:
                        background "#000080"
                        xsize 530
                        text "Remove a trait" style "serum_text_style_header"

                    frame:
                        background "#666666"
                        xalign 0.5
                        xsize 530
                        ysize 450
                        viewport:

                            scrollbars "vertical"
                            mousewheel True
                            vbox:
                                for trait in starting_serum.traits:
                                    $ trait_tags = get_exclude_tags(trait)

                                    $ trait_side_effects_text = get_trait_side_effect_text(trait)
                                    $ trait_mastery_text = get_trait_mastery_text(trait)

                                    textbutton trait.name + trait_tags + "\nMastery Level: [trait_mastery_text] | Side Effect Chance: [trait_side_effects_text] %":
                                        style "textbutton_style"
                                        text_style "serum_text_style"
                                        xsize 520
                                        action[
                                            Function(starting_serum.remove_trait,trait)
                                        ]
                                        hovered [
                                            SetScreenVariable("trait_tooltip", trait)
                                        ]
                                        #unhovered Hide("trait_tooltip")

                    vbox:
                        frame:
                            background "#000080"
                            xsize 530
                            text "Trait Information: [trait_tooltip.name]" style "serum_text_style_header"

                        frame:
                            background "#666666"
                            xsize 530
                            xalign 0.5
                            viewport:
                                draggable True
                                xsize 530
                                mousewheel "vertical"
                                vbox:
                                    spacing 5
                                    hbox:
                                        spacing 5
                                        vbox:
                                            frame:
                                                background "#43B197"
                                                xsize 255
                                                text "[trait_tooltip.positive_slug]" style "serum_text_style"
                                        vbox:
                                            frame:
                                                background "#B14365"
                                                xsize 255
                                                text "[trait_tooltip.negative_slug]" style "serum_text_style"
                                    hbox:
                                        frame:
                                            background "#000080"
                                            xsize 515
                                            text "[trait_tooltip.desc]" style "serum_text_style"

            frame:
                background "#888888"
                ysize 850
                vbox:
                    xsize 550
                    spacing 5
                    frame:
                        background "#000080"
                        xsize 550
                        text "Current Serum Statistics:" style "serum_text_style_header"

                    frame:
                        if effective_traits > starting_serum.slots:
                            background "#B14365"
                        else:
                            background "#000080"
                        xsize 550
                        text "Trait Slots: " + str(effective_traits) +"/[starting_serum.slots]" style "serum_text_style"

                    viewport:
                        draggable True
                        xsize 550
                        ysize 50
                        mousewheel "horizontal"
                        hbox:
                            xanchor 0.5
                            xalign 0.5
                            spacing 10
                            xsize 550
                            for num in __builtin__.range(__builtin__.max(starting_serum.slots,effective_traits)):
                                if num < effective_traits and num < starting_serum.slots:
                                    add "Serum_Slot_Full.png" xanchor 0.5 xalign 0.5
                                elif num < effective_traits and num >= starting_serum.slots:
                                    add "Serum_Slot_Incorrect.png" xanchor 0.5 xalign 0.5
                                else:
                                    add "Serum_Slot_Empty.png" xanchor 0.5 xalign 0.5
                    hbox:
                        spacing 5
                        vbox:
                            spacing 5
                            frame:
                                background "#000080"
                                xsize 270
                                text "Research Required: {color=#ff0000}[starting_serum.research_needed]{/color}" style "serum_text_style"
                            frame:
                                background "#000080"
                                xsize 270
                                text "Production Cost: {color=#ff0000}[starting_serum.production_cost]{/color}" style "serum_text_style"
                            frame:
                                background "#000080"
                                xsize 270
                                text "Value: ${color=#98fb98}[starting_serum.value]{/color}" style "serum_text_style"
                        vbox:
                            spacing 5
                            frame:
                                background "#000080"
                                xsize 270

                                $ calculated_profit = (starting_serum.value*mc.business.batch_size)-starting_serum.production_cost
                                if calculated_profit > 0:
                                    text "Expected Profit:{color=#98fb98} $[calculated_profit]{/color}" style "serum_text_style"
                                else:
                                    $ calculated_profit = 0 - calculated_profit
                                    text "Expected Profit:{color=#ff0000} -$[calculated_profit]{/color}" style "serum_text_style"

                            frame:
                                background "#000080"
                                xsize 270
                                text "Duration: [starting_serum.duration] Turns" style "serum_text_style"

                            null #Placeholder to keep the grid aligned

                    frame:
                        background "#000080"
                        xsize 550
                        text "Serum Effects:" style "serum_text_style_header"

                    viewport:
                        xsize 550
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        vbox:
                            for trait in starting_serum.traits:
                                textbutton trait.name:
                                    style "textbutton_style"
                                    text_style "serum_text_style"
                                    xsize 540
                                    action  NullAction()
                                    hovered SetScreenVariable("trait_tooltip", trait)

                                hbox:
                                    frame:
                                        background "#43B197"
                                        xsize 270
                                        margin [5, 0, 5, 0]
                                        text "[trait.positive_slug]" style "serum_text_style"
                                    frame:
                                        xsize 270
                                        background "#B14365"
                                        text "[trait.negative_slug]" style "serum_text_style"

        frame:
            background "#888888"
            xsize 250
            xanchor 0.5
            xalign 0.5
            yalign 0.93
            vbox:
                xanchor 0.5
                xalign 0.5
                textbutton "Create Design":
                    action [Hide("trait_tooltip"), Hide("serum_design_ui"), Hide("serum_tooltip"), Return(starting_serum)]
                    sensitive (starting_serum.slots >= effective_traits and __builtin__.len(starting_serum.traits) and starting_serum.has_tag("Production")) > 0

                    style "textbutton_style"
                    text_style "serum_text_style"
                    xanchor 0.5
                    xalign 0.5
                    xsize 230

                textbutton "Reject Design":
                    action [Hide("trait_tooltip"), Hide("serum_design_ui"), Hide("serum_tooltip"), Return("None")]

                    style "textbutton_style"
                    text_style "serum_text_style"
                    xanchor 0.5
                    xalign 0.5
                    xsize 230

        imagebutton:
            auto "/tutorial_images/restart_tutorial_%s.png"
            xsize 54
            ysize 54
            yanchor 1.0
            xalign 0.0
            yalign 1.0
            action Function(mc.business.reset_tutorial,"design_tutorial")

        $ design_tutorial_length = 5 #The number of  tutorial screens we have.
        if mc.business.event_triggers_dict["design_tutorial"] > 0 and mc.business.event_triggers_dict["design_tutorial"] <= design_tutorial_length: #We use negative numbers to symbolize the tutorial not being enabled
            imagebutton:
                auto
                sensitive True
                xsize 1920
                ysize 1080
                idle "/tutorial_images/design_tutorial_"+__builtin__.str(mc.business.event_triggers_dict["design_tutorial"])+".png"
                hover "/tutorial_images/design_tutorial_"+__builtin__.str(mc.business.event_triggers_dict["design_tutorial"])+".png"
                action Function(mc.business.advance_tutorial,"design_tutorial")

# # MC Serum UI
# # Based on screen designed by DaMatt
#
# init 2:
#     screen MC_serum_design():
#         add "Science_Menu_Background.png"
#
#         default type_selected = -1
#         default type_serums = [
#             ["Stat", mc.business, "Stat"],
#             ["Cum", mc.business, "Cum"],
#             ["Ability", mc.business, "Ability"]
#         ]
#
#         vbox:
#             xalign 0.5
#             xanchor 0.5
#             yalign 0.05
#             yanchor 0.0
#             spacing 20
#             frame:
#                 background "#1a45a1aa"
#                 xsize 1860
#                 ysize 60
#                 text "Creat Your Serum Dose" xalign 0.5 xanchor 0.5 yalign 0.5 yanchor 0.5 size 36 style "menu_text_style"
#
#             hbox:
#                 vbox:
#                     xsize 500
#                     yalign 0.0
#
#                     frame:
#                         background "#777777"
#                         xalign 0.5
#
#                         hbox:
#                             xalign 0.5
#                             vbox:
#                                 frame:
#                                     xsize 500
#                                     ysize 50
#                                     background "#000080"
#                                     text "Serum Type" style "serum_text_style_header"
#
#                                 viewport:
#                                     xsize 500
#                                     ysize 700
#                                     xalign 0.5
#                                     spacing 0
#
#                                     vbox:
#                                         for type_serum in range(0,__builtin__.len(type_serums)):
#                                             button:
#                                                 vbox:
#                                                     xalign 0.5
#                                                     text type_serums[type_serum][0] style "serum_text_style"
#                                                     text get_division_serum_name(division_serums[division]) style "serum_text_style" size 14
#                                                 style "textbutton_style"
#                                                 if type_selected == type_serum:
#                                                     background "#000080"
#                                                     hover_background "#0030A0"
#                                                 else:
#                                                     background "#222222"
#                                                     hover_background "#333333"
#                                                 xsize 500
#                                                 action SetScreenVariable("type_selected", type_serum)
#
#                 null width 10
#
#                 vbox:
#                     xsize 500
#                     if type_selected > -1:
#
#                         frame:
#                             background "#777777"
#                             xalign 0.5
#
#                             hbox:
#                                 xalign 0.5
#                                 vbox:
#                                     frame:
#                                         xsize 500
#                                         ysize 50
#                                         background "#000080"
#                                         text "Available Serums" style "serum_text_style_header"
#
#                                     viewport:
#                                         scrollbars "vertical"
#                                         mousewheel True
#                                         xsize 500
#                                         ysize 700
#                                         xalign 0
#
#                                         vbox:
#
#                                             button:
#                                                 xsize 500
#                                                 ysize 80
#                                                 vbox:
#                                                     xalign 0.5
#                                                     text "No serum" style "serum_text_style"
#                                                 style "textbutton_style"
#                                                 sensitive True
#                                                 if get_division_serum(division_serums[division_selected]) is None:
#                                                     background "#000080"
#                                                     hover_background "#0030A0"
#                                                 else:
#                                                     background "#222222"
#                                                     hover_background "#333333"
#                                                 action Function(set_division_serum, division_serums[division_selected], None)
#
#                                             for serum in get_avail_MC_serum_by_cat():
#                                                 button:
#                                                     xsize 500
#                                                     vbox:
#                                                         xalign 0.5
#                                                         text serum[0].name style "serum_text_style"
#                                                         text "Available: " + str(serum[1]) style "serum_text_style" size 14
#                                                     style "textbutton_style"
#                                                     sensitive True
#                                                     if get_division_serum(division_serums[division_selected]) == serum[0]:
#                                                         background "#000080"
#                                                         hover_background "#0030A0"
#                                                     else:
#                                                         background "#222222"
#                                                         hover_background "#333333"
#                                                     hovered [
#                                                         Show("serum_tooltip", None, serum[0],given_align = (0.97,0.12), given_anchor = (1.0,0.0))
#                                                     ]
#                                                     unhovered [
#                                                         Hide("serum_tooltip")
#                                                     ]
#                                                     action Function(set_division_serum, division_serums[division_selected], serum[0])
#
#             frame:
#                 background None
#                 anchor [0.5,0.5]
#                 align [0.5,0.55]
#                 xysize [500,120]
#                 imagebutton:
#                     align [0.5,0.5]
#                     auto "gui/button/choice_%s_background.png"
#                     focus_mask "gui/button/choice_idle_background.png"
#                     action [Hide("assign_division_serum"), Return(), Hide("serum_tooltip")]
#                 textbutton "Return" align [0.5,0.5] text_style "return_button_style"
