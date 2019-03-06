import sqlite3
def db2md():
	conn = sqlite3.connect('StandardEbooks.db')
	db = conn.cursor()
	for author in db.execute('select author from books group by author').fetchall():
		print('##', author[0])
		for books in db.execute('select * from books where author=?', author).fetchall():
			title = books[1]
			words = books[3]
			ease = books[4]
			description = books[5].replace("\n","\n\n")
			print('\n###', title)
			print('\n', 'There are', words, 'words in this book.\n')
			print('#### Description\n', description)

db2md()
