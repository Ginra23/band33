import mysql.connector
from random import randint
import time

# DB importavimas
database = mysql.connector.connect(host="localhost", user="root", password="", database="psp_2ld")
#database.autocommit(False)
cursor = database.cursor()
"""
query = "INSERT INTO testavimui1 (sk1, sk2, sk3, sk4) VALUES (%s, %s, %s, %s)"
komit_kas = 100
time1 = time.time()
for i in range(0, 100001, 1):
    sk1 = randint(0, 1000)
    sk2 = randint(0, 1000)
    sk3 = randint(0, 1000)
    sk4 = randint(0, 1000)
    cursor.execute(query, (sk1, sk2, sk3, sk4))
    if i % komit_kas == 0:
        database.commit()
database.commit()


"""
time1 = time.time()
#query1 = "SELECT COUNT(*)as kiekis FROM testavimui1"
#query1 = "SELECT * FROM testavimui1"
query1 = "SELECT * FROM testavimui1 where sk1>100"
cursor.execute(query1)
rezultatas = cursor.fetchall()
i=0
for irasas in rezultatas:
    #print(irasas)
    i = 0

time2 = time.time()
total_time = time2-time1
print("Query time",total_time)
database.disconnect()