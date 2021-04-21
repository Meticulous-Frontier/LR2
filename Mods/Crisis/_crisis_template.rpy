# init -1 python:
#     def crisis_template_requirement():
#         return False
#
# init 2 python:
#     crisis_template_action = ActionMod("Crisis Template", crisis_template_requirement, "crisis_template_action_label",
#         menu_tooltip = "A description of the crisis.", category = "Business", is_crisis = True, crisis_weight = 5)
#
# label crisis_template_label():
#
#     $ the_person = stephanie
#     $ some_new_variable = stephanie.name
#
#     $ scene_manager = Scene()  #Clean Scene
#     $ scene_manager.add_actor(the_person, position = "stand4", emotion = "happy", display_transform = character_center_flipped)
#     the_person "Lots of fun dialogue"
#
#     #You go downtown
#     $ mc.change_location(downtown)
#     $ mc.location.show_background()
#
#     if stephanie.get_opinion_score("public sex") > 0:
#         "Dialoague branches yay"
#     else:
#         $ scene_manager.update_actor(the_person, emotion = "sad")
#         "More dialogue branches but now I'm sad"
#     if the_person.sluttiness > 40:
#         if the_person.get_opinion_score("taking control"<= 0:
#             call fuck_person(the_person, start_position = blowjob, skip_intro = False, position_locked = False, private = True, skip_condom = True) from _crisis_template_01
#         else:
#             call get_fucked(the_person, the_goal = "vaginal creampie", start_position = cowgirl, private = True, skip_intro = True, allow_continue = False) from _crisis_template_02
#     "Yay her stats get updated."
#     $ the_person.change_stats(love = 5, happiness = 5, obedience = 5, slut_temp = 3, slut_core = 3)
#
#
#     $ scene_manager.clear_scene()
#     $ del some_new_variable
#
#     return
