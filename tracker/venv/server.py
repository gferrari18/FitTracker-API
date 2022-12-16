from flask import Flask, jsonify
from flask_cors import CORS
import pymysql
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "Hello World!!! x2"

# @app.route('/resetdb')
# def reset():
#     connstr = os.environ.get('datacon')
#     conn = pymysql.connect(connstr)
#     crsr = conn.cursor()

#     # # Drop the tables if they already exist

#     # sql = 'DROP TABLE IF EXISTS `tracker`.`login`;'
#     # crsr.execute(sql)
#     # sql = 'DROP TABLE IF EXISTS `tracker`.`user`;'
#     # crsr.execute(sql)
#     # sql = 'CREATE TABLE `tracker`.`user` (`id` INT NOT NULL AUTO_INCREMENT,`login` VARCHAR(255) NULL, PRIMARY KEY (`id`));'
#     # crsr.execute(sql)
#     # sql = 'CREATE TABLE `tracker`.`login` (`id` INT NOT NULL AUTO_INCREMENT,`userid` INT NULL,`date` DATETIME, PRIMARY KEY (`id`), FOREIGN KEY (userid) REFERENCES `user`(id));'per
#     # crsr.execute(sql)

#     # return 'Reset Successful'

@app.route('/login/<user>/<email>/<password>')
def login(user,email,password):

    conn = pymysql.connect(host="127.0.0.1",
        user="root", password="76495312",
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
    #     print('adding ' + str(crsr.rowcount) + ' user')
    #     conn.commit()
    #     print('re-executing ' + sql)
    #     crsr.execute(sql, (user))

    # res = crsr.fetchone()
    # userid = res[0]
    # # Now, add the login information
    # Note, CURRENT_TIMESTAMP is built into MySQL to get the current time
    # sql = 'insert into loginfo (`username`, `email`, `password`) values (%s,%s,%s)'
    # params = [user,email,password]
    # crsr.execute(sql, params)

    conn.commit()

    return("Success")

    # Finally, get the user's login count and the total login count
    # sql = 'select count(*) as logins from login where userid=%s'
    # crsr.execute(sql, (userid))
    # res = crsr.fetchone()
    # usercount = res[0]
    # sql = 'select count(*) as logins from login'
    # crsr.execute(sql)
    # res = crsr.fetchone()
    # totalcount = res[0]

    # return jsonify({'user': user, 'user count':usercount, 'total count':totalcount })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)