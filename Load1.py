import csv
import sqlite3

con = sqlite3.connect('nba1.sqlite')  # change to 'sqlite:///your_filename.db'
cur = con.cursor()
cur.execute("CREATE TABLE nbacsv(col1,col2,col3,col4,col5,col6,col7,col8,col9,col10);")  # use your column names here

with open('nba.csv', 'r') as fin:  # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin)  # comma is default delimiter
    to_db = [(i['Date'], i['Start (ET)'],i['Visitor/Neutral'],i['PTS'],i['Home/Neutral'],i['PTS.1'],i['Unnamed: 6'],i['Unnamed: 7'],i['Attend.'],i['Notes']) for i in dr]
    cur.executemany("INSERT INTO nbacsv (col1 , col2 , col3 , col4 , col5 , col6 , col7 , col8 , col9 , col10 ) VALUES (? ,? ,? ,? ,? ,? ,? ,? ,? ,? );", to_db)
con.commit()
con.close()
