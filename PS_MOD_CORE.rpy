#Mod Core by ParadigmShift at F95zone
#version 0.15.0
#Free to be included in all mods that utilize the mod core initialization.
#Free to be modified and used in any way, so long as credit is given to the top 4 lines are not altered.

init -1 python:
    ##PC Function Variables
    ps_mod_core_init = False
    ps_mod_core_version = 0.15
    mod_list = []

init 2 python:
    def PS_mod_core_init_requirement():
        if ps_mod_core_init == False:
            return True
        return False

    def pc_action_requirement():
        if ps_mod_core_init:
            return True
        return False


    ps_mod_core_init_event = Action("PC Mod Initialization Event",PS_mod_core_init_requirement,"PS_mod_core_init_label")
    crisis_list.append([ps_mod_core_init_event,1000])

label PS_mod_core_init_label():
    ###This is where the event scene code would go

    ###"Beginning Mod Core Initialization"
    python:

        pc_action = Action("Turn on PC",pc_action_requirement,"pc_action_description",
            menu_tooltip = "Interact with various Mod Options.")

        bedroom.actions.append(pc_action)
        ps_mod_core_init = True

    if ps_mod_core_init:
        "Your phone suddenly starts vibrating in your pocket. Looks like your mother sent you a text."
        mom.char "Hi sweety. :-) I left you a gift in your room to help you with your new business :-O"
        mom.char "It's nothing big, just an old computer from my office. I hope it will be of use to you. :-D"
        mom.char "I won't keep you any longer. I love you, sweetie, and I'm so proud of what you're doing. XOXO :-*"
        "You'll have to thank your mother later...and discuss with her about her use of smilies..."
        "*** A computer can now be found located in your bedroom ***"

    return

label pc_action_description:
    $ mod_count = 0
    $ mod_max = len(mod_list)
    $ init_count = 0
    

    call pc_loop from _call_pc_loop_1
    return

label pc_loop:
    menu:

        "Mod Initialization":
            "Running Mod Initialization Sequence"
            while mod_count < mod_max: #We need to keep this in a renpy loop, because a return call will always return to the end of an entire python block.
                $mod = mod_list[mod_count]
                if mod.is_action_enabled():
                    $ mod.call_action()
                    $ init_count += 1
                $ mod_count += 1
            if init_count == 0:
                "No new mods initialized"
            else:
                "[init_count] new mods initialized"
                $ init_count = 0
        

        "Turn off PC":
            return
    call pc_loop from _call_pc_loop_2
    return
    

