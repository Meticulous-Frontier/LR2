init 2: # Will give this a polish later, just wanted to enable categories from lists.
    screen policy_selection_screen():
        add "Paper_Background.png"
        modal True
        zorder 100
        $ tooltip = GetTooltip()

        $ categories = sorted(policy_selection_screen_categories) #This way we can append extra categories and lists with ease.

        default selected_category = categories[0] #Default to the first in our categories list
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
                                    action SetScreenVariable("selected_category", category)
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
                                for policy in sorted(selected_category[1], key = lambda x: x.cost):
                                    if policy.is_owned():

                                        textbutton "$" + str(policy.cost) + " - " + policy.name:
                                            tooltip policy.desc
                                            action NullAction()
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
                                                action Function(purchase_policy,policy)
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
                                                sensitive True
                                                xfill True
                                                ysize 100


                    if tooltip:
                        frame:
                            background "#1a45a1aa"
                            xfill True
                            text tooltip style "serum_text_style"

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
