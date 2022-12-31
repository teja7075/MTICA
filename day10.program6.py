import sqlite3 as lite
con = lite.connect('mtica.db')


cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS Cars")
cur.execute('''CREATE TABLE    Cars(Id INT,Name TEXT, Price INT)''')
print("table cars created.")
cur.execute("INSERT INTO CARS VALUES(1,'Audi',52642)")
cur.execute("INSERT INTO CARS VALUES(2,'mercedes',57127)")
cur.execute("INSERT INTO CARS VALUES(3,'skoda',9000)")
cur.execute("INSERT INTO CARS VALUES(4,'volvo',29000)")
cur.execute("INSERT INTO CARS VALUES(5,'bentley',350000)")
cur.execute("INSERT INTO CARS VALUES(6,'citroen',21000)")
cur.execute("INSERT INTO CARS VALUES(7,'hummer',41400)")
cur.execute("INSERT INTO CARS VALUES(8,'volswagen',21600)")
con.commit()
print("values in table car inserted.")
