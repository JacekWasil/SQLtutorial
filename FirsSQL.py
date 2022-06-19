import sqlite3
conn = sqlite3.connect("my_friends.db")
# create cursor object
c = conn.cursor()
# execute some sql
c.execute("CREATE TABLE IF NOT EXISTS friends (first_name TEXT, last_name TEXT, closeness INTEGER);")
insert_query = '''INSERT INTO friends
                    VALUES ('Merriwether', 'Lewis', 7)'''
c.execute(insert_query)
# commit changes
conn.commit()
conn.close()