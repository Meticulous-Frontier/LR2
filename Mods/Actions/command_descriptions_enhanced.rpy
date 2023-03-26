init 5 python:
    config.label_overrides["serum_demand_label"] = "serum_demand_label_enhanced"


label serum_demand_label_enhanced(the_person):
    if the_person.is_employee():
        mc.name "[the_person.title], we're running field trials and you're one of the test subjects. I'm going to need you to take this."
        "You pull out a vial of serum and present it to [the_person.title]."
        if mandatory_unpaid_serum_testing_policy.is_active():
            the_person "Sure no problem."
        else:
            the_person "What is it for, is it safe to take?"
            mc.name "Of course it is, you know about our testing procedures."
            the_person "Okay, I'm glad to help out."
    else:
        mc.name "[the_person.title], you're going to drink this for me."
        "You pull out a vial of serum and present it to [the_person.title]."
        if the_person.obedience < 150:
            the_person "What is it for, is it important?"
            mc.name "Of course it is, I wouldn't ask you to if it wasn't."
            "[the_person.title] hesitates for a second, then nods obediently."
            the_person "Okay, if that's what you need me to do."
        else:
            the_person "Sure no problem."

    call give_serum(the_person) from _call_give_serum_enhanced_serum_demand
    return
