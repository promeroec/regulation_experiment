from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):

    age = models.IntegerField(
        label='你的年龄？',
        min=13, max=125)

    gender = models.StringField(
        choices=['男性', '女性', '其它'],
        label='你的性别？',
        widget=widgets.RadioSelect)

    education = models.StringField(
        choices=['没有任何学校教育','小学','初中','高中',
        '大学未毕业','职业培训',
        '大学本科（包括在读）','硕士研究生','博士研究生'],
        label='你所获得的最高学历是什么？',
        widget=widgets.RadioSelect)

    language = models.StringField(
        label='你的母语是什么？',
        widget=widgets.TextInput)

    country = models.StringField(
        label='你在哪个国家出生？',
        widget=widgets.TextInput)

    intent = models.StringField(
        choices=['自私的','大方的','敌对的','合作的','理性的','不理性的'],
        label='你如何评价另一位参与者在做选择时的意图？',
        widget=widgets.RadioSelect)

    identity = models.StringField(
        choices=['会','不会','可能会'],
        label='假如你知道另一位参与者是谁，你的选择会不一样吗？',
        widget=widgets.RadioSelect)

    risk = models.StringField(
        choices=['0 完全不愿冒险','1','2','3','4','5','6','7','8','9','10 完全愿意冒险'],
        label='你如何评价你自己：你更倾向于冒险还是避免风险？请使用下面度量来回答这个问题。0代表“完全不愿冒险”，10代表“完全愿意冒险”。',        
        widget=widgets.RadioSelect)
