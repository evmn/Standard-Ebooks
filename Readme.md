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

Query total record:

```sql
sqlite> SELECT COUNT(title) from books;
242
```

