init -1:
    default persistent.stats = {}

    # initialize with defaults (standard)
    default GAME_SPEED = 1
    default TIER_0_TIME_DELAY = 1
    default TIER_1_TIME_DELAY = 3
    default TIER_2_TIME_DELAY = 7
    default TIER_3_TIME_DELAY = 14

init 2 python:
    config.label_overrides["start"] = "alternative_start"

    def update_game_speed(speed):
        global GAME_SPEED, TIER_0_TIME_DELAY, TIER_1_TIME_DELAY, TIER_2_TIME_DELAY, TIER_3_TIME_DELAY

        GAME_SPEED = speed
        if speed == 0:
            TIER_0_TIME_DELAY = -1
            TIER_1_TIME_DELAY = 1
            TIER_2_TIME_DELAY = 3
            TIER_3_TIME_DELAY = 7
        elif speed == 1:
            TIER_0_TIME_DELAY = 1
            TIER_1_TIME_DELAY = 3
            TIER_2_TIME_DELAY = 7
            TIER_3_TIME_DELAY = 14
        elif speed == 2:
            TIER_0_TIME_DELAY = 1
            TIER_1_TIME_DELAY = 5
            TIER_2_TIME_DELAY = 12
            TIER_3_TIME_DELAY = 20
        else:
            TIER_0_TIME_DELAY = 2
            TIER_1_TIME_DELAY = 7
            TIER_2_TIME_DELAY = 15
            TIER_3_TIME_DELAY = 30
        return

label alternative_start():
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

        "Semi-Realistic pregnancy content\n{size=16}Birth control is not 100%% effective. Girls may not be taking birth control.{/size}":
            $ persistent.pregnancy_pref = 2

        "Realistic pregnancy content\n{size=16}Realistic cycles. Girls know their fertile times. Pulling out not 100%% effective. Girls don't want to get pregnant.{/size}":
            $ persistent.pregnancy_pref = 3

    "MOD" "How quickly would you like stories from the mod to play out? This will affect spacing between story events."
    menu:
        "Quick":
            $ update_game_speed(0)
        "Standard":
            $ update_game_speed(1)
        "Epic":
            $ update_game_speed(2)
        "Marathon":
            $ update_game_speed(3)

    $ easy_mode = False
    "MOD" "Do you want to play with original game difficulty or make the game easier?"
    menu:
        "Default Game Play":
            pass
        "Easier Game Play":
            "MOD" "All options for making the game easier will be applied after character creation."
            $ easy_mode = True

    "MOD" "Finally, the game uses random generated characters, the mod offers you the ability to control the random generation."
    "MOD" "We will now open that screen for you, so you can set it to your preferences."

    call screen generic_preference_ui()

    "MOD" "Thats all, now back to the normal game start."

    $ renpy.block_rollback()
    if persistent.stats:
        $ name = persistent.stats['name']
        $ l_name = persistent.stats['l_name']
        $ b_name = persistent.stats['b_name']
    call screen enhanced_character_create_screen()
    $ return_arrays = _return #These are the stat, skill, and sex arrays returned from the character creator.
    $ setattr(persistent, "stats", {})
    $ [[persistent.stats["cha"],persistent.stats["int"],persistent.stats["foc"]], [persistent.stats["h_skill"],persistent.stats["m_skill"],persistent.stats["r_skill"],persistent.stats["p_skill"],persistent.stats["s_skill"]], [persistent.stats["F_skill"],persistent.stats["O_skill"],persistent.stats["V_skill"],persistent.stats["A_skill"]]] = _return
    $ [persistent.stats["name"],persistent.stats["l_name"],persistent.stats["b_name"]] = [store.name,store.l_name,store.b_name]


    python:
        renpy.show("Loading", layer = "solo", at_list = [truecenter], what = Image(get_file_handle("creating_world.png")))
        renpy.pause(0.5)
        renpy.game.interface.timeout(30)
        if easy_mode:
            for array in range(0, len(return_arrays)):
                for val in range(0, len(return_arrays[array])):
                    return_arrays[array][val] += 2

    call initialize_game_state(store.name,store.b_name,store.l_name,return_arrays[0],return_arrays[1],return_arrays[2], max_num_of_random = 2) from _call_initialize_game_state

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
            purchase_policy(max_attention_increase_1_policy, ignore_cost = True)
            renpy.hide("Loading", layer = "solo")

    $ renpy.block_rollback()
    menu:
        "Play introduction and tutorial":
            call tutorial_start from _call_tutorial_start

        "Skip introduction and tutorial":
            $ mc.business.event_triggers_dict["Tutorial_Section"] = False
    jump normal_start

screen enhanced_character_create_screen():
    if persistent.stats:
        default cha = persistent.stats['cha']
        default int = persistent.stats['int']
        default foc = persistent.stats['foc']

        default h_skill = persistent.stats['h_skill']
        default m_skill = persistent.stats['m_skill']
        default r_skill = persistent.stats['r_skill']
        default p_skill = persistent.stats['p_skill']
        default s_skill = persistent.stats['s_skill']

        default F_skill = persistent.stats['F_skill']
        default O_skill = persistent.stats['O_skill']
        default V_skill = persistent.stats['V_skill']
        default A_skill = persistent.stats['A_skill']

        default character_points = 0
    else:
        default cha = 0
        default int = 0
        default foc = 0

        default h_skill = 0
        default m_skill = 0
        default r_skill = 0
        default p_skill = 0
        default s_skill = 0

        default F_skill = 0
        default O_skill = 0
        default V_skill = 0
        default A_skill = 0

        default character_points = 20

    default name_select = 0
    default stat_max = 4
    default work_skill_max = 4
    default sex_skill_max = 4

    imagebutton auto "/gui/Text_Entry_Bar_%s.png" action [SetScreenVariable("name_select",1), SetVariable("name","")] pos (320,800) xanchor 0.5 yanchor 0.5 alternate SetScreenVariable("name_select",0)
    imagebutton auto "/gui/Text_Entry_Bar_%s.png" action [SetScreenVariable("name_select",3), SetVariable("l_name","")] pos (320,880) xanchor 0.5 yanchor 0.5 alternate SetScreenVariable("name_select",0)
    imagebutton auto "/gui/Text_Entry_Bar_%s.png" action [SetScreenVariable("name_select",2), SetVariable("b_name","")] pos (320,960) xanchor 0.5 yanchor 0.5 alternate SetScreenVariable("name_select",0)
    imagebutton auto "/gui/button/choice_%s_background.png" action Return([[cha,int,foc],[h_skill,m_skill,r_skill,p_skill,s_skill],[F_skill,O_skill,V_skill,A_skill]]) pos (1560,900) xanchor 0.5 yanchor 0.5 sensitive character_points == 0

    if name_select == 1: #Name
        input default name pos(320,800) changed name_func xanchor 0.5 yanchor 0.5 style "menu_text_style" length 25
    else:
        text name pos(320,800) xanchor 0.5 yanchor 0.5 style "menu_text_style"

    if name_select == 3: #Last Name
        input default l_name pos(320,880) changed l_name_func xanchor 0.5 yanchor 0.5 style "menu_text_style" length 25
    else:
        text l_name pos(320,880) xanchor 0.5 yanchor 0.5 style "menu_text_style"

    if name_select == 2: #Business Name
        input default b_name pos(320,960) changed b_name_func xanchor 0.5 yanchor 0.5 style "menu_text_style" length 25
    else:
        text b_name pos(320,960) xanchor 0.5 yanchor 0.5 style "menu_text_style"

    if name_select in [1,2,3] and renpy.mobile:
        textbutton "Hide Keyboard" action SetScreenVariable("name_select", 0) xalign 0.0 yalign 0.0 style "textbutton_style" text_style "textbutton_text_style"

    if character_points > 0:
        text "Spend All Character Points to Proceed" style "menu_text_style" anchor(0.5,0.5) pos(1560,900)
    else:
        text "Finish Character Creation" style "menu_text_style" anchor(0.5,0.5) pos(1560,900)

    text "Character Points Remaining: [character_points]" style "menu_text_style" xalign 0.5 yalign 0.1 size 30
    hbox: #Main Stats Section
        yalign 0.7
        xalign 0.5
        xanchor 0.5
        frame:
            background "#1a45a1aa"
            vbox:
                xsize 550
                text "Main Stats (3 points/level)" style "menu_text_style" size 25
                null height 40
                hbox:
                    text "Charisma: " style "menu_text_style"
                    textbutton "<" action [SetScreenVariable("cha",cha-1), SetScreenVariable("character_points", character_points+3)] sensitive cha>0 style "textbutton_style" text_style "textbutton_text_style"
                    text str(cha) + "/[stat_max]" style "textbutton_text_style"
                    textbutton ">" action [SetScreenVariable("cha",cha+1), SetScreenVariable("character_points", character_points-3)] sensitive character_points>2 and cha<stat_max style "textbutton_style" text_style "textbutton_text_style"
                text "     Your visual appearance and force of personality. Charisma is the key attribute for selling serums and managing your business." style "menu_text_style"
                null height 30
                hbox:
                    text "Intelligence: " style "menu_text_style"
                    textbutton "<" action [SetScreenVariable("int",int-1), SetScreenVariable("character_points", character_points+3)] sensitive int>0 style "textbutton_style" text_style "textbutton_text_style"
                    text str(int) + "/[stat_max]" style "textbutton_text_style"
                    textbutton ">" action [SetScreenVariable("int",int+1), SetScreenVariable("character_points", character_points-3)] sensitive character_points>2 and int<stat_max style "textbutton_style" text_style "textbutton_text_style"
                text "     Your raw knowledge and ability to think quickly. Intelligence is the key attribute for research and development of serums." style "menu_text_style"
                null height 30
                hbox:
                    text "Focus: " style "menu_text_style"
                    textbutton "<" action [SetScreenVariable("foc",foc-1), SetScreenVariable("character_points", character_points+3)] sensitive foc>0 style "textbutton_style" text_style "textbutton_text_style"
                    text str(foc) + "/[stat_max]" style "textbutton_text_style"
                    textbutton ">" action [SetScreenVariable("foc",foc+1), SetScreenVariable("character_points", character_points-3)] sensitive character_points>2 and foc<stat_max style "textbutton_style" text_style "textbutton_text_style"
                text "     Your mental endurance and precision. Focus is the key attribute for production and supply procurement." style "menu_text_style"

        null width 40
        frame:
            background "#1a45a1aa"
            vbox:
                xsize 550
                text "Work Skills (1 point/level)" style "menu_text_style" size 25
                null height 40
                hbox:
                    text "Human Resources: " style "menu_text_style"
                    textbutton "<" action [SetScreenVariable("h_skill",h_skill-1), SetScreenVariable("character_points", character_points+1)] sensitive h_skill>0 style "textbutton_style" text_style "textbutton_text_style"
                    text str(h_skill)+"/[work_skill_max]" style "textbutton_text_style"
                    textbutton ">" action [SetScreenVariable("h_skill",h_skill+1), SetScreenVariable("character_points", character_points-1)] sensitive character_points>0 and h_skill<work_skill_max style "textbutton_style" text_style "textbutton_text_style"
                text "     Your skill at human resources. Crucial for maintaining an efficient business." style "menu_text_style"
                null height 30
                hbox:
                    text "Marketing: " style "menu_text_style"
                    textbutton "<" action [SetScreenVariable("m_skill",m_skill-1), SetScreenVariable("character_points", character_points+1)] sensitive m_skill>0 style "textbutton_style" text_style "textbutton_text_style"
                    text str(m_skill)+"/[work_skill_max]" style "textbutton_text_style"
                    textbutton ">" action [SetScreenVariable("m_skill",m_skill+1), SetScreenVariable("character_points", character_points-1)] sensitive character_points>0 and m_skill<work_skill_max style "textbutton_style" text_style "textbutton_text_style"
                text "     Your skill at marketing. Higher skill will allow you to extend your market reach faster." style "menu_text_style"
                null height 30
                hbox:
                    text "Research and Development: " style "menu_text_style"
                    textbutton "<" action [SetScreenVariable("r_skill",r_skill-1), SetScreenVariable("character_points", character_points+1)] sensitive r_skill>0 style "textbutton_style" text_style "textbutton_text_style"
                    text str(r_skill)+"/[work_skill_max]" style "textbutton_text_style"
                    textbutton ">" action [SetScreenVariable("r_skill",r_skill+1), SetScreenVariable("character_points", character_points-1)] sensitive character_points>0 and r_skill<work_skill_max style "textbutton_style" text_style "textbutton_text_style"
                text "     Your skill at researching new serum traits and designs. Critical for improving your serum inventory." style "menu_text_style"
                null height 30
                hbox:
                    text "Production: " style "menu_text_style"
                    textbutton "<" action [SetScreenVariable("p_skill",p_skill-1), SetScreenVariable("character_points", character_points+1)] sensitive p_skill>0 style "textbutton_style" text_style "textbutton_text_style"
                    text str(p_skill)+"/[work_skill_max]" style "textbutton_text_style"
                    textbutton ">" action [SetScreenVariable("p_skill",p_skill+1), SetScreenVariable("character_points", character_points-1)] sensitive character_points>0 and p_skill<work_skill_max style "textbutton_style" text_style "textbutton_text_style"
                text "     Your skill at producing serum in the production lab. Produced serums can then be sold for profit or kept for personal use." style "menu_text_style"
                null height 30
                hbox:
                    text "Supply Procurement: " style "menu_text_style"
                    textbutton "<" action [SetScreenVariable("s_skill",s_skill-1), SetScreenVariable("character_points", character_points+1)] sensitive s_skill>0 style "textbutton_style" text_style "textbutton_text_style"
                    text str(s_skill)+"/[work_skill_max]" style "textbutton_text_style"
                    textbutton ">" action [SetScreenVariable("s_skill",s_skill+1), SetScreenVariable("character_points", character_points-1)] sensitive character_points>0 and s_skill<work_skill_max style "textbutton_style" text_style "textbutton_text_style"
                text "     Your skill at obtaining raw supplies for your production division. Without supply, nothing can be created in the lab." style "menu_text_style"
                null height 30
        null width 40
        frame:
            background "#1a45a1aa"
            vbox:
                xsize 550
                text "Sex Skills (1 point/level)" style "menu_text_style" size 25
                null height 40
                hbox:
                    text "Foreplay: " style "menu_text_style"
                    textbutton "<" action [SetScreenVariable("F_skill",F_skill-1), SetScreenVariable("character_points", character_points+1)] sensitive F_skill>0 style "textbutton_style" text_style "textbutton_text_style"
                    text str(F_skill)+"/[sex_skill_max]" style "textbutton_text_style"
                    textbutton ">" action [SetScreenVariable("F_skill",F_skill+1), SetScreenVariable("character_points", character_points-1)] sensitive character_points>0 and F_skill<sex_skill_max style "textbutton_style" text_style "textbutton_text_style"
                text "     Your skill at foreplay, including fingering, kissing, and groping." style "menu_text_style"
                null height 30
                hbox:
                    text "Oral: " style "menu_text_style"
                    textbutton "<" action [SetScreenVariable("O_skill",O_skill-1), SetScreenVariable("character_points", character_points+1)] sensitive O_skill>0 style "textbutton_style" text_style "textbutton_text_style"
                    text str(O_skill)+"/[sex_skill_max]" style "textbutton_text_style"
                    textbutton ">" action [SetScreenVariable("O_skill",O_skill+1), SetScreenVariable("character_points", character_points-1)] sensitive character_points>0 and O_skill<sex_skill_max style "textbutton_style" text_style "textbutton_text_style"
                text "     Your skill at giving oral to women, as well as being a pleasant recipient." style "menu_text_style"
                null height 30
                hbox:
                    text "Vaginal: " style "menu_text_style"
                    textbutton "<" action [SetScreenVariable("V_skill",V_skill-1), SetScreenVariable("character_points", character_points+1)] sensitive V_skill>0 style "textbutton_style" text_style "textbutton_text_style"
                    text str(V_skill)+"/[sex_skill_max]" style "textbutton_text_style"
                    textbutton ">" action [SetScreenVariable("V_skill",V_skill+1), SetScreenVariable("character_points", character_points-1)] sensitive character_points>0 and V_skill<sex_skill_max style "textbutton_style" text_style "textbutton_text_style"
                text "     Your skill at vaginal sex in any position." style "menu_text_style"
                null height 30
                hbox:
                    text "Anal: " style "menu_text_style"
                    textbutton "<" action [SetScreenVariable("A_skill",A_skill-1), SetScreenVariable("character_points", character_points+1)] sensitive A_skill>0 style "textbutton_style" text_style "textbutton_text_style"
                    text str(A_skill)+"/[sex_skill_max]" style "textbutton_text_style"
                    textbutton ">" action [SetScreenVariable("A_skill",A_skill+1), SetScreenVariable("character_points", character_points-1)] sensitive character_points>0 and A_skill<sex_skill_max style "textbutton_style" text_style "textbutton_text_style"
                text "     Your skill at anal sex in any position." style "menu_text_style"
                null height 30
