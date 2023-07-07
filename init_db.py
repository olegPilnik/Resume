import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()



''' ____________________projects___________________________'''

cur.execute("INSERT INTO projects (title, technologies) VALUES (?, ?)",
            ('Resume', 'Python, Flask, SQLite3')
            )

'''____________________contacts___________________________'''

cur.execute("INSERT INTO contacts (title, contact) VALUES (?, ?)",
            ('Phone number', '+38096-132-57-88')
            )
cur.execute("INSERT INTO contacts (title, contact) VALUES (?, ?)",
            ('Email', 'olegpilnik85@gmail.com')
            )

'''__________________tech_skills___________________________'''

cur.execute("INSERT INTO tech_skills (id, title) VALUES (?, ?)",
           (1, 'HTML, CSS')
            )
cur.execute("INSERT INTO tech_skills (id, title) VALUES (?, ?)",
            (2, 'JavaScript')
            )   
cur.execute("INSERT INTO tech_skills (id, title) VALUES (?, ?)",
            (3, 'React.js')
            )   
cur.execute("INSERT INTO tech_skills (id, title) VALUES (?, ?)",
            (4, 'Node.js')
            )   
cur.execute("INSERT INTO tech_skills (id, title) VALUES (?, ?)",
            (5, 'Python')
            )   
cur.execute("INSERT INTO tech_skills (id, title) VALUES (?, ?)",
            (6, 'SQL')
            ) 

'''________________soft_skills___________________________'''

cur.execute("INSERT INTO soft_skills (id, title) VALUES (?, ?)",
            (1, 'Scrum'))
cur.execute("INSERT INTO soft_skills (id, title) VALUES (?, ?)",
            (2, 'Agile'))   
cur.execute("INSERT INTO soft_skills (id, title) VALUES (?, ?)",
            (3, 'GTD'))   
cur.execute("INSERT INTO soft_skills (id, title) VALUES (?, ?)",
            (4, 'Teamwork'))   


connection.commit()
connection.close()