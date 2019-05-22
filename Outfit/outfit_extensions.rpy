

init -1:
    python:
        def remove_all_cum(self):
            remove_list = []
            for acc in self.accessories:
                if acc in [mouth_cum, tits_cum, stomach_cum, face_cum, ass_cum]:
                    remove_list.append(acc)
            for acc in remove_list:
                self.accessories.remove(acc)
            return
        
        Outfit.remove_all_cum = remove_all_cum
