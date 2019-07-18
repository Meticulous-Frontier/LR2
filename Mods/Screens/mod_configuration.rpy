init -1 python:
    def get_mod_category_list():
        cat_list = []
        for mod in action_mod_list:
            if not mod.category in cat_list:
                cat_list.append(mod.category)
        cat_list.sort()
        return cat_list

init 2:
    screen mod_configuration_ui: #How you select serum and trait research
        $ categories = get_mod_category_list()

        add "Science_Menu_Background.png"
        modal True
        frame:
            background "#888888"
            xalign 0.5
            xsize 1200
            yalign 0.5
            ysize 900
            hbox:
                spacing 20
                vbox:
                    spacing 5
                    frame:
                        background "#000080"
                        xsize 380
                        text "Crisis Events" style "serum_text_style"

                    viewport:
                        xsize 380
                        ysize 780
                        scrollbars "vertical"
                        mousewheel True
                        vbox:
                            xsize 370
                            for category in categories:
                                frame:
                                    background "#000080"
                                    xsize 360
                                    text category style "serum_text_style_header"

                                for mod in sorted(action_mod_list, key = lambda x: x.name):
                                    if mod.category == category and mod.allow_disable == True:
                                        $ name = mod.name.split('{')[0]
                                        textbutton "[name] {size=16}" + ("{color=#007000}Enabled" if mod.enabled else "{color=#930000}Disabled"):
                                            style "textbutton_style"
                                            text_style "serum_text_style_traits"
                                            tooltip mod.menu_tooltip
                                            action [Function(mod.toggle_enabled)]
                                            xsize 360

                vbox:
                    spacing 5
                    frame:
                        background "#000080"
                        xsize 380
                        text "Serum Traits" style "serum_text_style"

                    viewport:
                        xsize 380
                        ysize 780
                        scrollbars "vertical"
                        mousewheel True
                        vbox:
                            xsize 370
                            for i in range(1, 4):
                                frame:
                                    background "#000080"
                                    xsize 360
                                    text "Research Tier: [i]" style "serum_text_style_header"

                                for mod in sorted(serum_mod_list, key = lambda x: x.name):
                                    if mod.tier == i:
                                        textbutton "[mod.name] {size=16}" + ("{color=#007000}Enabled" if mod.enabled else "{color=#930000}Disabled"):
                                            style "textbutton_style"
                                            text_style "serum_text_style_traits"
                                            tooltip mod.desc
                                            action [Function(mod.toggle_enabled)]
                                            xsize 360
                # vbox:
                #     spacing 5
                #     frame:
                #         background "#000080"
                #         xsize 380
                #         text "Generic People Role" style "serum_text_style"
                #
                #     viewport:
                #         xsize 380
                #         ysize 780
                #         scrollbars "vertical"
                #         mousewheel True
                #         vbox:
                #             xsize 370
                #             textbutton "Change Schedule {size=16}" + ("{color=#007000}Enabled" if store.generic_people_role_change_schedule else "{color=#930000}Disabled"):
                #                 style "textbutton_style"
                #                 text_style "serum_text_style_traits"
                #                 action [Function(turn_generic_people_role_feature_on_or_off, "generic_people_role_change_schedule")]
                #                 tooltip "Schedule where the person should be throughout the day."
                #                 xsize 360
                #             textbutton "Follow You {size=16}" + ("{color=#007000}Enabled" if store.generic_people_role_follow else "{color=#930000}Disabled"):
                #                 style "textbutton_style"
                #                 text_style "serum_text_style_traits"
                #                 action [Function(turn_generic_people_role_feature_on_or_off, "generic_people_role_follow")]
                #                 tooltip "Tell a person to follow you where ever you go, until you tell them to stop following you."
                #                 xsize 360
                #             textbutton "Hire Person {size=16}" + ("{color=#007000}Enabled" if store.generic_people_role_hire_person else "{color=#930000}Disabled"):
                #                 style "textbutton_style"
                #                 text_style "serum_text_style_traits"
                #                 action [Function(turn_generic_people_role_feature_on_or_off, "generic_people_role_hire_person")]
                #                 tooltip "Hire a person to work for you."
                #                 xsize 360
                #             textbutton "Pay to Strip {size=16}" + ("{color=#007000}Enabled" if store.generic_people_role_pay_to_strip else "{color=#930000}Disabled"):
                #                 style "textbutton_style"
                #                 text_style "serum_text_style_traits"
                #                 action [Function(turn_generic_people_role_feature_on_or_off, "generic_people_role_pay_to_strip")]
                #                 tooltip "Pay someone to strip for you."
                #                 xsize 360
                #             textbutton "Rename Person {size=16}" + ("{color=#007000}Enabled" if store.generic_people_role_rename_person else "{color=#930000}Disabled"):
                #                 style "textbutton_style"
                #                 text_style "serum_text_style_traits"
                #                 action [Function(turn_generic_people_role_feature_on_or_off, "generic_people_role_rename_person")]
                #                 tooltip "Change the name of the person."
                #                 xsize 360
                #             textbutton "Spend the Night {size=16}" + ("{color=#007000}Enabled" if store.generic_people_role_spend_night else "{color=#930000}Disabled"):
                #                 style "textbutton_style"
                #                 text_style "serum_text_style_traits"
                #                 action [Function(turn_generic_people_role_feature_on_or_off, "generic_people_role_spend_night")]
                #                 tooltip "Spend the night together."
                #                 xsize 360

        textbutton "Close" action [Return()] style "textbutton_style" text_style "serum_text_style" yalign 0.91 xanchor 0.5 xalign 0.5
