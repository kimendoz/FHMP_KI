from ._builtin import Page, WaitPage

# Each page that a player sees is defined in this file
# Each class in this file represents a page

# Each page can inherit either a "Page" class or a "WaitPage" class
# If a page inherits a "WaitPage" class, the page is simply a page to wait until
# all players arrive
# Example 1: class BeginWaitPage(Waitpage) is a page class that inherits "WaitPage" class
# This page is not shown to players and is used to wait until all players are on the same page (no pun intended!)

# Example 2: class SellerChoice(Page) is a page that inherits "Page" class
# This page is shown to players

# For detailed documentation regarding pages, please refer to oTree's documentation page below
# https://otree.readthedocs.io/en/latest/pages.html


# This is a transition page that is not shown to the end-user
class BeginWaitPage(WaitPage):
	# This method is called once all players arrive at this page.
	def after_all_players_arrive(self):
		# init_round() is a method defined in models.py
		# The init_round() method does two things as described below
		# 1. It generates an estimated asset value between 1-20
		# 2. It determines the true asset value based on the estimated value from Step 1
		# 3. It sets initial budgets for all sellers and buyers
		self.group.init_round()


class SellerChoiceNotEnoughBudget(Page):
	def is_displayed(self):
		return self.player.role() == 'seller' and self.player.budget < self.group.get_high_detail_disclosure_cost()

	def vars_for_template(self):
		asset_est_values_by_player_id = {
			1: self.group.asset1_est_value,
			2: self.group.asset2_est_value,
			3: self.group.asset3_est_value
		}

		asset_est_value_text = "{0:.0f}".format(asset_est_values_by_player_id[self.player.id_in_group])

		return {
			'asset_est_value': asset_est_value_text
		}


class SellerChoiceLowHigh(Page):
	form_model = 'group'

	def is_displayed(self):
		return self.player.role() == 'seller' and self.player.budget >= self.group.get_high_detail_disclosure_cost()

	# Return disclose level form field based on player id
	def get_form_fields(self):
		form_fields_by_player_id = {
			1: ['asset1_disclose_high'],
			2: ['asset2_disclose_high'],
			3: ['asset3_disclose_high']
		}

		return form_fields_by_player_id[self.player.id_in_group]

	def vars_for_template(self):
		asset_est_values_by_player_id = {
			1: self.group.asset1_est_value,
			2: self.group.asset2_est_value,
			3: self.group.asset3_est_value
		}

		asset_est_value_text = "{0:.0f}".format(asset_est_values_by_player_id[self.player.id_in_group])

		return {
			'asset_est_value': asset_est_value_text
		}

	def before_next_page(self):
		if self.player.role() == 'seller':
			self.player.update_seller_budget_after_reporting()


class SellerChoiceDiscloseRange(Page):
	form_model = 'group'

	def is_displayed(self):
		return self.player.role() == 'seller'

	# Return disclose interval form field based on player id
	def get_form_fields(self):
		form_fields_by_player_id = {
			1: ['asset1_disclose_interval'],
			2: ['asset2_disclose_interval'],
			3: ['asset3_disclose_interval']
		}

		return form_fields_by_player_id[self.player.id_in_group]

	def vars_for_template(self):
		asset_est_values_by_player_id = {
			1: self.group.asset1_est_value,
			2: self.group.asset2_est_value,
			3: self.group.asset3_est_value
		}

		asset_disclose_high = {
			1: self.group.asset1_disclose_high,
			2: self.group.asset2_disclose_high,
			3: self.group.asset3_disclose_high
		}

		asset_est_value_text = "{0:.0f}".format(asset_est_values_by_player_id[self.player.id_in_group])

		return {
			'asset_est_value': asset_est_value_text,
			'asset_disclose_high': asset_disclose_high[self.player.id_in_group]
		}

	def before_next_page(self):
		pass


# This is a transition page that is not shown to the end-user
# By the time all players arrive on this page, sellers have finished
# picking reporting options and disclose range
# Seller grade calculation should be done in this step
class SellerChoiceResultWaitPage(WaitPage):
	def after_all_players_arrive(self):
		self.group.set_seller_grades()


class BuyerChoice(Page):
	form_model = 'player'

	# Input text fields to be shown to buyers
	form_fields = ['bid_asset1', 'bid_asset2', 'bid_asset3']

	# is_displayed() is used to show this page only to the buyers
	def is_displayed(self):
		return self.player.role() == 'buyer'

	def vars_for_template(self):
		return {
			'asset1_disclose_interval': self.group.asset1_disclose_interval,
			'asset2_disclose_interval': self.group.asset2_disclose_interval,
			'asset3_disclose_interval': self.group.asset3_disclose_interval,
			'seller1_grade': self.group.seller1_grade,
			'seller2_grade': self.group.seller2_grade,
			'seller3_grade': self.group.seller3_grade
		}

	def error_message(self, values):
		if values["bid_asset1"] + values["bid_asset2"] + values["bid_asset3"] > self.player.budget:
			return 'Sum of the bids exceeds your budget.'


# This is a transition page that is not shown to the end-user
# Bid winners and payoffs for each round are determined here
class RoundResultWaitPage(WaitPage):
	def after_all_players_arrive(self):
		self.group.determine_bid_winners()
		self.group.set_payoffs()


class RoundResult(Page):
	def vars_for_template(self):
		buyers = self.group.get_buyers()

		return {
			# This array of objects is used in the Results page
			# to display range of high asset probabilities, true asset value,
			# other buyers' bids, and winners

			'assets': [
				{
					'id': 1,
					'disclose_interval': self.group.asset1_disclose_interval,
					'true_value': self.group.asset1_true_value,
					'bids': list(map(lambda b: {
						'player_id': b.id_in_group,
						'amount': b.bid_asset1,
						'did_win': b.did_win_asset1,
						'is_self': b.id_in_group == self.player.id_in_group
					}, buyers))
				},
				{
					'id': 2,
					'disclose_interval': self.group.asset2_disclose_interval,
					'true_value': self.group.asset2_true_value,
					'bids': list(map(lambda b: {
						'player_id': b.id_in_group,
						'amount': b.bid_asset2,
						'did_win': b.did_win_asset2,
						'is_self': b.id_in_group == self.player.id_in_group
					}, buyers))
				},
				{
					'id': 3,
					'disclose_interval': self.group.asset2_disclose_interval,
					'true_value': self.group.asset3_true_value,
					'bids': list(map(lambda b: {
						'player_id': b.id_in_group,
						'amount': b.bid_asset3,
						'did_win': b.did_win_asset3,
						'is_self': b.id_in_group == self.player.id_in_group
					}, buyers))
				},
			],
		}


page_sequence = [
	BeginWaitPage,
	SellerChoiceNotEnoughBudget,
	SellerChoiceLowHigh,
	SellerChoiceDiscloseRange,
	SellerChoiceResultWaitPage,
	BuyerChoice,
	RoundResultWaitPage,
	RoundResult
]
