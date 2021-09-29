init 1 python:
    def _fraction_to_integer(fraction):
        """
        Internal helper for converting a fraction value to an integer
        between 0 and 255 inclusive.
        """
        num = fraction * 255
        e = num - math.floor(num)
        return e < 0.5 and int(math.floor(num)) or int(math.ceil(num))

    def rgb_fraction_to_rgb(rgb_fraction_triplet):
        return tuple(map(_fraction_to_integer, rgb_fraction_triplet))


    hair_color_names_to_hex = {}
    for color in list_of_hairs:
        hair_color_names_to_hex[color[0]] = normalize_hex(rgb_to_hex(rgb_fraction_to_rgb((color[1][0], color[1][1], color[1][2]))))
    hair_color_hex_to_names  = _reversedict(hair_color_names_to_hex)


    eye_color_names_to_hex = {}
    for color in list_of_eyes:
        eye_color_names_to_hex[color[0]] = normalize_hex(rgb_to_hex(rgb_fraction_to_rgb((color[1][0], color[1][1], color[1][2]))))
    eye_color_hex_to_names  = _reversedict(eye_color_names_to_hex)

    def closest_color_name(requested_colour, color_hex_to_name_map):
        min_colours = {}
        for key, name in color_hex_to_name_map.items():
            r_c, g_c, b_c = hex_to_rgb(key)
            rd = (r_c - requested_colour[0]) ** 2
            gd = (g_c - requested_colour[1]) ** 2
            bd = (b_c - requested_colour[2]) ** 2
            min_colours[(rd + gd + bd)] = name
        return min_colours[min(min_colours.keys())]

    def closest_hair_colour(requested_colour):
        return closest_color_name(requested_colour, hair_color_hex_to_names)

    def closest_eye_color(requested_colour):
        return closest_color_name(requested_colour, eye_color_hex_to_names)


    def person_set_eye_colour(self, new_colour):
        new_colour = Color(rgb=(new_colour.rgb)) #Make sure we don't have any alpha problems.
        eye_colour_name = closest_eye_color(new_colour).capitalize()
        eye_colour_list = [new_colour.rgb[0], new_colour.rgb[1], new_colour.rgb[2], 1.0]

        self.eyes = [eye_colour_name, eye_colour_list]

    Person.set_eye_colour = person_set_eye_colour

    def person_set_hair_colour(self, new_colour, change_pubes = True, darken_pubes_amount = 0.07):
        #NOTE: new_colour should be a Ren'py colour.
        new_colour = Color(rgb=(new_colour.rgb)) #Make sure we don't have any alpha problems.
        hair_colour_name = closest_hair_colour(new_colour).capitalize()
        hair_colour_list = [new_colour.rgb[0], new_colour.rgb[1], new_colour.rgb[2], 1.0]

        self.hair_colour = [hair_colour_name, hair_colour_list]

        if change_pubes:
            pubes_colour = new_colour.shade(1.0-darken_pubes_amount)
            self.pubes_colour = [pubes_colour.rgb[0], pubes_colour.rgb[1], pubes_colour.rgb[2], 1.0]
            self.pubes_colour = pubes_colour
        self.hair_style.colour = hair_colour_list

    Person.set_hair_colour = person_set_hair_colour