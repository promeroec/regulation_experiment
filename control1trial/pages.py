from ._builtin import Page, WaitPage


class Introduction(Page):
    def vars_for_template(self):
        return {
            'sufee' : self.session.config['participation_fee'],
            'erpoint' : self.session.config['real_world_currency_per_point']*100
        }


class Tree(Page):
    pass


class SendMessageP1(Page):
    form_model = 'player'
    form_fields = ['send_message']
    template_name = 'control1trial/SendMessage.html'

    def is_displayed(self):
        if self.player.id_in_group == 1:
            return True
        else:
            self.player.rand_send_message()
            return False


class Wait(WaitPage):
    pass


class SendMessageP2(Page):
    form_model = 'player'
    form_fields = ['send_answer']
    template_name = 'control1trial/SendMessage.html'

    def is_displayed(self):
        if self.player.id_in_group == 2:
            return True
        else:
            self.player.rand_send_answer()
            return False


class DecisionP1(Page):
    form_model = 'player'
    form_fields = ['decision']
    template_name = 'control1trial/Decision.html'

    def is_displayed(self):
        if self.player.id_in_group == 1:
            return True
        else:
            self.player.bot_result()
            return False


class DecisionP2(Page):
    form_model = 'player'
    form_fields = ['decision']
    template_name = 'control1trial/Decision.html'

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
        return 'control1'


# class Results(Page):
#     def vars_for_template(self):
#         me = self.player
#         opponent = me.other_player()
#         return {
#             'my_decision': me.decision,
#             'opponent_decision': opponent.decision,
#             'same_choice': me.decision == opponent.decision,
#         }
#
#     def app_after_this_page(self, upcoming_apps):
#         return 'control1'


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


page_sequence = [
    Introduction,
    Tree,
    Quiz,
    SendMessageP1,
    # Wait,
    SendMessageP2,
    # Wait,
    DecisionP1,
    DecisionP2,
    ResultsWaitPage
    # Results
]
