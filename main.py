import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import request

@app.route('/get_paciente')
def get_paciente():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("""SELECT * 
                        FROM paciente""")
        paciente_registros = cursor.fetchall()
        response = jsonify(paciente_registros)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()

@app.route('/Left_Join')
def Left_Join():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("""SELECT *
                        FROM paciente
                        LEFT JOIN comorbidade
                        ON paciente.id = comorbidade.paciente_id;""")
        paciente_comorbidade_LJ = cursor.fetchall()
        response = jsonify(paciente_comorbidade_LJ)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()

@app.route('/LeftJoin_Null')
def LeftJoin_Null():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("""SELECT *
                            FROM paciente
                            LEFT JOIN comorbidade
                            ON paciente.id = comorbidade.paciente_id
                            WHERE comorbidade.paciente_id IS NULL;""")
        paciente_comorbidade_Null = cursor.fetchall()
        response = jsonify(paciente_comorbidade_Null)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()
        

@app.route('/Right_Join')
def Right_Join():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("""SELECT *
                        FROM paciente
                        RIGHT JOIN comorbidade
                        ON paciente.id = comorbidade.paciente_id;""")
        paciente_comorbidade_RJ = cursor.fetchall()
        response = jsonify(paciente_comorbidade_RJ)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()

@app.route('/Right_Join_Null')
def Right_Join_Null():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("""SELECT *
                                FROM paciente
                                RIGHT JOIN comorbidade
                                ON paciente.id = comorbidade.paciente_id
                                WHERE paciente.id IS NULL;""")
        paciente_comorbidade_RJ_Null = cursor.fetchall()
        response = jsonify(paciente_comorbidade_RJ_Null)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()

@app.route('/Full_Outer')
def Full_Outer():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("""SELECT * FROM paciente 
                            LEFT JOIN comorbidade ON paciente.id = comorbidade.paciente_id
                            UNION 
                            SELECT * FROM paciente 
                            RIGHT JOIN comorbidade ON paciente.id = comorbidade.paciente_id;
                            """)
        paciente_comorbidade_FullOuter = cursor.fetchall()
        response = jsonify(paciente_comorbidade_FullOuter)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()

@app.route('/Full_Outer_2')
def Full_Outer_2():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("""SELECT * FROM paciente 
                            LEFT JOIN comorbidade ON paciente.id = comorbidade.paciente_id
                            WHERE paciente.id IS NULL OR
                                comorbidade.paciente_id IS NULL
                            UNION 
                            SELECT * FROM paciente 
                            RIGHT JOIN comorbidade ON paciente.id = comorbidade.paciente_id
                            WHERE paciente.id IS NULL OR
                                comorbidade.paciente_id IS NULL;""")
                                                        
        paciente_comorbidade_FullOuter_2 = cursor.fetchall()
        response = jsonify(paciente_comorbidade_FullOuter_2)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()

@app.route('/Inner_Join')
def Inner_Join():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("""SELECT *
                            FROM paciente
                            INNER JOIN comorbidade
                            ON paciente.id = comorbidade.paciente_id;""")
                                                        
        paciente_comorbidade_Inner_Join = cursor.fetchall()
        response = jsonify(paciente_comorbidade_Inner_Join)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()

@app.route('/get_paciente_nome', methods=['POST'])
def buscar_nome():
    try:        
        name = request.json['name']

        if request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)		
            cursor.execute(f"""SELECT * 
                               FROM paciente
                               WHERE nome LIKE '%{name}%'
                            """)
            paciente_registros = cursor.fetchall()
            response = jsonify(paciente_registros)
            response.status_code = 200
            return response
        else:
            return showMessage()
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close() 

@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    response = jsonify(message)
    response.status_code = 404
    return response
        
if __name__ == "__main__":
    app.run()