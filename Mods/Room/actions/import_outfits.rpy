# Import outfits by Trollden
# Use it as you see fit

init 2 python:
    def import_wardrobe_requirement():
        return True

    def give_uniform_requirement():
        if strict_uniform_policy.is_owned():
            return True
        else:
            return "Requires: [strict_uniform_policy.name] or higher"

    def import_wardrobe_mod_initialization(self):
        bedroom.actions.append(self)
        return
    def give_wardrobe_mod_initialization(self):
        clothing_store.actions.append(self)
        return
    def give_uniform_mod_initialization(self):
        office.actions.append(self)
        return

    import_wardrobe_action = ActionMod("Import Wardrobe from XML", import_wardrobe_requirement, "import_wardrobe_label",
        initialization = import_wardrobe_mod_initialization, menu_tooltip = "Type the name of the XML file to import, case sensitive", category = "Wardrobe")

    give_wardrobe_action = ActionMod("Give Wardrobe from XML", import_wardrobe_requirement, "give_wardrobe_label",
        initialization = give_wardrobe_mod_initialization, menu_tooltip = "Type the name of the XML file to give from, case sensitive", category = "Wardrobe")

    give_uniform_action = ActionMod("Give Uniforms from XML", give_uniform_requirement, "give_uniform_label",
        initialization = give_uniform_mod_initialization, menu_tooltip = "Type the name of the XML file to give from, case sensitive", category = "Wardrobe")

label import_wardrobe_label():
    "Speaker" "Enter the file name e.g Lily_Wardrobe then hit enter to import to your wardrobe"
    $ xml_filename = str(renpy.input("Wardrobe to import:"))
    $ import_wardrobe(mc.designed_wardrobe, xml_filename)
    return
#label import_wardrobe_input():
#    pass
label give_wardrobe_label():
    "Select who to give clothes"
    while True:
        $ tuple_list = known_people_in_the_game([mc]) + ["Back"]
        call screen person_choice(tuple_list, draw_hearts = True)
        $ person_choice = _return

        if person_choice == "Back":
            return # Where to go if you hit "Back".
        else:
            call give_wardrobe_input(person_choice)# What to do if "Back" was not the choice taken.

label give_wardrobe_input(person = the_person): # when called from action default to the person
    $ the_person = person
    $ the_person.draw_person()

    "Speaker" "Enter the file name e.g Lily_Wardrobe then hit enter to import to [the_person.name]'s wardrobe"
    $ xml_filename = str(renpy.input("Wardrobe to import:"))

    "Speaker" "You send a shipment of clothes to [the_person.name]"
    "Speaker" "Delivery complete."

    $ import_wardrobe(the_person.wardrobe, xml_filename)
    $renpy.scene("Active")
    return

label give_uniform_label():
    "Speaker" "Choose what division to assign uniforms to"
    menu:
        "All Divisions":
            "Speaker" "Enter the file name e.g Lily_Wardrobe then hit enter to import uniforms"

            $ xml_filename = str(renpy.input("Wardrobe to import:"))
            $ import_wardrobe(mc.business.all_uniform, xml_filename)

            "Speaker" "Uniforms assigned"
            return
        "Marketing Division":
            "Speaker" "Enter the file name e.g Lily_Wardrobe then hit enter to import uniforms"

            $ xml_filename = str(renpy.input("Wardrobe to import:"))
            $ import_wardrobe(mc.business.m_uniform, xml_filename)

            "Speaker" "Uniforms assigned"
            return
        "Production":
            "Speaker" "Enter the file name e.g Lily_Wardrobe then hit enter to import uniforms"

            $ xml_filename = str(renpy.input("Wardrobe to import:"))
            $ import_wardrobe(mc.business.p_uniform, xml_filename)

            "Speaker" "Uniforms assigned"
            return
        "Research Division":
            "Speaker" "Enter the file name e.g Lily_Wardrobe then hit enter to import uniforms"

            $ xml_filename = str(renpy.input("Wardrobe to import:"))
            $ import_wardrobe(mc.business.r_uniform, xml_filename)

            "Speaker" "Uniforms assigned"
            return
        "Supply Division":
            "Speaker" "Enter the file name e.g Lily_Wardrobe then hit enter to import uniforms"

            $ xml_filename = str(renpy.input("Wardrobe to import:"))
            $ import_wardrobe(mc.business.s_uniform, xml_filename)

            "Speaker" "Uniforms assigned"
            return
        "Human Resources Division":
            "Speaker" "Enter the file name e.g Lily_Wardrobe then hit enter to import uniforms"

            $ xml_filename = str(renpy.input("Wardrobe to import:"))
            $ import_wardrobe(mc.business.h_uniform, xml_filename)

            "Speaker" "Uniforms assigned"
            return
