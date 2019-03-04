from urllib.request import urlopen
import re, time, os, sys
from bs4 import BeautifulSoup
import sqlite3

# Returns a list of URLs to books listed on the standardebooks.org website.
def getBookPages():
	ebook_urls = []
	base_url = "https://standardebooks.org/ebooks/?page="
	root_url = "https://standardebooks.org"
	url = base_url + str(1)
	html = urlopen(url)
	bsObj = BeautifulSoup(html, "lxml")
	navigate = bsObj.find('main', attrs={"class":"ebooks"}).find('nav').findAll('li')
	lastpage = 	int(navigate[len(navigate)-1].find('a').get_text())+1#Return lastpage+1
	for i in range(1, lastpage):
		url = base_url + str(i)
		html = urlopen(url)
		bsObj = BeautifulSoup(html, "lxml")
		titleList = bsObj.find('ol').findAll('li')
		for link in titleList:
			ebook_urls.extend([root_url + link.find('a').get('href')])
	return ebook_urls

def saveMetainfo(links):
	#db.execute("select * from books")
	#localBooks = len(db.fetchall())
	localBooks = db.execute("select count(*) from books").fetchone()[0]
	serverBooks = len(links)
	print('\n\nThere are', serverBooks, 'books in StandardEbooks.org')
	print('there are', localBooks, 'books in local database\n')
	start = serverBooks - localBooks
	if start <= 0:
		print('no need to download')
		return
	print('We will download', start, 'books this time')
	#Traverse the list in reverse order
	#listObj[start:stop:step]
	for url in links[start-1::-1]:
		html = urlopen(url)
		bsObj = BeautifulSoup(html, "lxml")
		title = bsObj.find('article').find('h1').get_text()
		author = bsObj.find('article').find('p').get_text()
		#image = bsObj.find('article').find('img')
		reading_ease = bsObj.find('aside', attrs={"id":"reading-ease"}).find('p').get_text()
		words = getWords(reading_ease)
		readingeasy = getReadingEasy(reading_ease)
		description = bsObj.find('section', attrs={"id":"description"}).get_text().replace("Description\n","")
		db.execute('''insert into books(Title, Author, Words, Ease, Description)  values(?,?,?,?,?)''', (title, author, words, readingeasy, description))
		print(title, "-", author, "\t", words, "\t", readingeasy)
		#print(description)

def getWords(readingeasy):
	tmpList = re.findall(r'[\d,\.]+', readingeasy)
	words = int(tmpList[0].replace(",", ""))
	return words

def getReadingEasy(readingeasy):
	tmpList = re.findall(r'[\d,\.]+', readingeasy)
	easy = float(tmpList[len(tmpList)-1])
	return easy

conn = sqlite3.connect('StandardEbooks.db')
db = conn.cursor()
db.execute('''create table if not exists books 
	(ID integer primary key autoincrement,
	Title text, 
	Author text,
	Words int,
	Ease float,
	Description text)''')
saveMetainfo(getBookPages())
conn.commit()
