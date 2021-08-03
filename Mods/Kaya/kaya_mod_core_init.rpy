init 5 python:
    add_label_hijack("normal_start", "activate_kaya_mod_core")
    add_label_hijack("after_load", "update_kaya_mod_core")


label activate_kaya_mod_core(stack):
    python:

        kaya_mod_initialization()
        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label update_kaya_mod_core(stack):
    python:
        if "kaya" not in globals():
            kaya_mod_initialization()
        elif kaya_can_get_drinks() and not kaya_studies_with_lily():
            kaya.add_unique_on_room_enter_event(kaya_meet_lily_at_uni)
        execute_hijack_call(stack)
    return
