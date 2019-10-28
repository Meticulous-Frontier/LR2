
    # hair_styles
    # list_of_body_types
    # list_of_faces
    # list_of_tits
    # list_of_skins
    # the_person.age
    # the_person.name
    # the_person.last_name
init -2 python:

    def get_part_display_image(self, part_to_display = None): #Encapsulates what is done when drawing a person and produces a single displayable.

        if part_to_display in hair_styles:
            part_to_display.colour = self.hair_colour[1]
        cs = renpy.current_screen()

        position = "stand3"
        emotion = "default"
        special_modifier = None
        lighting = None

        list_of_bodies = cs.scope["list_of_bodies"]

        displayable_list = [] # We will be building up a list of displayables passed to us by the various objects on the person (their body, clothing, etc.)

        if part_to_display in list_of_bodies and type(part_to_display) is Clothing: # Seperate the parts (Clothing) so we draw things individually.
            displayable_list.append(part_to_display.generate_item_displayable(self.body_type, self.tits, position, lighting)) #Add the body displayable

        #displayable_list.extend(self.outfit.generate_draw_list(self,position,emotion,special_modifier, lighting = lighting)) #Get the displayables for everything we wear. Note that extnsions do not return anything because they have nothing to show.

        if part_to_display in list_of_faces:
            self.face_style = part_to_display
            displayable_list.append(self.expression_images.generate_emotion_displayable(position,emotion, special_modifier = special_modifier, eye_colour = self.eyes[1], lighting = lighting)) #Get the face displayable

        if part_to_display in hair_styles and type(part_to_display) is Clothing:
            displayable_list.append(self.expression_images.generate_emotion_displayable(position,emotion, special_modifier = special_modifier, eye_colour = self.eyes[1], lighting = lighting)) #Get the face displayable
            displayable_list.append(part_to_display.generate_item_displayable("standard_body",self.tits,position, lighting = lighting)) #Get hair



        if displayable_list:
            size_render = renpy.render(displayable_list[0], 10, 10, 0, 0) #We need a render object to check the actual size of the body displayable so we can build our composite accordingly.
            the_size = size_render.get_size() # Get the size. Without it our displayable would be stuck in the top left when we changed the size ofthings inside it.
            x_size = __builtin__.int(the_size[0])
            y_size = __builtin__.int(the_size[1])


            #NOTE: default return for the_size is floats, even though it is in exact pixels. Use int here otherwise positional modifiers like xanchor and yalign do not work (no displayable is shown at all!)
            composite_list = [(x_size,y_size)] #Now we build a list of our parameters, done like this so they are arbitrarily long
            for display in displayable_list:
                (composite_list.append((-150,10)) if part_to_display in hair_styles or part_to_display in list_of_faces else composite_list.append((-150,-160))) #Center all displaybles on the top left corner, because of how they are rendered they will all line up.
                composite_list.append(display) #Append the actual displayable

            final_image = Composite(*composite_list) # Create a composite image using all of the displayables
        #final_image = Flatten(final_image)

            return final_image

    def custom_set_field(the_person, field, item):

        cs = renpy.current_screen()
        if item in cs.scope["list_of_bodies"]:
            the_person.match_skin(item.name)

        if item in list_of_faces:
            the_person.face_style = item
            the_person.match_skin(the_person.skin)

        else:
            vars(the_person)[field] = (item.get_copy() if hasattr(item, "get_copy") else item) # face_style, body_type and tits are string while body_images and hair_style are cloth items.


    def toggle_dict_key(key): # I'm still too dumb to understand the ToggleDict action

        cs = renpy.current_screen()

        if cs.scope["categories"][key][1] == False:
            cs.scope["categories"][key][1] = True
        else:
            cs.scope["categories"][key][1] = False

    def get_part_image(part): # Get the image file path of a hair to display on the image_button
    # TODO: Maintain color information and maybe composite with face, eye color etc. intact


        image_set = part.position_sets.get("stand3")
        the_image = image_set.get_image("standard_body", "AA")
        #the_image = the_image.filename[:-4] + "_%s.png"
        return the_image.filename

screen body_customizer(the_person):
    # TODO: Make it so you can preview changes.
    #       Make images fit properly
    #       Maintain colors, possibly add color selection for hair and eyes (though I think I want to leave hair colors, and maybe hair overall since we have the hair salon)
    #       Add Clone action
    $ renpy.block_rollback()
    modal True
    zorder 999

    default list_of_bodies = [white_skin, tan_skin, black_skin] #Assemble the cloth items into a list. Revisit this later if a default list is created
    default categories = {"hair_style": [hair_styles, False], "body_images": [list_of_bodies, False], "expression_images": [list_of_faces, False]}
    frame:
        area(0, 100, 1500, 900)

        hbox:
            xfill True
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

                                    cols 4
                                    side_xalign 1.0
                                    draggable True
                                    mousewheel True
                                    scrollbars "vertical"

                                    for item in categories[cat][0]:
                                        frame:
                                            xsize 200
                                            ysize 200
                                            button:
                                                foreground Crop(( 0, 0, 190, 190), get_part_display_image(the_person, item))
                                                ysize 190
                                                action [
                                                    Function(custom_set_field, the_person, cat, item),
                                                    Function(the_person.draw_person, show_person_info = False)

                                                ]


            frame:
                xalign 1.0
                xsize 200
                ysize 200
                vbox:
                    textbutton "Return":
                        style "textbutton_no_padding_highlight"
                        text_style "serum_text_style"
                        action Hide("body_customizer")





#
