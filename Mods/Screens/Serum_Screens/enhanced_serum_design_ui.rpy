init 2:
    python:
        def get_exclude_tags(trait):
            tags = ""
            if trait.exclude_tags:
                tags = " - "
                for a_tag in trait.exclude_tags:
                    tags += "{color=#d38c19}[[" + a_tag + "]{/color}"
            return tags

        def get_trait_allowed(starting_serum, trait):
            for a_trait in starting_serum.traits:
                if any(t in a_trait.exclude_tags for t in trait.exclude_tags):
                    return False
            return True

        def get_trait_aspect_tags(trait):
            aspect_tags = "\n{size=14}"
            if trait.tier > mc.business.max_serum_tier:
                aspect_tags += "Tier: {color=#98fb98}" + str(trait.tier) + "{/color}"
            else:
                aspect_tags += "Tier:" + str(trait.tier)

            aspect_tags += "{color=#0049d8} Ment: " + str(trait.mental_aspect) + "{/color}"
            aspect_tags += "{color=#00AA00} Phys: " + str(trait.physical_aspect) + "{/color}"
            aspect_tags += "{color=#FFC0CB} Sex: " + str(trait.sexual_aspect) + "{/color}"
            aspect_tags += "{color=#FFFFFF} Medic: " + str(trait.medical_aspect) + "{/color}"
            aspect_tags += "{color=#BBBBBB} Flaw: " + str(trait.flaws_aspect) + "{/color}"
            aspect_tags += "{color=#FF6249} Attn: " + str(trait.attention) + "{/color}"
            aspect_tags += "{/size}"
            return aspect_tags


    screen serum_design_ui(starting_serum,current_traits):
        $ renpy.block_rollback()

        default decorated = sorted([(trait.exclude_tags or "zzz", trait.name, i, trait) for i, trait in enumerate(list_of_traits + mc.business.blueprinted_traits)])
        default sorted_traits = [trait for exclude_tags, name, i, trait in decorated]

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
                background "#0a142688"
                ysize 850

                vbox:
                    xsize 530
                    if not starting_serum.has_production_trait():
                        frame:
                            background "#000080"
                            xsize 530
                            text "Pick Production Type" style "menu_text_title_style" xalign .5
                        frame:
                            background "#0a142688"
                            xalign 0.5
                            xsize 530
                            ysize 175

                            viewport:
                                xsize 530
                                scrollbars "vertical"
                                mousewheel True
                                vbox:
                                    for trait in sorted(list_of_traits + mc.business.blueprinted_traits, key = lambda trait: trait.tier, reverse = True): # Sort traits by exclude tags (So all production traits are grouped, for example), then by tier (so the highest tier production tag ends up at the top
                                        if trait not in starting_serum.traits and trait.researched and "Production" in trait.exclude_tags:
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
                        background "#000080"
                        xsize 530
                        text "Add Serum Traits" style "menu_text_title_style" xalign .5

                    frame:
                        background "#0a142688"
                        xalign 0.5
                        xsize 530
                        ysize ((574 + 175) if starting_serum.has_production_trait() else 574)

                        viewport:
                            xsize 530
                            scrollbars "vertical"
                            mousewheel True

                            vbox:
                                for dt in range(mc.business.research_tier + 1, -1, -1):
                                    if any([x for x in list_of_traits + mc.business.blueprinted_traits if x.tier == dt and x not in starting_serum.traits and x.researched and "Production" not in x.exclude_tags]):

                                        frame:
                                            background "#000000"
                                            xsize 530
                                            text "Tier " + str(dt) style "serum_text_style_header" xalign 0.5

                                        for trait in sorted_traits:
                                            if trait.tier == dt and trait not in starting_serum.traits and trait.researched and "Production" not in trait.exclude_tags:
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
                background "#0a142688"
                ysize 850
                vbox:
                    frame:
                        background "#000080"
                        xsize 530
                        text "Remove a trait" style "menu_text_title_style" xalign .5

                    frame:
                        background "#0a142688"
                        xalign 0.5
                        xsize 530
                        ysize 450
                        viewport:

                            scrollbars "vertical"
                            mousewheel True
                            vbox:
                                for trait in starting_serum.traits:
                                    $ trait_tags = get_exclude_tags(trait)
                                    $ trait_aspect_tags = get_trait_aspect_tags(trait)
                                    $ trait_side_effects_text = get_trait_side_effect_text(trait)
                                    $ trait_mastery_text = get_trait_mastery_text(trait)

                                    textbutton trait.name + trait_tags + trait_aspect_tags + "\nMastery Level: [trait_mastery_text] | Side Effect Chance: [trait_side_effects_text]":
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
                            text "[trait_tooltip.name]" style "menu_text_title_style" xalign .5

                        frame:
                            background "#000080"
                            xsize 530
                            use aspect_grid(trait_tooltip)

                        frame:
                            background "#0a142688"
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
                background "#0a142688"
                ysize 850
                vbox:
                    xsize 550
                    spacing 5
                    frame:
                        background "#000080"
                        xsize 550
                        text "Current Serum Statistics:" style "menu_text_title_style" xalign .5

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
                            spacing 5
                            xsize 550
                            for num in __builtin__.range(__builtin__.max(starting_serum.slots,effective_traits)):
                                if num < effective_traits and num < starting_serum.slots:
                                    add "Serum_Slot_Full.png" xanchor 0.5 xalign 0.5
                                elif num < effective_traits and num >= starting_serum.slots:
                                    add "Serum_Slot_Incorrect.png" xanchor 0.5 xalign 0.5
                                else:
                                    add "Serum_Slot_Empty.png" xanchor 0.5 xalign 0.5

                    use aspect_grid(starting_serum)

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
                                if starting_serum.tier <= mc.business.max_serum_tier:
                                    text "Serum Tier: " + str(starting_serum.tier) style "serum_text_style"
                                else:
                                    text "Serum Tier: {color=#fb6868}" + str(starting_serum.tier) + "{/color}" style "serum_text_style"
                        vbox:
                            spacing 5
                            frame:
                                background "#000080"
                                xsize 270

                                $ calculated_profit = round(mc.business.get_serum_base_value(starting_serum)-(starting_serum.production_cost/mc.business.batch_size))
                                if calculated_profit >= 0:
                                    text "Expected Profit:{color=#98fb98} $[calculated_profit]{/color}" style "serum_text_style"
                                else:
                                    $ calculated_profit = 0 - calculated_profit
                                    text "Expected Profit:{color=#ff0000} -$[calculated_profit]{/color}" style "serum_text_style"

                            frame:
                                background "#000080"
                                xsize 270
                                text "Duration: [starting_serum.duration] Turns" style "serum_text_style"

                            frame:
                                background "#000080"
                                xsize 270
                                text "Unlock Cost: [starting_serum.clarity_needed] Clarity" style "serum_text_style"

                    frame:
                        background "#000080"
                        xsize 550
                        text "Serum Effects:" style "menu_text_title_style" xalign .5

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
            background "#0a142688"
            xsize 250
            xanchor 0.5
            xalign 0.5
            yalign 0.93
            hbox:
                xanchor 0.5
                xalign 0.5
                spacing 40
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

                textbutton "View Contracts":
                    action Show("contract_select")
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
