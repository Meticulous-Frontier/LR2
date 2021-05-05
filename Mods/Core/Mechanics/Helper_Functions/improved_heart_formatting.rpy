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
        if platinum_count > 4:  # prevent div by zero errors
            platinum_count = 4
        heart_start = 0
        heart_end = 100
        for x in range(0, platinum_count):
            heart_string += "{image=gui/heart/platinum_heart.png}"
            heart_start += 100
            heart_end += 100

        capacity = 100.0 / (5 - platinum_count)
        for x in range(heart_start, heart_end - 15, __builtin__.int(capacity)):
            heart_string += "{image=" + get_individual_heart(the_person.core_sluttiness - x, the_person.sluttiness - x, the_person.core_sluttiness + the_person.suggestibility - x, capacity) + "}"
        return heart_string

    def get_individual_heart(core_slut, temp_slut, suggest_slut, capacity  = 20): #Give this the core, temp, core+suggest slut, minus 20*(current heart-1) each and it will find out the current heart status for that chunk of the heart array.
        image_string = "gui/heart/"
        factor = capacity / 4.0

        #None of the core heart statuses were reached. We must be in a duel or tri-colour heart state.
        if core_slut < factor:
            #There is no gold to draw.
            if temp_slut < factor:
                #There's no temp to draw either.
                if suggest_slut < factor:
                    image_string += "empty_heart.png"
                    #can't happen, we checked for this above, it's a pure heart.

                elif suggest_slut < factor * 2:
                    #It's a quarter grey, three quarter empty
                    image_string += "quarter_grey_three_quarter_empty_heart.png"

                elif suggest_slut < factor * 3:
                    #It's half grey, half empty
                    image_string += "half_grey_half_empty_heart.png"

                elif suggest_slut < factor * 4:
                    #It's three quarters grey, 1 quarter empty
                    image_string += "three_quarter_grey_quarter_empty_heart.png"

                else:
                    image_string += "grey_heart.png"

            elif temp_slut < factor * 2:
                #It's a quarter red and...
                if suggest_slut < factor * 2:
                    #There's no suggest to draw, the rest is empty.
                    image_string += "quarter_red_three_quarter_empty_heart.png"

                elif suggest_slut < factor * 3:
                    #it's got a half grey, then empty
                    image_string += "quarter_red_quarter_grey_half_empty_heart.png"

                elif suggest_slut < factor * 4:
                    #the rest is grey
                    image_string += "quarter_red_half_grey_quarter_empty_heart.png"

                else:
                    #It's three quarters grey
                    image_string += "quarter_red_three_quarter_grey_heart.png"

            elif temp_slut < factor * 3:
                #It's two quarters red and...
                if suggest_slut < factor * 3:
                    # Nothing, it's half red, half empty
                    image_string += "half_red_half_empty_heart.png"

                elif suggest_slut < factor * 4:
                    # half red, quarter grey, quarter empty
                    image_string += "half_red_quarter_grey_quarter_empty_heart.png"

                else:
                    # half red, half grey
                    image_string += "half_red_half_grey_heart.png"

            elif temp_slut < factor * 4:
                #It's three quarters red and...
                if suggest_slut < factor * 4:
                    # three quarters red and 1 empty
                    image_string += "three_quarter_red_quarter_empty_heart.png"

                else:
                    # three quarters red and 1 grey
                    image_string += "three_quarter_red_quarter_grey_heart.png"

            else:
                image_string += "red_heart.png"

        elif core_slut < factor * 2:
            #It fits in the 5 catagory
            if temp_slut < factor * 2:
                #There's no temp slut worth worrying about
                if suggest_slut < factor * 2:
                    # quarter gold, rest empty.
                    image_string += "quarter_gold_three_quarter_empty_heart.png"

                elif suggest_slut < factor * 3:
                    #quarter gold, quarter grey, empty.
                    image_string += "quarter_gold_quarter_grey_half_empty_heart.png"

                elif suggest_slut < factor * 4:
                    #quarter gold, half grey, empty
                    image_string += "quarter_gold_half_grey_quarter_empty_heart.png"

                else:
                    #quarter gold, rest grey
                    image_string += "quarter_gold_three_quarter_grey_heart.png"

            elif temp_slut < factor * 3:
                #quarter gold, quarter red, and...
                if suggest_slut < factor * 3:
                    #quarter gold, quarter red, rest empty
                    image_string += "quarter_gold_quarter_red_half_empty_heart.png"
                elif suggest_slut < factor * 4:
                    #quarter gold, quarter red, quarter grey, rest empty
                    image_string += "quarter_gold_quarter_red_quarter_grey_quarter_empty_heart.png"
                else:
                    #quarter gold, quarter red, half grey
                    image_string += "quarter_gold_quarter_red_half_grey_heart.png"

            elif temp_slut < factor * 4:
                #quarter gold, half red, and..
                if suggest_slut < factor * 4:
                    #quarter gold, half red, empty
                    image_string += "quarter_gold_half_red_quarter_empty_heart.png"
                else:
                    #quarter gold, half red, quarter grey
                    image_string += "quarter_gold_half_red_quarter_grey_heart.png"

            else:
                #quarter gold, rest red
                image_string += "quarter_gold_three_quarter_red_heart.png"

        elif core_slut < factor * 3:
            #It fits in the 10 catagory, half is gold
            if temp_slut < factor * 3:
                #No temp slut
                if suggest_slut < factor * 3:
                    #half gold, rest empty
                    image_string += "half_gold_half_empty_heart.png"
                elif suggest_slut < factor * 4:
                    # half gold, quarter grey, empty
                    image_string += "half_gold_quarter_grey_quarter_empty_heart.png"
                else:
                    #Half gold, half grey
                    image_string += "half_gold_half_grey_heart.png"
            elif temp_slut < factor * 4:
                #half gold, quarter red...
                if suggest_slut < factor * 4:
                    #half gold, quarter red, rest empty
                    image_string += "half_gold_quarter_red_quarter_empty_heart.png"
                else:
                    #half gold, quarter red, rest grey
                    image_string += "half_gold_quarter_red_quarter_grey_heart.png"
            else:
                #half gold, half red
                image_string += "half_gold_half_red_heart.png"

        elif core_slut < factor * 4:
            #three quarters gold and..
            if temp_slut < factor * 4:
                #No temp slut
                if suggest_slut < factor * 4:
                    #three quarters gold, rest empty
                    image_string += "three_quarter_gold_quarter_empty_heart.png"
                else:
                    #three quarters gold, rest grey
                    image_string += "three_quarter_gold_quarter_grey_heart.png"
            else:
                image_string += "three_quarter_gold_quarter_red_heart.png"
                #three quarters gold, rest red

        else:
            image_string += "gold_heart.png"

        return image_string
