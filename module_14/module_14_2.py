import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute("DELETE FROM Users WHERE id = ?", (6, ))
cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]
cursor.execute("SELECT SUM(balance) FROM Users")
all_balances = cursor.fetchone()[0]
print(all_balances / total_users)
cursor.execute("SELECT AVG(balance) FROM Users")
print(cursor.fetchone()[0])

connection.commit()
connection.close()
