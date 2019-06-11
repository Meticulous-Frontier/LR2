init 3:
    # NOTE: Uses seperate mannequin screen and has no real use of the "preview_outfit" Outfit
    # Thinking of adding "Import" directly from this screen as well, but seems redundant.
    # Added the ability enter outfit editor by right clicking an outfit. Needs changes to script.rpy to work as intended. Reason: Easy to edit company wardrobe by entering the Remove an Outfit section and review / edit them from there.

    screen outfit_delete_manager(target_wardrobe): ##This screen is used and shared for MC, Company Uniforms and Person. Script.rpy should be calling correct Wardrobe at all times so no default currently needed. NOTE: Script.rpy does not support editing of outfits by default from this screen, but slight additions to it will make it work. Tested. Will propose the change to Vren at later time, pretty much copy paste from different section.
        add "Paper_Background.png"
        modal True
        zorder 99
        default preview_outfit = None
        hbox:
            spacing 20
            xalign 0.1
            yalign 0.1
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
                        text "Full Outfits" style "menu_text_style" size 30
                        for outfit in target_wardrobe.get_outfit_list():
                            default exported = []
                            textbutton "Delete "+outfit.name+ "\n(Sluttiness " +str(outfit.slut_requirement) +")" action [Function(target_wardrobe.remove_outfit,outfit)] hovered Show("mannequin", None, outfit) sensitive True alternate Show("outfit_creator", None, outfit.get_copy(), target_wardrobe) style "textbutton_style" text_style "outfit_description_style" xsize 210
                            textbutton "Export to .xml File" action [Function(exported.append,outfit), Function(log_outfit, outfit, outfit_class = "FullSets", wardrobe_name = "Exported_Wardrobe"), Function(renpy.notify, "Outfit exported to Exported_Wardrobe.xml")] sensitive outfit not in exported hovered SetScreenVariable("preview_outfit", outfit.get_copy()) unhovered SetScreenVariable("preview_outfit", None) style "textbutton_style" text_style "outfit_description_style" xsize 210

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
                        text "Overwear Sets" style "menu_text_style" size 30
                        for outfit in target_wardrobe.get_overwear_sets_list():
                            textbutton "Delete "+outfit.name+ "\n(Sluttiness " +str(outfit.get_overwear_slut_score()) +")" action [Function(target_wardrobe.remove_outfit,outfit)] hovered Show("mannequin", None, outfit) sensitive True alternate Show("outfit_creator", None, outfit.get_copy(), target_wardrobe) style "textbutton_style" text_style "outfit_description_style" xsize 210
                            default exported = []
                            textbutton "Export to .xml File" action [Function(exported.append,outfit), Function(log_outfit, outfit, outfit_class = "OverwearSets", wardrobe_name = "Exported_Wardrobe"), Function(renpy.notify, "Outfit exported to Exported_Wardrobe.xml")] sensitive outfit not in exported hovered SetScreenVariable("preview_outfit", outfit.get_copy()) unhovered SetScreenVariable("preview_outfit", None) style "textbutton_style" text_style "outfit_description_style" xsize 210
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
                        text "Underwear Sets" style "menu_text_style" size 30
                        for outfit in target_wardrobe.get_underwear_sets_list():
                            textbutton "Delete "+outfit.name+ "\n(Sluttiness " +str(outfit.get_underwear_slut_score()) +")" action [Function(target_wardrobe.remove_outfit,outfit)] hovered Show("mannequin", None, outfit) sensitive True alternate Show("outfit_creator", None, outfit.get_copy(), target_wardrobe) style "textbutton_style" text_style "outfit_description_style" xsize 210
                            default exported = []
                            textbutton "Export to .xml File" action [Function(exported.append,outfit), Function(log_outfit, outfit, outfit_class = "UnderwearSets", wardrobe_name = "Exported_Wardrobe"), Function(renpy.notify, "Outfit exported to Exported_Wardrobe.xml")] sensitive outfit not in exported hovered SetScreenVariable("preview_outfit", outfit.get_copy()) unhovered SetScreenVariable("preview_outfit", None) style "textbutton_style" text_style "outfit_description_style" xsize 210


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
