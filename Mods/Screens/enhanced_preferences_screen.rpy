init 2: # Add some additional
    screen preferences():

        tag menu
        if renpy.mobile:
            $ cols = 2
        else:
            $ cols = 4

        use game_menu(_("Preferences"), scroll="viewport"):

            vbox:

                hbox:
                    box_wrap True

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

                    if not renpy.mobile: #Animations are always disabled on mobile.
                        vbox:
                            style_prefix "radio"
                            label "Animation"
                            textbutton "Enable" action SetField(persistent, "vren_animation", True)
                            textbutton "Disable" action SetField(persistent, "vren_animation", False)

                    vbox:
                        style_prefix "check"
                        label "Text Style"
                        textbutton "{i}Italic{/i}" action [ToggleField(style.get("textbutton_text_style"), "italic", True, False), Function(style.rebuild)]
                        textbutton "{b}Bold{/b}" action [ToggleField(style.get("textbutton_text_style"), "bold", True, False), Function(style.rebuild)]
                        label "Text Size"
                        hbox: # Wanted to use a bar for this but ran into a paradox.
                            textbutton "18" action [SetField(style.get("textbutton_text_style"), "size", 18), Function(style.rebuild)]
                            textbutton "20" action [SetField(style.get("textbutton_text_style"), "size", 20), Function(style.rebuild)]
                            textbutton "22" action [SetField(style.get("textbutton_text_style"), "size", 22), Function(style.rebuild)]
                            textbutton "24" action [SetField(style.get("textbutton_text_style"), "size", 24), Function(style.rebuild)]
                            textbutton "26" action [SetField(style.get("textbutton_text_style"), "size", 26), Function(style.rebuild)]
                        #bar value FieldValue(style.get("textbutton_text_style"), "size", range = 50, step = 2, force_step = True) changed style.rebuild #action SetField(style.get("textbutton_text_style"), "size")
                        #textbutton "Text Size:" + str(style.get("textbutton_text_style").size) action NullAction() #[SetField(style.get("textbutton_text_style"), "size", 1)), Function(style.rebuild)]

                    if not renpy.mobile: #High Memory mode is always disabled on mobile.
                        vbox:
                            style_prefix "radio"
                            label "Memory Mode" 
                            textbutton "High":
                                sensitive True
                                tooltip "Allows the game to use a lot more memory for caching images, allowing for smoother menu's and transitions. Requires Restart to take effect."
                                action [
                                    SetField(persistent, "high_memory_mode", True),
                                    Function(renpy.reload_script)
                                ]
                            textbutton "Low":
                                sensitive True
                                tooltip "The game uses a lot less memory for caching images, recommended on low memory devices. Requires Restart to take effect."
                                action [
                                    SetField(persistent, "high_memory_mode", False),
                                    Function(renpy.reload_script)
                                ]


                    ## Additional vboxes of type "radio_pref" or "check_pref" can be
                    ## added here, to add additional creator-defined preferences.

                null height (4 * gui.pref_spacing)

                hbox:
                    style_prefix "slider"
                    box_wrap True

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
