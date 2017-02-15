from bank_models import Client, Banker, Account
import bank_views

class Bank:
	def __init__(self):
		self.welcome_view = bank_views.WelcomeView()
		self.client_view = bank_views.ClientView()
		self.banker_view = bank_views.BankerView()
		self.banker = Banker
		self.client = Client
		self.account = Account

	def start(self):
		is_banker = self.welcome_view.welcome_msg()
		#verifications can be in models, controller, or views... implementation decision
		if is_banker == "1":
			pass
			#banker and client classes

		else:
			self.client_start()

	def client_start(self):
		open_acct = self.client_view.client_menu()
		if open_acct == "1":
			name = self.client_view.existing_client()
			print("client start ", name)

			client = self.client.get_client(name)
			print ("instance of get_client class:", client.id)
			acct_owner = client.id

			return client.get_accounts()


		else:
			name, deposit = self.client_view.client_new_acct()
			print(name, deposit)
			
			self.banker.create_new_client(name, deposit)


	def banker_start(self):
		pass
		#banker_view stuff goes here


"""
check if banker- pass to banker table
if client- pass to client table
"""
bank = Bank()
bank.start()
