from urllib.request import urlopen
import re, time, os, sys
from bs4 import BeautifulSoup
import sqlite3

def bookLists():
	#Add new books page here
	ebook_urls = []
	ebook_urls.extend(['https://standardebooks.org/ebooks/henrik-ibsen/ghosts/william-archer'])
	return ebook_urls

def saveMetainfo(links):
	conn = sqlite3.connect('StandardEbooks.db')
	db = conn.cursor()
	db.execute('''
		create table if not exists books 
		(id integer primary key autoincrement,
		title text, 
		author text,
		words int,
		ease real,
		description text,
		cover text,
		epub text)''')
	for url in links:
		html = urlopen(url)
		bsObj = BeautifulSoup(html, "lxml")
		title = bsObj.find('article').find('h1').get_text()
		author = bsObj.find('article').find('p').get_text()
		#reading-easy: 89,519 words (5 hours 26 minutes) with a reading ease of 70.23 (fairly easy)
		reading_ease = bsObj.find('aside', attrs={"id":"reading-ease"}).find('p').get_text()
		words = getWords(reading_ease)
		readingeasy = getReadingEasy(reading_ease)
		description = bsObj.find('section', attrs={"id":"description"}).get_text().replace("Description\n","")
		cover = "https://standardebooks.org" + bsObj.find('article').find('img').get('src').replace("hero","cover")
		epub = "https://standardebooks.org" + bsObj.find('a', attrs={"class":"epub"}).get('href')
		db.execute('''insert into books(title, author, words, ease, description, cover, epub)  
				values(?,?,?,?,?,?,?)
				''', (title, author, words, readingeasy, description, cover, epub))
		#print(title, "-", author, "\t", words, "\t", readingeasy)
		print("\t", title, "\n", epub)
		conn.commit()
	conn.close()

def getWords(readingeasy):
	tmpList = re.findall(r'[\d,\.]+', readingeasy)
	words = int(tmpList[0].replace(",", ""))
	return words

def getReadingEasy(readingeasy):
	tmpList = re.findall(r'[\d,\.]+', readingeasy)
	easy = float(tmpList[len(tmpList)-1])
	return easy

if __name__ == "__main__":
	saveMetainfo(bookLists())
