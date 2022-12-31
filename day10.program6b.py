import sqlite3
carData= [
    (1,'Audi',52642),
    (2,'mercedes',57127),
    (9,'tej',9000),
    (4,'volvo',29000),
    (5,'bentley',350000),
    (6,'citroen',21000),
    (7,'hummer',41400),
    (8,'volswagen',21600),
    ]
con = sqlite3.connect('mtica.db')
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS Cars")
cur.execute('''CREATE TABLE    Cars(Id INT,Name TEXT, Price INT)''')
cur.executemany("INSERT INTO CARS VALUES(?,?,?)",carData)
con.commit()
con.close()
print("value inserted.")
