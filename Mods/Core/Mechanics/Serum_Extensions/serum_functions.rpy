# Enables extra functions for SerumDesign / SerumTraits.
init 2 python:
   def anorexia_serum_on_turn(person, the_serum, add_to_log):
      return person.change_weight(amount = -0.4536, chance = 30)

   def anorexia_serum_on_remove(person, the_serum, add_to_log):
      person.change_max_energy(20, add_to_log = add_to_log)
      return person.change_weight(amount = -0.4536, chance = 100)

   def hypothyroidism_serum_on_turn(person, the_serum, add_to_log):
      return person.change_weight(amount = 0.4536, chance = 30)

   def hypothyroidism_serum_on_remove(person, the_serum, add_to_log):
      person.change_max_energy(20, add_to_log = add_to_log)
      return person.change_weight(amount = 0.4536, chance = 100)

   def height_increase_on_turn(person, the_serum, add_to_log):
      if renpy.random.randint(0,100) < 3: # 3% chance of breast size increase
         new_tits = Person.get_larger_tit(person.tits)
         if new_tits != person.tits: #Double check we don't already have them to avoid increasing breast weight infinitely
            person.tits = new_tits
            person.personal_region_modifiers["breasts"] += 0.1 #Her breasts receive a boost in region weight because they're natural.
      return person.change_height(person.get_height_step(), 10)

   def height_decrease_on_turn(person, the_serum, add_to_log):
      if renpy.random.randint(0,100) < 3: # 3% chance of breast size decrease
            new_tits = Person.get_smaller_tit(person.tits)
            if new_tits != person.tits:
               person.tits = new_tits
               person.personal_region_modifiers["breasts"] -= 0.1 #Her breasts receive a boost in region weight because they're natural.
      return person.change_height(-person.get_height_step(), 10)

   # Override base game serum functions
   if 'weight_loss' in dir():
      weight_loss.desc = "Decrease target subject body mass, using peptide YY3-36 as a serum component that acts on the hypothalamic feeding centers to inhibit hunger and calorie intake."
      weight_loss.positive_slug = "-1 pound/On Remove\n+30% Chance/Turn"
      weight_loss.on_turn = anorexia_serum_on_turn
      weight_loss.on_remove = anorexia_serum_on_remove

      weight_gain.desc = "Increase target subject body mass, by reducing hormones from the thyroid gland slowing down metabolism, thus causing weight gain."
      weight_gain.positive_slug = "+1 pound/On Remove\n+30% Chance/Turn"
      weight_gain.on_turn = hypothyroidism_serum_on_turn
      weight_gain.on_remove = anorexia_serum_on_remove

   if 'height_increase' in dir():
      height_increase.positive_slug = "+1\" Height/On Remove\n+10% Chance/Turn"
      height_increase.negative_slug = "10% Chance/On Remove Breast Enhancement\n3% Chance/Turn"
      height_increase.on_day = None
      height_increase.on_turn = height_increase_on_turn
      height_increase.on_remove = height_increase_on_day
   if 'height_decrease' in dir():
      height_decrease.positive_slug = "-1\" Height/On Remove\n+10% Chance/Turn"
      height_decrease.negative_slug = "10% Chance/On Remove Breast Reduction\n+3% Chance/Turn"
      height_decrease.on_day = None
      height_decrease.on_turn = height_decrease_on_turn
      height_decrease_on_remove = height_decrease_on_day
