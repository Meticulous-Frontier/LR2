init -1 python:
    DEALBREAKER_HIGH_SEX_SKILL = 4
    DEALBREAKER_HIGH_ENERGY = 80
    DEALBREAKER_LOW_ENERGY = 30


init 5 python:
    def orgasm_location_formatted_menu(the_person, locations):
        # renpy.random.shuffle(opinion_question_list)

        formatted_opinion_list = []
        for item in locations:
            score = the_person.get_known_opinion_score(item[1])    # only colorize when opinion is known
            item_string = item[0]
            if score > 0:
                item_string = "{color=00e000}" + item[0] + "{/color}"
            elif score < 0:
                item_string = "{color=e00000}" + item[0] + "{/color}"

            formatted_opinion_list.append([item_string, item])
        return formatted_opinion_list
