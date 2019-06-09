#init -1 python: #TODO: Go through everything again so that it uses copies where it should and remove instances where it shouldn't.
                      # I want outfits to be editable without forcing commitet changes upon `selected_clothing`
                      # Right now, this seems to only be a problem when editing a `Person`'s wardrobe since the MC Wardrobe always use copies anyway.
                      # Fix issue with hitting "Abandon" when using Outfit Manager through "Add Outfit" for a Person, seems to be coming from the fact it does not give the expected return of "No Return".
                      # Best solution would be for Vren to change that in the main script so all the outfit screen expect the same return.
                      # Figure out why and fix actions only running certain functions on every second press.
                      # Add logic for the instances where multiple cloth items from a catagory can be applied so it displays properly at all times. (no known issues with the end result, just display)

init -1 python:

    def colour_changed_a(new_value): # Used to modify the alpha channel through user input
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

        cs.scope["current_a"] = __builtin__.round(float(new_value),2)
        renpy.restart_interaction()

    def in_outfit(self, cloth_name): # Checks if the clothing item exists in the outfit by name to account for instances where copies are used.
        for cloth in self.upper_body + self.lower_body + self.feet + self.accessories:
            if cloth.name == cloth_name:
                return True
        else:
            return False
    Outfit.in_outfit = in_outfit



    def get_catagory(item): # Should re-write this function if possible.
        cloth_master_list = [
        panties_list + neckwear_list + bracelet_list + rings_list +
        earings_list + shoes_list + bra_list + pants_list + skirts_list +
        shirts_list + dress_list +  socks_list
        ]
        for cloth in cloth_master_list:
            if item in panties_list:
                return "Panties"
            if item in bra_list:
                return "Bras"
            if item in pants_list:
                return "Pants"
            if item in skirts_list:
                return "Skirts"
            if item in dress_list:
                return "Dresses"
            if item in shirts_list:
                return "Shirts"
            if item in socks_list:
                return "Socks"
            if item in shoes_list:
                return "Shoes"
            if item in earings_list:
                return "Facial"
            if item in rings_list:
                return "Rings"
            if item in bracelet_list:
                return "Bracelets"
            if item in neckwear_list:
                return "Neckwear"
init 2:
    $ import_selection = False # Decides if the import viewport is showing
    $ selected_xml = "Exported_Wardrobe.xml"
    $ palette_grid_size = 1
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

        def add_palette(palette_grid_size):
            while len(persistent.colour_palette) < palette_grid_size*10:
                persistent.colour_palette.append([1,1,1,1])
            palette_grid_size = len(persistent.colour_palette)/10



    screen outfit_creator(starting_outfit, target_wardrobe = mc.designed_wardrobe): ##Pass a completely blank outfit instance for a new outfit, or an already existing instance to load an old one.| This overrides the default outfit creation screen

        add "Paper_Background.png"
        modal True
        zorder 100
        default catagory_selected = "Panties"
        default mannequin = True

        default cloth_pattern_selection = True
        default transparency_selection = True
        default outfit_stats = True
        default outfit_class_selected = "FullSets"
        default color_selection = True


        default quick_catagory = None # Used to get catagory of the item
        default selected_from_outfit = None # Used to temporarily remember what clothing you have selected from starting_outfit if any
        default compare_outfit = starting_outfit.get_copy() # Have a non- altered copy available for checks.
        default colour_cloth = None # A variable to fetch the copy of selected_clothing.get_copy()
        default demo_outfit = starting_outfit.get_copy()


        $ valid_catagories = ["Panties", "Bras", "Pants", "Skirts", "Dresses", "Shirts", "Socks", "Shoes", "Facial", "Rings", "Bracelets", "Neckwear"] #Holds the valid list of catagories strings to be shown at the top.

        $ catagories_mapping = {
            "Panties": [panties_list, Outfit.can_add_lower, Outfit.add_lower],  #Maps each catagory to the function it should use to determine if it is valid and how it should be added to the outfit.
            "Bras": [bra_list, Outfit.can_add_upper, Outfit.add_upper],
            "Pants": [pants_list, Outfit.can_add_lower, Outfit.add_lower],
            "Skirts": [skirts_list, Outfit.can_add_lower, Outfit.add_lower],
            "Dresses": [dress_list, Outfit.can_add_dress, Outfit.add_dress],
            "Shirts": [shirts_list, Outfit.can_add_upper, Outfit.add_upper],
            "Socks": [socks_list, Outfit.can_add_feet, Outfit.add_feet],
            "Shoes": [shoes_list, Outfit.can_add_feet, Outfit.add_feet],
            "Facial": [earings_list, Outfit.can_add_accessory, Outfit.add_accessory],
            "Rings": [rings_list, Outfit.can_add_accessory, Outfit.add_accessory],
            "Bracelets": [bracelet_list, Outfit.can_add_accessory, Outfit.add_accessory],
            "Neckwear": [neckwear_list, Outfit.can_add_accessory, Outfit.add_accessory]}


        default bar_select = 0 # 0 is nothing selected, 1 is red, 2 is green, 3 is blue, and 4 is alpha

        default selected_clothing = None
        default selected_clothing_colour = None
        default selected_colour = "colour" #If secondary we are alterning the patern colour. When changed it updates the colour of the clothing item. Current values are "colour" and "colour_pattern"

        default current_r = 1.0
        default current_g = 1.0
        default current_b = 1.0
        default current_a = 1.0


        # $ current_colour = [1.0,1.0,1.0,1.0] #This is the colour we will apply to all of the clothing

        #Each catagory below has a click to enable button. If it's false, we don't show anything for it.
        #TODO: refactor this outfit creator to remove as much duplication as possible.


        hbox: #The main divider between the new item adder and the current outfit view.
            xpos 15
            yalign 0.5
            yanchor 0.5
            spacing 15
            frame:
                background "#aaaaaa"
                padding (20,20)
                xysize (880, 1015)
                hbox:
                    spacing 15
                    vbox: #Catagories select on far left
                        spacing 15
                        for catagory in valid_catagories:
                            textbutton catagory:
                                style "textbutton_style"
                                text_style "serum_text_style"
                                if catagory == catagory_selected:
                                    background "#4f7ad6"
                                    hover_background "#4f7ad6"
                                else:
                                    background "#1a45a1"
                                    hover_background "#3a65c1"
                                text_align(0.5,0.5)
                                text_anchor(0.5,0.5)
                                xysize (220, 60)
                                action [
                                SetScreenVariable("catagory_selected",catagory),
                                SetScreenVariable("selected_clothing", None),
                                SetScreenVariable("selected_colour", "colour"),
                                If(selected_clothing is not None and not starting_outfit.has_clothing(selected_clothing),
                                Function(demo_outfit.remove_clothing, selected_clothing))
                                ] #Set the clothing to None when you change catagories to avoid breaking the clothing add function assignments
                    vbox:
                        spacing 15
                        viewport:
                            ysize 480
                            xminimum 605
                            scrollbars "vertical"
                            mousewheel True
                            frame:
                                xsize 620
                                yminimum 480
                                background "#888888"
                                vbox:
                                    #THIS IS WHERE ITEM CHOICES ARE SHOWN
                                    if catagory_selected in catagories_mapping:
                                        $ valid_check = catagories_mapping[catagory_selected][1]
                                        $ apply_method = catagories_mapping[catagory_selected][2]
                                        $ cloth_list_length = len(catagories_mapping[catagory_selected][0])

                                        for cloth in catagories_mapping[catagory_selected][0]:
                                            textbutton cloth.name:
                                                style "textbutton_style"
                                                text_style "custom_outfit_style"

                                                    background "#1a45a1"
                                                    hover_background "#3a65c1"

                                                if valid_check(starting_outfit, cloth) or selected_clothing in catagories_mapping[catagory_selected][0]:

                                                    background "#1a45a1"
                                                    hover_background "#3a65c1"

                                                else:
                                                    background "#444444"
                                                    hover_background "#444444"

                                                xfill True

                                                action [
                                                SensitiveIf(valid_check(starting_outfit, cloth) or selected_clothing in catagories_mapping[catagory_selected][0]),
                                                SetScreenVariable("selected_clothing", cloth),
                                                SetScreenVariable("selected_colour", "colour"),

                                                ]

                                                hovered [
                                                If(selected_clothing in catagories_mapping[catagory_selected][0],
                                                [Function(demo_outfit.remove_clothing, selected_clothing), # Remove then apply
                                                Function(apply_method, demo_outfit, cloth)],
                                                Function(apply_method, demo_outfit, cloth)), # Just remove
                                                Show("mannequin", None, demo_outfit)
                                                ]

                                                unhovered [
                                                SensitiveIf(valid_check(starting_outfit, cloth) or selected_clothing in catagories_mapping[catagory_selected][0]),
                                                If(cloth is selected_clothing and selected_clothing in catagories_mapping[catagory_selected][0],
                                                NullAction(),
                                                Function(demo_outfit.remove_clothing, cloth)),
                                                If(selected_clothing is not None,
                                                Function(apply_method, demo_outfit, selected_clothing))
                                                ]
                        frame:
                            #THIS IS WHERE SELECTED ITEM OPTIONS ARE SHOWN
                            xysize (605, 480)
                            background "#888888"
                            viewport:
                                xsize 605
                                draggable True
                                mousewheel True
                                yfill True
                                vbox:
                                    spacing 10
                                    if selected_clothing is not None:
                                        frame:
                                            background "#aaaaaa"
                                            xfill True
                                            textbutton "Add " + selected_clothing.name + " to outfit" + "\n+" + __builtin__.str(selected_clothing.slut_value) + " Slut Requirement":

                                                style "textbutton_no_padding_highlight"
                                                text_style "serum_text_style"
                                                background "#1a45a1"
                                                hover_background "#3a65c1"
                                                xalign 0.5
                                                xfill True

                                                action [
                                                SensitiveIf([
                                                valid_check(starting_outfit, selected_clothing)
                                                and selected_clothing in catagories_mapping[catagory_selected][0]
                                                or starting_outfit.in_outfit(selected_clothing.name)]),

                                                SetField(selected_clothing, selected_colour,[current_r,current_g,current_b,current_a]), #Make sure color is updated
                                                If(starting_outfit is not None and starting_outfit.in_outfit(selected_clothing.name) or selected_from_outfit in catagories_mapping[catagory_selected][0],
                                                [Function(starting_outfit.remove_clothing, selected_from_outfit),
                                                Function(apply_method, starting_outfit, selected_clothing)],
                                                Function(apply_method, starting_outfit, selected_clothing)),
                                                Show("mannequin", None, starting_outfit),
                                                SetScreenVariable("selected_clothing", None)] # NOTE: We are no longer interested in the demo outfit so view the final outfit, starting_outfit


                                                hovered [
                                                If(selected_from_outfit is not None and selected_clothing in catagories_mapping[catagory_selected][0], Function(demo_outfit.remove_clothing, selected_from_outfit)),
                                                Function(apply_method, demo_outfit, selected_clothing),
                                                SetField(selected_clothing, selected_colour,[current_r,current_g,current_b,current_a]),
                                                Show("mannequin", None, demo_outfit)
                                                ]

                                        if __builtin__.type(selected_clothing) is Clothing: #Only clothing items have patterns, facial accessories do not (currently).
                                            vbox:
                                                spacing 5
                                                hbox:
                                                    frame:
                                                        background "#aaaaaa"
                                                        xfill True
                                                        textbutton "Cloth Pattern Selection":
                                                            style "textbutton_no_padding_highlight"
                                                            text_style "serum_text_style"
                                                            xfill True

                                                            action ToggleScreenVariable("cloth_pattern_selection")
                                                hbox:
                                                    spacing 5
                                                    if cloth_pattern_selection:
                                                        frame:
                                                            background "#aaaaaa"
                                                            ysize 50
                                                            viewport:
                                                                mousewheel "horizontal"
                                                                draggable True

                                                                grid len(selected_clothing.supported_patterns) 1:
                                                                    xfill True
                                                                    for pattern in selected_clothing.supported_patterns:

                                                                        textbutton pattern:
                                                                            style "textbutton_no_padding_highlight"
                                                                            text_style "serum_text_style"
                                                                            xalign 0.5
                                                                            xfill True

                                                                            if selected_clothing.pattern == selected_clothing.supported_patterns[pattern]:
                                                                                background "#4f7ad6"
                                                                                hover_background "#4f7ad6"
                                                                            else:
                                                                                background "#1a45a1"
                                                                                hover_background "#3a65c1"

                                                                            sensitive True
                                                                            action SetField(selected_clothing,"pattern",selected_clothing.supported_patterns[pattern])

                                                hbox:
                                                    xfill True
                                                    spacing 5 #We will manually handle spacing so we can have our colour predictor frames
                                                    frame:
                                                        ysize 50
                                                        background "#aaaaaa"
                                                        hbox:
                                                            spacing 5
                                                            textbutton "Primary Colour":
                                                                style "textbutton_no_padding_highlight"
                                                                text_style "serum_text_style"

                                                                if selected_colour == "colour":
                                                                    background "#4f7ad6"
                                                                    hover_background "#4f7ad6"
                                                                else:
                                                                    background "#1a45a1"
                                                                    hover_background "#3a65c1"
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
                                                                    action NullAction()

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
                                                                        background "#4f7ad6"
                                                                        hover_background "#4f7ad6"
                                                                    else:
                                                                        background "#1a45a1"
                                                                        hover_background "#3a65c1"
                                                                    sensitive True
                                                                    if selected_colour == "colour":
                                                                        action [
                                                                        SetField(selected_clothing,"colour",[current_r,current_g,current_b,current_a]),
                                                                        SetScreenVariable("selected_colour","colour_pattern"),
                                                                        SetScreenVariable("current_r",selected_clothing.colour_pattern[0]),
                                                                        SetScreenVariable("current_g",selected_clothing.colour_pattern[1]),
                                                                        SetScreenVariable("current_b",selected_clothing.colour_pattern[2]),
                                                                        SetScreenVariable("current_a",selected_clothing.colour_pattern[3])]
                                                                    else:
                                                                        action NullAction()
                                                                frame:
                                                                    if selected_colour == "colour_pattern":
                                                                        background Color(rgb=(current_r,current_g,current_b,current_a))
                                                                    else:
                                                                        background Color(rgb=(selected_clothing.colour_pattern[0], selected_clothing.colour_pattern[1], selected_clothing.colour_pattern[2]))
                                                                    yfill True
                                                                    xsize 50

                                        vbox:
                                            hbox:
                                                spacing 5
                                                textbutton "Color Selection":
                                                    style "textbutton_no_padding_highlight"
                                                    text_style "serum_text_style"
                                                    xfill True

                                                    action ToggleScreenVariable("color_selection")
                                            hbox:
                                                spacing 5
                                                if color_selection:
                                                    grid 2 2:
                                                        xfill True
                                                        frame:

                                                            background "#aaaaaa"
                                                            hbox:
                                                                button:
                                                                    background "#dd1f1f"
                                                                    action ToggleScreenVariable("bar_select", 1, 0)

                                                                    if bar_select == 1:
                                                                        input default current_r length 4 changed colour_changed_r allow ".0123456789" style "serum_text_style"
                                                                    else:
                                                                        text "Red "+ "%.2f" % current_r style "serum_text_style" yalign 0.5
                                                                    xsize 75
                                                                    ysize 45
                                                                bar value ScreenVariableValue("current_r", 1.0) xfill True ysize 45 style style.slider unhovered [SetScreenVariable("current_r",__builtin__.round(current_r,2)), SetField(selected_clothing, selected_colour,[current_r,current_g,current_b,current_a])]
                                                        frame:

                                                            background "#aaaaaa"
                                                            hbox:
                                                                button:
                                                                    background "#3ffc45"
                                                                    action ToggleScreenVariable("bar_select", 2, 0)

                                                                    if bar_select == 2:
                                                                        input default current_g length 4 changed colour_changed_g allow ".0123456789" style "serum_text_style"
                                                                    else:
                                                                        text "Green "+ "%.2f" % current_g style "serum_text_style" yalign 0.5
                                                                    xsize 75
                                                                    ysize 45

                                                                bar value ScreenVariableValue("current_g", 1.0) xfill True ysize 45 style style.slider unhovered [SetScreenVariable("current_g",__builtin__.round(current_g,2)), SetField(selected_clothing, selected_colour,[current_r,current_g,current_b,current_a])]
                                                        frame:

                                                            background "#aaaaaa"
                                                            hbox:
                                                                button:
                                                                    background "#3f87fc"
                                                                    action ToggleScreenVariable("bar_select", 3, 0)
                                                                    if bar_select == 3:
                                                                        input default current_b length 4 changed colour_changed_b allow ".0123456789" style "serum_text_style"
                                                                    else:
                                                                        text "Blue "+ "%.2f" % current_b style "serum_text_style" yalign 0.5

                                                                    xsize 75
                                                                    ysize 45

                                                                bar value ScreenVariableValue("current_b", 1.0) xfill True ysize 45 style style.slider unhovered [
                                                                SetScreenVariable("current_b",__builtin__.round(current_b,2)),
                                                                SetField(selected_clothing, selected_colour,[current_r,current_g,current_b,current_a])
                                                                ]

                                                        frame:

                                                            background "#aaaaaa"
                                                            hbox:
                                                                button:
                                                                    background "#111111"
                                                                    action ToggleScreenVariable("bar_select", 4, 0)

                                                                    if bar_select == 4:
                                                                        input default current_a length 4 changed colour_changed_a allow ".0123456789" style "serum_text_style"
                                                                    else:
                                                                        text "Alpha "+ "%.2f" % current_a style "serum_text_style" yalign 0.5
                                                                    xsize 75
                                                                    ysize 45

                                                                bar value ScreenVariableValue("current_a", 1.0) xfill True ysize 45 style style.slider unhovered [SetScreenVariable("current_a",__builtin__.round(current_a,2)), SetField(selected_clothing, selected_colour,[current_r,current_g,current_b,current_a])]

                                        vbox:
                                            spacing 5
                                            hbox:
                                                frame:
                                                    background "#aaaaaa"
                                                    xfill True
                                                    textbutton "Transparency":
                                                        style "textbutton_no_padding_highlight"
                                                        text_style "serum_text_style"

                                                        xfill True

                                                        action ToggleScreenVariable("transparency_selection")
                                            hbox:
                                                if transparency_selection:
                                                    frame:
                                                        background "#aaaaaa"
                                                        ysize 50
                                                        viewport:
                                                            xfill True
                                                            draggable True
                                                            mousewheel "horizontal"
                                                            ysize 50
                                                            hbox:
                                                                spacing 5
                                                                textbutton "Normal":
                                                                    style "textbutton_no_padding_highlight"
                                                                    text_style "serum_text_style"
                                                                    xalign 0.5
                                                                    xsize 200

                                                                    if current_a == 1.0:
                                                                        background "#4f7ad6"
                                                                    else:
                                                                        background "#1a45a1"
                                                                    action [
                                                                    SetScreenVariable("current_a", 1.0),
                                                                    SetField(selected_clothing, selected_colour,[current_r,current_g,current_b,current_a])
                                                                    ]

                                                                textbutton "Sheer":
                                                                    style "textbutton_no_padding_highlight"
                                                                    text_style "serum_text_style"
                                                                    xalign 0.5
                                                                    xsize 200
                                                                    if current_a == 0.95:
                                                                        background "#4f7ad6"
                                                                    else:
                                                                        background "#1a45a1"

                                                                    action [
                                                                    SetScreenVariable("current_a", 0.95),
                                                                    SetField(selected_clothing, selected_colour,[current_r,current_g,current_b,current_a])
                                                                    ]

                                                                textbutton "Translucent":
                                                                    style "textbutton_no_padding_highlight"
                                                                    text_style "serum_text_style"
                                                                    xalign 0.5
                                                                    xsize 200
                                                                    if current_a == 0.8:
                                                                        background "#4f7ad6"
                                                                    else:
                                                                        background "#1a45a1"


                                                                    action [
                                                                    SetScreenVariable("current_a", 0.8),
                                                                    SetField(selected_clothing, selected_colour,[current_r,current_g,current_b,current_a])
                                                                    ]


                                        hbox:
                                            spacing 5
                                            for count, a_colour in __builtin__.enumerate(persistent.colour_palette):
                                                frame:
                                                    background "#aaaaaa"
                                                    button:
                                                        background Color(rgb=(a_colour[0], a_colour[1], a_colour[2]))
                                                        xysize (40,40)
                                                        sensitive True
                                                        action [

                                                        SetScreenVariable("current_r", a_colour[0]),
                                                        SetScreenVariable("current_g", a_colour[1]),
                                                        SetScreenVariable("current_b", a_colour[2]),
                                                        SetScreenVariable("current_a", a_colour[3]),
                                                        SetField(selected_clothing, selected_colour,[current_r,current_g,current_b,current_a]),
                                                        ]
                                                        alternate [
                                                        Function(update_colour_palette, count, current_r, current_g, current_b, current_a)
                                                        ]






                # vbox: #Items selector
                #     #W/ item customixing window at bottom
                #
            vbox:
                spacing 15
                frame:
                    xysize (540, 500)
                    background "#aaaaaa"
                    vbox:
                        spacing 5
                        grid 2 1:
                            xfill True
                            spacing 5
                            frame:
                                background "#888888"
                                xfill True
                                textbutton "View Outfit Stats":
                                    style "textbutton_no_padding_highlight"
                                    text_style "serum_text_style"
                                    xfill True

                                    action ToggleScreenVariable("outfit_stats")
                            frame:
                                background "#888888"
                                xfill True
                                textbutton "Current Items":
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
                                        background "#888888"
                                        yfill True
                                        viewport:
                                            draggable True
                                            mousewheel True
                                            yfill True
                                            xsize 250
                                            vbox:

                                                textbutton "Sluttiness (Full Outfit): " + str(demo_outfit.slut_requirement):
                                                    style "textbutton_no_padding"
                                                    text_style "serum_text_style_traits"
                                                    xfill True

                                                    action NullAction()
                                                if demo_outfit.is_suitable_underwear_set():

                                                    textbutton "Sluttiness (Underwear): " + str(demo_outfit.get_underwear_slut_score()):
                                                        style "textbutton_no_padding"
                                                        text_style "serum_text_style_traits"
                                                        xfill True

                                                        action NullAction()
                                                else:
                                                    textbutton "Sluttiness (Underwear): Invalid":
                                                        style "textbutton_no_padding"
                                                        text_style "serum_text_style_traits"
                                                        xfill True

                                                        action NullAction()

                                                if demo_outfit.is_suitable_overwear_set():
                                                    textbutton "Sluttiness (Overwear): " + str(demo_outfit.get_overwear_slut_score()):
                                                        style "textbutton_no_padding"
                                                        text_style "serum_text_style_traits"
                                                        xfill True

                                                        action NullAction()
                                                else:
                                                    textbutton "Sluttiness (Overwear): Invalid":
                                                        style "textbutton_no_padding"
                                                        text_style "serum_text_style_traits"
                                                        xfill True

                                                        action NullAction()

                                                textbutton "Tits Visible: " + str(demo_outfit.tits_visible()):
                                                    style "textbutton_no_padding"
                                                    text_style "serum_text_style_traits"
                                                    xfill True

                                                    action NullAction()
                                                textbutton "Tits Usable: " + str(demo_outfit.tits_available()):
                                                    style "textbutton_no_padding"
                                                    text_style "serum_text_style_traits"
                                                    xfill True

                                                    action NullAction()
                                                textbutton "Wearing a Bra: " + str(demo_outfit.wearing_bra()):
                                                    style "textbutton_no_padding"
                                                    text_style "serum_text_style_traits"
                                                    xfill True

                                                    action NullAction()
                                                textbutton "Bra Covered: " + str(demo_outfit.bra_covered()):
                                                    style "textbutton_no_padding"
                                                    text_style "serum_text_style_traits"
                                                    xfill True

                                                    action NullAction()
                                                textbutton "Pussy Visible: " + str(demo_outfit.vagina_visible()):
                                                    style "textbutton_no_padding"
                                                    text_style "serum_text_style_traits"
                                                    xfill True

                                                    action NullAction()
                                                textbutton "Pussy Usable: " + str(demo_outfit.vagina_available()):
                                                    style "textbutton_no_padding"
                                                    text_style "serum_text_style_traits"
                                                    xfill True

                                                    action NullAction()
                                                textbutton "Wearing Panties: " + str(demo_outfit.wearing_panties()):
                                                    style "textbutton_no_padding"
                                                    text_style "serum_text_style_traits"
                                                    xfill True

                                                    action NullAction()
                                                textbutton "Panties Covered: " + str(demo_outfit.panties_covered()):
                                                    style "textbutton_no_padding"
                                                    text_style "serum_text_style_traits"
                                                    xfill True

                                                    action NullAction()
                            vbox:
                                frame:
                                    background "#888888"

                                    xfill True
                                    viewport:
                                            scrollbars "vertical"
                                            mousewheel True
                                            yfill True
                                            xfill True
                                            vbox:

                                                spacing 5 #TODO: Add a viewport here too.
                                                for cloth in starting_outfit.upper_body + starting_outfit.lower_body + starting_outfit.feet + starting_outfit.accessories:
                                                    if not cloth.is_extension: #Don't list extensions for removal.
                                                        button:
                                                            background Color(rgb = (cloth.colour[0], cloth.colour[1], cloth.colour[2]))

                                                            action [ # NOTE: Left click makes more sense for selection than right clicking

                                                            SetScreenVariable("selected_from_outfit", cloth),
                                                            SetScreenVariable("catagory_selected", get_catagory(cloth)),
                                                            SetScreenVariable("selected_clothing", cloth),
                                                            If(selected_clothing is cloth, SetScreenVariable("selected_clothing", None)),
                                                            If(demo_outfit.has_clothing(cloth) and selected_clothing is cloth,
                                                            [Function(demo_outfit.remove_clothing, cloth), #Remove the cloth
                                                            Function(apply_method, demo_outfit, cloth)]), # Add the copy of cloth
                                                            Function(apply_method, demo_outfit, cloth),  # Add the copy of cloth
                                                            SetScreenVariable("current_r",cloth.colour[0]),
                                                            SetScreenVariable("current_g",cloth.colour[1]),
                                                            SetScreenVariable("current_b",cloth.colour[2]),
                                                            SetScreenVariable("current_a",cloth.colour[3]),


                                                            Show("mannequin", None, demo_outfit) # Make sure it is showing the correct outfit during changes, demo_outfit is a copy of starting_outfit

                                                            ]
                                                            alternate [
                                                            Function(starting_outfit.remove_clothing, cloth),
                                                            Function(demo_outfit.remove_clothing, cloth)
                                                            ]
                                                            xalign 0.5
                                                            xfill True
                                                            yfill True
                                                            text cloth.name xalign 0.5 yalign 0.5 xfill True yfill True style "custom_outfit_style"


                frame:
                    background "#aaaaaa"

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
                                        background "#888888"
                                        xsize 250
                                        vbox:
                                            xalign 0.5
                                            textbutton "Save Outfit":
                                                style "textbutton_no_padding_highlight"
                                                text_style "serum_text_style"
                                                xfill True

                                                action [
                                                    If(target_wardrobe is mc.designed_wardrobe, Return(starting_outfit.get_copy()),
                                                    [Return(starting_outfit)]), #TODO: Commit changes to a person only when using the "Save Outfit", right now the changes are not saved to the Wardrobe only Outfit.copy
                                                    Hide("mannequin"),
                                                    Hide("outfit_creator")
                                                    ]

                                            textbutton "Abandon / Exit":
                                                style "textbutton_no_padding_highlight"
                                                text_style "serum_text_style"
                                                xfill True

                                                action [
                                                    If(target_wardrobe is mc.designed_wardrobe, [
                                                    Return("Not_New")]), # Solves default creation errors, but load outfit expects "No Return" instead so that will throw an error.
                                                    SetScreenVariable("starting_wardrobe", compare_outfit), # This doesn't really do anything at the moment. I'm thinking that an easy way of reseting the starting_outfit to be compare_outfit which is a copy of starting_outfit could be a good way of dealing with accidental commits and discarding unwanted changes. Without the need of further logic.
                                                    Hide("mannequin"), Hide("outfit_creator")
                                                    ]
                                    frame:
                                        background "#888888"
                                        xsize 250
                                        vbox:
                                            xalign 0.5
                                            textbutton "Export to [selected_xml]":
                                                style "textbutton_no_padding_highlight"
                                                text_style "serum_text_style"
                                                xfill True

                                                action [
                                                Function(custom_log_outfit, starting_outfit, outfit_class = outfit_class_selected,
                                                wardrobe_name = selected_xml),
                                                Function(renpy.notify, "Outfit exported to [selected_xml]")
                                                ]

                                            textbutton "Type: [outfit_class_selected]":
                                                xfill True
                                                style "textbutton_no_padding_highlight"
                                                text_style "serum_text_style"
                                                action [
                                                If(outfit_class_selected == "FullSets", SetScreenVariable("outfit_class_selected", "OverwearSets")),
                                                If(outfit_class_selected == "OverwearSets", SetScreenVariable("outfit_class_selected", "UnderwearSets")),
                                                If(outfit_class_selected == "UnderwearSets", SetScreenVariable("outfit_class_selected", "FullSets"))
                                                ]
                                                alternate [
                                                If(outfit_class_selected == "FullSets", SetScreenVariable("outfit_class_selected", "UnderwearSets")),
                                                If(outfit_class_selected == "OverwearSets", SetScreenVariable("outfit_class_selected", "FullSets")),
                                                If(outfit_class_selected == "UnderwearSets", SetScreenVariable("outfit_class_selected", "OverwearSets"))
                                                ]


                                vbox:

                                    frame:
                                        background "#888888"
                                        xsize 250
                                        textbutton "Import Design" action ToggleVariable("import_selection") style "textbutton_no_padding_highlight" text_style "serum_text_style" xfill True xalign 0.5
                                    if import_selection:
                                        frame:
                                            background "#888888"
                                            xsize 250
                                            viewport:
                                                scrollbars "vertical"
                                                mousewheel True
                                                draggable True
                                                vbox:
                                                    for n in get_xml_files_from_path(["game/wardrobes/", "game/Mods/Wardrobes/"]):
                                                        textbutton n:
                                                            style "textbutton_no_padding_highlight"
                                                            text_style "serum_text_style"
                                                            xfill True
                                                            xalign 0.5

                                                            action [
                                                            Show("import_outfit_manager", None, target_wardrobe, n)
                                                            ]
                                                            alternate [ #Right clicking selects the path that outfits should be exported to
                                                            SetVariable("selected_xml", n)
                                                            ]



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
