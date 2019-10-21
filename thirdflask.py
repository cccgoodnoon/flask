import psycopg2
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

conn = psycopg2.connect(
        database="postgres", user="postgres", password="tongji2018openedu", host="202.120.167.50", port="5432")


# @app.route('/rest/anon/tasks/<string:name>/<string:studentId>/<string:phone>/<string:email>/<string:wechatId>/<string:roomId>',methods=['POST'])
@app.route('/rest/anon/tasks',methods=['POST'])
# def create(name,studentId,phone,email,wechatId,roomId):
def create():
    cur = conn.cursor()
    data = request.get_json()
    # print(name)
    # print(studentId)
    # print(phone)
    # print(email)
    # print(wechatId)
    # print(roomId)
    cur.execute("insert into tasktwo(name, studentid, phone, email, wechatId, roomId) values(%s,%s,%s,%s,%s,%s)",
             (data['name'], data['studentId'], data['phone'], data['email'], data['wechatId'], data['roomId']))
    conn.commit()
    return "1"


@app.route('/rest/anon/tasks',methods=['GET'])
def read():
    cur = conn.cursor()
    # data = request.get_json()
    cur.execute(
        "select * from tasktwo")
    rows = cur.fetchall()
    l = []
    for row in rows:
        print(row)
        dic= {'id': str(row[0]),'name': str(row[1]),'studentId':str(row[2]),'phone':str(row[3]),'email':str(row[4]),'wechatId':str(row[5]),'roomId':str(row[6])}
        l.append(dic)
    return jsonify(l)


# @app.route('/rest/anon/tasks/getByState/<string:state>',methods=['GET'])
# def read_state(state):
#     cur = conn.cursor()
    
#     cur.execute(
#         "select * from tasktwo where state="+state)
#     rows = cur.fetchall()
#     l = []
#     for row in rows:
#         dic= {'id': str(row[0]),'description': str(row[1]),'begintime':str(row[2]),'endtime':str(row[3]),'state':str(row[4])}
#         l.append(dic)
#     return jsonify(l)


@app.route('/rest/anon/tasks/<string:id>', methods=['PUT'])
def update(id):
    cur = conn.cursor()
    data = request.get_json()

    cur.execute("UPDATE tasktwo SET phone = '{}', email = '{}', wechatId = '{}', roomId = '{}'  WHERE id = {}"
        .format(data['phone'],data['email'],data['wechatId'],data['roomId'], id))


    conn.commit()
    return "1"

# @app.route('/rest/anon/tasks/editState/<string:state>/<string:dId>', methods=['PATCH'])
# def update_state(state,dId):
#     cur = conn.cursor()
#     data = request.get_json()

#     cur.execute("UPDATE tasktwo SET state = "+state+" WHERE id = " + dId);
#     conn.commit()
#     return "1"


@app.route('/rest/anon/tasks/<string:id>', methods=['DELETE'])
def delete(id):
    cur = conn.cursor()
    # cur.execute("DELETE from tasktwo where id="+ id)
    cur.execute("DELETE from tasktwo where id=%s", id)
    conn.commit() 
    return "1"

if __name__ == '__main__':
    # app = create_app()
    app.run(
        # host='127.0.0.1',
        # port=8080,
    )
