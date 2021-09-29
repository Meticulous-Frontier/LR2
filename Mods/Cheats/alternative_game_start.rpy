init 2 python:
    config.label_overrides["start"] = "alternative_start"

label alternative_start:
    scene bg paper_menu_background with fade
    "Lab Rats 2 contains adult content. If you are not over 18 or your country's equivalent age you should not view this content."
    menu:
        "I am over 18":
            "Excellent, let's continue then."

        "I am not over 18":
            $renpy.full_restart()

    "Vren" "[config.version] represents an early iteration of Lab Rats 2. Expect to run into limited content, unexplained features, and unbalanced game mechanics."
    "Vren" "Would you like to view the FAQ?"
    menu:
        "View the FAQ":
            call faq_loop from _call_faq_loop_alternative_start
        "Get on with the game!":
            "You can access the FAQ from your bedroom at any time."

    "Vren" "Lab Rats 2 contains content related to impregnation and pregnancy. These settings may be changed in the menu at any time."
    menu:
        "No pregnancy content\n{size=16}Girls never become pregnant. Most pregnancy content hidden.{/size}":
            $ persistent.pregnancy_pref = 0

        "Predictable pregnancy content\n{size=16}Birth control is 100%% effective. Girls always default to taking birth control.{/size}":
            $ persistent.pregnancy_pref = 1

        "Realistic pregnancy content\n{size=16}Birth control is not 100%% effective. Girls may not be taking birth control.{/size}":
            $ persistent.pregnancy_pref = 2

    $ easy_mode = False
    "MOD" "Do you want to play with original game difficulty or make the game easier?"
    menu:
        "Default Game Play":
            pass
        "Easier Game Play":
            "MOD" "All options for making the game easier will be applied after character creation."
            $ easy_mode = True

    $ renpy.block_rollback()
    call screen character_create_screen()
    $ return_arrays = _return #These are the stat, skill, and sex arrays returned from the character creator.

    python:
        if easy_mode:
            for array in range(0, len(return_arrays)):
                for val in range(0, len(return_arrays[array])):
                    return_arrays[array][val] += 2

    call initialize_game_state(store.name,store.b_name,store.l_name,return_arrays[0],return_arrays[1],return_arrays[2]) from _call_initialize_game_state

    python:
        if easy_mode:
            # increased business stats
            mc.business.funds = 10000
            mc.business.supply_count = 1000
            mc.business.supply_goal = 1000
            mc.business.effectiveness_cap = 110
            mc.business.marketability = 100
            # increased player stats
            mc.max_energy = 120
            mc.free_clarity += 500
            # default unlock policies
            purchase_policy(mandatory_paid_serum_testing_policy, ignore_cost = True)
            purchase_policy(serum_size_1_policy, ignore_cost = True)
            purchase_policy(recruitment_batch_one_policy, ignore_cost = True)
            purchase_policy(recruitment_knowledge_one_policy, ignore_cost = True)
            purchase_policy(recruitment_skill_improvement_policy, ignore_cost = True)
            purchase_policy(business_size_1_policy, ignore_cost = True)
            purchase_policy(theoretical_research, ignore_cost = True)

    $ renpy.block_rollback()
    menu:
        "Play introduction and tutorial":
            call tutorial_start from _call_tutorial_start

        "Skip introduction and tutorial":
            $ mc.business.event_triggers_dict["Tutorial_Section"] = False
    jump normal_start