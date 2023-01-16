from flask import Flask, jsonify
from flask_cors import CORS
import pymysql
app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "Hello World!!! x2"


@app.route('/login/<user>/<email>/<password>')
def login(user,email,password):

    conn = pymysql.connect(host="*",
        user="*", password="*",
        port=3306, database="nice")
    crsr = conn.cursor()

    # First, check if this user already exists
    sql = 'select username from loginfo where username=%s'
    crsr.execute(sql, (user))
    print('returned ' + str(crsr.rowcount) + ' rows')
    if crsr.rowcount == 0:
        print('adding ' + user)
        sql = 'insert into loginfo (`username`, `email`, `password`) values (%s,%s,%s)'
        params = [user,email,password]
        crsr.execute(sql, params)
        conn.commit()
        return jsonify({'message': "Thank you for registering"})
    else:
        return jsonify({'message': "Sorry, username or email already used"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)