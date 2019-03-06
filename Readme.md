# Standard Ebooks


Save book info to local sqlite3 database.

|ID|Title|Author|Words|Ease|Description|
|:-|:-|:-|:-|:-|:-|
1|The Time Machine|H. G. Wells|32575|71.04
2|The Lady of the Barge|W. W. Jacobs|47269|82.34
3|Candide|Voltaire|33776|67.89
4|Heart of Darkness|Joseph Conrad|38791|71.44
5|The Book of Wonder|Lord Dunsany|23006|66.3
6|Beyond Good and Evil|Friedrich Nietzsche|63621|34.83
7|The Call of the Wild|Jack London|32031|77.37
8|The Mysterious Affair at Styles|Agatha Christie|57825|77.03
9|White Fang|Jack London|72797|81.22
10|The Narrative of Arthur Gordon Pym of Nantucket|Edgar Allan Poe|70791|51.21
...|...|...|...|...|...
...|...|...|...|...|...
242|Greenmantle|John Buchan|100167|81.53


```sh
python3 meta.py
```

## database


Query total/average/max/min words of all books:


```sql
sqlite> SELECT SUM(words) FROM books;
22372822
sqlite> SELECT AVG(words) FROM books;
92449.6776859504
sqlite> SELECT MAX(words) from books;
801665
sqlite> SELECT MIN(words) from books;
5166
```

Query records number:

```sql
sqlite> SELECT COUNT(*) from books;
242
```

## Debugging programs 

## Books without azw3 format

There's no azw3 format of [The Rubáiyát of Omar Khayyám](https://standardebooks.org/ebooks/omar-khayyam/the-rubaiyat-of-omar-khayyam/edward-fitzgerald/edmund-dulac) 

Maybe we should use a `try ... catch` here

```sh
$ python3 meta.py 


There are 242 books in StandardEbooks.org
there are 0 books in local database
We will download 242 books this time

https://standardebooks.org/ebooks/h-g-wells/the-time-machine/dist/h-g-wells_the-time-machine.azw3
https://standardebooks.org/ebooks/w-w-jacobs/the-lady-of-the-barge/maurice-greiffenhagen/dist/w-w-jacobs_the-lady-of-the-barge.azw3
https://standardebooks.org/ebooks/voltaire/candide/the-modern-library/dist/voltaire_candide.azw3
https://standardebooks.org/ebooks/joseph-conrad/heart-of-darkness/dist/joseph-conrad_heart-of-darkness.azw3
https://standardebooks.org/ebooks/lord-dunsany/the-book-of-wonder/sidney-h-sime/dist/lord-dunsany_the-book-of-wonder.azw3
https://standardebooks.org/ebooks/friedrich-nietzsche/beyond-good-and-evil/helen-zimmern/dist/friedrich-nietzsche_beyond-good-and-evil.azw3
https://standardebooks.org/ebooks/jack-london/the-call-of-the-wild/dist/jack-london_the-call-of-the-wild.azw3
https://standardebooks.org/ebooks/agatha-christie/the-mysterious-affair-at-styles/dist/agatha-christie_the-mysterious-affair-at-styles.azw3
https://standardebooks.org/ebooks/jack-london/white-fang/dist/jack-london_white-fang.azw3
https://standardebooks.org/ebooks/edgar-allan-poe/the-narrative-of-arthur-gordon-pym-of-nantucket/dist/edgar-allan-poe_the-narrative-of-arthur-gordon-pym-of-nantucket.azw3
https://standardebooks.org/ebooks/thomas-de-quincey/confessions-of-an-english-opium-eater/dist/thomas-de-quincey_confessions-of-an-english-opium-eater.azw3
https://standardebooks.org/ebooks/laozi/tao-te-ching/james-legge/dist/laozi_tao-te-ching.azw3
https://standardebooks.org/ebooks/bram-stoker/dracula/dist/bram-stoker_dracula.azw3
https://standardebooks.org/ebooks/henry-james/the-turn-of-the-screw/dist/henry-james_the-turn-of-the-screw.azw3
https://standardebooks.org/ebooks/oscar-wilde/the-picture-of-dorian-gray/dist/oscar-wilde_the-picture-of-dorian-gray.azw3
https://standardebooks.org/ebooks/oscar-wilde/the-importance-of-being-earnest/dist/oscar-wilde_the-importance-of-being-earnest.azw3
https://standardebooks.org/ebooks/niccolo-machiavelli/the-prince/w-k-marriott/dist/niccolo-machiavelli_the-prince.azw3
https://standardebooks.org/ebooks/james-joyce/dubliners/dist/james-joyce_dubliners.azw3
https://standardebooks.org/ebooks/epictetus/the-enchiridion/elizabeth-carter/dist/epictetus_the-enchiridion.azw3
https://standardebooks.org/ebooks/anton-chekhov/short-fiction/constance-garnett/dist/anton-chekhov_short-fiction.azw3
https://standardebooks.org/ebooks/robert-frost/north-of-boston/dist/robert-frost_north-of-boston.azw3
https://standardebooks.org/ebooks/henry-david-thoreau/walden/dist/henry-david-thoreau_walden.azw3
Traceback (most recent call last):
  File "meta.py", line 82, in <module>
    saveMetainfo(bookLists())
  File "meta.py", line 62, in saveMetainfo
    azw3 = "https://standardebooks.org" + bsObj.find('a', attrs={"class":"amazon"}).get('href')
AttributeError: 'NoneType' object has no attribute 'get
```