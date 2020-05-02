# The hint system is designed, so it does not need to be stored in a save game.
# Because it is not stored, we can update the list (or fix an issue) without breaking existing save games.
# A hint has a start condition and a completion condition.
# Only when the start condition evaluates to True and the completion condition evaluates to False it will be shown to the user.

init -1 python:
    game_hints = []

    # Hints for Sarah
    game_hints.append(Hint("Meet Sarah", "You should stay home for a day and see who knocks on your door.", "day > 2", "HR_director_creation_requirement() or employee_role in sarah.special_role or sarah.event_triggers_dict.get('rejected', False) == True"))
    game_hints.append(Hint("Join Sarah and Friends", "While working on saturday, Sarah might ask you to join her for drinks with friends.", "exists_in_mandatory_crisis_list('Sarah_third_wheel_label') and sarah.core_sluttiness > 15", "not exists_in_mandatory_crisis_list('Sarah_third_wheel_label')"))
    game_hints.append(Hint("Date with Sarah", "While working on saturday, Sarah might ask you on a date.", "exists_in_mandatory_crisis_list('Sarah_get_drinks_label') and sarah.core_sluttiness > 30", "not exists_in_mandatory_crisis_list('Sarah_get_drinks_label')"))

    # Hints for HR Director Role
    game_hints.append(Hint("HR Director", "Purchase the business policy for the HR Director at your main office.", "HR_director_creation_requirement() and not HR_director_creation_policy.is_owned()", "HR_director_creation_policy.is_owned()"))

    # Hints for Cousin
    game_hints.append(Hint("Cousin at your house", "You should go home in the afternoon, why is your cousin in your house?", "exists_in_room_enter_list(cousin, 'cousin_house_phase_two_label') and cousin.schedule[2] == hall", "exists_in_mandatory_crisis_list('cousin_house_phase_three_label') or exists_in_room_enter_list(cousin, 'cousin_blackmail_intro_label') or cousin.event_triggers_dict.get('blackmail_level', 0) > 0"))
    game_hints.append(Hint("Catch Cousin", "You should check your sisters bedroom in the afternoon, something is happening there.", "exists_in_room_enter_list(cousin, 'cousin_blackmail_intro_label') and cousin.schedule[2] == lily_bedroom", "not exists_in_room_enter_list(cousin, 'cousin_blackmail_intro_label')"))

    # Hints for Alexia
    game_hints.append(Hint("Meet Alexia", "You should go downtown and see if you run into someone you know.", "alexia in downtown.people and exists_in_room_enter_list(alexia, 'alexia_intro_phase_one_label')", "not exists_in_room_enter_list(alexia, 'alexia_intro_phase_one_label')"))
    game_hints.append(Hint("Hire Alexia", "You should head downtown and get to know her a little better so you can hire her as employee in your company.", "exists_in_role_action_list(alexia_role, 'alexia_hire_label')", "not exists_in_role_action_list(alexia_role, 'alexia_hire_label')"))

    # Hints for Nora
    game_hints.append(Hint("Nora's Research", "Don't try to research the Nora serum, just create a serum with the Nora trait and give it a person, then interact with them until you have increased your mastery level sufficiently.", "exists_in_location_action_list(university, 'nora_research_up_label') and mc.business.research_tier == 1 and round(mc.business.event_triggers_dict.get('nora_trait_researched').mastery_level, 1) < 2", "exists_in_location_action_list(university, 'nora_research_up_label') and mc.business.research_tier == 2"))
    game_hints.append(Hint("Nora's Research Finished", "Go to the university during business hours to hand in the trait you researched for Nora.", "exists_in_location_action_list(university, 'nora_research_up_label') and mc.business.research_tier == 1 and round(mc.business.event_triggers_dict.get('nora_trait_researched').mastery_level, 1) >= 2", "exists_in_location_action_list(university, 'nora_research_up_label') and mc.business.research_tier == 2"))


    # Hints for Research
    game_hints.append(Hint("Research Idle", "Your research department is not working on anything at the moment, this is the core of your business so give them something to do.", "mc.business.active_research_design is None", "not mc.business.active_research_design is None"))
    game_hints.append(Hint("Research Mastered", "Your development effort is directed at a well researched component, your efforts might be better spent on something else.", "mc.business.active_research_design and isinstance(mc.business.active_research_design, SerumTrait) and mc.business.active_research_design.mastery_level >= 2 and mc.business.active_research_design.get_effective_side_effect_chance() < 5", "mc.business.active_research_design and isinstance(mc.business.active_research_design, SerumTrait) and mc.business.active_research_design.get_effective_side_effect_chance() > 5"))
    game_hints.append(Hint("Advance Research", "You have researched all traits for your current research level, talk to your head researcher about advancing your research to the next level.", "mc.business.research_tier < 3 and researched_all_at_level()", "not researched_all_at_level()"))

    # Hint for Dungeon
    game_hints.append(Hint("Build Dungeon", "When you work in you company during the weekend, you might have a good idea.", "not dungeon.visible and day > 24 and mc.business.funds > 20000", "not exists_in_mandatory_crisis_list('dungeon_intro_label')"))

    # DEBUG HINTS (for fitting an positioning)
    # game_hints.append(Hint("Always Visible Hint", "This hint is always visible in the hint list.", "True", "False"))
    # hints with long text
    # game_hints.append(Hint("Nora's Research", "Don't try to research the Nora serum, just create a serum with the Nora trait and give it a person, then interact with them until you have increased your mastery level sufficiently.", "True", "False"))
    # game_hints.append(Hint("Hire Alexia", "You should head downtown and get to know her a little better so you can hire her as employee in your company.", "True", "False"))

    def number_of_hints():
        return len(active_hints())

    def active_hints():
        return [x for x in game_hints if x.is_active and not x.is_complete]
    
    def exists_in_mandatory_crisis_list(effect_name):
        return find_in_list(lambda x: x.effect == effect_name, mc.business.mandatory_crises_list)

    def exists_in_morning_crisis_list(effect_name):
        return find_in_list(lambda x: x.effect == effect_name, morning_crisis_list)

    def exists_in_room_enter_list(person, effect_name):
        return find_in_list(lambda x: x.effect == effect_name, person.on_room_enter_event_list)

    def exists_in_talk_event_list(person, effect_name):
        return find_in_list(lambda x: x.effect == effect_name, person.on_talk_event_list)

    def exists_in_role_action_list(role, effect_name):
        return find_in_list(lambda x: x.effect == effect_name, role.actions)

    def exists_in_location_action_list(location, effect_name):
        return find_in_list(lambda x: x.effect == effect_name, location.actions)

    def researched_all_at_level():
        for trait in list_of_traits:
            if not trait.researched and trait.tier == mc.business.research_tier:
                return False
        return True

init 2:
    # remove research reminder crisis (we have a hint for it)
    python:
        found = find_in_list(lambda x: x[0].effect == "research_reminder_crisis_label", crisis_list)
        if found:
            crisis_list.remove(found)

    screen game_hints_tooltip():
        $ count = number_of_hints()
        $ hint_height = 90
        $ window_height = count * hint_height

        zorder 100
        frame:
            background "#1a45a1aa"
            xpos 420
            ypos 1040 - window_height
            xsize 630
            ysize window_height - ((count-1) * 5)

            vbox:
                spacing 5
                for hint in active_hints():
                    frame:
                        background "#33333388"
                        xsize 620
                        ysize hint_height - 10
                        padding (0,0)
                        vbox:
                            spacing 0
                            text "{size=18}[hint.title]{/size}" style "serum_text_style_header" xalign 0 text_align 0 xpos 2
                            text "{size=14}[hint.description]{/size}" style "serum_text_style_traits" xalign 0 text_align 0 xpos 2

