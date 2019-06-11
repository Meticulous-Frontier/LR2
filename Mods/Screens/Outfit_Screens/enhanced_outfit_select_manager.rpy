init 2:
    #TODO: Solve the error when having used outfit_creator screen and abandoning design
    # We want it to just hide the outfit_creator and then display this screen again, not return out of screen.
    screen outfit_select_manager(slut_limit = 999, show_export = False, show_sets = False, show_overwear = True, show_underwear = True, show_outfits = True): ##Brings up a list of the players current saved outfits, returns the selected outfit or None.
    #If sluttiness_limit is passed, you cannot exit the creator until the proposed outfit has a sluttiness below it.

        if the_person is not None: # NOTE: Determine this here as the script.rpy does not use the mc.designed_wardrobe when calling screen by default
            $ target_wardrobe = the_person.wardrobe
        else:
            $ target_wardrobe = mc.designed_wardrobe

        add "Paper_Background.png"
        modal True
        zorder 99
        default preview_outfit = None
        default import_selection = False
        hbox:
            spacing 20
            xalign 0.1
            yalign 0.1
            if show_outfits:
                frame:
                    background "#888888"
                    xsize 450
                    ysize 750
                    hbox:
                        viewport:
                            scrollbars "vertical"
                            xsize 225
                            ysize 750
                            mousewheel True
                            vbox:
                                spacing 0
                                textbutton "Full Outfits" action NullAction() style "textbutton_style" text_style "textbutton_text_style" text_text_align 0.5 text_xalign 0.5 xsize 225 xanchor 0.0
                                null height 10
                                for outfit in mc.designed_wardrobe.get_outfit_list():
                                    #hbox:
                                    textbutton outfit.name+ "\n(Sluttiness " +str(outfit.slut_requirement) +")" action [Return(outfit.get_copy()), Hide("mannequin")] sensitive (outfit.slut_requirement <= slut_limit) hovered Show("mannequin", None, outfit) style "textbutton_style" text_style "outfit_description_style" xsize 410
                                    if show_export:
                                        default exported = []
                                        textbutton "Export to .xml File" action [Function(exported.append,outfit), Function(log_outfit, outfit, outfit_class = "FullSets", wardrobe_name = "Exported_Wardrobe"), Function(renpy.notify, "Outfit exported to Exported_Wardrobe.xml")] sensitive outfit not in exported hovered SetScreenVariable("preview_outfit", outfit.get_copy()) unhovered SetScreenVariable("preview_outfit", None) style "textbutton_style" text_style "outfit_description_style" xsize 410
                                    null height 15
                        vbox:
                            textbutton "Import Design" action ToggleScreenVariable("import_selection") style "textbutton_style" text_style "textbutton_text_style" text_text_align 0.5 text_xalign 0.5 xsize 225 xanchor 0.0
                            if import_selection:
                                viewport:
                                    scrollbars "vertical"
                                    mousewheel True
                                    ysize 750
                                    xsize 225
                                    vbox:
                                        for n in get_xml_files_from_path(["game/wardrobes/", "game/Mods/Wardrobes/"]):
                                            textbutton n action [Show("import_outfit_manager", None, target_wardrobe, n)] style "textbutton_style" text_style "textbutton_text_style" text_text_align 0.5 text_xalign 0.5 xanchor 0.0

            if show_sets:
                if show_overwear:
                    frame:
                        background "#888888"
                        xsize 450
                        ysize 750
                        viewport:
                            scrollbars "vertical"
                            xsize 450
                            ysize 750
                            mousewheel True
                            vbox:
                                spacing 0
                                text "Overwear Sets" style "menu_text_style" size 30
                                null height 10
                                for outfit in mc.designed_wardrobe.get_overwear_sets_list():
                                    #hbox:
                                    textbutton outfit.name+ "\n(Sluttiness " +str(outfit.get_overwear_slut_score()) +")" action [Return(outfit.get_copy()), Hide("mannequin")] sensitive (outfit.get_overwear_slut_score() <= slut_limit) hovered Show("mannequin", None, outfit) style "textbutton_style" text_style "outfit_description_style" xsize 410
                                    if show_export:
                                        default exported = []
                                        textbutton "Export to .xml File" action [Function(exported.append,outfit), Function(log_outfit, outfit, outfit_class = "OverwearSets", wardrobe_name = "Exported_Wardrobe"), Function(renpy.notify, "Outfit exported to Exported_Wardrobe.xml")] sensitive outfit not in exported hovered SetScreenVariable("preview_outfit", outfit.get_copy()) unhovered SetScreenVariable("preview_outfit", None) style "textbutton_style" text_style "outfit_description_style" xsize 410
                                    null height 15
                if show_underwear:
                    frame:
                        background "#888888"
                        xsize 450
                        ysize 750
                        viewport:
                            scrollbars "vertical"
                            xsize 450
                            ysize 750
                            mousewheel True
                            vbox:
                                spacing 0
                                text "Underwear Sets" style "menu_text_style" size 30
                                null height 10
                                for outfit in mc.designed_wardrobe.get_underwear_sets_list():
                                    #hbox:
                                    textbutton outfit.name+ "\n(Sluttiness " +str(outfit.get_underwear_slut_score()) +")" action [Return(outfit.get_copy()), Hide("mannequin")] sensitive (outfit.get_underwear_slut_score() <= slut_limit) hovered Show("mannequin", None, outfit) style "textbutton_style" text_style "outfit_description_style" xsize 410
                                    if show_export:
                                        default exported = []
                                        textbutton "Export to .xml File" action [Function(exported.append,outfit), Function(log_outfit, outfit, outfit_class = "UnderwearSets", wardrobe_name = "Exported_Wardrobe"), Function(renpy.notify, "Outfit exported to Exported_Wardrobe.xml")] sensitive outfit not in exported hovered SetScreenVariable("preview_outfit", outfit.get_copy()) unhovered SetScreenVariable("preview_outfit", None) style "textbutton_style" text_style "outfit_description_style" xsize 410
                                    null height 15



        frame:
            background None
            anchor [0.5,0.5]
            align [0.5,0.88]
            xysize [500,125]
            imagebutton:
                align [0.5,0.5]
                auto "gui/button/choice_%s_background.png"
                focus_mask "gui/button/choice_idle_background.png"
                action [Return("No Return"), Hide("mannequin")]
            textbutton "Return" align [0.5,0.5] text_style "return_button_style"
