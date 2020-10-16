
    # hair_styles
    # list_of_body_types
    # list_of_faces
    # list_of_tits
    # list_of_skins
    # the_person.age
    # the_person.name
    # the_person.last_name
init -2 python:

    def get_part_display_image(self, part_to_display = None): # Takes a specific part that it attempts to display based on other attributes of a person, note that it's done in a lazy way so refactoring it is fair game. It is a tweaked def build_person_displayable()
        cs = renpy.current_screen()

        body_type = None
        tits = None

        if part_to_display in pube_styles:
            part_to_display.colour = self.pubes_colour
        if part_to_display in hair_styles:
            part_to_display.colour = self.hair_colour[1]

        if part_to_display in cs.scope["list_of_cup_sizes"]:
            tits = part_to_display
            part_to_display = self.body_images

        if part_to_display in list_of_body_types:
            body_type = part_to_display
            part_to_display = self.body_images

        position = "stand3"
        emotion = "default"
        special_modifier = None
        lighting = None

        list_of_bodies = cs.scope["list_of_bodies"]

        displayable_list = [] # We will be building up a list of displayables passed to us by the various objects on the person (their body, clothing, etc.)


        if part_to_display in list_of_bodies: # Seperate the parts (Clothing) so we draw things individually.
            displayable_list.append(part_to_display.generate_item_displayable((self.body_type if body_type is None else body_type), (self.tits if tits is None else tits), position, lighting)) #Add the body displayable

        if part_to_display in list_of_faces:
            displayable_list.append(Image("character_images/" + emotion + "_" + part_to_display + "_" + position + "_" + self.skin + ".png")) #Get the face displayable
            displayable_list.append(self.hair_style.generate_item_displayable("standard_body", self.tits,position, lighting = lighting))
        #if part_to_display in hair_styles and type(part_to_display) is Clothing:
        #    displayable_list.append(self.expression_images.generate_emotion_displayable(position,emotion, special_modifier = special_modifier, eye_colour = self.eyes[1], lighting = lighting)) #Get the face displayable
        #    displayable_list.append(part_to_display.generate_item_displayable("standard_body", self.tits,position, lighting = lighting)) #Get hair

        if part_to_display in pube_styles:
            displayable_list.append(self.body_images.generate_item_displayable((self.body_type if body_type is None else body_type), (self.tits if tits is None else tits), position, lighting))
            displayable_list.append(part_to_display.generate_item_displayable((self.body_type if body_type is None else body_type), (self.tits if tits is None else tits), position, lighting))

        if displayable_list:
            size_render = renpy.render(displayable_list[0], 10, 10, 0, 0) #We need a render object to check the actual size of the body displayable so we can build our composite accordingly.
            the_size = size_render.get_size() # Get the size. Without it our displayable would be stuck in the top left when we changed the size ofthings inside it.
            x_size = __builtin__.int(the_size[0])
            y_size = __builtin__.int(the_size[1])


            #NOTE: default return for the_size is floats, even though it is in exact pixels. Use int here otherwise positional modifiers like xanchor and yalign do not work (no displayable is shown at all!)
            composite_list = [(x_size,y_size)] #Now we build a list of our parameters, done like this so they are arbitrarily long
            for display in displayable_list: # NOTE: Align images depending on what part is supposed to be in focus.
                if part_to_display in (hair_styles + list_of_faces):
                    composite_list.append((-150,10)) #Center all displaybles on the top left corner, because of how they are rendered they will all line up.

                elif part_to_display in pube_styles:
                    composite_list.append((-170, -400))
                elif tits is not None:
                    composite_list.append((-150,-160))
                else:
                    composite_list.append((-150,-200))

                composite_list.append(display) #Append the actual displayable

            final_image = Composite(*composite_list) # Create a composite image using all of the displayables

            return final_image

    #Person.get_part_display_image = get_part_display_image


    def custom_set_field(the_person, field, item):

        cs = renpy.current_screen()
        if item in cs.scope["list_of_bodies"]:
            the_person.match_skin(item.name)

        if item in list_of_faces:
            the_person.face_style = item
            the_person.match_skin(the_person.skin)

        else:
            vars(the_person)[field] = (item.get_copy() if hasattr(item, "get_copy") else item) # face_style, body_type and tits are string while body_images and hair_style are cloth items.

init 2 python:
    import collections

    def toggle_dict_key(key): # I'm still too dumb to understand the ToggleDict action

        cs = renpy.current_screen()

        if cs.scope["categories"][key][1] == False:
            cs.scope["categories"][key][1] = True
        else:
            cs.scope["categories"][key][1] = False

    #def get_part_image(part): # Get the image file path of a hair to display on the image_button
    # TODO: Maintain color information and maybe composite with face, eye color etc. intact


    #    image_set = part.position_sets.get("stand3")
    #    the_image = image_set.get_image("standard_body", "AA")
        #the_image = the_image.filename[:-4] + "_%s.png"
    #    return the_image.filename

screen body_customizer(the_person = the_person):
    # TODO: Make it so you can preview changes.
    #       Make images fit properly
    #       Maintain colors, possibly add color selection for hair and eyes (though I think I want to leave hair colors, and maybe hair overall since we have the hair salon)
    #       Add Clone action
    $ the_person.draw_person()
    $ renpy.block_rollback()
    modal True
    zorder 99

    default list_of_bodies = [white_skin, tan_skin, black_skin] #Assemble the cloth items into a list. Revisit this later if a default list is created
    default list_of_cup_sizes = [x[0] for x in list_of_tits] # Create a standarized list

    default editing_target = the_person

    default clone_name = the_person.name
    default clone_last_name = the_person.last_name
    default clone_age = the_person.age

    default fallback_person = copy.copy(the_person)

    default category_unsorted = {"face_style": [list_of_faces, False, 0], "tits": [list_of_cup_sizes, False, 1], "pubes_style": [pube_styles, False, 2],"body_images": [list_of_bodies, False, 3] , "body_type": [list_of_body_types, False, 4]} # "hair_style": [hair_styles, False, 0] # Key is the attribute to fetch via getattr, [0] is the list of items to select / display from and [1] is a bool to determine if [0] is shown
    default categories = collections.OrderedDict(sorted(category_unsorted.items(), key = lambda t: t[1][2]))
    frame:
        #area(0, 100, 1500, 900)
        ypos 50
        xpos 50
        xsize 1500
        ysize 1000
        hbox:
            xfill True
            vpgrid id "mainport":
                cols 1
                draggable True
                mousewheel True
                vbox:
                    for cat in categories:
                        hbox:
                            frame:
                                xsize 200
                                ysize 200

                                button:
                                    background "#666666"
                                    foreground Crop(( 0, 0, 190, 190), get_part_display_image(the_person, getattr(the_person, cat))) # TODO: Change positional alignment and crop size to fit all types of images

                                    ysize 190

                                    action Function(toggle_dict_key, cat) # Should probably be using ToggleDict here.

                            if categories[cat][1]:
                                frame:
                                    ysize 200
                                    vpgrid:

                                        yfill True

                                        cols 5
                                        side_xalign 1.0
                                        draggable True
                                        mousewheel True
                                        scrollbars "vertical"

                                        for item in categories[cat][0]:
                                            frame:
                                                xsize 200
                                                ysize 200
                                                button:
                                                    if item == getattr(the_person, cat):
                                                        background "#1aaa00"
                                                    foreground Crop(( 0, 0, 190, 190), get_part_display_image(the_person, item))
                                                    ysize 190
                                                    action [
                                                        If(fallback_person is None, SetScreenVariable("fallback_person", the_person)),
                                                        Function(custom_set_field, the_person, cat, item),
                                                        Function(renpy.notify, (str(item.name) if hasattr(item, "name") else item)),
                                                        Function(the_person.draw_person, show_person_info = False)

                                                    ]


            frame:
                xalign 1.0
                xsize 200
                ysize 200
                vbox:
                    textbutton "Save | Return":
                        xfill True

                        style "textbutton_no_padding_highlight"
                        text_style "serum_text_style"
                        action [Hide("body_customizer"), Function(clear_scene)]

                    textbutton "Discard | Undo":
                        xfill True

                        style "textbutton_no_padding_highlight"
                        text_style "serum_text_style"
                        action [ #TODO: Revisit this clause

                            SetField(the_person, "body_images", fallback_person.body_images),
                            SetField(the_person, "face_style", fallback_person.face_style),
                            SetField(the_person, "skin", fallback_person.skin),
                            SetField(the_person, "tits", fallback_person.tits),
                            SetField(the_person, "body_type", fallback_person.body_type),
                            SetField(the_person, "hair_style", fallback_person.hair_style),
                            SetField(the_person, "name", fallback_person.name),
                            SetField(the_person, "last_name", fallback_person.last_name),
                            SetField(the_person, "pubes_style", fallback_person.pubes_style),

                            Function(the_person.match_skin, fallback_person.skin),
                            Function(the_person.draw_person, show_person_info = False)
                            ]



init 2 python:

    def set_clone_names(new_name):

        cs = renpy.current_screen()
        if cs.scope["name_type"] == "name":
            cs.scope["clone_name"] = new_name
        if cs.scope["name_type"] == "last_name":
            cs.scope["clone_last_name"] = new_name

        renpy.restart_interaction()

screen name_select_popup(the_person): #
    modal True
    zorder 100
    default name_type = None
    default editing_target = the_person

    if "clone_name" not in renpy.current_screen().scope:
        default clone_name = None
    if "clone_last_name" not in renpy.current_screen().scope:
        default clone_last_name = None

    default categories = {"Name": ["name", False, "clone_name"], "Last Name": ["last_name", False, "clone_last_name"]}
    frame:
        xalign 0.3
        yalign 0.4
        xsize 700
        ysize 500
        vbox:
            for cat in categories:
                frame:
                    grid 1 2:
                        frame:
                            background "#666666"
                            ysize 60
                            xfill True
                            text str(cat) style "serum_text_style" xalign 0.5
                        frame:
                            button:

                                if not categories[cat][1]:
                                    text (getattr(the_person, categories[cat][0]) if renpy.current_screen().scope[str(categories[cat][2])] is None else renpy.current_screen().scope[str(categories[cat][2])]) style "serum_text_style"
                                xfill True
                                action Function(toggle_dict_key, cat)
                                hovered SetScreenVariable("name_type", categories[cat][0])

                                if categories[cat][1]:

                                    input default renpy.current_screen().scope[str(categories[cat][2])]:
                                        changed set_clone_names
                                        style "serum_text_style"

            frame:
                textbutton "Return":
                    xfill True

                    text_style "serum_text_style"
                    action Hide(renpy.current_screen().screen_name)



#
