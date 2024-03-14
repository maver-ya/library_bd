from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_DATABASE_HOST'] = 'std-mysql'
app.config['MYSQL_DATABASE_USER'] = 'std_2609_home_library'
app.config['MYSQL_DATABASE_USER'] = 'Cerf67789$'
app.config['MYSQL_DATABASE_DB'] = 'std_2609_home_library'

mysql = MySQL(app)


@app.route('/')
def db_req():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Authors")
    result = cur.fetchall()
    cur.close
    return str(result)


if __name__ == '__main__':
    app.run()
