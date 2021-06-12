# Allows you to preview and select singular items from an XML file before importing.

init 2 python:
    def import_add_outfit(wardrobe, the_outfit, outfit_type = "full"):
        if not wardrobe.has_outfit_with_name(the_outfit.name):
            if outfit_type == "under":
                wardrobe.add_underwear_set(the_outfit)
            elif outfit_type == "over":
                wardrobe.add_overwear_set(the_outfit)
            else: #outfit_type = full
                wardrobe.add_outfit(the_outfit)
        return

    def import_add_outfit_to_wardrobes(list_of_wardrobes, the_outfit, outfit_type = "full"): #Adds the outfit to every wardrobe in the list of wardrobes passed to it
        for wardrobe in list_of_wardrobes:
            import_add_outfit(wardrobe, the_outfit, outfit_type)
        return

    def import_remove_outfit_from_wardrobes(list_of_wardrobes, the_outfit):
        for wardrobe in list_of_wardrobes:
            if import_wardrobes_has_outfit_with_name(list_of_wardrobes, the_outfit.name):
                wardrobe.remove_outfit(the_outfit)

    def import_wardrobes_has_outfit_with_name(list_of_wardrobes, the_name): # Check if every Wardrobe in the list has the outfit already
        count = 0
        for wardrobe in list_of_wardrobes:
            for checked_outfit in wardrobe.all_outfits:
                if checked_outfit.name == the_name:
                    count += 1
        if count == __builtin__.len(list_of_wardrobes):
            return True
        else:
            return False

    def get_wardrobe_name_for_outfit_with_name(import_wardrobes, the_name):
        count = 0
        found_in = []
        for wardrobes in sorted(import_wardrobes):
            if import_wardrobes_has_outfit_with_name(import_wardrobes[wardrobes], the_name):
                found_in.append(wardrobes.split(" ")[0])
                count+=1
        if count > 0:
            return "-".join(found_in)
        elif count == __builtin__.len(import_wardrobes):
            return "All"
        return ""

    def calculate_outfit_slut_score(wardrobe, outfit):
        if outfit in wardrobe.outfits:
            return outfit.get_full_outfit_slut_score()
        elif outfit in wardrobe.overwear_sets:
            return outfit.get_overwear_slut_score()
        return outfit.get_underwear_slut_score()

    def selected_xml_wardrobe(target_wardrobe, xml_filename): # TODO: Use this instead -> Show("import_outfit_manager", None, target_wardrobe, n)
        renpy.show_screen("import_outfit_manager", target_wardrobe, xml_filename)
    def selected_xml_clothing(outfit):
        renpy.show_screen("outfit_creator", outfit.get_copy())

    def get_default_import_wardrobes(slut_limit):
        import_wardrobes = {}
        if slut_limit is None: # If slut_limit is None then add any and all options

            import_wardrobes["Player Wardrobe"] = [mc.designed_wardrobe]
            import_wardrobes["Slaves"] = [x.wardrobe for x in people_in_role(slave_role)]

        import_wardrobes["Marketing Division"] = [mc.business.m_uniform]
        import_wardrobes["Research Division"] = [mc.business.r_uniform]
        import_wardrobes["Production Division"] = [mc.business.p_uniform]
        import_wardrobes["Supply Division"] = [mc.business.s_uniform]
        import_wardrobes["HR Division"] = [mc.business.h_uniform]
        import_wardrobes["All Division"] = [mc.business.all_uniform]
        return import_wardrobes

    def get_strip_club_import_wardrobes():
        import_wardrobes = {}
        import_wardrobes["Player Wardrobe"] = [mc.designed_wardrobe]
        import_wardrobes["All Strip Club Outfits"] = [mc.business.stripclub_wardrobe]
        import_wardrobes["Strippers"] = [mc.business.stripper_wardrobe]
        import_wardrobes["Waitresses"] = [mc.business.waitress_wardrobe]
        import_wardrobes["Manager"] = [mc.business.manager_wardrobe]
        import_wardrobes["Mistress"] = [mc.business.mistress_wardrobe]
        import_wardrobes["BDSM performers"] = [mc.business.bdsm_wardrobe]
        return import_wardrobes

init 2:
    screen import_outfit_manager(target_wardrobe, xml_filename = None, show_export = True, slut_limit = None, underwear_limit = None, use_strip_club_wardrobe = False, outfit_type = None): ##Brings up a list of the players current saved outfits, returns the selected outfit or None.

        default outfit_categories = {"Full": ["FullSets", "full", "get_outfit_list"], "Overwear": ["OverwearSets", "over", "get_overwear_sets_list"], "Underwear": ["UnderwearSets", "under", "get_underwear_sets_list"]} #NOTE: Key is display name, [0] is XML's category type, [1] is outfit type, [2] is function to retrive [0]
        default import_mode = {"Import": [], "Assign": []}
        add "Paper_Background.png"
        modal True
        zorder 100
        default preview_outfit = None
        default targeted_outfit = None
        default mannequin = "mannequin"

        #default business_wardrobes = [mc.business.m_uniform, mc.business.p_uniform, mc.business.r_uniform, mc.business.s_uniform, mc.business.h_uniform, mc.business.all_uniform]

        default import_wardrobes = get_default_import_wardrobes(slut_limit) if not use_strip_club_wardrobe else get_strip_club_import_wardrobes() # Holds the wardrobes you want to be able to import into or select #NOTE: Make sure it is a list inside of a list [[]]

        python:
            if xml_filename:
                wardrobe = wardrobe_from_xml(xml_filename)
            else:
                temp_wardrobe = Wardrobe("Temporary Wardrobe")
                for category in import_wardrobes:
                    for wardrobes in import_wardrobes[category]:
                        for outfit in wardrobes.outfits + mc.designed_wardrobe.outfits:
                            if outfit not in temp_wardrobe.outfits:
                                temp_wardrobe.outfits.append(outfit)

                        for outfit in wardrobes.overwear_sets + mc.designed_wardrobe.overwear_sets:
                            if outfit not in temp_wardrobe.overwear_sets:
                                temp_wardrobe.overwear_sets.append(outfit)

                        for outfit in wardrobes.underwear_sets + mc.designed_wardrobe.underwear_sets:
                            if outfit not in temp_wardrobe.underwear_sets:
                                temp_wardrobe.underwear_sets.append(outfit)

                wardrobe = temp_wardrobe

        # default import_wardrobes = {"Your Wardrobe": [[mc.designed_wardrobe]], "Marketing Division": [[mc.business.m_uniform]], "Research Division": [[mc.business.r_uniform]], "Production Division": [[mc.business.p_uniform]], "Supply Division": [[mc.business.s_uniform]], "HR Division": [[mc.business.h_uniform]], "All Divisions": [[mc.business.all_uniform]]}
        # $ import_wardrobes["Slaves"] = [[x.wardrobe for x in people_in_role(slave_role)]]

        grid __builtin__.len(outfit_categories) 1:
            for category in sorted(outfit_categories): # NOTE: Dictionary is not sorted. Don't know the best way to make it so.
                vbox:
                    xsize 480
                    frame:
                        background "#0a142688"
                        text category style "menu_text_title_style" xalign 0.5
                        xfill True
                    if not outfit_type or outfit_categories[category][1] == outfit_type:
                        viewport:
                            ysize 880
                            if __builtin__.len(getattr(wardrobe, outfit_categories[category][2])()) > 7:
                                scrollbars "vertical"
                            mousewheel True
                            vbox:
                                if __builtin__.len(getattr(wardrobe, outfit_categories[category][2])()) > 0: #Don't show a frame if it is empty
                                    frame:
                                        background None
                                        vbox:
                                            for outfit in sorted(getattr(wardrobe, outfit_categories[category][2])(), key = lambda outfit: (outfit.slut_requirement, outfit.name)):  # Not sure if there's any good reason to sort XML lists since the default way it works is to place the newest outfit at the bottom which is predictable.
                                                $ effective_slut_score = calculate_outfit_slut_score(wardrobe, outfit)
                                                frame:
                                                    background "#0a142688"
                                                    vbox:
                                                        id str(outfit)
                                                        xfill True
                                                        textbutton outfit.name.replace("_", " ").title() + "\n" + get_heart_image_list_cloth(effective_slut_score, 1):
                                                            xfill True
                                                            style "textbutton_no_padding_highlight"
                                                            text_style "serum_text_style"

                                                            if underwear_limit == 0 and (outfit in wardrobe.outfits or outfit in wardrobe.underwear_sets) :
                                                                background "#222222"
                                                            elif slut_limit and (outfit in wardrobe.outfits or outfit in wardrobe.overwear_sets) and effective_slut_score > slut_limit:
                                                                background "#222222"
                                                                action Function(renpy.notify, "Can not assign due to policy enforced sluttiness limit [" + str(slut_limit) + "].\nPurchase new uniform policies to increase limit.")
                                                            elif underwear_limit and outfit in wardrobe.underwear_sets and effective_slut_score > underwear_limit:
                                                                background "#222222"
                                                                action Function(renpy.notify, "Can not assign due to policy enforced sluttiness limit [" + str(underwear_limit) + "].\nPurchase new uniform policies to increase limit.")
                                                            else:
                                                                action [
                                                                    Show("outfit_creator", None, outfit.get_copy(), outfit_categories[category][1], slut_limit, target_wardrobe), # Bring the outfit into the outfit_creator for editing when left clicked
                                                                    Hide(renpy.current_screen().screen_name)
                                                                    ]

                                                            hovered Function(draw_average_mannequin, outfit)

                                                        if show_export: # If export mode is on show the export button that saves the outfits into Exported_Wardrobe.xml NOTE: Consider specifying specific XML file later (to quickly make wardrobe sets for sharing)
                                                            default exported = []

                                                            textbutton "Export to .xml File":
                                                                style "textbutton_no_padding_highlight"
                                                                text_style "serum_text_style"
                                                                xfill True

                                                                action [
                                                                    Function(exported.append, outfit), Function(log_outfit, outfit, outfit_class = outfit_categories[category][0], wardrobe_name = "Exported_Wardrobe"),
                                                                    Function(renpy.notify, "Outfit exported to Exported_Wardrobe.xml")
                                                                    ]

                                                                sensitive outfit not in exported


                                                        textbutton ("Direct Import Selection:" if slut_limit is None else "Assigned to: " + get_wardrobe_name_for_outfit_with_name(import_wardrobes, outfit.name)): # Put the outfit directly into wardrobe(s), see the import_wardrobes dictionary to add more alternatives.

                                                            style "textbutton_no_padding_highlight"
                                                            text_style "serum_text_style"
                                                            xfill True

                                                            if underwear_limit == 0 and (outfit in wardrobe.outfits or outfit in wardrobe.underwear_sets):
                                                                background "#222222"
                                                                action Function(renpy.notify, "Full and underwear uniforms require [reduced_coverage_uniform_policy.name]")
                                                            elif slut_limit and (outfit in wardrobe.outfits or outfit in wardrobe.overwear_sets) and effective_slut_score > slut_limit:
                                                                background "#222222"
                                                                action Function(renpy.notify, "Can not assign due to policy enforced sluttiness limit [" + str(slut_limit) + "].\nPurchase new uniform policies to increase limit.")
                                                            elif underwear_limit and outfit in wardrobe.underwear_sets and effective_slut_score > underwear_limit:
                                                                background "#222222"
                                                                action Function(renpy.notify, "Can not assign due to policy enforced sluttiness limit [" + str(underwear_limit) + "].\nPurchase new uniform policies to increase limit.")
                                                            else:
                                                                action ToggleScreenVariable("targeted_outfit", renpy.get_widget(renpy.current_screen(), str(outfit)), None)

                                                        if targeted_outfit == renpy.get_widget(renpy.current_screen(), str(outfit)):
                                                            frame:
                                                                background "#0a142688"
                                                                vbox:
                                                                    for wardrobes in sorted(import_wardrobes):
                                                                        textbutton str(wardrobes):
                                                                            style "textbutton_no_padding_highlight"
                                                                            text_style "serum_text_style"
                                                                            xfill True

                                                                            if not import_wardrobes_has_outfit_with_name(import_wardrobes[wardrobes], outfit.name):
                                                                                action [
                                                                                    If(slut_limit != None, Function(mc.business.listener_system.fire_event, "add_uniform", the_outfit = outfit, the_type = outfit_categories[category][1])), # Make sure it registers progress towards work_goals. #NOTE: Needs testing as I have been unable to setup proper test
                                                                                    Function(import_add_outfit_to_wardrobes, import_wardrobes[wardrobes], outfit, outfit_type = outfit_categories[category][1]),
                                                                                    Function(renpy.notify, ("Outfit imported to " + wardrobes if slut_limit is None else "Outfit assigned to " + wardrobes)),

                                                                                    ]
                                                                            else:

                                                                                if slut_limit is not None:
                                                                                    if wardrobes == "Player Wardrobe" or wardrobes == "All Strip Club Outfits":  # don't allow remove from player / dressing room wardrobes
                                                                                        background "#aa4433"
                                                                                        sensitive False
                                                                                    elif import_wardrobes_has_outfit_with_name(import_wardrobes[wardrobes], outfit.name):
                                                                                        background "#3ffc45"
                                                                                    #If the outfit is imported / assigned already then attempt to remove it.
                                                                                    action [
                                                                                        Function(import_remove_outfit_from_wardrobes, import_wardrobes[wardrobes], outfit),
                                                                                        Function(renpy.notify, "Outfit removed from " + wardrobes)
                                                                                        ]

        frame:
            background None
            anchor [0.5,0.5]
            align [0.5,0.92]
            xysize [500,125]
            imagebutton:
                align [0.5,0.5]
                auto "gui/button/choice_%s_background.png"
                focus_mask "gui/button/choice_idle_background.png"
                if slut_limit is None:
                    action Hide("import_outfit_manager")
                else:
                    action Return("No Return")
                    hovered Function(hide_mannequin)
            textbutton "Return" align [0.5,0.5] text_style "return_button_style"
