from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants



class Instruction(Page):
    def is_displayed(self):
        return self.round_number == 1


class Task1(Page):
    form_model = models.Player
    form_fields = ['catches', 'clicks', 'score', 'expense']

    def vars_for_template(self):
        return {
            'prize': self.player.prize,
            'cost': self.player.cost,
            'round_num': self.round_number,
        }

    def before_next_page(self):
        self.player.set_payoff()

    def is_displayed(self):
        return self.round_number <6


class Task2(Page):
    form_model = models.Player
    form_fields = ['catches', 'clicks', 'score', 'expense']

    def vars_for_template(self):
        return {
            'prize': self.player.prize,
            'cost': self.player.cost,
            'round_num': self.round_number - 5,
        }

    def before_next_page(self):
        self.player.set_payoff()

    def is_displayed(self):
        return self.round_number >5 and self.round_number<11



class Task3(Page):
    form_model = models.Player
    form_fields = ['catches', 'clicks', 'score', 'expense']

    def vars_for_template(self):
        return {
            'prize': self.player.prize,
            'cost': self.player.cost,
            'round_num': self.round_number - 10,
        }

    def before_next_page(self):
        self.player.set_payoff()

    def is_displayed(self):
        return self.round_number >10 and self.round_number<16



class Task4(Page):
    form_model = models.Player
    form_fields = ['catches', 'clicks', 'score', 'expense']

    def vars_for_template(self):
        return {
            'prize': self.player.prize,
            'cost': self.player.cost,
            'round_num': self.round_number - 15,
        }

    def before_next_page(self):
        self.player.set_payoff()
        self.player.store_payoff()

    def is_displayed(self):
        return self.round_number>15

#
# class ResultsWaitPage(WaitPage):
#     pass


class Results(Page):
    def vars_for_template(self):
        if self.round_number<6:
            return{
                'game_num':1,
                'round_num':self.round_number,
            }
        elif self.round_number>5 and self.round_number<11:
            return{
                'game_num':2,
                'round_num':self.round_number-5,
            }
        elif self.round_number>10 and self.round_number<16:
            return{
                'game_num':3,
                'round_num':self.round_number-10,
            }
        elif self.round_number>15:
            return{
                'game_num':4,
                'round_num':self.round_number-15,
            }




page_sequence = [
    Instruction,
    Task1,
    Task2,
    Task3,
    Task4,
    Results,
]
