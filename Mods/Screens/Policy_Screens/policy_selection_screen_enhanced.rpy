init 2: # Will give this a polish later, just wanted to enable categories from lists.
    screen policy_selection_screen():
        add "Paper_Background.png"
        modal True
        zorder 100
        $ tooltip = GetTooltip()

        $ categories = sorted(policy_selection_screen_categories) #This way we can append extra categories and lists with ease.



        default selected_category = categories[0] #Default to the first in our categories list
        default selected_policy = None
        default selected_tooltip = None
        vbox:
            xalign 0.5
            yalign 0.15
            spacing 30
            frame: #Top frame holding the policy categories that we have.
                xsize 1320
                ysize 140
                background "#1a45a1aa"
                vbox:
                    frame:
                        margin [10, 10, 10, 10]
                        background "#000080"
                        xfill True
                        text "Policy Categories" style "serum_text_style"

                    viewport:

                        xfill True
                        draggable True
                        mousewheel "horizontal"


                        grid len(categories) 1: # Properly display categories, this will shrink the more categories are added. Force hbox when it's above a certain amount so that we can use the viewport?
                            xfill True
                            xalign 0.5

                            for category in categories:
                                textbutton category[0]:
                                    ysize 80
                                    xfill True
                                    action [SetScreenVariable("selected_category", category), SetScreenVariable("selected_policy", None), SetScreenVariable("selected_tooltip", None)]
                                    sensitive selected_category != category
                                    style "textbutton_no_padding_highlight"
                                    text_style "serum_text_style"

            frame: #Holds the list of business policies. Needs to be scrollable.
                xsize 1320
                ysize 650
                background "#1a45a1aa"
                hbox:
                    frame:
                        #background None
                        #yfill True
                        xsize 660
                        viewport:
                            mousewheel True
                            if len(selected_category[1]) > 5: #Only take up scrollbar space if needed.
                                 scrollbars "vertical"
                            xfill True
                            #yfill True

                            grid 1 len(selected_category[1]):
                                for policy in sorted(sorted(sorted(selected_category[1], key = lambda x: x.cost), key = lambda x: x.is_owned()), key = lambda x: x.requirement(), reverse = True):
                                    if policy.is_owned():

                                        textbutton "$" + str(policy.cost) + " - " + policy.name:
                                            tooltip policy.desc
                                            action [ToggleScreenVariable("selected_policy", policy, None)]
                                            hovered SetScreenVariable("selected_tooltip", policy.desc)
                                            style "textbutton_no_padding_highlight"
                                            xalign 0.5
                                            text_style "serum_text_style"
                                            background "#59853f"
                                            hover_background "#78b156"
                                            sensitive True
                                            xfill True
                                            ysize 100

                                    else:
                                        if policy.requirement() and (policy.cost < mc.business.funds or policy.cost == mc.business.funds):
                                            textbutton "$" + str(policy.cost) + " - " + policy.name:
                                                tooltip policy.desc
                                                style "textbutton_no_padding_highlight"
                                                text_style "serum_text_style"
                                                action [Function(purchase_policy, policy), ToggleScreenVariable("selected_policy", policy, None)]
                                                hovered SetScreenVariable("selected_tooltip", policy.desc)
                                                sensitive policy.requirement() and (policy.cost < mc.business.funds or policy.cost == mc.business.funds)
                                                xfill True
                                                ysize 100

                                        else:
                                            textbutton "$" + str(policy.cost) + " - " + policy.name:
                                                tooltip policy.desc
                                                style "textbutton_no_padding_highlight"
                                                text_style "serum_text_style"
                                                background "#666666"
                                                action [ToggleScreenVariable("selected_policy", policy, None)]
                                                hovered SetScreenVariable("selected_tooltip", policy.desc)
                                                sensitive True
                                                xfill True
                                                ysize 100



                    vbox:
                        # if tooltip:
                        if selected_tooltip is not None:
                            frame:
                                xfill True
                                ysize 100
                                viewport:
                                    scrollbars "vertical"
                                    draggable True
                                    mousewheel True
                                    vbox:
                                        text selected_tooltip style "serum_text_style" #tooltip
                        else:
                            frame: # A hidden frame to avoid things from moving around
                                background None
                                xfill True
                                ysize 100

                        if selected_policy is not None and (hasattr(selected_policy, "children") and selected_policy.children):
                            frame:
                                grid 1 len(selected_policy.children):
                                    for policy in sorted(sorted(sorted(selected_policy.children, key = lambda x: x.cost), key = lambda x: x.is_owned()), key = lambda x: x.requirement(), reverse = True):
                                        if policy.is_owned():

                                            textbutton "$" + str(policy.cost) + " - " + policy.name:
                                                tooltip policy.desc
                                                action NullAction()
                                                alternate [Function(policy.buy_policy, True), If(policy.refresh is not None, Function(renpy.call_in_new_context, policy.refresh))]
                                                hovered SetScreenVariable("selected_tooltip", policy.desc)
                                                style "textbutton_no_padding_highlight"
                                                xalign 0.5
                                                text_style "serum_text_style"
                                                background "#59853f"
                                                hover_background "#78b156"
                                                sensitive True
                                                xfill True
                                                ysize 100

                                        else:
                                            if policy.requirement() and (policy.cost <= mc.business.funds):
                                                textbutton "$" + str(policy.cost) + " - " + policy.name:
                                                    tooltip policy.desc
                                                    style "textbutton_no_padding_highlight"
                                                    text_style "serum_text_style"

                                                    action [Function(policy.buy_policy), If(policy.refresh is not None, Function(renpy.call_in_new_context, policy.refresh))]
                                                    alternate [Function(policy.buy_policy, True), If(policy.refresh is not None, Function(renpy.call_in_new_context, policy.refresh))]

                                                    hovered SetScreenVariable("selected_tooltip", policy.desc)
                                                    sensitive policy.requirement() and (policy.cost < mc.business.funds or policy.cost == mc.business.funds)
                                                    xfill True
                                                    ysize 100

                                            else:
                                                textbutton "$" + str(policy.cost) + " - " + policy.name:
                                                    tooltip policy.desc
                                                    style "textbutton_no_padding_highlight"
                                                    text_style "serum_text_style"
                                                    background "#666666"
                                                    action NullAction()
                                                    hovered SetScreenVariable("selected_tooltip", policy.desc)
                                                    sensitive True
                                                    xfill True
                                                    ysize 100
        frame:
            background None
            anchor [0.5,0.5]
            align [0.5,0.88]
            xysize [500,125]
            imagebutton:
                align [0.5,0.5]
                auto "gui/button/choice_%s_background.png"
                focus_mask "gui/button/choice_idle_background.png"
                action Return()
            textbutton "Return" align [0.5,0.5] text_style "return_button_style"

        imagebutton:
            auto "/tutorial_images/restart_tutorial_%s.png"
            xsize 54
            ysize 54
            yanchor 1.0
            xalign 0.0
            yalign 1.0
            action Function(mc.business.reset_tutorial,"policy_tutorial")

        $ policy_tutorial_length = 4 #The number of  tutorial screens we have.
        if mc.business.event_triggers_dict["policy_tutorial"] > 0 and mc.business.event_triggers_dict["policy_tutorial"] <= policy_tutorial_length: #We use negative numbers to symbolize the tutorial not being enabled
            imagebutton:
                auto
                sensitive True
                xsize 1920
                ysize 1080
                idle "/tutorial_images/policy_tutorial_"+__builtin__.str(mc.business.event_triggers_dict["policy_tutorial"])+".png"
                hover "/tutorial_images/policy_tutorial_"+__builtin__.str(mc.business.event_triggers_dict["policy_tutorial"])+".png"
                action Function(mc.business.advance_tutorial,"policy_tutorial")
