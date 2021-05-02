init 2 python:
    def get_red_heart(sluttiness, level = 0): #A recursive function, feed it a sluttiness and it will return a string of all red heart images for it. Hearts that are entirely empty are left out.
        #TODO: Expand this to let you ask for a minimum number of empty hearts.
        if level > 4:
            return ""

        the_final_string = ""
        if sluttiness >= 20:
            the_final_string += "{image=gui/heart/red_heart.png}"
            the_final_string += get_red_heart(sluttiness - 20, level + 1) #Call it recursively if we might have another heart after this.
        elif sluttiness >= 15:
            the_final_string += "{image=gui/heart/three_quarter_red_quarter_empty_heart.png}"
        elif sluttiness >= 10:
            the_final_string += "{image=gui/heart/half_red_half_empty_heart.png}"
        elif sluttiness >= 5:
            the_final_string += "{image=gui/heart/quarter_red_three_quarter_empty_heart.png}"

        return the_final_string

    def get_gold_heart(sluttiness, level = 0):
        if level > 4:
            return ""

        the_final_string = ""
        if sluttiness >= 20:
            the_final_string += "{image=gui/heart/gold_heart.png}"
            the_final_string += get_gold_heart(sluttiness - 20, level + 1) #Call it recursively if we might have another heart after this.
        elif sluttiness >= 15:
            the_final_string += "{image=gui/heart/three_quarter_gold_quarter_empty_heart.png}"
        elif sluttiness >= 10:
            the_final_string += "{image=gui/heart/half_gold_half_empty_heart.png}"
        elif sluttiness >= 5:
            the_final_string += "{image=gui/heart/quarter_gold_three_quarter_empty_heart.png}"

        return the_final_string


    def get_heart_image_list(the_person): ##Returns a formatted string that will add coloured hearts in line with text, perfect for menu choices, ect.
        heart_string = ""
        platinum_count = __builtin__.int(the_person.core_sluttiness // 100)
        heart_start = 0
        heart_end = 100
        for x in range(0, platinum_count):
            heart_string += "{image=gui/heart/platinum_heart.png}"
            heart_start += 100
            heart_end += 100

        for x in range(heart_start, heart_end, 20):
            heart_string += "{image=" + get_individual_heart(the_person.core_sluttiness - x, the_person.sluttiness - x, the_person.core_sluttiness + the_person.suggestibility - x) + "}"
        return heart_string
