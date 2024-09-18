# Задача "Первые пользователи":
import sqlite3


connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER)''')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users(email)")
# for i in range(1, 11):
#     cursor.execute("INSERT INTO Users VALUES (?, ?, ?, ?, ?)", (i, f"User{i}", f"example{i}@gmail.com", i * 10, "1000"))

# for i in range(2, 11):
#     if i % 2 == 0:
#         cursor.execute("UPDATE Users SET balance = ? WHERE id = ?", (500, i))
for i in range(1, 11, 3):
    cursor.execute("DELETE FROM Users WHERE id = ?", (i,))
connection.commit()
connection.close()
