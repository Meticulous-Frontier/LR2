init 5 python:
    config.label_overrides["lunch_date_plan_label"] = "lunch_date_plan_enhanced_label"

    def lunch_date_create_topics_menu(the_person):
        opinion_question_list = []

        #Generates a list with a few (usually 4, unless there's some opinion collision, but it's not important enough to filter things out more intelligently) opinions, one of which she likes
        while len(opinion_question_list) < 3:
            possible_opinion = get_random_opinion()
            if possible_opinion not in opinion_question_list:
                opinion_question_list.append(possible_opinion)

        key_opinion = the_person.get_random_opinion(only_positive = True, include_sexy = the_person.effective_sluttiness() > 50)

        if key_opinion is not None and key_opinion not in opinion_question_list:
            opinion_question_list.append(key_opinion)

        renpy.random.shuffle(opinion_question_list)

        formatted_opinion_list = []
        for item in opinion_question_list:
            score = the_person.get_known_opinion_score(item)    # only colorize when opinion is known
            item_string = item
            if score > 0:
                item_string = "{color=00e000}" + item + "{/color}"
            elif score < 0:
                item_string = "{color=e00000}" + item + "{/color}"

            formatted_opinion_list.append(["Chat about " + item_string, item])
        return formatted_opinion_list


label lunch_date_plan_enhanced_label(the_person):
    if the_person == kaya and the_person.location == coffee_shop:
        mc.name "I was thinking about getting some lunch. Do you have a lunch break?"
        if the_person.love < 40:
            the_person "Sorry, I work a short shift, so I don't get a lunch break."
            the_person "You seem nice though... maybe we could do something after I get off?"
            mc.name "Okay, I'll try to swing by later."
        else:
            the_person "You know I don't get a break! Swing by later, maybe we can get a drink after I get off?"
            mc.name "Okay, I'll try to swing by later."
        return

    $ del config.label_overrides["lunch_date_plan_label"]
    call lunch_date_plan_label(the_person) from _call_lunch_date_plan_label_enhanced
    $ config.label_overrides["lunch_date_plan_label"] = "lunch_date_plan_enhanced_label"
    return
