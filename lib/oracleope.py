import cx_Oracle
import collections
import json


class OracleOpe():
    def createTable(self):
        conn = cx_Oracle.connect('C##DHQ/Oracle123@localhost:1521/orcl')
        cur = conn.cursor()
        cur.execute(
            "CREATE TABLE \"C##DHQ\".\"_tst\" (\"NAME\" VARCHAR2(255),\"CLASS\" VARCHAR2(255),\"NUMBER\" VARCHAR2(255),\"SCORE\" VARCHAR2(255))")
        conn.commit()
        conn.close()
        return "成功创建数据库"

    def getData(self):
        conn = cx_Oracle.connect('C##DHQ/Oracle123@localhost:1521/orcl')
        cur = conn.cursor()
        cur.execute("SELECT * FROM \"stu\"")
        data = cur.fetchall()
        req = []
        for row in data:
            dic = collections.OrderedDict()
            dic['name'] = row[0]
            dic['class'] = row[1]
            dic['number'] = row[2]
            dic['score'] = row[3]
            req.append(dic)
            rspstr = json.dumps(req)
        return (rspstr.encode('utf-8').decode('unicode_escape'))
        conn.close()

    def emptyTable(self):
        conn = cx_Oracle.connect('C##DHQ/Oracle123@localhost:1521/orcl')
        cursor = conn.cursor()
        # 删除慢可回退
        cursor.execute("DELETE FROM \"stu\"")
        conn.commit()
        cursor.close()
        conn.close()
        return "已清空表"