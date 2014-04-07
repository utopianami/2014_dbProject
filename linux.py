
import MySQLdb


db = MySQLdb.connect("10.73.45.56", "utopianami", "next1234", "music")
#db = MySQLdb.connect(host="10.73.45.56", port=3306, user="next", passwd="next1234", db="music")
cursor = db.cursor()

t = "asdf"
cursor.execute("INSERT INTO test VALUES (%s, %s)" , (444, t))
db.commit()

