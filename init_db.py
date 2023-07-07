import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

''' ____________________projects___________________________'''

cur.execute("INSERT INTO projects (title, technologies, path_) VALUES (?, ?, ?)",
            ('https://hellen.p.goit.global/', 'technologies', 'https://hellen.p.goit.global/'))


''' ____________________contacts___________________________'''

cur.execute("INSERT INTO contacts (title, content) VALUES (?, ?)",
            ('Phone number', '+380961111111'))
cur.execute("INSERT INTO contacts (title, content) VALUES (?, ?)",
            ('Email', 'oleg@gmail.com'))


''' __________________tech_skills___________________________'''

cur.execute("INSERT INTO tech_skills (title) VALUES (?,)",
            ('HTML, CSS',))
cur.execute("INSERT INTO tech_skills (title) VALUES (?,)",
            ('JavaScript',))   
cur.execute("INSERT INTO tech_skills (title) VALUES (?,)",
            ('React.js',))   
cur.execute("INSERT INTO tech_skills (title) VALUES (?,)",
            ('Node.js',))   
cur.execute("INSERT INTO tech_skills (title) VALUES (?,)",
            ('Python',))   
cur.execute("INSERT INTO tech_skills (title) VALUES (?,)",
            ('SQL',)) 


''' __________________soft_skills___________________________'''

cur.execute("INSERT INTO soft_skills (title) VALUES (?,)",
            ('Scrum',))
cur.execute("INSERT INTO soft_skills (title) VALUES (?,)",
            ('Agile',))   
cur.execute("INSERT INTO soft_skills (title) VALUES (?,)",
            ('GTD',))   
cur.execute("INSERT INTO soft_skills (title) VALUES (?,)",
            ('Teamwork',))   


connection.commit()
connection.close()