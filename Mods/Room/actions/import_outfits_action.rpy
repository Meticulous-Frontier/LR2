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

    def check_import_xml_file(xml_filename):
        for file in renpy.list_files():
            if xml_filename in file:
                return True
        return False

    import_wardrobe_action = ActionMod("Import Wardrobe from XML", import_wardrobe_requirement, "import_wardrobe_label",
        initialization = import_wardrobe_mod_initialization, menu_tooltip = "Import wardrobe into player wardrobe from xml", category = "Wardrobe")

    give_wardrobe_action = ActionMod("Add Wardrobe from XML", import_wardrobe_requirement, "give_wardrobe_label",
        initialization = give_wardrobe_mod_initialization, menu_tooltip = "Import wardrobe into person wardrobe from xml", category = "Wardrobe")

    give_uniform_action = ActionMod("Add Uniforms from XML", give_uniform_requirement, "give_uniform_label",
        initialization = give_uniform_mod_initialization, menu_tooltip = "Import wardrobe into company division wardrobe from xml", category = "Wardrobe")

label import_wardrobe_label():
    "Speaker" "Enter the file name e.g Lily_Wardrobe (case sensitive) then hit enter to import to your wardrobe"
    $ xml_filename = str(renpy.input("Wardrobe to import:"))
    if check_import_xml_file(xml_filename):
        $ import_wardrobe(mc.designed_wardrobe, xml_filename)
    else:
        "Speaker" "File not found."
    return

label give_wardrobe_label():
    $ people_list = get_sorted_people_list(known_people_in_the_game([mc]), "Clothes for", ["Back"])
    call screen main_choice_display([people_list])
    $ person_choice = _return
    $ del people_list
    
    if not person_choice == "Back":
        call give_wardrobe_input(person_choice) from _call_give_wardrobe_input# What to do if "Back" was not the choice taken.
    return

label give_wardrobe_input(person = the_person): # when called from action default to the person
    $ the_person = person
    $ the_person.draw_person()

    "Speaker" "Enter the file name e.g Lily_Wardrobe (case sensitive) then hit enter to import to [the_person.name]'s wardrobe"
    $ xml_filename = str(renpy.input("Wardrobe to import:"))

    if check_import_xml_file(xml_filename):
        $ import_wardrobe(the_person.wardrobe, xml_filename)
        "Speaker" "You send a shipment of clothes to [the_person.name]"
        "Speaker" "Delivery complete."
    else:
        "Speaker" "File not found."

    $renpy.scene("Active")
    return

label give_uniform_label():
    $ target_wardrobe = None
    "Speaker" "Choose what division to assign uniforms to"
    menu:
        "All Divisions":
            $ target_wardrobe = mc.business.all_uniform
        "Marketing Division":
            $ target_wardrobe = mc.business.m_uniform
        "Production":
            $ target_wardrobe = mc.business.p_uniform
        "Research Division":
            $ target_wardrobe = mc.business.r_uniform
        "Supply Division":
            $ target_wardrobe = mc.business.s_uniform
        "Human Resources Division":
            $ target_wardrobe = mc.business.h_uniform
        "Back":
            return

    "Speaker" "Enter the file name e.g Lily_Wardrobe (case sensitive) then hit enter to import uniforms"

    $ xml_filename = str(renpy.input("Wardrobe to import:"))
    if check_import_xml_file(xml_filename):
        $ import_wardrobe(target_wardrobe, xml_filename)
        "Speaker" "Uniforms assigned"
    else:
        "Speaker" "File not found."            

    return
