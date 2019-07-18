

init -1 python:
    def remove_all_cum(self):
        remove_list = []
        for acc in self.accessories:
            if acc in [mouth_cum, tits_cum, stomach_cum, face_cum, ass_cum]:
                remove_list.append(acc)
        for acc in remove_list:
            self.accessories.remove(acc)
        return
    
    Outfit.remove_all_cum = remove_all_cum

    def get_overwear_slut_score_enhanced(self): #Calculates the sluttiness of this outfit assuming it's an overwear set. That means we assume a modest underwear set is used (ie. one that denies access).
        new_score = 0
        if self.tits_visible():
            new_score += 20
        elif self.tits_available():
            new_score += 10          

        if self.vagina_visible():
            new_score += 20
        elif self.vagina_available():
            new_score += 10

        new_score += self.get_total_slut_modifiers()

        return new_score

    Outfit.get_overwear_slut_score = get_overwear_slut_score_enhanced