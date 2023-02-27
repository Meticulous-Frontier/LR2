init 2: # Add some additional
    style pref_label_text:
        yalign 1.0
        size 26

    style radio_button_text is gui_button_text:
        size 22

    style check_button_text is gui_button_text:
        size 22

    screen preferences():

        tag menu
        use game_menu(_("Preferences"), scroll="viewport"):

            frame:
                background "#000000aa"
                xalign 0.5
                xanchor 0.5
                padding (20, 20)
                vbox:
                    hbox:
                        spacing 20
                        if renpy.variant("pc"):
                            vbox:
                                style_prefix "radio"
                                label _("Display")
                                textbutton _("Window") action Preference("display", "window")
                                textbutton _("Fullscreen") action Preference("display", "fullscreen")

                        vbox:
                            style_prefix "radio"
                            label _("Rollback Side")
                            textbutton _("Disable") action Preference("rollback side", "disable")
                            textbutton _("Left") action Preference("rollback side", "left")
                            textbutton _("Right") action Preference("rollback side", "right")

                        vbox:
                            style_prefix "check"
                            label _("Skip")
                            textbutton _("Unseen Text") action Preference("skip", "toggle")
                            textbutton _("After Choices") action Preference("after choices", "toggle")
                            textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                    null height (2 * gui.pref_spacing)

                    hbox:
                        spacing 20

                        vbox:
                            style_prefix "radio"
                            label "Pregnancy Settings"
                            textbutton "Disabled" action SetField(persistent, "pregnancy_pref", 0)
                            textbutton "Predictable" action SetField(persistent, "pregnancy_pref", 1)
                            textbutton "Semi Realistic" action SetField(persistent, "pregnancy_pref", 2)
                            textbutton "Realistic" action SetField(persistent, "pregnancy_pref", 3)

                        vbox:
                            style_prefix "radio"
                            label "Embedded NTR"
                            textbutton "Enabled":
                                sensitive True
                                tooltip "Enables NTR like scenarios in events, that are not NTR events by default."
                                action [
                                    SetField(persistent, "show_ntr", True)
                                ]
                            textbutton "Disabled":
                                sensitive True
                                tooltip "Disables NTR like scenarios in events, that are not NTR events by default."
                                action [
                                    SetField(persistent, "show_ntr", False)
                                ]

                        vbox:
                            style_prefix "radio"
                            label "Always Ask Condom"
                            textbutton "Enabled":
                                sensitive True
                                tooltip "The condom dialog will always be triggered during sex scenes."
                                action [
                                    SetField(persistent, "always_ask_condom", True)
                                ]
                            textbutton "Disabled":
                                sensitive True
                                tooltip "When a girl is slutty enough, the condom dialog will be skipped."
                                action [
                                    SetField(persistent, "always_ask_condom", False)
                                ]

                    null height (2 * gui.pref_spacing)

                    hbox:
                        spacing 20

                        vbox:
                            style_prefix "radio"
                            label "MC Non Consent"
                            textbutton "Disabled" action SetField(persistent, "mc_noncon_pref", 0)
                            textbutton "Roleplay" action SetField(persistent, "mc_noncon_pref", 1)
                            textbutton "Enabled" action SetField(persistent, "mc_noncon_pref", 2)

                        vbox:
                            style_prefix "check"
                            label "In Game Notifications"
                            textbutton "Serum Related" action [ToggleField(persistent, "serum_messages", True, False)]
                            textbutton "Clarity Related" action [ToggleField(persistent, "clarity_messages", True, False)]
                            textbutton "Stat Changes" action [ToggleField(persistent, "stat_change_messages", True, False)]
                            textbutton "Skill Changes" action [ToggleField(persistent, "skill_change_messages", True, False)]
                            textbutton "Energy Changes" action [ToggleField(persistent, "energy_messages", True, False)]


                    null height (2 * gui.pref_spacing)

                    hbox:
                        spacing 20

                        vbox:
                            style_prefix "check"
                            label "Text Style"
                            textbutton "{i}Italic{/i}" action [ToggleField(style.get("textbutton_text_style"), "italic", True, False), Function(style.rebuild)]
                            textbutton "{b}Bold{/b}" action [ToggleField(style.get("textbutton_text_style"), "bold", True, False), Function(style.rebuild)]
                            label "Text Effects"
                            textbutton "All Effects" action [ToggleField(persistent, "text_effects", True, False)]

                        vbox:
                            style_prefix "check"
                            label "Visualization"
                            textbutton "Show Character Portrait" action [ToggleField(persistent, "show_portrait", True, False)] text_size 24
                            textbutton "Show Detailed Goals" action [ToggleField(persistent, "show_goal_ui", True, False)] text_size 24
                            label "Dialog Opacity" text_size 18
                            bar value FieldValue(persistent, 'say_window_alpha', 1.0, max_is_zero=False, offset=0, step=.1) ysize 20 xsize 300
                            label "Hud Opacity" text_size 18
                            bar value FieldValue(persistent, 'hud_alpha', 1.0, max_is_zero=False, offset=0, step=.1) ysize 20 xsize 300


                        # vbox:
                        #     style_prefix "radio"
                        #     label "Clean Memory"
                        #     textbutton "Every Time Slot":
                        #         sensitive True
                        #         tooltip "Every time slot call the renpy.free_memory() function, to prevent memory errors."
                        #         action [
                        #             SetField(persistent, "clear_memory_mode", 0)
                        #         ]
                        #     textbutton "Each Game Day":
                        #         sensitive True
                        #         tooltip "Daily call the renpy.free_memory() function, to prevent memory errors."
                        #         action [
                        #             SetField(persistent, "clear_memory_mode", 1)
                        #         ]


                        # if not renpy.mobile: #High Memory mode is always disabled on mobile and free_memory is called daily.
                        #     vbox:
                        #         style_prefix "radio"
                        #         label "Memory Mode"
                        #         textbutton "High":
                        #             sensitive True
                        #             tooltip "Allows the game to use a lot more memory for caching images, allowing for smoother menu's and transitions. Requires Restart to take effect."
                        #             action [
                        #                 SetField(persistent, "memory_mode", 2),
                        #                 Function(renpy.full_restart)
                        #             ]
                        #         textbutton "Medium":
                        #             sensitive True
                        #             tooltip "Allows the game to use a normal amount if memory for caching images, allowing for smoother menu's and transitions. Requires Restart to take effect."
                        #             action [
                        #                 SetField(persistent, "memory_mode", 1),
                        #                 Function(renpy.full_restart)
                        #             ]
                        #         textbutton "Low":
                        #             sensitive True
                        #             tooltip "The game uses a lot less memory for caching images, recommended on low memory devices. Requires Restart to take effect."
                        #             action [
                        #                 SetField(persistent, "memory_mode", 0),
                        #                 Function(renpy.full_restart)
                        #             ]
                        #     if persistent.memory_mode > 1:
                        #         vbox:
                        #             style_prefix "radio"
                        #             label "Clean Memory"
                        #             textbutton "Once Game Week":
                        #                 sensitive True
                        #                 tooltip "Weekly call the renpy.free_memory() function, to prevent memory errors."
                        #                 action [
                        #                     SetField(persistent, "use_free_memory", False)
                        #                 ]
                        #             textbutton "Each Game Day":
                        #                 sensitive True
                        #                 tooltip "Daily call the renpy.free_memory() function, to prevent memory errors."
                        #                 action [
                        #                     SetField(persistent, "use_free_memory", True)
                        #                 ]


                        ## Additional vboxes of type "radio_pref" or "check_pref" can be
                        ## added here, to add additional creator-defined preferences.

                    null height (2 * gui.pref_spacing)

                    hbox:
                        spacing 20

                        if not (renpy.android or renpy.mobile): #Animations are always disabled on mobile.
                            vbox:
                                style_prefix "radio"
                                label "Animation"
                                textbutton "Enable" action SetField(persistent, "vren_animation", True)
                                textbutton "Disable" action SetField(persistent, "vren_animation", False)

                        vbox:
                            style_prefix "radio"
                            label "Character Background"
                            textbutton "Aura" action SetField(persistent, "vren_display_pref", "Float")
                            textbutton "None" action SetField(persistent, "vren_display_pref", "None")

                        vbox:
                            style_prefix "check"
                            label "Misc [[Requires Restart]"
                            textbutton "Cache Images on Startup" action [ToggleField(persistent, "zip_cache_preload", True, False)]
                            textbutton "Empty Wardrobe for Random Girls" action [ToggleField(persistent, "low_memory_wardrobes", True, False)]
                            textbutton "Keep Patreon Characters" action [ToggleField(persistent, "keep_patreon_characters", True, False)]

                    null height (2 * gui.pref_spacing)

                    hbox:
                        spacing 20
                        style_prefix "slider"

                        vbox:

                            label _("Text Speed")

                            bar value Preference("text speed")

                            label _("Auto-Forward Time")

                            bar value Preference("auto-forward time")

                        vbox:

                            if config.has_music:
                                label _("Music Volume")

                                hbox:
                                    bar value Preference("music volume")

                            if config.has_sound:

                                label _("Sound Volume")

                                hbox:
                                    bar value Preference("sound volume")

                                    if config.sample_sound:
                                        textbutton _("Test") action Play("sound", config.sample_sound)


                            if config.has_voice:
                                label _("Voice Volume")

                                hbox:
                                    bar value Preference("voice volume")

                                    if config.sample_voice:
                                        textbutton _("Test") action Play("voice", config.sample_voice)

                            if config.has_music or config.has_sound or config.has_voice:
                                null height gui.pref_spacing

                                textbutton _("Mute All"):
                                    action Preference("all mute", "toggle")
                                    style "mute_all_button"
