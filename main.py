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
        
if __name__ == "__main__":
    app.run()