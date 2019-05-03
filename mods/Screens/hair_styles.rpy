init -1 python:
    mannequin = None

screen hair_creator(person): ##Pass a completely blank outfit instance for a new outfit, or an already existing instance to load an old one.\
    #add "Paper_Background.png"
    modal True
    #zorder 0
    default catagory_selected = "Hair Style"

    default demo_outfit = person.hair_style.get_copy()

    if mannequin == None:
        $ mannequin = create_random_person()
    $ mannequin.body_type = person.body_type
    $ mannequin.face_style = person.face_style
    $ mannequin.skin = person.skin
    $ mannequin.expression_images = person.expression_images
    $ mannequin.height = person.height
    $ mannequin.hair_style = person.hair_style
    $ mannequin.tits = person.tits
    $ mannequin.outfit = person.outfit
    $ mannequin.idle_pose = person.idle_pose
    $ mannequin.body_images = person.body_images
    $ renpy.scene("Active")



    $ mannequin.draw_person()


    $ valid_catagories = ["Hair Style"] #Holds the valid list of catagories strings to be shown at the top.

    $ catagories_mapping = {
        #"Hair Color": [list_of_hairs]
        "Hair Style": [hair_styles]}

    default bar_select = 0 # 0 is nothing selected, 1 is red, 2 is green, 3 is blue, and 4 is alpha

    default selected_colour = "colour" #If secondary we are alterning the patern colour. When changed it updates the colour of the clothing item. Current values are "colour" and "colour_pattern"
    default current_r = 1.0
    default current_g = 1.0
    default current_b = 1.0
    default current_a = 1.0

    default selected_clothing = person.hair_style.get_copy()

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
                            action [SetScreenVariable("catagory_selected",catagory), SetScreenVariable("selected_clothing", selected_clothing), SetScreenVariable("selected_colour", "colour")] #Set the clothing to None when you change catagories to avoid breaking the clothing add function assignment

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
                                #    $ valid_check = catagories_mapping[catagory_selected][1]
                                #    $ apply_method = catagories_mapping[catagory_selected][2]
                                    $ cloth_list_length = len(catagories_mapping[catagory_selected][0])
                                    for cloth in catagories_mapping[catagory_selected][0]:
                                        textbutton cloth.name:
                                            style "textbutton_style"
                                            text_style "textbutton_text_style"


                                            background "#1a45a1"
                                            hover_background "#3a65c1"
                                            xfill True
                                            sensitive True
                                            action [SetScreenVariable("selected_clothing", cloth), SetScreenVariable("selected_colour", "colour"), SetField(mannequin, "hair_style", selected_clothing), Function(renpy.scene, "Active"), Function(mannequin.draw_person)]

                    frame:
                        #THIS IS WHERE SELECTED ITEM OPTIONS ARE SHOWN
                        xysize (605, 480)
                        background "#888888"
                        vbox:
                            spacing 10
                            if selected_clothing is not None:
                                text selected_clothing.name style "textbutton_text_style"

                                hbox:
                                    spacing -5 #We will manually handle spacing so we can have our colour predictor frames
                                    textbutton "Primary Colour":
                                        style "textbutton_style"
                                        text_style "textbutton_text_style"
                                        if selected_colour == "colour":
                                            background "#4f7ad6"
                                            hover_background "#4f7ad6"
                                        else:
                                            background "#1a45a1"
                                            hover_background "#3a65c1"
                                        sensitive True
                                        if selected_colour == "colour_pattern": #Hopefully will support patterns for hairs
                                            action [SetField(selected_clothing,"colour_pattern",[current_r,current_g,current_b,current_a]), SetScreenVariable("selected_colour","colour"), SetScreenVariable("current_r",selected_clothing.colour[0]), SetScreenVariable("current_g",selected_clothing.colour[1]), SetScreenVariable("current_b",selected_clothing.colour[2]), SetScreenVariable("current_a",selected_clothing.colour[3])]
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

                                            bar value ScreenVariableValue("current_r", 1.0)  xsize 120 ysize 45 style style.slider #unhovered #SetScreenVariable("current_r",__builtin__.round(current_r,2))
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

                                            bar value ScreenVariableValue("current_g", 1.0) xsize 120 ysize 45 style style.slider #unhovered SetScreenVariable("current_g",__builtin__.round(current_g,2))
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

                                            bar value ScreenVariableValue("current_b", 1.0) xsize 120 ysize 45 style style.slider #unhovered SetScreenVariable("current_b",__builtin__.round(current_b,2))

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
                                        action SetScreenVariable("current_a", 1.0)

                                    button:
                                        if current_a == 0.95:
                                            background "#4f7ad6"
                                        else:
                                            background "#1a45a1"
                                        text "Sheer" style "menu_text_style" xalign 0.5 xanchor 0.5 yalign 0.5 yanchor 0.5
                                        xysize (120, 40)
                                        action SetScreenVariable("current_a", 0.95)

                                    button:
                                        if current_a == 0.8:
                                            background "#4f7ad6"
                                        else:
                                            background "#1a45a1"
                                        text "Translucent" style "menu_text_style" xalign 0.5 xanchor 0.5 yalign 0.5 yanchor 0.5
                                        xysize (120, 40)
                                        action SetScreenVariable("current_a", 0.8)
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
                                                action [SetScreenVariable("current_r", a_colour[0]), SetScreenVariable("current_g", a_colour[1]), SetScreenVariable("current_b", a_colour[2]), SetScreenVariable("current_a", a_colour[3])]
                                                alternate Function(update_colour_palette, count, current_r, current_g, current_b, current_a)

                        if selected_clothing:
                            textbutton "Dye Hair":
                                style "textbutton_style"
                                text_style "textbutton_text_style"
                                background "#1a45a1"
                                hover_background "#3a65c1"
                                xalign 0.5
                                yalign 1.0
                                xanchor 0.5
                                yanchor 1.0
                                sensitive True
                                action [SetField(selected_clothing, selected_colour,[current_r,current_g,current_b,current_a]), SetField(mannequin, "hair_style", selected_clothing), Function(renpy.scene, "Active"), Function(mannequin.draw_person)]
                                #hovered [SetField(selected_clothing, selected_colour,[current_r,current_g,current_b,current_a]), SetField(mannequin, "hair_style", selected_clothing), Function(mannequin.draw_person)]


        vbox:
            spacing 15
            frame:
                xysize (440, 500)
                background "#aaaaaa"
                padding (20,20)
                vbox:
                    spacing 15
                    text "Current Hair Style" style "textbutton_text_style"
                    frame:
                        xfill True
                        yfill True
                        background "#888888"
                        vbox:
                            spacing 5 #TODO: Add a viewport here too.
                            button:
                                background Color(rgb = (selected_clothing.colour[0], selected_clothing.colour[1], selected_clothing.colour[2]))
                                xysize (380, 40)
                                action NullAction()
                                xalign 0.5
                                yalign 0.0
                                text selected_clothing.name xalign 0.5 xanchor 0.5 yalign 0.5 yanchor 0.5 style "outfit_style"




            frame:
                background "#aaaaaa"
                xysize (440, 500)
                padding (20,20)
                vbox:
                    yalign 0.0
                    hbox:
                        yalign 1.0
                        xalign 0.5
                        xanchor 0.5
                        spacing 50
                        textbutton "Save Haircut" action [SetField(person,"hair_style", selected_clothing), Function(person.draw_person), Return] style "textbutton_style" text_style "textbutton_text_style" text_text_align 0.5 text_xalign 0.5 xysize (155,80)
                        textbutton "Abandon Design" action Return style "textbutton_style" text_style "textbutton_text_style" text_text_align 0.5 text_xalign 0.5 xysize (185,80)
#    fixed: #TODO: Move this to it's own screen so it can be shown anywhere
#        pos (1450,0)

        #add mannequin_average
    #    for cloth in demo_outfit.generate_draw_list(None,"stand3"):
        #    add cloth
