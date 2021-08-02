
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request
from flask import jsonify
from flask_cors import CORS
from flask_mysqldb import MySQL


app = Flask(__name__)
CORS(app)


app.config['MYSQL_HOST'] = 'Zainulabideen.mysql.pythonanywhere-services.com'
app.config['MYSQL_USER'] = 'Zainulabideen'
app.config['MYSQL_PASSWORD'] = 'Za03008306558'
app.config['MYSQL_DB'] = 'Zainulabideen$Zain'

mysql = MySQL(app)

Result = []


@app.route('/')
def home():
    return jsonify({
        'name' : 'zain'
    })


@app.route('/addData', methods=['GET', 'POST'])
def addData():
    if request.method == "POST":
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Ecode(id, title, name, extra1, extra2, extra3, categary, info, comment) VALUES ('E102','TITLE2','NAME2','EXTRA12','EXTRA22','EXTRA32','CATEGARY2','INFO2','COMMENT2')")
        mysql.connection.commit()
        cur.close()
        return 'Successfully Stored'


@app.route('/getData', methods=['GET', 'POST'])
def getData():
    Ecode = ecode
    cur = mysql.connection.cursor()
    value = cur.execute("SELECT * from Ecode WHERE id = %s", (Ecode,))
    if value > 0:
        user = cur.fetchone()
        return jsonify(user)
    else:
        return jsonify({'error' : 'Error'})


@app.route('/getFromUser', methods=['GET', 'POST'])
def getFromUser():
        global ecode
        Data = request.get_json()
        Ecode = Data['ecode']
        ecode = Ecode
        return 'Success'


@app.route('/getting')
def getting():
        return jsonify(ecode)




if __name__ == '__main__':
    app.run(debug=True)