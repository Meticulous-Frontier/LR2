init 2: # Will give this a polish later, just wanted to enable categories from lists.
    screen policy_selection_screen():
        add "Paper_Background.png"
        modal True
        zorder 100
        $ tooltip = GetTooltip()

        $ categories = sorted(policy_selection_screen_categories) #This way we can append extra categories and lists with ease.

        default selected_catagory = categories[0] #Default to the first in our categories list
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
                        text "Policy categories" style "serum_text_style"

                    viewport:

                        xfill True
                        draggable True
                        mousewheel "horizontal"

                        hbox: # Properly display categories
                            xfill True
                            for catagory in categories:
                                textbutton catagory[0]:
                                    ysize 80
                                    xsize 200
                                    xalign 0.5
                                    action SetScreenVariable("selected_catagory", catagory)
                                    sensitive selected_catagory != catagory
                                    style "textbutton_no_padding_highlight"
                                    text_style "serum_text_style"

            frame: #Holds the list of business policies. Needs to be scrollable.
                xsize 1320
                ysize 650
                background "#1a45a1aa"
                viewport:
                    mousewheel True
                    scrollbars "vertical"
                    xsize 800
                    ysize 650
                    vbox:
                        spacing 10
                        for policy in selected_catagory[1]:
                            if policy.is_owned():
                                textbutton "$" + str(policy.cost) + " - " + policy.name:
                                    tooltip policy.desc
                                    action NullAction()
                                    style "textbutton_no_padding_highlight"
                                    text_style "serum_text_style"
                                    background "#59853f"
                                    hover_background "#78b156"
                                    sensitive True
                                    xsize 800
                                    ysize 100
                            else:
                                if policy.requirement() and (policy.cost < mc.business.funds or policy.cost == mc.business.funds):
                                    textbutton "$" + str(policy.cost) + " - " + policy.name:
                                        tooltip policy.desc
                                        style "textbutton_no_padding_highlight"
                                        text_style "serum_text_style"
                                        action Function(purchase_policy,policy)
                                        sensitive policy.requirement() and (policy.cost < mc.business.funds or policy.cost == mc.business.funds)
                                        xsize 800
                                        ysize 100
                                else:
                                    textbutton "$" + str(policy.cost) + " - " + policy.name:
                                        tooltip policy.desc
                                        style "textbutton_no_padding_highlight"
                                        text_style "serum_text_style"
                                        background "#666666"
                                        action NullAction()
                                        sensitive True
                                        xsize 800
                                        ysize 100


        if tooltip:
            frame:
                background "#1a45a1aa"
                anchor [1.0,0.0]
                align [0.84,0.2]
                xsize 500
                text tooltip style "menu_text_style"

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
