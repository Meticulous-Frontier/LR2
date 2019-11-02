# Allows you to preview and select singular items from an XML file before importing.

init 2 python:
    def add_outfit(wardrobe, the_outfit, outfit_type = "full"):
            if outfit_type == "under":
                wardrobe.add_underwear_set(the_outfit)
            elif outfit_type == "over":
                wardrobe.add_overwear_set(the_outfit)
            else: #outfit_type = full
                wardrobe.add_outfit(the_outfit)

    def selected_xml_wardrobe(target_wardrobe, xml_filename): # TODO: Use this instead -> Show("import_outfit_manager", None, target_wardrobe, n)
        renpy.show_screen("import_outfit_manager", target_wardrobe, xml_filename)
    def selected_xml_clothing(outfit):
        renpy.show_screen("outfit_creator", outfit.get_copy())

init 2:
    screen import_outfit_manager(target_wardrobe, xml_filename, slut_limit = 999, show_export = True, show_sets = True, show_overwear = True, show_underwear = True, show_outfits = True): ##Brings up a list of the players current saved outfits, returns the selected outfit or None.
        $ wardrobe = wardrobe_from_xml(xml_filename)
        add "Paper_Background.png"
        modal True
        zorder 101
        default preview_outfit = None
        hbox:
            spacing 20
            xalign 0.1
            yalign 0.1
            if show_outfits:
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
                            text "Full Outfits" style "menu_text_style" size 30
                            null height 10
                            for outfit in wardrobe.get_outfit_list():
                                #hbox:
                                textbutton outfit.name+ "\n(Sluttiness " +str(outfit.slut_requirement) +")" action [Show("outfit_creator", None, outfit.get_copy(), target_wardrobe, outfit_type = "full"), Hide("import_outfit_manager")] sensitive (outfit.slut_requirement <= slut_limit) hovered Show("mannequin", None, outfit) style "textbutton_style" text_style "outfit_description_style" xsize 410
                                if show_export:
                                    default exported = []
                                    textbutton "Export to .xml File" action [Function(exported.append,outfit), Function(log_outfit, outfit, outfit_class = "FullSets", wardrobe_name = "Exported_Wardrobe"), Function(renpy.notify, "Outfit exported to Exported_Wardrobe.xml")] sensitive outfit not in exported style "textbutton_style" text_style "outfit_description_style" xsize 410
                                    textbutton "Import to wardrobe: [target_wardrobe.name]" action [Function(add_outfit, target_wardrobe, outfit, outfit_type = "full"), Function(renpy.notify, "Outfit imported")] sensitive not target_wardrobe.has_outfit_with_name(outfit.name) style "textbutton_style" text_style "outfit_description_style" xsize 410

                                null height 15

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
                                for outfit in wardrobe.get_overwear_sets_list():
                                    #hbox:
                                    textbutton outfit.name+ "\n(Sluttiness " +str(outfit.get_overwear_slut_score()) +")" action [Show("outfit_creator", None, outfit.get_copy(), target_wardrobe, outfit_type = "over"), Hide("import_outfit_manager")] sensitive (outfit.get_overwear_slut_score() <= slut_limit) hovered Show("mannequin", None, outfit) style "textbutton_style" text_style "outfit_description_style" xsize 410
                                    if show_export:
                                        default exported = []
                                        textbutton "Export to .xml File" action [Function(exported.append,outfit), Function(log_outfit, outfit, outfit_class = "OverwearSets", wardrobe_name = "Exported_Wardrobe"), Function(renpy.notify, "Outfit exported to Exported_Wardrobe.xml")] sensitive outfit not in exported  style "textbutton_style" text_style "outfit_description_style" xsize 410
                                        textbutton "Import to wardrobe: [target_wardrobe.name]" action [Function(add_outfit, target_wardrobe, outfit, outfit_type = "over"), Function(renpy.notify, "Outfit imported")] sensitive not target_wardrobe.has_outfit_with_name(outfit.name) style "textbutton_style" text_style "outfit_description_style" xsize 410
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
                                for outfit in wardrobe.get_underwear_sets_list():
                                    #hbox:
                                    textbutton outfit.name+ "\n(Sluttiness " +str(outfit.get_underwear_slut_score()) +")" action [Show("outfit_creator", None, outfit.get_copy(), target_wardrobe, outfit_type = "under"), Hide("import_outfit_manager")] sensitive (outfit.get_underwear_slut_score() <= slut_limit) hovered Show("mannequin", None, outfit) style "textbutton_style" text_style "outfit_description_style" xsize 410
                                    if show_export:
                                        default exported = []
                                        textbutton "Export to .xml File" action [Function(exported.append,outfit), Function(log_outfit, outfit, outfit_class = "UnderwearSets", wardrobe_name = "Exported_Wardrobe"), Function(renpy.notify, "Outfit exported to Exported_Wardrobe.xml")] sensitive outfit not in exported hovered SetScreenVariable("preview_outfit", outfit.get_copy()) unhovered SetScreenVariable("preview_outfit", None) style "textbutton_style" text_style "outfit_description_style" xsize 410
                                        textbutton "Import to wardrobe: [target_wardrobe.name]" action [Function(add_outfit, target_wardrobe, outfit, outfit_type = "under"), Function(renpy.notify, "Outfit imported")] sensitive not target_wardrobe.has_outfit_with_name(outfit.name) style "textbutton_style" text_style "outfit_description_style" xsize 410
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
                action Hide("import_outfit_manager")
            textbutton "Return" align [0.5,0.5] text_style "return_button_style"
