init -2 python:
    mannequin = None

screen hair_creator(person): ##Pass a completely blank outfit instance for a new outfit, or an already existing instance to load an old one.\
    #add "Paper_Background.png"
    modal True
    #zorder 0
    default catagory_selected = "Hair Style"

    default hair_style_colour_palette = [ 
        ["blond", [0.84,0.75,0.47,1]], 
        ["brown", [0.73,0.43,0.24,1]],
        ["black", [0.1,0.09,0.08,1]],
        ["red", [0.3,0.05,0.05,1]],
        ["hot pink", [1,0.5,0.8,1]],
        ["sky blue", [0.4,0.5,0.9,1]], 
        ["alt blond", [0.882, 0.733, 0.580,1]],
        ["light grey", [0.866, 0.835, 0.862,1]],
        ["fire red", [0.909, 0.368, 0.368,1]],
        ["knight red", [0.745, 0.117, 0.235,1]],
        ["purple" , [0.686, 0.156, 0.686,1]],
        ["dark grey" , [0.705, 0.690, 0.709,1]],
        ["turquoise" , [0.435, 0.807, 0.788,1]],
        ["lime green" , [0.647, 0.854, 0.564,1]],
        ["mango" , [0.894, 0.737, 0.466,1]],
        ["ocean" , [0.188, 0.494, 0.611,1]],
        ["pulp" , [0.643, 0.439, 0.541,1]],
        ["saturated" , [0.905, 0.898, 0.513,1]],
        ["emerald" , [0.098, 0.721, 0.541,1]],
        ["light brown" , [0.658, 0.537, 0.380,1]]
        ]

    if mannequin is None:
        $ mannequin = create_random_person()
    
    $ mannequin.body_type = person.body_type
    $ mannequin.face_style = person.face_style
    $ mannequin.expression_images = person.expression_images
    $ mannequin.height = person.height
    $ mannequin.hair_style = person.hair_style
    $ mannequin.tits = person.tits
    $ mannequin.outfit = person.outfit
    $ mannequin.idle_pose = person.idle_pose
    $ mannequin.body_images = person.body_images
    $ mannequin.draw_person(emotion="happy")

    default valid_catagories = ["Hair Style"] #Holds the valid list of catagories strings to be shown at the top.
   
    $ catagories_mapping = {
        "Hair Style": [hair_styles]
    }

    default bar_select = 0 # 0 is nothing selected, 1 is red, 2 is green, 3 is blue, and 4 is alpha

    default selected_colour = "colour" #If secondary we are alterning the patern colour. When changed it updates the colour of the clothing item. Current values are "colour" and "colour_pattern"
    default current_r = person.hair_style.colour[0]
    default current_g = person.hair_style.colour[1]
    default current_b = person.hair_style.colour[2]
    default current_a = person.hair_style.colour[3]

    default selected_hair_colour = person.hair_colour
    default selected_hair_style = person.hair_style

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
                            action [SetScreenVariable("catagory_selected",catagory),
                                SetField(mannequin, "hair_style", selected_hair_style),
                                SetScreenVariable("selected_colour", "colour")] #Set the clothing to None when you change catagories to avoid breaking the clothing add function assignment

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
                                if catagory_selected in catagories_mapping:
                                    #    $ valid_check = catagories_mapping[catagory_selected][1]
                                    #    $ apply_method = catagories_mapping[catagory_selected][2]
                                    #    $ cloth_list_length = len(catagories_mapping[catagory_selected][0])
                                    for hair_style_item in catagories_mapping[catagory_selected][0]:
                                        textbutton hair_style_item.name:
                                            style "textbutton_style"
                                            text_style "textbutton_text_style"
                                            background "#1a45a1"
                                            hover_background "#3a65c1"
                                            xfill True
                                            sensitive True
                                            action [
                                                SetScreenVariable("selected_colour", "colour"), 
                                                SetScreenVariable("selected_hair_style", hair_style_item),
                                                SetField(hair_style_item, "colour", [current_r, current_g, current_b, current_a]),
                                                SetField(mannequin, "hair_style", hair_style_item),
                                                Function(mannequin.draw_person)]

                    frame:
                        #THIS IS WHERE SELECTED ITEM OPTIONS ARE SHOWN
                        xysize (605, 480)
                        background "#888888"
                        vbox:
                            spacing 10
                            if selected_hair_style is not None:
                                text selected_hair_style.name style "textbutton_text_style"

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
                                        action NullAction()

                                    frame:
                                        background Color(rgb=(current_r,current_g,current_b,current_a))
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
                                for block_count, hair_colour_list in __builtin__.enumerate(split_list_in_blocks(hair_style_colour_palette, 10)):
                                    hbox:
                                        spacing 5
                                        xalign 0.5
                                        xanchor 0.5
                                        yanchor (block_count * .1)
                                        for count, hair_colour in __builtin__.enumerate(hair_colour_list):
                                            frame:
                                                background "#aaaaaa"
                                                button:
                                                    background Color(rgb=(hair_colour[1][0], hair_colour[1][1], hair_colour[1][2]))
                                                    xysize (40,40)
                                                    sensitive True
                                                    action [
                                                        SetScreenVariable("selected_hair_colour", hair_colour[0]),
                                                        SetScreenVariable("current_r", hair_colour[1][0]), SetScreenVariable("current_g", hair_colour[1][1]), SetScreenVariable("current_b", hair_colour[1][2]), SetScreenVariable("current_a", hair_colour[1][3])]
                                                    # We use a fixed pallette of hair colours
                                                    # alternate Function(update_colour_palette, count, current_r, current_g, current_b, current_a)

                        if selected_hair_style:
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
                                action [SetField(selected_hair_style, "colour", [current_r,current_g,current_b,current_a]), 
                                    SetField(mannequin, "hair_colour", selected_hair_colour),
                                    SetField(mannequin, "hair_style", selected_hair_style), 
                                    Function(mannequin.draw_person)]
                                #hovered [SetField(selected_hair_style, selected_colour,[current_r,current_g,current_b,current_a]), SetField(mannequin, "hair_style", selected_hair_style), Function(mannequin.draw_person)]


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
                                background Color(rgb = (selected_hair_style.colour[0], selected_hair_style.colour[1], selected_hair_style.colour[2]))
                                xysize (380, 40)
                                action NullAction()
                                xalign 0.5
                                yalign 0.0
                                text selected_hair_style.name xalign 0.5 xanchor 0.5 yalign 0.5 yanchor 0.5 style "outfit_style"




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
                        textbutton "Save Haircut" action [SetField(person, "hair_style", selected_hair_style), SetField(person, "hair_colour", selected_hair_colour),
                            Function(person.draw_person), Return] style "textbutton_style" text_style "textbutton_text_style" text_text_align 0.5 text_xalign 0.5 xysize (155,80)
                        textbutton "Abandon Design" action Return style "textbutton_style" text_style "textbutton_text_style" text_text_align 0.5 text_xalign 0.5 xysize (185,80)
#    fixed: #TODO: Move this to it's own screen so it can be shown anywhere
#        pos (1450,0)

        #add mannequin_average
    #    for cloth in demo_outfit.generate_draw_list(None,"stand3"):
        #    add cloth
