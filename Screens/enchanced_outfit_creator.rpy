#init -1 python: #TODO: Go through everything again so that it uses copies where it should and remove instances where it shouldn't.
                      # I want outfits to be editable without forcing commitet changes upon `selected_clothing`
                      # Right now, this seems to only be a problem when editing a `Person`'s wardrobe since the MC Wardrobe always use copies anyway.

#    def add_outfit(self, new_outfit): # Removes the possibility of duplicates when manipulating non- copies, decide on how to proceed before enabling or removing.
#        if new_outfit in self.outfits:
#            self.outfits.remove(new_outfit)
#            self.outfits.append(new_outfit)
#        else:
#            self.outfits.append(new_outfit)
#
#    Wardrobe.add_outfit = add_outfit

init 2:

    $ import_selection = False # Decides if the import viewport is showing

    screen outfit_creator(starting_outfit, target_wardrobe = mc.designed_wardrobe): ##Pass a completely blank outfit instance for a new outfit, or an already existing instance to load an old one.\
        add "Paper_Background.png"
        modal True
        zorder 100
        default catagory_selected = "Panties"
        default mannequin = True


        if target_wardrobe == mc.designed_wardrobe: # Always make copies if MC Wardrobe
            default demo_outfit = starting_outfit.get_copy()
        else:
            default demo_outfit = starting_outfit # We usually want to directly manipulate their outfit

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
                                text_style "textbutton_text_style"
                                if catagory == catagory_selected:
                                    background "#4f7ad6"
                                    hover_background "#4f7ad6"
                                else:
                                    background "#1a45a1"
                                    hover_background "#3a65c1"
                                text_align(0.5,0.5)
                                text_anchor(0.5,0.5)
                                xysize (220, 60)
                                action [SetScreenVariable("catagory_selected",catagory), SetScreenVariable("selected_clothing", None), SetScreenVariable("selected_colour", "colour"), If(selected_clothing is not None, Function(demo_outfit.remove_clothing, selected_clothing))] #Set the clothing to None when you change catagories to avoid breaking the clothing add function assignments
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
                                                text_style "textbutton_text_style"
                                                if valid_check(starting_outfit, cloth):
                                                    background "#1a45a1"
                                                    hover_background "#3a65c1"
                                                else:
                                                    background "#444444"
                                                    hover_background "#444444"
                                                xfill True
                                                sensitive valid_check(starting_outfit, cloth)
                                                action SetScreenVariable("selected_clothing", cloth), SetScreenVariable("selected_colour", "colour")
                                                hovered [
                                                If(selected_clothing, [Function(demo_outfit.remove_clothing, selected_clothing), Function(apply_method, demo_outfit, cloth)],
                                                Function(apply_method, demo_outfit, cloth)),
                                                Show("mannequin", None, demo_outfit)]
                                                unhovered [If(cloth is selected_clothing, NullAction(), Function(demo_outfit.remove_clothing, cloth)), If(selected_clothing is not None and not demo_outfit.has_clothing(selected_clothing), Function(apply_method, demo_outfit, selected_clothing))]

                        frame:
                            #THIS IS WHERE SELECTED ITEM OPTIONS ARE SHOWN
                            xysize (605, 480)
                            background "#888888"
                            vbox:
                                spacing 10
                                if selected_clothing is not None:
                                    text selected_clothing.name + ", +" + __builtin__.str(selected_clothing.slut_value) + " Slut Requirement" style "textbutton_text_style"
                                    if __builtin__.type(selected_clothing) is Clothing: #Only clothing items have patterns, facial accessories do not (currently).
                                        hbox:
                                            spacing 5
                                            for pattern in selected_clothing.supported_patterns:
                                                textbutton pattern:
                                                    style "textbutton_style"
                                                    text_style "textbutton_text_style"
                                                    if selected_clothing.pattern == selected_clothing.supported_patterns[pattern]:
                                                        background "#4f7ad6"
                                                        hover_background "#4f7ad6"
                                                    else:
                                                        background "#1a45a1"
                                                        hover_background "#3a65c1"
                                                    xfill False
                                                    xsize 120
                                                    text_xalign 0.5
                                                    text_xanchor 0.5
                                                    text_size 12
                                                    sensitive True
                                                    action SetField(selected_clothing,"pattern",selected_clothing.supported_patterns[pattern])

                                    hbox:
                                        spacing -5 #We will manually handle spacing so we can have our colour predictor frames
                                        textbutton "Primary Colour":
                                            style "textbutton_style"
                                            text_style "textbutton_text_style"
                                            text_size 12
                                            xsize 120
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
                                            xysize (45,45)
                                            yanchor 0.5
                                            yalign 0.5

                                        if __builtin__.type(selected_clothing) is Clothing and selected_clothing.pattern is not None:
                                            null width 15
                                            textbutton "Pattern Colour":
                                                style "textbutton_style"
                                                text_style "textbutton_text_style"
                                                text_size 12
                                                xsize 120
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
                                                xysize (45,45)
                                                yanchor 0.5
                                                yalign 0.5

                                    hbox:
                                        spacing 10
                                        vbox:
                                            text "Red" style "textbutton_text_style"
                                            hbox:
                                                if bar_select == 1:
                                                    frame:
                                                        input default current_r length 4 changed colour_changed_r allow ".0123456789" style "menu_text_style"
                                                        xsize 70
                                                        ysize 50
                                                else:
                                                    button:
                                                        background "#888888"
                                                        action SetScreenVariable("bar_select",1)
                                                        text "%.2f" % current_r style "menu_text_style"
                                                        xsize 70
                                                        ysize 50

                                                bar value ScreenVariableValue("current_r", 1.0) xsize 120 ysize 45 style style.slider unhovered [SetScreenVariable("current_r",__builtin__.round(current_r,2)), SetField(selected_clothing, selected_colour,[current_r,current_g,current_b,current_a])]
                                        vbox:
                                            text "Green" style "textbutton_text_style"
                                            hbox:
                                                if bar_select == 2:
                                                    frame:
                                                        input default current_g length 4 changed colour_changed_g allow ".0123456789" style "menu_text_style"
                                                        xsize 70
                                                        ysize 50
                                                else:
                                                    button:
                                                        background "#888888"
                                                        action SetScreenVariable("bar_select",2)
                                                        text "%.2f" % current_g style "menu_text_style"
                                                        xsize 70
                                                        ysize 50

                                                bar value ScreenVariableValue("current_g", 1.0) xsize 120 ysize 45 style style.slider unhovered [SetScreenVariable("current_g",__builtin__.round(current_g,2)), SetField(selected_clothing, selected_colour,[current_r,current_g,current_b,current_a])]
                                        vbox:
                                            text "Blue" style "textbutton_text_style"
                                            hbox:
                                                if bar_select == 3:
                                                    frame:
                                                        input default current_b length 4 changed colour_changed_b allow ".0123456789" style "menu_text_style"
                                                        xsize 70
                                                        ysize 50
                                                else:
                                                    button:
                                                        background "#888888"
                                                        action SetScreenVariable("bar_select",3)
                                                        text "%.2f" % current_b style "menu_text_style"
                                                        xsize 70
                                                        ysize 50

                                                bar value ScreenVariableValue("current_b", 1.0) xsize 120 ysize 45 style style.slider unhovered [SetScreenVariable("current_b",__builtin__.round(current_b,2)), SetField(selected_clothing, selected_colour,[current_r,current_g,current_b,current_a])]

                                    text "Transparency: " style "menu_text_style"
                                    hbox:
                                        spacing 20
                                        button:
                                            if current_a == 1.0:
                                                background "#4f7ad6"
                                            else:
                                                background "#1a45a1"
                                            text "Normal" style "menu_text_style" xalign 0.5 xanchor 0.5 yalign 0.5 yanchor 0.5
                                            xysize (120, 40)
                                            action [SetScreenVariable("current_a", 1.0),SetField(selected_clothing, selected_colour,[current_r,current_g,current_b,current_a])]

                                        button:
                                            if current_a == 0.95:
                                                background "#4f7ad6"
                                            else:
                                                background "#1a45a1"
                                            text "Sheer" style "menu_text_style" xalign 0.5 xanchor 0.5 yalign 0.5 yanchor 0.5
                                            xysize (120, 40)
                                            action [SetScreenVariable("current_a", 0.95), SetField(selected_clothing, selected_colour,[current_r,current_g,current_b,current_a])]

                                        button:
                                            if current_a == 0.8:
                                                background "#4f7ad6"
                                            else:
                                                background "#1a45a1"
                                            text "Translucent" style "menu_text_style" xalign 0.5 xanchor 0.5 yalign 0.5 yanchor 0.5
                                            xysize (120, 40)
                                            action [SetScreenVariable("current_a", 0.8), SetField(selected_clothing, selected_colour,[current_r,current_g,current_b,current_a])]

                                                            #[SetField(cloth,"colour",[current_r,current_g,current_b,current_a]), Function(apply_method, demo_outfit, cloth)]

                                    hbox:
                                        spacing 5
                                        xalign 0.5
                                        xanchor 0.5
                                        for count, a_colour in __builtin__.enumerate(persistent.colour_palette):
                                            frame:
                                                background "#aaaaaa"
                                                button:
                                                    background Color(rgb=(a_colour[0], a_colour[1], a_colour[2]))
                                                    xysize (40,40)
                                                    sensitive True
                                                    action [
                                                    SetScreenVariable("selected_colour","colour"),
                                                    SetScreenVariable("current_r", a_colour[0]),
                                                    SetScreenVariable("current_g", a_colour[1]),
                                                    SetScreenVariable("current_b", a_colour[2]),
                                                    SetScreenVariable("current_a", a_colour[3]),
                                                    SetField(selected_clothing, selected_colour,[current_r,current_g,current_b,current_a]),
                                                    ]
                                                    alternate Function(update_colour_palette, count, current_r, current_g, current_b, current_a)



                            #TODO: Change this "Add" butotn to "Remove" when you're selecting something that is arleady part of the outfit.
                            if selected_clothing:
                                textbutton "Add to Outfit":
                                    style "textbutton_style"
                                    text_style "textbutton_text_style"
                                    background "#1a45a1"
                                    hover_background "#3a65c1"
                                    xalign 0.5
                                    yalign 1.0
                                    xanchor 0.5
                                    yanchor 1.0
                                    sensitive [
                                    If(demo_outfit.has_clothing(selected_clothing), # If it's already in the outfit it is valid so don't make a check.
                                    NullAction(),
                                    valid_check(starting_outfit, selected_clothing))]

                                    action [ # NOTE: We are no longer interested in the demo outfit so view the final outfit
                                    SetField(selected_clothing, selected_colour,[current_r,current_g,current_b,current_a]),
                                    Function(apply_method, starting_outfit, selected_clothing), Show("mannequin", None, starting_outfit)]


                                    hovered [
                                    Function(apply_method, demo_outfit, selected_clothing)
                                    ]




                # vbox: #Items selector
                #     #W/ item customixing window at bottom
                #
            vbox:
                spacing 15
                frame:
                    xysize (540, 500)
                    background "#aaaaaa"
                    padding (20,20)
                    vbox:
                        spacing 15
                        text "Current Items" style "textbutton_text_style"
                        frame:
                            xfill True
                            yfill True
                            background "#888888"
                            vbox:
                                spacing 5 #TODO: Add a viewport here too.
                                for cloth in starting_outfit.upper_body + starting_outfit.lower_body + starting_outfit.feet + starting_outfit.accessories:
                                    if not cloth.is_extension: #Don't list extensions for removal.
                                        button:
                                            background Color(rgb = (cloth.colour[0], cloth.colour[1], cloth.colour[2]))
                                            xysize (380, 40)
                                            action [ # NOTE: Left click makes more sense for selection than right clicking
                                            SetScreenVariable("selected_clothing", cloth),
                                            SetScreenVariable("current_r",cloth.colour[0]),
                                            SetScreenVariable("current_g",cloth.colour[1]),
                                            SetScreenVariable("current_b",cloth.colour[2]),
                                            SetScreenVariable("current_a",cloth.colour[3]),
                                            Function(apply_method, demo_outfit, cloth.get_copy()),
                                            Show("mannequin", None, starting_outfit) # Make sure it is showing the correct outfit

                                            ]
                                            alternate [Function(starting_outfit.remove_clothing, cloth),Function(demo_outfit.remove_clothing, cloth)]
                                            xalign 0.5
                                            yalign 0.0
                                            text cloth.name xalign 0.5 xanchor 0.5 yalign 0.5 yanchor 0.5 style "outfit_style"

                frame:
                    background "#aaaaaa"
                    xysize (540, 500)
                    #padding (20,20)
                    hbox:
                        vbox:
                            yalign 0.0
                            text "Outfit Stats" style "menu_text_style" size 20
                            text "Sluttiness (Full Outfit) : " + str(demo_outfit.slut_requirement) style "menu_text_style"
                            if demo_outfit.is_suitable_underwear_set():
                                text "Sluttiness (Underwear): " + str(demo_outfit.get_underwear_slut_score()) style "menu_text_style"
                            else:
                                text "Sluttiness (Underwear): Invalid" style "menu_text_style"

                            if demo_outfit.is_suitable_overwear_set():
                                text "Sluttiness (Overwear): " + str(demo_outfit.get_overwear_slut_score()) style "menu_text_style"
                            else:
                                text "Sluttiness (Overwear): Invalid" style "menu_text_style"
                            text "Tits Visible: " + str(demo_outfit.tits_visible()) style "menu_text_style"
                            text "Tits Usable: " + str(demo_outfit.tits_available()) style "menu_text_style"
                            text "Wearing a Bra: " + str(demo_outfit.wearing_bra()) style "menu_text_style"
                            text "Bra Covered: " + str(demo_outfit.bra_covered()) style "menu_text_style"
                            text "Pussy Visible: " + str(demo_outfit.vagina_visible()) style "menu_text_style"
                            text "Pussy Usable: " + str(demo_outfit.vagina_available()) style "menu_text_style"
                            text "Wearing Panties: " + str(demo_outfit.wearing_panties()) style "menu_text_style"
                            text "Panties Covered: " + str(demo_outfit.panties_covered()) style "menu_text_style"

                            hbox:
                                #yalign 1.0
                                #xalign 0.4
                                #xanchor 0.5
                                spacing 10
                                vbox:
                                    textbutton "Save Outfit" style "textbutton_style" text_style "textbutton_text_style" text_text_align 0.5 text_xalign 0.5 action [
                                    If(target_wardrobe is mc.designed_wardrobe, Return(starting_outfit.get_copy()),
                                    [Return(starting_outfit)]), # <--- Function(target_wardrobe.add_outfit, starting_outfit), TODO: Get this to work without making duplicates and forcing changes.
                                    Hide("mannequin"),
                                    Hide("outfit_creator")]
                                    textbutton "Abandon Design" action [If(target_wardrobe is mc.designed_wardrobe, Return("Not_New")), Hide("mannequin"), Hide("outfit_creator")] style "textbutton_style" text_style "textbutton_text_style" text_text_align 0.5 text_xalign 0.5
                        vbox:
                            textbutton "Import Design" action ToggleVariable("import_selection") style "textbutton_style" text_style "textbutton_text_style" text_text_align 0.5 text_xalign 0.5 xsize 250 xanchor 0.0
                            if import_selection:
                                viewport:
                                    scrollbars "vertical"
                                    mousewheel True
                                    ysize 440
                                    vbox:
                                        for n in os.listdir("game/wardrobes/"):
                                            textbutton n action [Show("import_outfit_manager", None, target_wardrobe, n)] style "textbutton_style" text_style "textbutton_text_style" text_text_align 0.5 text_xalign 0.5 xanchor 0.0








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
