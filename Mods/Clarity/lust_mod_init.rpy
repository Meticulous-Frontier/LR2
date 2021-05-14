init 5 python:
    add_label_hijack("normal_start", "activate_lust_mod_core")
    add_label_hijack("after_load", "update_lust_mod_core")


label activate_lust_mod_core(stack):
    call lust_mod_init() from _init_lust_mod_01
    python:
        execute_hijack_call(stack)
    return

label update_lust_mod_core(stack):
    if not mc.business.event_triggers_dict.get("lust_mod_init", False):
        call lust_mod_init() from _init_lust_mod_02
    python:

        execute_hijack_call(stack)
    return


label lust_mod_init():
    $ mc.business.event_triggers_dict["lust_mod_init"] = True
    $ mc.business.add_mandatory_crisis(lust_blowjob_intro)
    return
