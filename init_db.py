import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()



''' ____________________projects___________________________'''

cur.execute("INSERT INTO projects (title, technologies) VALUES (?, ?)",
            ('Resume', 'Python, Flask, SQLite3')
            )

''' ___________________education__________________________'''

cur.execute("INSERT INTO education (name_institution, specialty, study_period) VALUES (?, ?, ?)",
            ('Study Less', 'English Beginer', 'April 2023 - up to now | Ukraine')
            )
cur.execute("INSERT INTO education (name_institution, specialty, study_period) VALUES (?, ?, ?)",
            ('Prog Academy', 'Python', 'February 2023 - up to now | Ukraine')
            )
cur.execute("INSERT INTO education (name_institution, specialty, study_period) VALUES (?, ?, ?)",
            ('Skill-Up', 'Software testing', 'March 2019 - June 2019 | Ukraine')
            )
cur.execute("INSERT INTO education (name_institution, specialty, study_period) VALUES (?, ?, ?)",
            ('Odesa National Academy of Communication', 'Master of Telecommunications', 
             'September 2005 - May 2009 | Ukraine')
            )
cur.execute("INSERT INTO education (name_institution, specialty, study_period) VALUES (?, ?, ?)",
            ('Dnipropetrovsk Radio Instrumentation College', 'Junior Specialist',
             'September 2000 - May 2004 | Ukraine')
            )



'''____________________contacts___________________________'''

cur.execute("INSERT INTO contacts (icon, title, contact, contact_link) VALUES (?, ?, ?, ?)",
            ('C', 'Phone number', '+38096-132-57-88', 'tel:+30961325788')
            )
cur.execute("INSERT INTO contacts (icon, title, contact, contact_link) VALUES (?, ?, ?, ?)",
            ('E', 'Email', 'olegpilnik85@gmail.com', 'mailto:olegpilnik85@gmail.com')
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