import sqlite3
from datetime import datetime


connection = sqlite3.connect('bank.db')
cursor = connection.cursor()


class UserDatabaseWrapper:
#sql queries
	@classmethod #fcn decorator, takes fcn below it and wraps it....
	def add_user(cls, username, permission_level):
		cursor.execute("""
			INSERT INTO users(username, time_created, permission_level) VALUES (?, ?, ?);
		""", (username, datetime.now(), permission_level) 
			)
		connection.commit()
		return cursor.lastrowid
		#return cursor.users.id

	def delete_user():
		pass

	@classmethod
	def get_user(cls, username):
		print("wrapper", username)
		cursor.execute("""
			SELECT id, username, time_created, permission_level FROM users WHERE username = ?;
		""", (username,))
		return cursor.fetchone()
		#returns tuple with column vals

		#would like to get JUST the PK



	def update():
		pass


class AccountDatabaseWrapper:

	@classmethod
	def add_acct(cls, account_num, balance, user_id):

		cursor.execute("""
			INSERT INTO accounts(account_num, balance, user_id) VALUES (?, ?, ?);
		""", (account_num, balance, user_id) 
			)
		connection.commit()
		return cursor.lastrowid
	
	@classmethod
	def get_acct(cls, acct_owner):
		cursor.execute("""
			SELECT account_num, balance FROM accounts WHERE user_id = ?;
			""", (acct_owner,)
			)
		return cursor.fetchone()



	def update():
		pass

	def delete():
		pass

# class JoinWrapper:
# 	def user_acct_join:
# 		cursor.execute("""
# 			SELECT 
# 		"""; 
# 			)



