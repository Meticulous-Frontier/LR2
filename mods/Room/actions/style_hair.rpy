# Made by Trollden.
# This file is dedicated to the style_hair label and corrseponding functions.
# With slight alterations to the label calls you can re-use it however you like.
init -1 python:
    def salon_redraw_hair(): # Call this whenever you have made changes to the hair style or hair color
                             # NOTE:  You can define your own colors here by following the established format.
                             #        It makes the assumption that the_person.hair_colour is set.
                             #        After having defined a color add a button that sets the_person.hair_colour in the menu.

        # Page 1
        if the_person.hair_colour == "blond":
             the_person.hair_style.colour = [0.84,0.75,0.47,1] # Hair color is in normalized RGB decimal format. [R, G, B, Alpha]

        elif the_person.hair_colour == "brown":
             the_person.hair_style.colour = [0.73,0.43,0.24,1]

        elif the_person.hair_colour == "black":
             the_person.hair_style.colour = [0.1,0.09,0.08,1]

        elif the_person.hair_colour == "red":
             the_person.hair_style.colour = [0.3,0.05,0.05,1]

        # Page 2
        elif the_person.hair_colour == "hot pink": # Custom Color
             the_person.hair_style.colour = [1,0.5,0.8,1]

        elif the_person.hair_colour == "sky blue": # Custom Color
             the_person.hair_style.colour = [0.4,0.5,0.9,1]

        elif the_person.hair_colour == "alt blond": # Custom Color
             the_person.hair_style.colour = [0.882, 0.733, 0.580,1]

        elif the_person.hair_colour == "light grey": # Custom Color
             the_person.hair_style.colour = [0.866, 0.835, 0.862,1]

        # Page 3
        elif the_person.hair_colour == "fire red": # Custom Color
             the_person.hair_style.colour = [0.909, 0.368, 0.368,1]

        elif the_person.hair_colour == "knight red": # Custom Color
             the_person.hair_style.colour = [0.745, 0.117, 0.235,1]

        elif the_person.hair_colour == "purple":
            the_person.hair_style.colour = [0.686, 0.156, 0.686,1]

        elif the_person.hair_colour == "dark grey":
            the_person.hair_style.colour = [0.705, 0.690, 0.709,1]

        # Page 4
        elif the_person.hair_colour == "turquoise":
            the_person.hair_style.colour = [0.435, 0.807, 0.788,1]
        elif the_person.hair_colour == "lime green":
            the_person.hair_style.colour = [0.647, 0.854, 0.564,1]
        elif the_person.hair_colour == "mango":
            the_person.hair_style.colour = [0.894, 0.737, 0.466,1]
        elif the_person.hair_colour == "ocean":
            the_person.hair_style.colour = [0.188, 0.494, 0.611,1]

        # Page 5
        elif the_person.hair_colour == "pulp":
            the_person.hair_style.colour = [0.643, 0.439, 0.541,1]
        elif the_person.hair_colour == "saturated":
            the_person.hair_style.colour = [0.905, 0.898, 0.513,1]
        elif the_person.hair_colour == "emerald":
            the_person.hair_style.colour = [0.098, 0.721, 0.541,1]
        elif the_person.hair_colour == "light brown":
            the_person.hair_style.colour = [0.658, 0.537, 0.380,1]

        the_person.draw_person(the_person.hair_style)
        #        elif the_person.hair_colour == "":
        #            the_person.hair_style.colour = [,1]

# Append to list_of_hairs incase it becomes relevant later.
    list_of_hairs.append("alt blond")
    list_of_hairs.append("hot pink")
    list_of_hairs.append("sky blue")
    list_of_hairs.append("light grey")
    list_of_hairs.append("fire red")
    list_of_hairs.append("knight red")
    list_of_hairs.append("purple")
    list_of_hairs.append("dark grey")
    list_of_hairs.append("turquoise")
    list_of_hairs.append("lime green")
    list_of_hairs.append("mango")
    list_of_hairs.append("ocean")
    list_of_hairs.append("pulp")
    list_of_hairs.append("saturated")
    list_of_hairs.append("emerald")
    list_of_hairs.append("light brown")
#    list_of_hairs.append()
#    list_of_hairs.append()
#    list_of_hairs.append()

label hair_colors(person):
        $ page = 1
        $ leave = 0
        while(leave ==0):

            menu:
                "Choose a hair color for [person.name], currently has [person.hair_colour] hair"
                # Page 1, four elements per page
                "Blond" if page == 1:
                    $ person.hair_colour = "blond"
                    $ salon_redraw_hair()

                "Brown" if page == 1:
                    $ person.hair_colour = "brown"
                    $ salon_redraw_hair()

                "Black" if page == 1:
                    $ person.hair_colour = "black"
                    $ salon_redraw_hair()

                "Red" if page == 1:
                    $ person.hair_colour = "red"
                    $ salon_redraw_hair()

                # Page 2
                "Hot Pink" if page == 2:
                    $ person.hair_colour = "hot pink"
                    $ salon_redraw_hair()

                "Alt Blond" if page == 2:
                    $ person.hair_colour = "alt blond"
                    $ salon_redraw_hair()

                "Sky Blue" if page == 2:
                    $ person.hair_colour = "sky blue"
                    $ salon_redraw_hair()

                "Grey" if page == 2:
                    $ person.hair_colour = "light grey"
                    $ salon_redraw_hair()

                # Page 3
                "Fire Red" if page == 3:
                    $ person.hair_colour = "fire red"
                    $ salon_redraw_hair()

                "Knight Red" if page == 3:
                    $ person.hair_colour = "knight red"
                    $ salon_redraw_hair()

                "Purple" if page == 3:
                    $ person.hair_colour = "purple"
                    $ salon_redraw_hair()

                "Dark Grey" if page == 3:
                    $ person.hair_colour = "dark grey"
                    $ salon_redraw_hair()

                #Page 4

                "Turquoise" if page == 4:
                    $ person.hair_colour = "turquoise"
                    $ salon_redraw_hair()

                "Lime" if page == 4:
                    $ person.hair_colour = "lime green"
                    $ salon_redraw_hair()

                "Mango" if page == 4:
                    $ person.hair_colour = "mango"
                    $ salon_redraw_hair()

                "Ocean" if page == 4:
                    $ person.hair_colour = "ocean"
                    $ salon_redraw_hair()

                #Page 5

                "Pulp" if page == 5:
                    $ person.hair_colour = "pulp"
                    $ salon_redraw_hair()

                "Saturated" if page == 5:
                    $ person.hair_colour = "saturated"
                    $ salon_redraw_hair()

                "Emerald" if page == 5:
                    $ person.hair_colour = "emerald"
                    $ salon_redraw_hair()

                "Light Brown" if page == 5:
                    $ person.hair_colour = "light brown"
                    $ salon_redraw_hair()

                "Next page":
                    if page < 5:
                        $ page += 1
                    else:
                        $ page = 1
                "Back.":
                    return

#"" if page == :
#    $ person.hair_colour = ""
#    $ salon_redraw_hair()
label hair_style(person):

    $ hair_style_check = person.hair_style #If hair_style_check is different than person.hair_style it means a "purchase" has been made.
    $ hair_color_check = person.hair_colour

    $ salon_style_cost = int(60)
    $ salon_dye_cost = int(30)

    $ salon_total_cost = salon_style_cost + salon_dye_cost


    $ page = 1
    $ leave = 0
    while(leave == 0):
                menu:
                    "Choose hair style, [person.name] currently has [person.hair_style.name]"
                    # Page 1, have four elements per page
                    "Short hair" if page == 1:
                        $ person.hair_style = short_hair
                        $ salon_redraw_hair()

                    "Twin Ponytails" if page == 1:
                        $ person.hair_style = twintail
                        $ salon_redraw_hair()

                    "Ponytail" if page == 1:
                        $ person.hair_style = ponytail
                        $ salon_redraw_hair()

                    "Messy Ponytail" if page == 1:
                        $ person.hair_style = messy_ponytail
                        $ salon_redraw_hair()

                    # Page 2
                    "Shaved Side Hair" if page == 2:
                        $ person.hair_style = shaved_side_hair
                        $ salon_redraw_hair()

                    "Long Hair" if page == 2:
                        $ person.hair_style = long_hair
                        $ salon_redraw_hair()

                    "Bow Hair" if page == 2:
                        $ person.hair_style = bow_hair
                        $ salon_redraw_hair()

                    "Messy Short Hair" if page == 2:
                        $ person.hair_style = messy_short_hair
                        $ salon_redraw_hair()

                    # Page 3
                    "Messy Long Hair" if page == 3:
                        $ person.hair_style = messy_hair
                        $ salon_redraw_hair()

                    # Throwing in a couple of empty buttons to keep formating.
                    "" if page == 3:
                        pass
                    "" if page == 3:
                        pass
                    "" if page == 3:
                        pass

                    "Hair color selection...":
                        call hair_colors(person)

                    "Next page":
                        if page < 3:
                            $ page += 1
                        else:
                            $ page = 1

                    "Back":
                        $ leave = 1
                        call salon_checkout() #Will return here if nothing qualifies
                        $renpy.scene("Active")
                        jump game_loop
