# init -1 python:
#     class Sex_Shop_Owner(Person):
#         #shop_progress_stage = 0
#         # shop_investment_total = 0
#         # shop_investment_rate = 0
#         #shop_stage_one_investment_total = 0
#         # shop_stage_two_investment_total = 0
#         # shop_stage_three_investment_total = 0
#         shop_invest_one_max = 5000
#         shop_invest_two_max = 20000
#         shop_invest_three_max = 30000
#         shop_owner_relationship_stage = 0
#
#         def run_day(self):
#             if self.shop_progress_stage > 0:
#                 investment_return = self.calc_investment_return()
#                 if (investment_return > 0) :
#                     mc.business.funds += investment_return
#                     business_message = "Sex shop has returned $" + str(investment_return) + " on your investment!"
#                     mc.business.add_normal_message(business_message)
#
#             super(Sex_Shop_Owner, self).run_day()
#         pass
#
#         def calc_investment_return(self):
#             investment_return = 0
#             if self.shop_progress_stage > 0:
#                 investment_return += (30 * store.shop_difficulty_value)
#                 investment_return += int (self.shop_stage_one_investment_total * self.shop_investment_rate * 0.01 * store.shop_difficulty_value)
#             if self.shop_progress_stage > 1:
#                 investment_return += int (self.shop_stage_two_investment_total * self.shop_investment_rate * 0.006 * store.shop_difficulty_value)
#             if self.shop_progress_stage > 2:
#                 investment_return += int (self.shop_stage_three_investment_total * self.shop_investment_rate * 0.004 * store.shop_difficulty_value)
#             return investment_return
