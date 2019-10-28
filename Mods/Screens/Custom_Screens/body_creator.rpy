
    # hair_styles
    # list_of_body_types
    # list_of_faces
    # list_of_tits
    # list_of_skins
    # the_person.age
    # the_person.name
    # the_person.last_name
init -2 python:

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
    default categories = {"hair_style": [hair_styles, False], "body_images": [list_of_bodies, False]}
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
                                foreground Crop(( 0, 0, 350, 190), get_part_image(getattr(the_person, cat)), xpos = -150) # TODO: Change positional alignment and crop size to fit all types of images

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
                                                foreground Crop(( 0, 0, 350, 190), get_part_image(item), xpos = -150)
                                                ysize 190
                                                action [
                                                    SetField(the_person, cat, item.get_copy()),

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
