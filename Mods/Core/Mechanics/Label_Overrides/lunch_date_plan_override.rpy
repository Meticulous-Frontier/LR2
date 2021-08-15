init 5 python:
    config.label_overrides["lunch_date_plan_label"] = "lunch_date_plan_enhanced_label"


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
