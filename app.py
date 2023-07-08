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
    education = conn.execute('SELECT * FROM education').fetchall()
    contacts = conn.execute('SELECT * FROM contacts').fetchall()
    tech_skills = conn.execute('SELECT * FROM tech_skills').fetchall()
    soft_skills = conn.execute('SELECT * FROM soft_skills').fetchall()
    
    conn.close()
    return render_template('base.html', 
                            education=education,
                            contacts=contacts,
                            tech_skills=tech_skills,
                            soft_skills=soft_skills
                            )

