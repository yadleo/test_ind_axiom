from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Lottery_pairs(Page):
    form_model = "player"
    form_fields = ["lottery_picked"]

    def lottery_picked_choices(self):
        import random
        l = self.player.current_lottery_pair()

        # suffle a lottery pair before being displayed
        return random.sample(list(l.values()), len((l.values())))
        l["lottery_A"], l["lottery_B"]


class Results(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        player_in_all_rounds = self.player.in_all_rounds()
        return {
            "player_in_all_rounds": player_in_all_rounds,
        }


page_sequence = [
    Lottery_pairs,
    Results
]
