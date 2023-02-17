init 2:
    python:
        def get_formatted_date_string():
            day_name = day_names[day%7]
            day_in_month = (day%30) + 1
            month_name = month_names[int((day/30) + 8)%12]
            day_part = time_names[time_of_day]
            return "{day_name} {month_name} {day_in_month} - {day_part}".format(day_name = day_name, day_in_month = day_in_month, month_name = month_name, day_part = day_part)

    screen main_ui(): #The UI that shows most of the important information to the screen.
        python:
            known = len(known_people_in_the_game())
            total = len(all_people_in_the_game())
            day_info = "{size=16}" + get_formatted_date_string() + " (day "+ str(day) + "){/size}"
            arousal_info = get_arousal_with_token_string(mc.arousal, mc.max_arousal)
            energy_info = get_energy_string(mc.energy, mc.max_energy)
            clarity_info = str(__builtin__.int(mc.free_clarity))
            locked_clarity_info = get_locked_clarity_with_token_string(mc.locked_clarity)
            attention_info = get_attention_string(mc.business.attention, mc.business.max_attention)

        frame:
            background Transform("Info_Frame_1.png", alpha=persistent.hud_alpha)
            xsize 600
            ysize 400
            yalign 0.0
            vbox:
                text "[day_info]" style "menu_text_style" size 18
                textbutton "Outfit Manager" action Call("outfit_master_manager",from_current=True) style "textbutton_style" text_style "textbutton_text_style" xsize 220 tooltip "Design outfits to set as uniforms or give to suggest to women."
                textbutton "Check Inventory" action ui.callsinnewcontext("check_inventory_loop") style "textbutton_style" text_style "textbutton_text_style" xsize 220 tooltip "Check what serums you are currently carrying."
                if mc.stat_goal.completed or mc.work_goal.completed or mc.sex_goal.completed:
                    textbutton "Character Sheet" action Show("mc_character_sheet") style "textbutton_style" text_style "textbutton_text_style" xsize 220 background "#44BB44" insensitive_background "#222222" hover_background "#aaaaaa" tooltip "Check your stats, skills, and goals."
                else:
                    textbutton "Character Sheet" action Show("mc_character_sheet") style "textbutton_style" text_style "textbutton_text_style" xsize 220 tooltip "Check your stats, skills, and goals."
                textbutton "Perk Sheet" action Show("mc_perk_sheet") style "textbutton_style" text_style "textbutton_text_style" xsize 220 tooltip "Check your stat, item, and ability perks."

                null height 10

                textbutton "Arousal: [arousal_info]":
                    style "transparent_style"
                    text_style "menu_text_style"
                    tooltip "Your personal arousal. When you reach your limit you will be forced to climax and your energy will drop."
                    action NullAction()

                textbutton "Energy: [energy_info]":
                    style "transparent_style"
                    text_style "menu_text_style"
                    tooltip "Many actions require energy to perform, sex especially. Energy comes back slowly throughout the day, and most of it is recovered after a good night's sleep."
                    action NullAction()

                textbutton "Clarity: [clarity_info]":
                    style "transparent_style"
                    text_style "menu_text_style"
                    tooltip "Post-nut clarity is generated by climaxing. The higher the lust, the higher the clarity gained. It can be used to unlock new serum traits for research or to create new serum designs."
                    action NullAction()

                textbutton "Lust: [locked_clarity_info]":
                    style "transparent_style"
                    text_style "menu_text_style"
                    tooltip "Exposure to sexual encounters produces lust. Converts into clarity during orgasm. Different lust to clarity ratios may create different dialogue options."
                    action NullAction()

                textbutton "Attention: [attention_info]":
                    style "transparent_style"
                    text_style "menu_text_style"
                    tooltip "The attention your company is attracting from the local authorities."
                    action NullAction()

                textbutton "World: [known]/[total]":
                    style "transparent_style"
                    text_style "menu_text_style"
                    tooltip "Shows the number of known and total people in your world."
                    action NullAction()
