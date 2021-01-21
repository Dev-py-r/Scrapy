# import sqlite3
#
# conn = sqlite3.connect('myquotes.db') #Create or connect db

import sqlite3

conn = sqlite3.connect('myquotes1.db')
curr = conn.cursor()

# curr.execute("""create table quotes_tb(
#                                 title text,
#                                 author text,
#                                 tag text
#                                 )""")

curr.execute("""insert into quotes_tb values ('Python is awesome!','buildwithpython','python')""")

conn.commit()
conn.close()