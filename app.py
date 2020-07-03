from flask import Flask, render_template, app, request
import os
from lib.oracleope import OracleOpe
import cx_Oracle

BASE_DIR = os.path.dirname(__file__)
app = Flask(__name__,
            template_folder=os.path.join(BASE_DIR, "templates"),
            static_folder=os.path.join(BASE_DIR, "static"),
            static_url_path="/static")

app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/createTable', methods=['GET', 'POST'])
def createTable():
    return str(OracleOpe().createTable())


@app.route('/queryData', methods=['GET', 'POST'])
def queryData():
    return str(OracleOpe().getData())


@app.route('/addData', methods=['GET', 'POST'])
def addData():
    return render_template('add.html')


@app.route('/adds', methods=['post'])
def adds():
    _name = request.form.get('_name')
    _class = request.form.get('_class')
    _number = request.form.get('_number')
    _score = request.form.get('_score')
    conn = cx_Oracle.connect('C##DHQ/Oracle123@localhost:1521/orcl')
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO \"stu\"(\"NAME\",\"CLASS\",\"NUMBER\",\"SCORE\") VALUES(\'%s\',\'%s\',\'%s\',\'%s\')" % (_name, _class, _number, _score))
    conn.commit()
    cur.close()
    conn.close()
    return render_template('add.html')


@app.route('/displayData', methods=['GET', 'POST'])
def displayData():
    return render_template('ncov.html')


@app.route('/emptyTable', methods=['GET', 'POST'])
def emptyTable():
    return str(OracleOpe().emptyTable())


@app.route('/change', methods=['GET', 'POST'])
def change():
    return render_template('change.html')

@app.route('/changes', methods=['post'])
def changes():
    _name = request.form.get('_name')
    _score = request.form.get('_score')
    conn = cx_Oracle.connect('C##DHQ/Oracle123@localhost:1521/orcl')
    cur = conn.cursor()
    cur.execute(
        "UPDATE \"stu\" SET \"SCORE\" = \'%s\' WHERE NAME = \'%s\'" % (_score,_name))
    conn.commit()
    cur.close()
    conn.close()
    return render_template('change.html')


@app.route('/delete', methods=['GET', 'POST'])
def delete():
    return render_template('delete.html')

@app.route('/deletes', methods=['post'])
def deletes():
    _name = request.form.get('_name')
    _number = request.form.get('_number')
    conn = cx_Oracle.connect('C##DHQ/Oracle123@localhost:1521/orcl')
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM \"stu\" WHERE \"NAME\" = \'%s\' AND \"NUMBER\" = \'%s\'" % (_name,_number))
    conn.commit()
    cur.close()
    conn.close()
    return render_template('delete.html')

if __name__ == '__main__':
    app.run()
