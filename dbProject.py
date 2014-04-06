from flask import Flask, render_template, request
import MySQLdb

app = Flask(__name__)




@app.route("/")
def index():
    sql = "INSERT INTO user (age, sex) VALUES (%s, %d,%d)" %("aaa", 188,90)
    print sql
    return render_template('index.html')


@app.route("/signUp", methods=["POST"])
def signUp():
    userEmail = request.form['email'].encode('ascii', 'ignore')
    userAge = int(request.form['age'])
    userSex = int(request.form['sex'])

    db = MySQLdb.connect("localhost", "utopianami", "1234", "music")
    cursor = db.cursor()
    try:
        cursor.execute("INSERT INTO user (email, age, sex) VALUES (%s, %s,%s)" , (userEmail, userAge, userSex))
        db.commit()
    except:
        db.rollback()

    db.close()
    return render_template('index.html')


if __name__ =='__main__':
    app.run(debug=True, host='0.0.0.0')

