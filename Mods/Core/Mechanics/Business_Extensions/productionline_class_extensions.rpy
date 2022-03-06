init 2 python:

    def clear_product(self):
        self.spare_production_points = 0
        self.autosell = False
        self.autosell_amount = 0
        self.selected_design = None
        self.production_weight = 0

    ProductionLine.clear_product = clear_product
