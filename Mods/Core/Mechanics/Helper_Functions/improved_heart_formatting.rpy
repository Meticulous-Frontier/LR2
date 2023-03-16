init 2 python:
    # override default function to limit call stack depth
    @renpy.pure
    def get_red_heart(sluttiness, depth = 0): #A recursive function, feet it a sluttiness and it will return a string of all red heart images for it. Heatrts taht are entirely empty are left out.
        if depth >= 5:
            return ""

        the_final_string = ""
        if sluttiness >= 20:
            the_final_string += "{image=gui/heart/red_heart.png}"
            the_final_string += get_red_heart(sluttiness - 20, depth + 1) #Call it recursively if we might have another heart after this.
        elif sluttiness >= 15:
            the_final_string += "{image=gui/heart/three_quarter_red_quarter_empty_heart.png}"
        elif sluttiness >= 10:
            the_final_string += "{image=gui/heart/half_red_half_empty_heart.png}"
        elif sluttiness >= 5:
            the_final_string += "{image=gui/heart/quarter_red_three_quarter_empty_heart.png}"

        return the_final_string

    # override default function to limit call stack depth
    @renpy.pure
    def get_gold_heart(sluttiness, depth = 0):
        if depth >= 5:
            return ""

        the_final_string = ""
        if sluttiness >= 20:
            the_final_string += "{image=gui/heart/gold_heart.png}"
            the_final_string += get_gold_heart(sluttiness - 20, depth + 1) #Call it recursively if we might have another heart after this.
        elif sluttiness >= 15:
            the_final_string += "{image=gui/heart/three_quarter_gold_quarter_empty_heart.png}"
        elif sluttiness >= 10:
            the_final_string += "{image=gui/heart/half_gold_half_empty_heart.png}"
        elif sluttiness >= 5:
            the_final_string += "{image=gui/heart/quarter_gold_three_quarter_empty_heart.png}"

        return the_final_string

    @renpy.pure
    def get_heart_image_list(sluttiness, effective_sluttiness): ##Returns a formatted string that will add coloured hearts in line with text, perfect for menu choices, ect.
        heart_string = ""
        platinum_count = __builtin__.int((sluttiness - 1) // 100)
        if platinum_count > 4:  # prevent div by zero errors
            platinum_count = 4
        if platinum_count < 0: # prevent failure with negative numbers
            platinum_count = 0
        heart_start = 0
        heart_end = 100
        for x in range(0, platinum_count):
            heart_string += "{image=gui/heart/platinum_heart.png}"
            heart_start += 100
            heart_end += 100

        capacity = 100.0 / (5 - platinum_count)
        for x in range(heart_start, heart_end - 15, __builtin__.int(capacity)):
            heart_string += "{image=" + get_individual_heart(sluttiness - x, effective_sluttiness - x, capacity) + "}"
        return heart_string


    @renpy.pure
    def get_individual_heart(base_sluttiness, actual_sluttiness, capacity  = 20): #Give this the core, temp, core+suggest slut, minus 20*(current heart-1) each and it will find out the current heart status for that chunk of the heart array.
        image_string = "gui/heart/"
        factor = capacity / 4.0

        if base_sluttiness > actual_sluttiness:
            # We need missing heart segments to be displayed.
            # Effectively a mirror of below but counting backwards
            if base_sluttiness < factor:
                image_string += "empty_heart"
            elif base_sluttiness < factor * 2:
                if actual_sluttiness < factor:
                    image_string += "quarter_grey_three_quarter_empty_heart"
                else:
                    image_string += "quarter_gold_three_quarter_empty_heart"
            elif base_sluttiness < factor * 3:
                if actual_sluttiness < factor:
                    image_string += "half_grey_half_empty_heart"
                elif actual_sluttiness < factor * 2:
                    image_string += "quarter_gold_quarter_grey_half_empty_heart"
                else:
                    image_string += "half_gold_half_empty_heart"
            elif base_sluttiness < factor * 4:
                if actual_sluttiness < factor:
                    image_string += "three_quarter_grey_quarter_empty_heart"
                elif actual_sluttiness < factor * 2:
                    image_string += "quarter_gold_half_grey_quarter_empty_heart"
                elif actual_sluttiness < factor * 3:
                    image_string += "half_gold_quarter_grey_quarter_empty_heart"
                else:
                    image_string += "three_quarter_gold_quarter_empty_heart"
            else:
                if actual_sluttiness < factor:
                    image_string += "grey_heart"
                elif actual_sluttiness < factor * 2:
                    image_string += "quarter_gold_three_quarter_grey_heart"
                elif actual_sluttiness < factor * 3:
                    image_string += "half_gold_half_grey_heart"
                elif actual_sluttiness < factor * 4:
                    image_string += "three_quarter_gold_quarter_grey_heart"
                else:
                    image_string += "gold_heart"

        else:
            # We need gold heart segments to be displayed.
            if actual_sluttiness < factor: #0 segments filled
                image_string += "empty_heart" #Segment isn't filled at all

            elif actual_sluttiness < factor * 2: #1 segment filled
                if base_sluttiness < factor:
                    image_string += "quarter_red_three_quarter_empty_heart"
                else:
                    image_string += "quarter_gold_three_quarter_empty_heart"
            elif actual_sluttiness < factor * 3: #2 segments filled
                if base_sluttiness < factor:
                    image_string += "half_red_half_empty_heart"
                elif base_sluttiness < factor * 2:
                    image_string += "quarter_gold_quarter_red_half_empty_heart"
                else:
                    image_string += "half_gold_half_empty_heart"
            elif actual_sluttiness < factor * 4: #3 segments filled
                if base_sluttiness < factor:
                    image_string += "three_quarter_red_quarter_empty_heart"
                elif base_sluttiness < factor * 2:
                    image_string += "quarter_gold_half_red_quarter_empty_heart"
                elif base_sluttiness < factor * 3:
                    image_string += "half_gold_quarter_red_quarter_empty_heart"
                else:
                    image_string += "three_quarter_gold_quarter_empty_heart"
            else: #fully filled
                if base_sluttiness < factor:
                    image_string += "red_heart"
                elif base_sluttiness < factor * 2:
                    image_string += "quarter_gold_three_quarter_red_heart"
                elif base_sluttiness < factor * 3:
                    image_string += "half_gold_half_red_heart"
                elif base_sluttiness < factor * 4:
                    image_string += "three_quarter_gold_quarter_red_heart"
                else:
                    image_string += "gold_heart"

        return image_string + ".png"
