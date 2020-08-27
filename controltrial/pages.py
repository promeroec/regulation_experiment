from ._builtin import Page, WaitPage


class Introduction(Page):
    def vars_for_template(self):
        return {
            'sufee': self.session.config['participation_fee'],
            'erpoint': self.session.config['real_world_currency_per_point'] * 100
        }


class Tree(Page):
    pass


class Quiz(Page):
    form_model = 'player'
    form_fields = ['question_1', 'question_2']

    def error_message(self, values):
        if values['question_1'] != 40 and values['question_2'] != 20:
            return '问题1和2的答案不正确'
        elif values['question_1'] == 40 and values['question_2'] != 20:
            return '问题2的答案不正确'
        elif values['question_1'] != 40 and values['question_2'] == 20:
            return '问题1的答案不正确'


class DecisionP1(Page):
    form_model = 'player'
    form_fields = ['decision']
    template_name = 'controltrial/Decision.html'

    def is_displayed(self):
        if self.player.id_in_group == 1:
            return True
        else:
            self.player.bot_result()
            return False


class DecisionP2(Page):
    form_model = 'player'
    form_fields = ['decision']
    template_name = 'controltrial/Decision.html'

    def is_displayed(self):
        if self.player.id_in_group == 2:
            return True
        else:
            self.player.bot_result()
            return False


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        for p in self.group.get_players():
            p.set_payoff()

    def app_after_this_page(self, upcoming_apps):
        return 'control'


# class Results(Page):
#     def vars_for_template(self):
#         me = self.player.decision
#         opponent = self.player.bot_decision
#         return {
#             'my_decision': me,
#             'opponent_decision': opponent,
#             'same_choice': me == opponent,
#         }


page_sequence = [
    Introduction,
    Tree,
    Quiz,
    DecisionP1,
    DecisionP2,
    ResultsWaitPage
    # Results
]
