
import MySQLdb


#db = MySQLdb.connect("10.73.45.130:3306", "utopianami", "gradation", "utopia")
db = MySQLdb.connect(host="10.73.45.130", port=3306, user="utopianami", passwd="gradation", db="utopia")
cursor = db.cursor()

t = "asdf"
cursor.execute("""create table a""")
db.commit()

