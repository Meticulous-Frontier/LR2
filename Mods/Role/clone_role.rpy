init 2 python:
    def clone_recall_requirement(person):
        if person not in dungeon.people:
            return True

    def clone_rent_apartment_requirement(person):
        if not person.home is dungeon:
            return False
        if mc.business.funds < 25000:
            return "Insufficient funds."
        return person.home is dungeon

    # Clone Recall - Brings the clone back to base
    clone_recall_action = Action("Recall clone", clone_recall_requirement, "clone_recall_label", menu_tooltip = "Bring the clone back to the dungeon for modifications")

    # Clone Rent House - Rent a house for your clone
    clone_rent_apartment_action = Action("Rent Apartment (-$25000)", clone_rent_apartment_requirement, "clone_rent_apartment_label", menu_tooltip = "Rent a apartment for your clone.")

    clone_role = Role("Clone", [clone_recall_action, clone_rent_apartment_action])



# Labels
label clone_recall_label(the_person):
    "You order [the_person.title] back to [dungeon.name]"

    $ mc.location.move_person(the_person, dungeon)

    the_person.char "Okay, [the_person.mc_title]. I'll head there next."
    return

label clone_rent_apartment_label(the_person):
    $ the_person.draw_person()
    mc.name "Listen, [the_person.name], you are very dear to me and I have decided that you are mature enough to live on your own."
    mc.name "So I am willing to rent you a place where you can live by yourself."
    the_person.char "Please [the_person.mc_title], I love being with you, do I really have to go?"
    menu:
        "Let her stay":
            mc.name "Do you really want to live here, in my dungeon?"
            the_person.char "Yes, [the_person.mc_title], please let me stay..."
            mc.name "Ok, if that is what you want."
            return
        "Rent the apartment":
            mc.name "I think its better for your development if you have your own place. Trust me."
            the_person.char "Ok [the_person.mc_title], if you think that is best, I will honor your wish."

            python:
                the_person.home = None
                the_person.generate_home()
                mc.business.change_funds(-25000)
                the_person.set_schedule([1,2,3], None)

            "You make all the necessary arrangements, your clone [the_person.name] will now stay at her own place at night and live her life."

    $ renpy.scene("Active")
    return