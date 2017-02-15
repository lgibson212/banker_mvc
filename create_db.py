import sqlite3
from datetime import datetime
from random import randint


connection = sqlite3.connect('bank.db')
c = connection.cursor()

# c.execute(DROP TABLE IF EXISTS 'users')

c.execute(
	'''
		CREATE TABLE 'users' (
		'id' INTEGER PRIMARY KEY AUTOINCREMENT,
		'username' TEXT,
		'time_created' TEXT,
		'permission_level' INTEGER
		);
	
''')
print("user table CREATED!!!")

# c.execute(DROP TABLE IF EXISTS 'accounts')

c.execute(
	'''
		CREATE TABLE 'accounts' (
		'id' INTEGER PRIMARY KEY AUTOINCREMENT,
		'account_num' INTEGER,
		'balance' NUMERIC,
		'user_id' TEXT,
		FOREIGN KEY(user_id) REFERENCES users(id)
		);

''')
print("accounts table CREATED!!!")
print("seeding db")


for user in ["Banker1", "Banker2"]:
	
	c.execute(
		'''
		INSERT INTO users(username, time_created, permission_level) VALUES ("{}", "{}", "banker");
		'''.format(user, datetime.now())
		)

	user_id = c.lastrowid #sets variable in python, not SQL
	#lastrowid only prints out WRITES, not READS
	print(user_id)

	c.execute(
		'''
		INSERT INTO accounts(account_num, balance, user_id) VALUES ("{}", 5000.00, {});
		'''.format(randint(1000, 9999), user_id)
		) #.format is taking user_id from python variable above

connection.commit() #specific to SQLite
connection.close() #SQLite locks applications from using it until other one closes it



