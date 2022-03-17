init 10 python:

    def get_heart_image_list_cloth(slut_value, multiplier = 5): ## Returns a string of hearts. Since we are dealing with lower values this version has 20 as it's 100% filled value. Used to indicate sluttiness requirement for the cloth item.
        heart_string = "{image=" + get_individual_heart(0, slut_value*multiplier, 0) + "}"
        heart_string += "{image=" + get_individual_heart(0, slut_value*multiplier-20, 0) + "}"
        heart_string += "{image=" + get_individual_heart(0, slut_value*multiplier-40, 0) + "}"
        heart_string += "{image=" + get_individual_heart(0, slut_value*multiplier-60, 0) + "}"
        heart_string += "{image=" + get_individual_heart(0, slut_value*multiplier-80, 0) + "}"
        return heart_string

    renpy.pure(get_heart_image_list_cloth)

    def update_outfit_color(cloth_to_color):
        cs = renpy.current_screen()
        if cs.scope["selected_colour"] == "colour_pattern":
            cloth_to_color.colour_pattern = [cs.scope["current_r"], cs.scope["current_g"], cs.scope["current_b"], cs.scope["current_a"]]
        else:
            cloth_to_color.colour = [cs.scope["current_r"], cs.scope["current_g"], cs.scope["current_b"], cs.scope["current_a"]]
        return

    def hide_mannequin():
        cs = renpy.current_screen()
        # release display resources
        if "mannequin" in cs.scope.keys() and isinstance(cs.scope["mannequin"], Person):
            renpy.hide(cs.scope["mannequin"].identifier, layer = "8")
        else:
            renpy.hide("mannequin_dummy", layer = "8")
        return

    def preview_outfit(outfit = "demo_outfit"):
        cs = renpy.current_screen()
        hide_list = []
        if cs.scope["hide_underwear"]:
            hide_list.append(1)
        if cs.scope["hide_base"]:
            hide_list.append(2)
        if cs.scope["hide_overwear"]:
            hide_list.append(3)

        cs.scope["hide_list"] = hide_list
        if cs.scope["mannequin"] == "mannequin":
            draw_average_mannequin(cs.scope[outfit], hide_list = hide_list)
        else:
            draw_mannequin(cs.scope["mannequin"], cs.scope[outfit], cs.scope["mannequin_pose"], hide_list = hide_list)
        return

    def preview_clothing(apply_method, cloth, outfit = "demo_outfit"):
        cs = renpy.current_screen()

        cloth.colour[0] = cs.scope["current_r"]
        cloth.colour[1] = cs.scope["current_g"]
        cloth.colour[2] = cs.scope["current_b"]
        cloth.colour[3] = cs.scope["current_a"]

        apply_method(cs.scope[outfit], cloth)
        return

    def hide_preview(cloth, outfit = "demo_outfit"):
        cs = renpy.current_screen()
        cs.scope[outfit].remove_clothing(cloth)
        return

    def get_slut_score():
        cs = renpy.current_screen()

        if cs.scope["outfit_type"] == "full":
            return cs.scope["demo_outfit"].get_full_outfit_slut_score()
        elif cs.scope["outfit_type"] == "under":
            return cs.scope["demo_outfit"].get_underwear_slut_score()
        elif cs.scope["outfit_type"] == "over":
            return cs.scope["demo_outfit"].get_overwear_slut_score()
        return 0

    def get_outfit_type_name():
        cs = renpy.current_screen()

        if cs.scope["outfit_type"] == "full":
            return "Full Outfit"
        elif cs.scope["outfit_type"] == "under":
            return "Underwear"
        elif cs.scope["outfit_type"] == "over":
            return "Overwear"
        return 0

    def get_category(item):
        cs = renpy.current_screen()

        for cat in cs.scope["valid_categories"]:
            for cloth in cs.scope["categories_mapping"][cat][0]:
                if item.name == cloth.name:
                    return cat
        return cs.scope["valid_categories"][0]

    def set_generated_outfit(category, slut_value, min_slut_value = 0):
        cs = renpy.current_screen()
        outfit = cs.scope["outfit_builder"].build_outfit(cs.scope["outfit_class_selected"], slut_value, min_slut_value)
        outfit.update_name()
        cs.scope["demo_outfit"] = outfit
        duplicate_outfit(cs.scope["starting_outfit"], outfit)
        preview_outfit()
        return

    def personalize_generated_outfit():
        cs = renpy.current_screen()
        cs.scope["outfit_builder"].personalize_outfit(cs.scope["demo_outfit"], max_alterations = 2, swap_bottoms = True)
        cs.scope["demo_outfit"].update_name()
        duplicate_outfit(cs.scope["starting_outfit"], cs.scope["demo_outfit"])
        preview_outfit()
        return

    # replace all items in outfit with a copy from source outfit
    def duplicate_outfit(outfit, source_outfit):
        outfit.upper_body = []
        outfit.lower_body = []
        outfit.feet = []
        outfit.accessories = []

        for feet in source_outfit.feet:
            outfit.feet.append(feet.get_copy())

        for lower in source_outfit.lower_body:
            if not lower.is_extension:
                outfit.lower_body.append(lower.get_copy())

        for upper in source_outfit.upper_body:
            upper_copy = upper.get_copy()
            outfit.upper_body.append(upper_copy)
            if upper.has_extension:
                outfit.lower_body.append(upper_copy.has_extension)

        for accessory in source_outfit.accessories:
            outfit.accessories.append(accessory.get_copy())
        return

    def update_outfit_name(outfit):
        default_names = ["New Outfit", "New Overwear Set", "New Underwear Set"]
        if outfit.name in default_names or outfit.name == "":
            outfit.update_name()
        return

    def colour_changed_bar(new_value): # Handles the changes to clothing colors, both normal and with patterns. Covers all channels.
        if not new_value:
            new_value = 0
        try:
            new_value = float(new_value)
        except ValueError:
            new_value = 0
        if float(new_value) < 0:
            new_value = 0
        elif float(new_value) > 1:
            new_value = 1.0

        cs = renpy.current_screen()
        bar_value = cs.scope["bar_value"]

        if bar_value == "current_a":
            cs.scope["current_a"] = __builtin__.round(float(new_value),2)
            if cs.scope["selected_colour"] == "colour_pattern":
                cs.scope["selected_clothing"].colour_pattern = [cs.scope["current_r"], cs.scope["current_g"], cs.scope["current_b"], __builtin__.round(float(new_value),2)]
            else:
                cs.scope["selected_clothing"].colour = [cs.scope["current_r"], cs.scope["current_g"], cs.scope["current_b"], __builtin__.round(float(new_value),2)]

        if bar_value == "current_r":
            cs.scope["current_r"] = __builtin__.round(float(new_value),2)
            if cs.scope["selected_colour"] == "colour_pattern":
                cs.scope["selected_clothing"].colour_pattern = [__builtin__.round(float(new_value),2), cs.scope["current_g"], cs.scope["current_b"], cs.scope["current_a"]]
            else:
                cs.scope["selected_clothing"].colour = [__builtin__.round(float(new_value),2), cs.scope["current_g"], cs.scope["current_b"], cs.scope["current_a"]]

        if bar_value == "current_g":
            cs.scope["current_g"] = __builtin__.round(float(new_value),2)
            if cs.scope["selected_colour"] == "colour_pattern":
                cs.scope["selected_clothing"].colour_pattern = [cs.scope["current_r"], __builtin__.round(float(new_value),2), cs.scope["current_b"], cs.scope["current_a"]]
            else:
                cs.scope["selected_clothing"].colour = [cs.scope["current_r"], __builtin__.round(float(new_value),2), cs.scope["current_b"], cs.scope["current_a"]]

        if bar_value == "current_b":
            cs.scope["current_b"] = __builtin__.round(float(new_value),2)
            if cs.scope["selected_colour"] == "colour_pattern":
                cs.scope["selected_clothing"].colour_pattern = [cs.scope["current_r"], cs.scope["current_g"], __builtin__.round(float(new_value),2), cs.scope["current_a"]]
            else:
                cs.scope["selected_clothing"].colour = [cs.scope["current_r"], cs.scope["current_g"], __builtin__.round(float(new_value),2), cs.scope["current_a"]]
        preview_outfit()
        renpy.restart_interaction()
        return

    def update_transparency(new_value):
        cs = renpy.current_screen()

        cs.scope["current_a"] = __builtin__.round(float(new_value),2)
        if cs.scope["selected_colour"] == "colour_pattern":
            cs.scope["selected_clothing"].colour_pattern = [cs.scope["current_r"], cs.scope["current_g"], cs.scope["current_b"], __builtin__.round(float(new_value),2)]
        else:
            cs.scope["selected_clothing"].colour = [cs.scope["current_r"], cs.scope["current_g"], cs.scope["current_b"], __builtin__.round(float(new_value),2)]
        preview_outfit()
        return

    def update_slut_generation(new_value):
        cs = renpy.current_screen()

        if new_value < cs.scope["min_slut_generation"]:
            new_value = cs.scope["min_slut_generation"]
        if new_value > 12:
            new_value = 12

        cs.scope["slut_generation"] = new_value
        renpy.restart_interaction()
        return

    def update_min_slut_generation(new_value):
        cs = renpy.current_screen()

        if new_value < 0:
            new_value = 0
        if new_value > 5:
            new_value = 5
        elif new_value > cs.scope["slut_generation"]:
            new_value = cs.scope["slut_generation"]

        cs.scope["min_slut_generation"] = new_value
        renpy.restart_interaction()
        return

init 2:
    python:
        def custom_log_outfit(the_outfit, outfit_class = "FullSets", wardrobe_name = "Exported_Wardrobe"): #NOTE: This is just a version of the default log_outfit that does not append .xml to the file name
            file_path = os.path.abspath(os.path.join(config.basedir, "game"))
            file_path = os.path.join(file_path,"wardrobes")
            file_name = os.path.join(file_path, wardrobe_name)

            if not os.path.isfile(file_name): #We assume if the file exists that it is well formed. Otherwise we will create it and guarantee it is well formed.
                #Note: if the file is changed (by inserting extra outfits, for example) exporting outfits may crash due to malformed xml, but we do not overwrite the file.
                missing_file = open(file_name,"w+")
                starting_element = ET.Element("Wardrobe",{"name":wardrobe_name})
                starting_tree = ET.ElementTree(starting_element)
                ET.SubElement(starting_element,"FullSets")
                ET.SubElement(starting_element,"UnderwearSets")
                ET.SubElement(starting_element,"OverwearSets")

                indent(starting_element)
                starting_tree.write(file_name,encoding="UTF-8")


            wardrobe_tree = ET.parse(file_name)
            tree_root = wardrobe_tree.getroot()
            outfit_root = tree_root.find(outfit_class)

            outfit_element = ET.SubElement(outfit_root,"Outfit",{"name":the_outfit.name})
            upper_element = ET.SubElement(outfit_element, "UpperBody")
            lower_element = ET.SubElement(outfit_element, "LowerBody")
            feet_element = ET.SubElement(outfit_element, "Feet")
            accessory_element = ET.SubElement(outfit_element, "Accessories")

            for cloth in the_outfit.upper_body:
                item_dict = build_item_dict(cloth)
                if not cloth.is_extension:
                    ET.SubElement(upper_element,"Item", item_dict)
            for cloth in the_outfit.lower_body:
                item_dict = build_item_dict(cloth)
                if not cloth.is_extension:
                    ET.SubElement(lower_element,"Item", item_dict)
            for cloth in the_outfit.feet:
                item_dict = build_item_dict(cloth)
                if not cloth.is_extension:
                    ET.SubElement(feet_element,"Item", item_dict)
            for cloth in the_outfit.accessories:
                item_dict = build_item_dict(cloth)
                if not cloth.is_extension:
                    ET.SubElement(accessory_element,"Item", item_dict)

            indent(tree_root)
            wardrobe_tree.write(file_name,encoding="UTF-8")

init 2:
    screen outfit_creator(starting_outfit, outfit_type = "full", slut_limit = None, target_wardrobe = mc.designed_wardrobe): ##Pass a completely blank outfit instance for a new outfit, or an already existing instance to load an old one.| This overrides the default outfit creation screen
        add "Paper_Background.png"
        modal True

        frame:
            background "#ffffff18"
            xpos 1520
            ypos 0
            xysize (400, 1080)

        $ renpy.block_rollback()

        default fluids_list = [face_cum, mouth_cum, stomach_cum, tits_cum, ass_cum, creampie_cum]

        default category_selected = "Panties"
        default mannequin = "mannequin"
        default mannequin_pose = "stand3"
        default mannequin_selection = False
        default mannequin_poser = False

        default selected_xml = "Exported_Wardrobe.xml"
        default cloth_pattern_selection = True
        default transparency_selection = True
        default outfit_stats = True
        default outfit_class_selected = "FullSets"
        default color_selection = True
        default import_selection = False

        default demo_outfit = starting_outfit.get_copy()
        default outfit_builder = WardrobeBuilder(None)
        default max_slut = outfit_type == "over" and 8 or 12
        default hide_underwear = False
        default hide_base = False
        default hide_overwear = False
        default hide_list = []

        if outfit_type == "under":
            $ valid_layers = [0,1]
            $ outfit_class_selected = "UnderwearSets"
        elif outfit_type == "over":
            $ valid_layers = [2,3]
            $ outfit_class_selected = "OverwearSets"
        else:
            $ valid_layers = [0,1,2,3]
            $ outfit_class_selected = "FullSets"

        default valid_categories = ["Panties", "Bras", "Pants", "Skirts", "Dresses", "Shirts", "Socks", "Shoes", "Facial", "Rings", "Bracelets", "Neckwear", "Not Paint"] #Holds the valid list of categories strings to be shown at the top.

        default categories_mapping = {
            "Panties": [panties_list, Outfit.can_add_lower, Outfit.add_lower],  #Maps each category to the function it should use to determine if it is valid and how it should be added to the outfit.
            "Bras": [bra_list, Outfit.can_add_upper, Outfit.add_upper],
            "Pants": [[x for x in pants_list if not x in [cop_pants]] , Outfit.can_add_lower, Outfit.add_lower],
            "Skirts": [skirts_list, Outfit.can_add_lower, Outfit.add_lower],
            "Dresses": [dress_list, Outfit.can_add_dress, Outfit.add_dress],
            "Shirts": [[x for x in shirts_list if not x in [cop_blouse]], Outfit.can_add_upper, Outfit.add_upper],
            "Socks": [socks_list, Outfit.can_add_feet, Outfit.add_feet],
            "Shoes": [shoes_list, Outfit.can_add_feet, Outfit.add_feet],
            "Facial": [earings_list, Outfit.can_add_accessory, Outfit.add_accessory],
            "Rings": [rings_list, Outfit.can_add_accessory, Outfit.add_accessory],
            "Bracelets": [bracelet_list, Outfit.can_add_accessory, Outfit.add_accessory],
            "Neckwear": [neckwear_list, Outfit.can_add_accessory, Outfit.add_accessory],
            "Not Paint": [fluids_list, Outfit.can_add_accessory, Outfit.add_accessory]}

        default gold_heart = Composite((24, 24), (0, 1), Image(get_file_handle("gold_heart.png")))

        default bar_select = 0 # 0 is nothing selected, 1 is red, 2 is green, 3 is blue, and 4 is alpha
        default bar_value = None # Stores information about which bar is being changed and is then passed to colour_changed_bar() as default value

        default selected_clothing = None
        default selected_clothing_colour = None
        default selected_colour = "colour" #If secondary we are alterning the patern colour. When changed it updates the colour of the clothing item. Current values are "colour" and "colour_pattern"

        default current_r = 1.0
        default current_g = 1.0
        default current_b = 1.0
        default current_a = 1.0

        default slut_generation = 0
        default min_slut_generation = 0

        # $ current_colour = [1.0,1.0,1.0,1.0] #This is the colour we will apply to all of the clothing

        #Each category below has a click to enable button. If it's false, we don't show anything for it.
        #TODO: refactor this outfit creator to remove as much duplication as possible.


        hbox: #The main divider between the new item adder and the current outfit view.
            xpos 15
            yalign 0.5
            yanchor 0.5
            spacing 15
            frame:
                background "#0a142688"
                padding (20,20)
                xysize (880, 1015)
                hbox:
                    spacing 15
                    frame:
                        background "#0a142688"
                        xsize 200

                        viewport:
                            mousewheel True
                            draggable True
                            grid 1 __builtin__.len(valid_categories): #categories select on far left
                                for category in valid_categories:
                                    textbutton category:
                                        style "textbutton_style"
                                        text_style "serum_text_style"

                                        xfill True
                                        sensitive category is not category_selected
                                        if category == category_selected:
                                            background "#143869"
                                            hover_background "#1a45a1"
                                        else:
                                            background "#143869"
                                            hover_background "#1a45a1"
                                        insensitive_background "#171717"

                                        action [
                                            SetScreenVariable("category_selected", category),
                                            SetScreenVariable("selected_clothing", None),
                                            SetScreenVariable("selected_colour", "colour")
                                        ]
                    vbox:
                        spacing 5
                        viewport:
                            ysize 560
                            xminimum 605
                            scrollbars "vertical"
                            mousewheel True
                            frame:
                                xsize 605
                                yminimum 560
                                background "#0a142688"
                                padding 0,0

                                vbox:
                                    #THIS IS WHERE ITEM CHOICES ARE SHOWN
                                    if category_selected in categories_mapping:
                                        $ valid_check = categories_mapping[category_selected][1]
                                        $ apply_method = categories_mapping[category_selected][2]
                                        $ cloth_list_length = __builtin__.len(categories_mapping[category_selected][0])

                                        for cloth in sorted(categories_mapping[category_selected][0], key = lambda x: (x.layer, x.slut_value, x.name)):
                                            $ is_sensitive = valid_check(starting_outfit, cloth) and cloth.layer in valid_layers
                                            if cloth.has_extension and cloth.has_extension.layer not in valid_layers:
                                                $ is_sensitive = False

                                            frame:
                                                xsize 605
                                                ysize 50
                                                background None
                                                padding 0,0

                                                textbutton cloth.name.title():
                                                    xalign 0.0
                                                    ysize 50
                                                    text_align .5
                                                    xfill True
                                                    style "textbutton_style"
                                                    text_style "custom_outfit_style"

                                                    if valid_check(starting_outfit, cloth):
                                                        background "#143869"
                                                        hover_background "#1a45a1"
                                                    else:
                                                        background "#143869"
                                                        hover_background "#1a45a1"
                                                    insensitive_background "#171717"
                                                    sensitive is_sensitive
                                                    action [
                                                        SetScreenVariable("selected_clothing", cloth.get_copy()),
                                                        SetScreenVariable("selected_colour", "colour")
                                                    ]
                                                    hovered [
                                                        Function(preview_clothing, apply_method, cloth),
                                                        Function(preview_outfit)
                                                    ]
                                                    unhovered [
                                                        Function(hide_preview, cloth),
                                                        Function(preview_outfit)
                                                    ]


                                                text cloth.generate_stat_slug():
                                                    style "custom_outfit_style"
                                                    ysize 50
                                                    xalign .95
                                                    yalign 1
                                                    yoffset 10
                        frame:
                            #THIS IS WHERE SELECTED ITEM OPTIONS ARE SHOWN
                            xysize (605, 400)
                            background "#0a142688"
                            if selected_clothing is not None:
                                vbox:
                                    text selected_clothing.name + " " + selected_clothing.generate_stat_slug() style "serum_text_style_header"

                                    frame:
                                        background "#0a142688"
                                        yfill True
                                        xfill True
                                        viewport:
                                            xsize 605
                                            draggable True
                                            mousewheel True
                                            yfill True
                                            vbox:
                                                spacing 5
                                                if __builtin__.type(selected_clothing) is Clothing: #Only clothing items have patterns, facial accessories do not (currently).
                                                    vbox:
                                                        spacing 5
                                                        hbox:
                                                            spacing 5
                                                            if cloth_pattern_selection:
                                                                frame:
                                                                    background "#0a142688"
                                                                    ysize 50
                                                                    viewport:
                                                                        mousewheel "horizontal"
                                                                        draggable True

                                                                        grid __builtin__.len(selected_clothing.supported_patterns) 1:
                                                                            xfill True
                                                                            for pattern in selected_clothing.supported_patterns:

                                                                                textbutton pattern:
                                                                                    style "textbutton_no_padding_highlight"
                                                                                    text_style "serum_text_style"
                                                                                    xalign 0.5
                                                                                    xfill True

                                                                                    if selected_clothing.pattern == selected_clothing.supported_patterns[pattern]:
                                                                                        hover_background "#143869"
                                                                                        background "#14386988"
                                                                                    else:
                                                                                        hover_background "#143869"
                                                                                        background "#171717"

                                                                                    sensitive True
                                                                                    action [
                                                                                        SetField(selected_clothing,"pattern",selected_clothing.supported_patterns[pattern]),
                                                                                        Function(preview_outfit)
                                                                                    ]

                                                        hbox:
                                                            xfill True
                                                            spacing 5 #We will manually handle spacing so we can have our colour predictor frames
                                                            frame:
                                                                ysize 50
                                                                background "#0a142688"
                                                                hbox:
                                                                    spacing 5
                                                                    textbutton "Primary Colour":
                                                                        style "textbutton_no_padding_highlight"
                                                                        text_style "serum_text_style"

                                                                        if selected_colour == "colour":
                                                                            hover_background "#143869"
                                                                            background "#14386988"
                                                                        else:
                                                                            hover_background "#143869"
                                                                            background "#171717"
                                                                        sensitive True
                                                                        if selected_colour == "colour_pattern":
                                                                            action [
                                                                                SetField(selected_clothing,"colour_pattern",[current_r,current_g,current_b,current_a]),
                                                                                SetScreenVariable("selected_colour","colour"),
                                                                                SetScreenVariable("current_r",selected_clothing.colour[0]),
                                                                                SetScreenVariable("current_g",selected_clothing.colour[1]),
                                                                                SetScreenVariable("current_b",selected_clothing.colour[2]),
                                                                                SetScreenVariable("current_a",selected_clothing.colour[3])
                                                                            ]
                                                                        else:
                                                                            action ToggleScreenVariable("color_selection")

                                                                    frame:
                                                                        if selected_colour == "colour":
                                                                            background Color(rgb=(current_r,current_g,current_b,current_a))
                                                                        else:
                                                                            background Color(rgb=(selected_clothing.colour[0], selected_clothing.colour[1], selected_clothing.colour[2]))
                                                                        yfill True
                                                                        xsize 50


                                                                    if __builtin__.type(selected_clothing) is Clothing and selected_clothing.pattern is not None:
                                                                        textbutton "Pattern Colour":
                                                                            style "textbutton_no_padding_highlight"
                                                                            text_style "serum_text_style"

                                                                            if selected_colour == "colour_pattern":
                                                                                hover_background "#143869"
                                                                                background "#14386988"
                                                                            else:
                                                                                hover_background "#143869"
                                                                                background "#171717"
                                                                            sensitive True
                                                                            if selected_colour == "colour":
                                                                                action [
                                                                                    SetField(selected_clothing,"colour",[current_r,current_g,current_b,current_a]),
                                                                                    SetScreenVariable("selected_colour","colour_pattern"),
                                                                                    SetScreenVariable("current_r",selected_clothing.colour_pattern[0]),
                                                                                    SetScreenVariable("current_g",selected_clothing.colour_pattern[1]),
                                                                                    SetScreenVariable("current_b",selected_clothing.colour_pattern[2]),
                                                                                    SetScreenVariable("current_a",selected_clothing.colour_pattern[3])
                                                                                ]
                                                                            else:
                                                                                action ToggleScreenVariable("color_selection")
                                                                        frame:
                                                                            if selected_colour == "colour_pattern":
                                                                                background Color(rgb=(current_r,current_g,current_b,current_a))
                                                                            else:
                                                                                background Color(rgb=(selected_clothing.colour_pattern[0], selected_clothing.colour_pattern[1], selected_clothing.colour_pattern[2]))
                                                                            yfill True
                                                                            xsize 50

                                                vbox:
                                                    spacing 5
                                                    hbox:
                                                        spacing 5
                                                        if color_selection:
                                                            vbox:
                                                                spacing 5
                                                                grid 3 1:
                                                                    xfill True
                                                                    frame:

                                                                        background "#0a142688"
                                                                        hbox:
                                                                            button:
                                                                                background "#dd1f1f"
                                                                                action ToggleScreenVariable("bar_select", 1, 0)
                                                                                hovered SetScreenVariable("bar_value", "current_r")

                                                                                if bar_select == 1:
                                                                                    input default current_r length 4 changed colour_changed_bar allow ".0123456789" style "serum_text_style" size 16
                                                                                else:
                                                                                    text "R "+ "%.2f" % current_r style "serum_text_style" yalign 0.5 size 16
                                                                                xsize 75
                                                                                ysize 45
                                                                            bar:
                                                                                adjustment ui.adjustment(range = 1.00, value = current_r, step = 0.1, changed = colour_changed_bar)
                                                                                xfill True
                                                                                ysize 45
                                                                                style style.slider

                                                                                hovered SetScreenVariable("bar_value", "current_r")
                                                                                unhovered [SetScreenVariable("current_r",__builtin__.round(current_r,2))]

                                                                    frame:

                                                                        background "#0a142688"
                                                                        hbox:
                                                                            button:
                                                                                background "#3ffc45"
                                                                                action ToggleScreenVariable("bar_select", 2, 0)
                                                                                hovered SetScreenVariable("bar_value", "current_g")

                                                                                if bar_select == 2:
                                                                                    input default current_g length 4 changed colour_changed_bar allow ".0123456789" style "serum_text_style" size 16
                                                                                else:
                                                                                    text "G "+ "%.2f" % current_g style "serum_text_style" yalign 0.5 size 16
                                                                                xsize 75
                                                                                ysize 45
                                                                            bar:
                                                                                adjustment ui.adjustment(range = 1.00, value = current_g, step = 0.1, changed = colour_changed_bar)
                                                                                xfill True
                                                                                ysize 45
                                                                                style style.slider

                                                                                hovered SetScreenVariable("bar_value", "current_g")
                                                                                unhovered [SetScreenVariable("current_g",__builtin__.round(current_g,2))]
                                                                    frame:

                                                                        background "#0a142688"
                                                                        hbox:
                                                                            button:
                                                                                background "#3f87fc"
                                                                                action ToggleScreenVariable("bar_select", 3, 0)
                                                                                hovered SetScreenVariable("bar_value", "current_b")

                                                                                if bar_select == 3:
                                                                                    input default current_b length 4 changed colour_changed_bar allow ".0123456789" style "serum_text_style" size 16
                                                                                else:
                                                                                    text "B "+ "%.2f" % current_b style "serum_text_style" yalign 0.5 size 16

                                                                                xsize 75
                                                                                ysize 45
                                                                            bar:
                                                                                adjustment ui.adjustment(range = 1.00, value = current_b, step = 0.1, changed = colour_changed_bar)
                                                                                xfill True
                                                                                ysize 45
                                                                                style style.slider

                                                                                hovered SetScreenVariable("bar_value", "current_b")
                                                                                unhovered [SetScreenVariable("current_b",__builtin__.round(current_b,2))]

                                                                # frame:
                                                                #     background "#0a142688"
                                                                #     hbox:
                                                                #         button:
                                                                #             background "#111111"
                                                                #             action ToggleScreenVariable("bar_select", 4, 0)
                                                                #             hovered SetScreenVariable("bar_value", "current_a")

                                                                #             if bar_select == 4:
                                                                #                 input default current_a length 4 changed colour_changed_bar allow ".0123456789" style "serum_text_style" size 16
                                                                #             else:
                                                                #                 text "A "+ "%.2f" % current_a style "serum_text_style" yalign 0.5 size 16
                                                                #             xsize 75
                                                                #             ysize 45

                                                                #         bar:

                                                                #             adjustment ui.adjustment(range = 1.00, value = current_a, step = 0.1, changed = colour_changed_bar)
                                                                #             xfill True
                                                                #             ysize 45
                                                                #             style style.slider

                                                                #             hovered SetScreenVariable("bar_value", "current_a")
                                                                #             unhovered [SetScreenVariable("current_a",__builtin__.round(current_a,2))]

                                                                hbox:
                                                                    spacing 5
                                                                    for trans in ['1.0', '0.95', '0.9', '0.8', '0.75', '0.66', '0.5', '0.33']:
                                                                        $ trans_name = str(int(float(trans)*100)) + "%"
                                                                        button:
                                                                            if current_a == float(trans):
                                                                                hover_background "#143869"
                                                                                background "#14386988"
                                                                            else:
                                                                                hover_background "#143869"
                                                                                background "#171717"
                                                                            text trans_name style "menu_text_style" xalign 0.5 xanchor 0.5 yalign 0.5 yanchor 0.5
                                                                            xysize (60, 40)
                                                                            action [Function(update_transparency, float(trans))]
                                                                    frame:
                                                                        padding (0,0)
                                                                        xysize (60, 40)
                                                                        background "#143869"
                                                                        text str(int(float(current_a)*100)) + "%" style "serum_text_style" yalign 0.5 size 16

                                                    if color_selection:
                                                        for block_count, colour_list in __builtin__.enumerate(split_list_in_blocks(persistent.colour_palette, 13)):
                                                            hbox:
                                                                spacing 0
                                                                yanchor (block_count * .1)

                                                                for count, a_colour in __builtin__.enumerate(colour_list):
                                                                    frame:
                                                                        background "#0a142688"
                                                                        padding (3, 3)
                                                                        button:
                                                                            background Color(rgb=(a_colour[0], a_colour[1], a_colour[2]))
                                                                            xysize (38, 38)
                                                                            sensitive True
                                                                            xalign True
                                                                            yalign True
                                                                            action [
                                                                                SetScreenVariable("current_r", a_colour[0]),
                                                                                SetScreenVariable("current_g", a_colour[1]),
                                                                                SetScreenVariable("current_b", a_colour[2]),
                                                                                SetScreenVariable("current_a", a_colour[3]),
                                                                                Function(update_outfit_color, selected_clothing),
                                                                                Function(preview_outfit)
                                                                            ]
                                                                            alternate [
                                                                                Function(update_colour_palette, count + (block_count * 13), current_r, current_g, current_b, current_a)
                                                                            ]

                                    frame:
                                        background "#0a142688"
                                        xfill True
                                        textbutton "Add " + selected_clothing.name:
                                            style "textbutton_no_padding_highlight"
                                            text_style "serum_text_style"
                                            hover_background "#143869"
                                            background "#0a142688"
                                            insensitive_background"#171717"
                                            xalign 0.5
                                            xfill True

                                            sensitive valid_check(starting_outfit, selected_clothing)

                                            action [
                                                SetField(selected_clothing, selected_colour,[current_r,current_g,current_b,current_a]),
                                                Function(apply_method, starting_outfit, selected_clothing)
                                            ]
                                            hovered [
                                                SetField(selected_clothing, selected_colour,[current_r,current_g,current_b,current_a]),
                                                Function(apply_method, demo_outfit, selected_clothing),
                                                Function(preview_outfit)
                                            ]
                                            unhovered [
                                                Function(demo_outfit.remove_clothing, selected_clothing),
                                                Function(preview_outfit)
                                            ]

                # vbox: #Items selector
                #     #W/ item customixing window at bottom
                #
            vbox:
                spacing 15
                frame:
                    xysize (540, 500)
                    background "#0a142688"
                    vbox:
                        spacing 5
                        frame:
                            background "#0a142688"
                            xfill True
                            ysize 60
                            textbutton demo_outfit.name:
                                style "textbutton_no_padding_highlight"
                                text_style "serum_text_style"
                                xfill True
                                ysize 60
                                action [
                                    Function(demo_outfit.update_name)
                                ]
                                tooltip "Current outfit name. Click to generate new name based on current clothing."

                        vbox:
                            grid 2 1:
                                xfill True
                                spacing 5
                                frame:
                                    background "#0a142688"
                                    xfill True
                                    textbutton "View Outfit Stats":
                                        style "textbutton_no_padding_highlight"
                                        text_style "serum_text_style"
                                        xfill True

                                        action ToggleScreenVariable("outfit_stats")
                                frame:
                                    background "#0a142688"
                                    xfill True
                                    textbutton "Current (" + get_slut_value_classification(get_slut_score()) + ")":
                                        style "textbutton_no_padding"
                                        text_style "serum_text_style"
                                        xfill True

                                        action NullAction()

                            hbox:
                                spacing 5
                                vbox:
                                    xalign 0.5
                                    if outfit_stats:
                                        frame:
                                            background "#0a142688"
                                            ysize 314
                                            viewport:
                                                draggable True
                                                mousewheel True
                                                yfill True
                                                xsize 250
                                                vbox:
                                                    frame:
                                                        background "#143869"
                                                        xsize 250
                                                        padding (1,1)
                                                        text "Sluttiness (" + get_outfit_type_name() + "): " + str(get_slut_score()) style "serum_text_style_traits"
                                                    frame:
                                                        background "#143869"
                                                        xsize 250
                                                        padding (1,1)
                                                        text "Tits Visible: " + str(demo_outfit.tits_visible()) style "serum_text_style_traits"
                                                    frame:
                                                        background "#143869"
                                                        xsize 250
                                                        padding (1,1)
                                                        text "Tits Usable: " + str(demo_outfit.tits_available()) style "serum_text_style_traits"
                                                    frame:
                                                        background "#143869"
                                                        xsize 250
                                                        padding (1,1)
                                                        text "Wearing a Bra: " + str(demo_outfit.wearing_bra()) style "serum_text_style_traits"
                                                    frame:
                                                        background "#143869"
                                                        xsize 250
                                                        padding (1,1)
                                                        text "Bra Covered: " + str(demo_outfit.bra_covered()) style "serum_text_style_traits"
                                                    frame:
                                                        background "#143869"
                                                        xsize 250
                                                        padding (1,1)
                                                        text "Pussy Visible: " + str(demo_outfit.vagina_visible()) style "serum_text_style_traits"
                                                    frame:
                                                        background "#143869"
                                                        xsize 250
                                                        padding (1,1)
                                                        text "Pussy Usable: " + str(demo_outfit.vagina_available()) style "serum_text_style_traits"
                                                    frame:
                                                        background "#143869"
                                                        xsize 250
                                                        padding (1,1)
                                                        text "Wearing Panties: " + str(demo_outfit.wearing_panties()) style "serum_text_style_traits"
                                                    frame:
                                                        background "#143869"
                                                        xsize 250
                                                        padding (1,1)
                                                        text "Panties Covered: " + str(demo_outfit.panties_covered()) style "serum_text_style_traits"

                                                    # DEBUG CODE TO SEE WHAT IS SELECTED WHEN WE CLICK AROUND
                                                    # frame:
                                                    #     background "#43B197"
                                                    #     xsize 250
                                                    #     padding (1,1)
                                                    #     if (selected_clothing):
                                                    #         text "Seletect Item: " + selected_clothing.name style "serum_text_style_traits"

                                    frame:
                                        background "#0a142688"
                                        xsize 262
                                        vbox:
                                            frame:
                                                background "#143869"
                                                padding (1,1)
                                                xsize 250
                                                text "Visible Layers:" style "serum_text_style_traits"
                                            hbox:
                                                xfill True
                                                textbutton "Under":
                                                    style "textbutton_no_padding_highlight"
                                                    text_style "serum_text_style"
                                                    xsize 78
                                                    hover_background "#143869"
                                                    background ("#171717" if hide_underwear else "#14386988")
                                                    action [ToggleScreenVariable("hide_underwear", False, True), Function(preview_outfit)]
                                                textbutton "Clothing":
                                                    style "textbutton_no_padding_highlight"
                                                    text_style "serum_text_style"
                                                    xsize 86
                                                    hover_background "#143869"
                                                    background ("#171717" if hide_base else "#14386988")
                                                    action [ToggleScreenVariable("hide_base", False, True), Function(preview_outfit)]
                                                textbutton "Over":
                                                    style "textbutton_no_padding_highlight"
                                                    text_style "serum_text_style"
                                                    xsize 78
                                                    hover_background "#143869"
                                                    background ("#171717" if hide_overwear else "#14386988")
                                                    action [ToggleScreenVariable("hide_overwear", False, True), Function(preview_outfit)]

                                vbox:
                                    frame:
                                        background "#0a142688"

                                        xfill True
                                        viewport:
                                            scrollbars "vertical"
                                            mousewheel True
                                            xfill True
                                            vbox:
                                                spacing 5
                                                for cloth in demo_outfit.upper_body + demo_outfit.lower_body + demo_outfit.feet + demo_outfit.accessories:
                                                    if not cloth.is_extension and not cloth.layer in hide_list:
                                                        button:
                                                            background Color(rgb = (cloth.colour[0], cloth.colour[1], cloth.colour[2]))

                                                            action [ # NOTE: Left click makes more sense for selection than right clicking
                                                                SetScreenVariable("category_selected", get_category(cloth)),
                                                                SetScreenVariable("selected_clothing", cloth),
                                                                SetScreenVariable("selected_colour", "colour"),

                                                                SetScreenVariable("current_r", cloth.colour[0]),
                                                                SetScreenVariable("current_g", cloth.colour[1]),
                                                                SetScreenVariable("current_b", cloth.colour[2]),
                                                                SetScreenVariable("current_a", cloth.colour[3]),

                                                                Function(preview_outfit) # Make sure it is showing the correct outfit during changes, demo_outfit is a copy of starting_outfit
                                                            ]
                                                            alternate [
                                                                Function(hide_mannequin),
                                                                Function(starting_outfit.remove_clothing, cloth),
                                                                Function(demo_outfit.remove_clothing, cloth),
                                                                Function(preview_outfit)
                                                            ]
                                                            xalign 0.5
                                                            xfill True
                                                            ysize 34
                                                            text cloth.name xalign 0.5 yalign 0.5 xfill True yoffset 2 style "custom_outfit_style"

                frame:
                    background "#0a142688"

                    xysize (540, 500)
                    #padding (20,20)
                    hbox:
                        spacing 5
                        vbox:
                            hbox:
                                spacing 5
                                vbox:
                                    spacing 5
                                    frame:
                                        background "#0a142688"
                                        xsize 250
                                        vbox:
                                            xalign 0.5

                                            $ save_button_name = "Save Outfit"
                                            if slut_limit is not None:
                                                $ save_button_name += " {size=14}{color=#FF0000}Max: " + str(slut_limit) + " slut{/color}{/size}"

                                            textbutton save_button_name:
                                                style "textbutton_no_padding_highlight"
                                                text_style "serum_text_style"
                                                xfill True
                                                sensitive slut_limit is None or get_slut_score() <= slut_limit

                                                action [
                                                    Function(update_outfit_name, demo_outfit),
                                                    Function(hide_mannequin),
                                                    Return(demo_outfit),
                                                ]

                                            textbutton "Abandon / Exit":
                                                style "textbutton_no_padding_highlight"
                                                text_style "serum_text_style"
                                                xfill True

                                                action [
                                                    Function(hide_mannequin),
                                                    Return("Not_New"),
                                                ]
                                    frame:
                                        background "#0a142688"
                                        xsize 250
                                        vbox:
                                            xalign 0.5
                                            textbutton ("Export to [selected_xml]" if mannequin == "mannequin" else "Add to [mannequin.name] wardrobe"):
                                                style "textbutton_no_padding_highlight"
                                                text_style "serum_text_style"
                                                xfill True

                                                if mannequin == "mannequin":
                                                    action [
                                                        Function(custom_log_outfit, demo_outfit, outfit_class = outfit_class_selected,
                                                        wardrobe_name = selected_xml),
                                                        Function(renpy.notify, "Outfit exported to " + selected_xml + "]")
                                                    ]

                                                else:
                                                    if outfit_type == "full":
                                                        action [
                                                            Function(mannequin.wardrobe.add_outfit, demo_outfit),
                                                            Function(renpy.notify, "Outfit added to " + mannequin.name + " wardrobe")
                                                        ]
                                                    elif outfit_type == "over":
                                                        action [
                                                            Function(mannequin.wardrobe.add_overwear_set, demo_outfit),
                                                            Function(renpy.notify, "Outfit added to " + mannequin.name + " wardrobe")
                                                        ]

                                                    elif outfit_type == "under":
                                                        action [
                                                            Function(mannequin.wardrobe.add_underwear_set, demo_outfit),
                                                            Function(renpy.notify, "Outfit added to " + mannequin.name + " wardrobe")
                                                        ]

                                    frame:
                                        background "#0a142688"
                                        xsize 254
                                        vbox:
                                            textbutton "Generate [outfit_class_selected]":
                                                xfill True
                                                style "textbutton_no_padding_highlight"
                                                text_style "serum_text_style"
                                                tooltip "Generate random outfit based on clothing sluttiness values and selected girl."
                                                action [
                                                    Function(set_generated_outfit, category_selected, slut_generation, min_slut_generation)
                                                ]

                                            if mannequin != "mannequin":
                                                textbutton "Personalize Outfit":
                                                    xfill True
                                                    style "textbutton_no_padding_highlight"
                                                    text_style "serum_text_style"
                                                    tooltip "Personalize outfit for selected girl."
                                                    action [
                                                        Function(personalize_generated_outfit)
                                                    ]

                                            hbox:
                                                button:
                                                    background "#505050"
                                                    text "Slut "+ str(slut_generation) style "serum_text_style" yalign 0.5 size 16
                                                    xsize 90
                                                    ysize 24
                                                bar:
                                                    adjustment ui.adjustment(range = max_slut, value = slut_generation, step = 1, changed = update_slut_generation)
                                                    xfill True
                                                    ysize 24
                                                    thumb gold_heart
                                                    style style.slider

                                            if slut_generation > 0:
                                                hbox:
                                                    button:
                                                        background "#505050"
                                                        text "Min "+ str(min_slut_generation) style "serum_text_style" yalign 0.5 size 16
                                                        xsize 90
                                                        ysize 24
                                                    bar:
                                                        adjustment ui.adjustment(range = (slut_generation if slut_generation < 5 else 5), value = min_slut_generation, step = 1, changed = update_min_slut_generation)
                                                        xfill True
                                                        ysize 24
                                                        thumb gold_heart
                                                        style style.slider


                                    $ love_list = outfit_builder.get_love_list()
                                    $ hate_list = outfit_builder.get_hate_list()
                                    if outfit_builder and len(love_list + hate_list) > 0:
                                        frame:
                                            background "#0a142688"
                                            xsize 250
                                            vbox:
                                                spacing 0
                                                frame:
                                                    background "#000080"
                                                    xsize 240
                                                    padding (1,1)
                                                    text "Preferences:" style "serum_text_style_traits"
                                                viewport:
                                                    scrollbars "vertical"
                                                    draggable True
                                                    mousewheel True
                                                    yfill True
                                                    xsize 240
                                                    vbox:
                                                        if __builtin__.len(love_list) > 0:
                                                            for pref in love_list:
                                                                frame:
                                                                    background "#43B197"
                                                                    xsize 220
                                                                    padding (1,1)
                                                                    text pref style "serum_text_style_traits"
                                                        if __builtin__.len(hate_list) > 0:
                                                            for pref in hate_list:
                                                                frame:
                                                                    background "#B14365"
                                                                    xsize 220
                                                                    padding (1,1)
                                                                    text pref style "serum_text_style_traits"

                                vbox:

                                    frame:
                                        background "#0a142688"
                                        xfill True
                                        vbox:
                                            textbutton "Import Design":
                                                style "textbutton_no_padding_highlight"
                                                text_style "serum_text_style"
                                                xfill True
                                                xalign 0.5

                                                if import_selection:
                                                    background "#4f7ad6"
                                                    hover_background "#4f7ad6"

                                                action [
                                                ToggleScreenVariable("import_selection"),
                                                If(mannequin_selection or mannequin_poser, [SetScreenVariable("mannequin_selection", False), SetScreenVariable("mannequin_poser", False)])
                                                ]

                                            textbutton "Mannequin Selection":
                                                style "textbutton_no_padding_highlight"
                                                text_style "serum_text_style"
                                                xfill True
                                                xalign 0.5

                                                if mannequin_selection:
                                                    background "#4f7ad6"
                                                    hover_background "#4f7ad6"

                                                action [
                                                ToggleScreenVariable("mannequin_selection"),
                                                If(import_selection or mannequin_poser, [SetScreenVariable("import_selection", False), SetScreenVariable("mannequin_poser", False)])
                                                ]

                                            textbutton "Mannequin Poser":
                                                style "textbutton_no_padding_highlight"
                                                text_style "serum_text_style"
                                                xfill True
                                                xalign 0.5
                                                if mannequin_poser:
                                                    background "#4f7ad6"
                                                    hover_background "#4f7ad6"


                                                action [
                                                    SensitiveIf(mannequin != "mannequin"),
                                                    ToggleScreenVariable("mannequin_poser"),
                                                    If(import_selection or mannequin_selection, [SetScreenVariable("import_selection", False), SetScreenVariable("mannequin_selection", False)])
                                                ]

                                    if import_selection:
                                        frame:
                                            background "#0a142688"
                                            xfill True
                                            viewport:
                                                scrollbars "vertical"
                                                mousewheel True
                                                draggable True
                                                vbox:
                                                    for n in get_xml_files_from_path():
                                                        textbutton n:
                                                            style "textbutton_no_padding_highlight"
                                                            text_style "serum_text_style"
                                                            xfill True
                                                            xalign 0.5

                                                            if selected_xml == n:
                                                                background "#4f7ad6"
                                                                hover_background "#4f7ad6"

                                                            action [
                                                                Show("import_outfit_manager", None, target_wardrobe, n, outfit_type)
                                                            ]
                                                            alternate [ #Right clicking selects the path that outfits should be exported to
                                                            SetVariable("selected_xml", n)
                                                            ]

                                    if mannequin_selection:
                                        frame:
                                            background "#0a142688"
                                            xfill True
                                            viewport:
                                                scrollbars "vertical"
                                                mousewheel True
                                                draggable True
                                                vbox:
                                                    textbutton "Default Mannequin":
                                                        style "textbutton_no_padding_highlight"
                                                        text_style "serum_text_style"
                                                        xfill True
                                                        xalign 0.5

                                                        action [
                                                            SetScreenVariable("mannequin", "mannequin"),
                                                            SetScreenVariable("outfit_builder", WardrobeBuilder(None)),
                                                            Function(preview_outfit)
                                                        ]
                                                    for person in sorted(known_people_in_the_game(), key = lambda x: x.name):
                                                        textbutton person.name:
                                                            style "textbutton_no_padding_highlight"
                                                            text_style "serum_text_style"
                                                            xfill True
                                                            xalign 0.5

                                                            if mannequin == person:
                                                                background "#4f7ad6"
                                                                hover_background "#4f7ad6"

                                                            action [
                                                                SetScreenVariable("mannequin", person),
                                                                SetScreenVariable("outfit_builder", WardrobeBuilder(person)),
                                                                Function(preview_outfit)
                                                            ]

                                    if mannequin_poser:
                                        frame:
                                            background "#0a142688"
                                            xfill True
                                            viewport:
                                                scrollbars "vertical"
                                                mousewheel True
                                                draggable True
                                                vbox:
                                                    for x in sorted(["stand2","stand3","stand4","stand5","walking_away","kissing","kneeling1","doggy","missionary","blowjob","against_wall","back_peek","sitting","standing_doggy","cowgirl"]):
                                                        textbutton x:
                                                            style "textbutton_no_padding_highlight"
                                                            text_style "serum_text_style"
                                                            xfill True
                                                            xalign 0.5

                                                            if mannequin_pose == x:
                                                                background "#4f7ad6"
                                                                hover_background "#4f7ad6"

                                                            action [
                                                            SetScreenVariable("mannequin_pose", x),
                                                            Function(preview_outfit)
                                                            ]

                                                            alternate NullAction()

        imagebutton:
            auto "/tutorial_images/restart_tutorial_%s.png"
            xsize 54
            ysize 54
            yanchor 1.0
            xanchor 1.0
            xalign 1.0
            yalign 1.0
            action Function(mc.business.reset_tutorial,"outfit_tutorial")


        $ outfit_tutorial_length = 8 #The number of  tutorial screens we have.
        if mc.business.event_triggers_dict["outfit_tutorial"] > 0 and mc.business.event_triggers_dict["outfit_tutorial"] <= outfit_tutorial_length: #We use negative numbers to symbolize the tutorial not being enabled
            imagebutton:
                auto
                sensitive True
                xsize 1920
                ysize 1080
                idle "/tutorial_images/outfit_tutorial_"+__builtin__.str(mc.business.event_triggers_dict["outfit_tutorial"])+".png"
                hover "/tutorial_images/outfit_tutorial_"+__builtin__.str(mc.business.event_triggers_dict["outfit_tutorial"])+".png"
                action Function(mc.business.advance_tutorial,"outfit_tutorial")
