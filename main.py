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