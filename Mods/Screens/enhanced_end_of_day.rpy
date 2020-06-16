init 2:
    screen end_of_day_update():
        add "Paper_Background.png"
        zorder 100

        hbox:
            xalign 0.5
            yoffset 20
            spacing 200
            ysize 100

            text mc.business.name style "textbutton_text_style" size 40 color "#cccccc"

        frame:
            background "#1a45a1aa"
            yoffset 100
            xalign 0.05
            xanchor 0.0
            yanchor 0.0
            xsize 1700
            ysize 230

            hbox:
                spacing 100
                vbox:
                    xsize 800
                    text "Daily Statistics:" style "textbutton_text_style" size 26
                    text "     " + "Company Efficiency: " + str(mc.business.team_effectiveness) + "%" style "textbutton_text_style"
                    text "     " + "Production Potential: " + str(__builtin__.round(mc.business.production_potential, 2)) style "textbutton_text_style"
                    text "     " + "Supplies Procured: " + str(mc.business.supplies_purchased) + " Units" style "textbutton_text_style"
                    text "     " + "Production Used: " + str(__builtin__.round(mc.business.production_used, 2)) + " Units" style "textbutton_text_style"
                    text "     " + "Research Produced: " + str(__builtin__.round(mc.business.research_produced, 2)) style "textbutton_text_style"

                vbox:
                    xsize 800
                    $ salary_costs = 0
                    if day % 7 > 0 and day % 7 < 6: # day count already changed before summary is shown
                        $ salary_costs = mc.business.calculate_salary_cost()
                    $ profit = mc.business.funds - mc.business.funds_yesterday
                    $ mc.business.listener_system.fire_event("daily_profit", profit = profit)
                    $ mc.business.listener_system.fire_event("side_money", count = starbuck.calc_investment_return())
                    if profit > 0:
                        text "Profit: $" + str(__builtin__.round(profit, 2))  style "textbutton_text_style" size 26 color "#00A000"
                    else:
                        text "Loss: $" + str(__builtin__.round(abs(profit), 2))  style "textbutton_text_style" size 26 color "#A00000"

                    text "     " + "Sales Made: $" + str(__builtin__.round(mc.business.sales_made, 2)) style "textbutton_text_style"
                    text "     " + "Daily Salary Paid: $" + str(__builtin__.round(salary_costs, 2)) style "textbutton_text_style"
                    text "     " + "Serums Sold Today: " + str(mc.business.serums_sold) style "textbutton_text_style"
                    text "     " + "Serums Ready for Sale: " + str(mc.business.sale_inventory.get_any_serum_count()) style "textbutton_text_style"

        frame:
            background "#1a45a1aa"
            xalign 0.05
            yoffset 350
            xanchor 0.0
            yanchor 0.0

            viewport:
                mousewheel True
                scrollbars "vertical"
                xsize 1690
                ysize 500
                vbox:
                    text "Highlights:" style "textbutton_text_style" size 26
                    for item in mc.business.message_list:
                        text "     " + item style "textbutton_text_style" size 20

                    for item in mc.business.counted_message_list:
                        text "     " + item + " x " + str(int(mc.business.counted_message_list[item])) style "textbutton_text_style" size 20

        frame:
            background None
            anchor [0.5,0.5]
            align [0.5,0.9]
            xysize [500,125]
            imagebutton:
                align [0.5,0.5]
                auto "gui/button/choice_%s_background.png"
                focus_mask "gui/button/choice_idle_background.png"
                action Return()
            textbutton "End Day" align [0.5,0.5] style "button_text"
