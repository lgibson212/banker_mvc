class WelcomeView:
	#dont need an instance/init. having a class makes it cleaner (instead of just functions in the file). when large project, makes more sense

	def welcome_msg(self):
		print("Hello, welcome to the Bank. Are you a [1] banker or a [2] client? Please enter 1 or 2.")
		return input()


class ClientView:
	def client_menu(self):
		print("Do you have an [1] existing account or [2] would you like to open a new one? Please enter 1 or 2.")
		return input()

	def existing_client(self):
		name = input("what is your username? ")
		print ("one moment while the banker pulls up your account")
		return name
		#use username to find userID and then bankID and all accounts

	def client_new_acct(self):
		name = input("please enter a username: ")
		deposit = int(input("how much money are you opening with, in numbers? "))
		print ("one moment while the banker opens your account")
		return name, deposit


class BankerView:
	pass



