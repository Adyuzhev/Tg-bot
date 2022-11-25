import sqlite3 as sql

#connect to SQLite
con = sql.connect('questions.db')

#Create a Connection
cur = con.cursor()

#Drop users table if already exsist.
cur.execute("DROP TABLE IF EXISTS questions")

#Create users table  in db_web database
sql ='''CREATE TABLE "questions" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"question"	TEXT,
	"answer"	TEXT,
	"score"	FLOAT
)'''
cur.execute(sql)

#commit changes
con.commit()

#close the connection
con.close()
