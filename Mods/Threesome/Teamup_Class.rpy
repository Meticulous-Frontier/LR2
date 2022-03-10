#This class is designed to hold all the variables and labels required to create a teamup scene.
#Class contains labels for all parts of the scene in a list, which progresses automatically in corruption based on specified conditions
#Class should track what stage the teamup is at so it can be referenced easily and should save the progress in save file
#Class should compile at startup the list of stages of the teamup so that it can be modified and added to as necessary
#Class may have to reference another class in the event of a branching storyline 4  4

init -2 python:
    #Default function to run between cycles if we do a default unit test.
    def teamup_test_func_default(the_person_one, the_person_two):
        the_person_one.change_slut(10, 100)
        the_person_one.change_energy(200)
        the_person_two.change_slut(10, 100)
        the_person_two.change_energy(200)
        time_of_day = 1
        return

    class Teamup_Scene():

        def __init__(self, compile_scenes, start_scene_list, req_list, trans_list, final_scene_list, intro_scene, exit_scene, teamup_action, choice_scene,
            stage = -1, advance_time = True, business_action = False, person_action = False, is_random = False, unit_test_func = None):

            self.stage = stage  #The corruption level of the teamup event
            self.compile_scenes = compile_scenes #Use this function to recompile the lists. Should be run on game load and initial game start.
            self.intro_scene = intro_scene  #Scene to play the first time this teamup is called
            self.exit_scene = exit_scene    #If MC decides not to participate.
            self.choice_scene = choice_scene    #Use this to determine if MC wants to stay or leave the event.
            self.teamup_action = teamup_action  #Use this as a generic action that can be added to any girl to proc the event.
            self.start_scene_list = start_scene_list    #Scene to play at the beginning of the teamup. Mostly to build lust and set the stage.
            self.req_list = req_list    #Requirements used to determine if we are advancing corruption levels
            self.trans_list = trans_list    #A transition between corruption levels.
            self.final_scene_list = final_scene_list    #The act of the teamup itself
            self.advance_time = advance_time    #IF the event should advance time. Probably yes?
            self.business_action = business_action  #If the action should be a business crisis
            self.person_action = person_action      #if the action should be a person crisis
            self.is_random = is_random              #If this action only pops up randomly.
            if unit_test_func == None:
                self.unit_test_func = teamup_test_func_default
            else:
                self.unit_test_func = unit_test_func

        def get_stage(self):
            return self.stage

        def set_stage(self, stage):
            self.stage = stage

        def call_intro(self, the_person_one, the_person_two):
            renpy.call(self.intro_scene, the_person_one, the_person_two)
            return

        def call_start_scene(self, the_person_one, the_person_two):
            renpy.call(self.start_scene_list[self.stage], the_person_one, the_person_two)
            return

        def call_trans_scene(self, the_person_one, the_person_two):
            renpy.call(self.trans_list[self.stage], the_person_one, the_person_two)
            return

        def call_final_scene(self, the_person_one, the_person_two):
            renpy.call(self.final_scene_list[self.stage], the_person_one, the_person_two)
            return

        def call_exit_scene(self, the_person_one, the_person_two):
            renpy.call(self.exit_scene, the_person_one, the_person_two)

        def call_choice_scene(self, the_person_one, the_person_two):
            return renpy.call(self.choice_scene, the_person_one, the_person_two)

        def call_scene(self, the_person_one, the_person_two):
            if self.business_action:
                mc.business.add_mandatory_crisis(self.teamup_action)
            if self.person_action:
                the_person_one.add_unique_on_room_enter_event(self.teamup_action)
            if self.stage == -1:
                self.set_stage(0)
                self.call_intro(the_person_one, the_person_two)
                return
            self.call_start_scene(the_person_one, the_person_two)
            self.call_choice_scene(the_person_one, the_person_two)
            if not _return:
                self.call_exit_scene(the_person_one, the_person_two)
                return
            if len(self.req_list) > self.stage + 1: #Only try if there is another scene
                if self.req_list[self.stage + 2](the_person_one, the_person_two):
                    self.set_stage(self.stage + 1)
                    self.call_trans_scene(the_person_one, the_person_two)

            self.call_final_scene(the_person_one, the_person_two)
            return

        def recompile_scenes(self):
            self.compile_scenes(self)
            return

        def run_unit_test(self, the_person_one, the_person_two, cycles = 10):
            scene_count = 0
            while scene_count < cycles:
                self.call_scene(the_person_one, the_person_two)
                self.unit_test_func(the_person_one, the_person_two)
            return

label teamup_scene_label(teamup, the_person_one, the_person_two):
    if teamup.business_action:
        $ mc.business.add_mandatory_crisis(teamup.teamup_action)
    if teamup.person_action:
        $ the_person_one.add_unique_on_room_enter_event(teamup.teamup_action)
    if teamup.stage == -1:
        $ teamup.stage = 0
        $ teamup.call_intro(the_person_one, the_person_two)
        return
    $ teamup.call_start_scene(the_person_one, the_person_two)
    $ teamup.call_choice_scene(the_person_one, the_person_two)
    if not _return:
        $ teamup.call_exit_scene(the_person_one, the_person_two)
        return
    if len(teamup.req_list) > teamup.stage + 1: #Only try if there is another scene
        if teamup.req_list[teamup.stage + 1](the_person_one, the_person_two):
            $ teamup.stage = teamup.stage + 1
            $ teamup.call_trans_scene(the_person_one, the_person_two)

    $ teamup.call_final_scene(the_person_one, the_person_two)
    return

# call teamup_scene_label(kaya_erica_teamup, kaya, erica)
