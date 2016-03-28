


import MySQLdb
db = MySQLdb.connect(host="localhost", user="root",passwd="innovacion", db="innovacionharnes")
cursor = db.cursor()
recs=cursor.execute("SELECT * FROM gps_main")
for x in range(recs):
   print cursor.fetchone()