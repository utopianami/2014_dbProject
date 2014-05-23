
import MySQLdb


db = MySQLdb.connect("10.73.45.56", "utopianami", "next1234", "music")
cursor = db.cursor()

t = "asdf"
nameList = ["nam", "jang", "lee", "kim", "in", "yang", "ho", "doek", "jung"]


i = 0
for name in nameList:
    cursor.execute("insert into dbMember values (%s, %s)", (name, i))
    i+=1
db.commit()

