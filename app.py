import sqlite3
from flask import Flask, render_template


'''Далее вы создадите функцию, которая обеспечивает подключение к базе данных,
 и вернете ее'''

def get_db_connection():            
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)    #  create instance class Flask


@app.route('/')
def index():
    conn = get_db_connection()
    tech_skills = conn.execute('SELECT * FROM tech_skills').fetchall()
    conn.close()
    return render_template('base.html', tech_skills=tech_skills)

