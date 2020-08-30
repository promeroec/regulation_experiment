from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


author = 'Lingbo Huang'

doc = """
Ball-Catching Task
"""


class Constants(BaseConstants):
    name_in_url = 'ball_catch'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):

    def creating_session(self):

        for p in self.get_players():
            p.prize = 10
            p.cost = 0
            # p.condition = p.participant.vars['my_prize_and_cost'][self.round_number - 1]
            # if p.condition <= 3:
            #     p.prize = 10
            #     p.cost = 5 * (p.condition - 1)
            # else:
            #     p.prize = 20
            #     p.cost = 5 * (p.condition - 4)


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    # condition = models.IntegerField()
    prize = models.IntegerField()
    cost = models.IntegerField()

    catches = models.IntegerField()
    clicks = models.IntegerField()
    score = models.IntegerField()
    expense = models.IntegerField()

    def set_payoff(self):
        self.payoff = self.score - self.expense

    def store_payoff(self):
        if self.round_number ==20:
            g1_ran = random.choice([1,2,3,4,5])
            g2_ran = random.choice([6,7,8,9,10])
            g3_ran = random.choice([11,12,13,14,15])
            g4_ran = random.choice([16,17,18,19,20])
            self.participant.vars['g1_po_round'] = g1_ran
            self.participant.vars['g2_po_round'] = g2_ran
            self.participant.vars['g1_payoff'] = self.in_round(g1_ran).payoff
            self.participant.vars['g2_payoff'] = self.in_round(g2_ran).payoff

            self.participant.vars['g3_po_round'] = g3_ran
            self.participant.vars['g4_po_round'] = g4_ran
            self.participant.vars['g3_payoff'] = self.in_round(g3_ran).payoff
            self.participant.vars['g4_payoff'] = self.in_round(g4_ran).payoff

            self.participant.payoff = self.participant.vars['g1_payoff']+self.participant.vars['g2_payoff']\
                                      +self.participant.vars['g3_payoff']+self.participant.vars['g4_payoff']
