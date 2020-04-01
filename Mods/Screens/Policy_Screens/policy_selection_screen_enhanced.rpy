init 2 python:

    def get_from_policy_list(policy):

        persistent_policy = find_in_list(lambda x: x.name == policy.name, mc.business.policy_list)
        if not persistent_policy:
            return False
        return persistent_policy

    def format_policy_name(policy):
        if policy.cost <= mc.business.funds:
            policy_cost = "$" + str(policy.cost) + " - "
        else:
            policy_cost = "$" + str(policy.cost) + " - "

        if not policy.is_owned():
            if not (policy.requirement() and (policy.cost <= mc.business.funds)):
                policy_name = policy_cost + policy.name
            policy_name = "Purchase: " + policy_cost + policy.name
        else:
            policy_name = policy.name
        if policy.is_active() and policy.toggleable:
            policy_name += "\n[[Active]"
            blocking_policies = [a_policy for a_policy in policy.depender_policies if a_policy.is_active()]
            if blocking_policies:
                policy_name += "\n{size=12}Required for: "
            for requirement in blocking_policies:
                policy_name += requirement.name
                if requirement is not blocking_policies[-1]:
                    policy_name += ","
                policy_name += "{/size}"
        elif policy.is_owned() and policy.toggleable:
            policy_name += "\n[[Disabled]"



        return policy_name

init 2: # Will give this a polish later, just wanted to enable categories from lists.
    screen policy_selection_screen():
        add "Paper_Background.png"
        modal True
        zorder 49
        $ tooltip = GetTooltip()

        $ categories = sorted(policy_selection_screen_categories) #This way we can append extra categories and lists with ease.


        default hovered_enough_time = False
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

            frame: #Holds the list of business policies, that do not depend on other policies (parent policy). Needs to be scrollable. Child policies of the parent are displayed
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
                            if len([policy for policy in selected_category[1] if not policy.dependant_policies]) > 5: #Only take up scrollbar space if needed.
                                 scrollbars "vertical"
                            xfill True
                            #yfill True

                            grid 1 len([policy for policy in selected_category[1] if not policy.dependant_policies]): # Filter out any non- parent Policies
                                for policy in sorted(sorted(selected_category[1], key = lambda x: x.cost), key = lambda x: x.requirement(), reverse = True):
                                    if not policy.dependant_policies:


                                        textbutton format_policy_name(policy):
                                            tooltip policy.desc
                                            if selected_policy != policy: # TODO: Make diagnoal hovers less tedious, use a timer?
                                                hovered [ToggleScreenVariable("selected_policy", policy, None)]
                                            style "textbutton_no_padding_highlight"
                                            xalign 0.5
                                            text_style "serum_text_style"
                                            sensitive True
                                            xfill True
                                            ysize 100
                                            action NullAction()
                                            if policy.is_owned():
                                                background "#59853f"
                                                hover_background "#a9d59f"
                                                insensitive_background "#222222"

                                                if policy.is_toggleable():
                                                    action Function(toggle_policy, policy)
                                            else:
                                                if policy.requirement() and (policy.cost <= mc.business.funds):
                                                    background "#000080"
                                                    action Function(purchase_policy, policy)
                                                else:
                                                    background "#000040"
                                                hover_background "#1a45a1"
                                                insensitive_background "#222222"



                    if (selected_policy is not None and selected_policy.depender_policies):
                        vbox:
                            frame:
                                viewport:
                                    mousewheel True
                                    if len(selected_policy.depender_policies) > 5: #Only take up scrollbar space if needed.
                                         scrollbars "vertical"
                                    xfill True

                                    grid 1 len(selected_policy.depender_policies):
                                        for policy in sorted(sorted(selected_policy.depender_policies, key = lambda x: x.cost), key = lambda x: x.requirement(), reverse = True):
                                            textbutton format_policy_name(policy):
                                                tooltip policy.desc
                                                style "textbutton_no_padding_highlight"
                                                xalign 0.5
                                                text_style "serum_text_style"
                                                sensitive True
                                                xfill True
                                                ysize 100
                                                action NullAction()
                                                if policy.is_owned():
                                                    background "#59853f"
                                                    hover_background "#a9d59f"
                                                    insensitive_background "#222222"

                                                    if policy.is_toggleable():
                                                        action Function(toggle_policy, policy)
                                                else:
                                                    if policy.requirement() and (policy.cost <= mc.business.funds):
                                                        background "#000080"
                                                        action Function(purchase_policy, policy)
                                                    else:
                                                        background "#000040"
                                                    hover_background "#1a45a1"
                                                    insensitive_background "#222222"

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
