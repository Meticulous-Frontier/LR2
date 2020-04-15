# Fixes the nora traits names, since we only compare by name
# the mastery of all serums with the same name is raised when observing results
# since the nora traits have the same name, it causes the research
# Nora trait game mechanic to fail.

init 5 python:
    add_label_hijack("normal_start", "fix_nora_serum_traits")
    add_label_hijack("after_load", "fix_nora_serum_traits")

    def fix_nora_serum_traits_names():
        nora_suggest_up.name = "Nora's Research Trait XRC"
        nora_nightmares.name = "Nora's Research Trait CBX"
        nora_obedience_swing.name = "Nora's Research Trait XBR"
        nora_sluttiness_boost.name = "Nora's Research Trait RXC"
        return


label fix_nora_serum_traits(stack):
    python:
        $ fix_nora_serum_traits_names()
        # continue on the hijack stack if needed
        execute_hijack_call(stack)        
    return