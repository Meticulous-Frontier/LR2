#This class is designed to hold all the variables and labels required to create a corruption progression scene.
#Class contains labels for all parts of the scene in a list, which progresses automatically in corruption based on specified conditions
#Class should track what stage the progression is at so it can be referenced easily and should save the progress in save file
#Class should compile at startup the list of stages of the progression_scene so that it can be modified and added to as necessary
#Class may have to reference another class in the event of a branching storyline
#Use a character's init file to call their progression scene recompiles.


init -2 python:
    #Default function to run between cycles if we do a default unit test.
    def progression_scene_test_func_default(the_group = []):
        for person in the_group:
            person_one.change_slut(10, 100)
            person_one.change_energy(200)
        time_of_day = 1
        return

    class Progression_Scene():

        def __init__(self, compile_scenes, start_scene_list, req_list, trans_list, final_scene_list, intro_scene, exit_scene, progression_scene_action, choice_scene,
            stage = -1, advance_time = True, business_action = False, person_action = False, is_random = False, unit_test_func = None,
            is_multiple_choice = False, multiple_choice_scene = None, regress_scene_list = []):

            self.stage = stage  #The corruption level of the progression_scene event
            self.compile_scenes = compile_scenes #Use this function to recompile the lists. Should be run on game load and initial game start.
            self.intro_scene = intro_scene  #Scene to play the first time this progression_scene is called
            self.exit_scene = exit_scene    #If MC decides not to participate.
            self.choice_scene = choice_scene    #Use this to determine if MC wants to stay or leave the event.
            self.progression_scene_action = progression_scene_action  #Use this as a generic action that can be added to any girl to proc the event.
            self.start_scene_list = start_scene_list    #Scene to play at the beginning of the progression_scene. Mostly to build lust and set the stage.
            self.req_list = req_list    #Requirements used to determine if we are advancing corruption levels
            self.trans_list = trans_list    #A transition between corruption levels.
            self.final_scene_list = final_scene_list    #The act of the progression_scene itself
            self.advance_time = advance_time    #IF the event should advance time. Probably yes?
            self.business_action = business_action  #If the action should be a business crisis
            self.person_action = person_action      #if the action should be a person crisis
            self.is_random = is_random              #If this action only pops up randomly.
            if unit_test_func == None:              #Set a unit test function
                self.unit_test_func = progression_scene_test_func_default
            else:
                self.unit_test_func = unit_test_func
            self.is_multiple_choice = is_multiple_choice    #Set to true if we want MC to decide which final scene to play.
            self.multiple_choice_scene = multiple_choice_scene  #Use this scene to setup the choice. IE how do you fuck her, etc.
            self.regress_scene_list = regress_scene_list        #Fill this list if we want progress here to be capable of regressing.
            self.scene_unlock_list = []                         #Hold a list of scene refences. Should be numbers only, EG: [0,1,2,5]

        def get_stage(self):
            return self.stage

        def set_stage(self, stage):
            self.stage = stage

        def call_intro(self, the_group):
            renpy.call(self.intro_scene, the_group)
            return

        def call_start_scene(self, the_group):
            renpy.call(self.start_scene_list[self.stage], the_group)
            return

        def call_trans_scene(self, the_group):
            renpy.call(self.trans_list[self.stage], the_group)
            return

        def call_regress_scene(self, the_group):
            renpy.call(self.regress_scene_list[self.stage], the_group)

        def call_final_scene(self, the_group):
            renpy.call(self.final_scene_list[self.stage], the_group)
            return

        def call_exit_scene(self, the_group):
            renpy.call(self.exit_scene, the_group)

        def call_choice_scene(self, the_group):
            return renpy.call(self.choice_scene, the_group)

        def is_progress_only(self):
            if len(self.regress_scene_list) == 0:
                return True
            return False

        def recompile_scenes(self):
            self.compile_scenes(self)
            return

        def call_scene(self, the_group):
            renpy.call("progression_scene_label", self, the_group)
            return

        def run_unit_test(self, the_group, cycles = 10):
            scene_count = 0
            while scene_count < cycles:
                self.call_scene(the_group)
                self.unit_test_func(the_group)
            return

label progression_scene_label(progression_scene, the_group):
    #First, add the event back so that it recurs. For a role event, leave these two properties false.
    if progression_scene.business_action:
        $ mc.business.add_mandatory_crisis(progression_scene.progression_scene_action)
    if progression_scene.person_action:
        $ the_group[0].add_unique_on_room_enter_event(progression_scene.progression_scene_action)

    # If the stage is -1, it has not been run before. Call the intro.
    if progression_scene.stage == -1:
        $ progression_scene.stage = 0
        "Progressions stage should now be 0"
        if progression_scene.is_multiple_choice:    #IF it is multiple choice, add the basic scene to the list of options.
            $ progression_scene.scene_unlock_list.append(0)
        $ progression_scene.call_intro(the_group)
        if progression_scene.advance_time:
            call advance_time from _call_advance_progression_scene_class_02
        return

    #First, play the start scene
    $ progression_scene.call_start_scene(the_group)
    #Allow players to opt out
    $ progression_scene.call_choice_scene(the_group)
    if not _return:
        $ progression_scene.call_exit_scene(the_group)
        return

    #If the scene is multiple choice, check and see if we unlocked any new "choices"
    if progression_scene.is_multiple_choice:
        pass

    scene_transition = False    #pass in to the final scene if we played a transition or not. It may change the final scene.

    #if it is linear progression, first check if we can progress this scene.
    if len(progression_scene.req_list) > progression_scene.stage + 1: #Only try if there is another scene
        if progression_scene.req_list[progression_scene.stage + 1](the_group):
            $ progression_scene.stage = progression_scene.stage + 1
            $ progression_scene.call_trans_scene(the_group)
            scene_transition = True
    #If the scene can regress, check and see if we need to regress a step
    if not progression_scene.is_progress_only() and progression_scene.stage != 0:
        if not progression_scene.req_list[progression_scene.stage](the_group):
            $ progression_scene.stage = progression_scene.stage - 1
            $ progression_scene.call_regress_scene(the_group)
            scene_transition = True

    #Call the appropriate final scene.
    $ progression_scene.call_final_scene(the_group, scene_transition)
    if progression_scene.advance_time:
        call advance_time from _call_advance_progression_scene_class_01
    return
