from bank_wrappers import UserDatabaseWrapper, AccountDatabaseWrapper

from datetime import datetime
from random import randint


class User:
	def __init__(self, id, username, time_created, permission_level):
		self.id = id
		self.username = username
		self.time_created = time_created
		self.permission_level = permission_level

class Client(User):

	user_manager = UserDatabaseWrapper
	@classmethod #takes fcn right below and returns a new fcn of the class
	# class method used for returning instances of the class - when each instance will be different
	def get_client(cls, username):
		print("client model", username)
		row = cls.user_manager.get_user(username)
		print("get client cls method")
		#factory method/constructor fcn - creates instances of the class
		return cls(*row)

		#splat returns unpacked row in tuple, so each value is its own
		# id - id
		# username - name
		# time created - time
		# permission level - 2

	'''
	-view accounts
	-deposit, withdraw from own accounts
	-transfer money from accounts
	'''
class Banker(User):

	user_manager = UserDatabaseWrapper()
	#works for class method or instance method
	acct_manager = AccountDatabaseWrapper
	#creates instance of ADW
	#only works for class method

	def create_new_client(self, name, deposit):
		user_id = self.add_user(name)
		self.create_acct(randint(1000,9999), deposit, user_id)
		#create rand acct num

	def add_user(self, username, permission_level="client"):
		print("user created")
		return self.user_manager.add_user(username, permission_level)
		#default permission = 2 = client
		#validations for user database info in this class (as opposed to user input validations)

	def create_acct(self, account_num, balance, user_id):
		print("acct created")
		return self.acct_manager.add_acct(account_num, balance, user_id)
	'''
	-create account
	-deposit and withdraw from ANY account
	-no money in own account
	'''


class Account:
	def __init__(self, id, account_num, balance,user_id):
		self.id = id
		self.account_num = account_num
		self.balance =  balance
		self.user_id = user_id

	acct_manager = AccountDatabaseWrapper
	@classmethod
	def get_client_acct(cls, acct_owner):
		print("getting client acct")
		row = cls.acct_manager.get_acct(acct_owner)
		print("get acct cls method")
		return cls(*row)



