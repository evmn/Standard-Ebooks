import sqlite3
def db2md():
	conn = sqlite3.connect('StandardEbooks.db')
	db = conn.cursor()
	for books in db.execute('select * from books order by ease asc').fetchall():
	#for books in db.execute('select * from books order by ease desc').fetchall():
	#for books in db.execute('select * from books order by author').fetchall():
		id = books[0]
		title = books[1]
		author = books[2]
		words = books[3]
		ease = books[4]
		description = books[5].replace("\n","\n\n")
		print('##', author, '-', title)
		print('\n', 'There are', words, 'words in this book.\n')
		print('### Description\n', description)

db2md()
