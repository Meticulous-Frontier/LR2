Any template in the `Mods/Crisis/Template/` folder can be copy and pasted individually. Replace the content and TEMPLATE with a unique name.
ActionMod type events will automatically be filterable in the options list in MC's room.
If the crisis is content that you want to be disabled initially, you can add
`initialization = init_action_mod_disabled`
As an argument to the ActionMod init, EG:

```
TEMPLATE_action = ActionMod("TEMPLATE event description", crisis_TEMPLATE_requirement,"crisis_TEMPLATE_label",
      menu_tooltip = "Expanded Description.", initialization = init_action_mod_disabled, category="Home", is_crisis = True, is_morning_crisis = True)
```

If you have questions or suggestions, please let me know on the discord! -Starbuck
