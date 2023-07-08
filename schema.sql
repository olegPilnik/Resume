DROP TABLE IF EXISTS projects;
DROP TABLE IF EXISTS education;
DROP TABLE IF EXISTS contacts;
DROP TABLE IF EXISTS tech_skills;
DROP TABLE IF EXISTS soft_skills;



CREATE TABLE projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    technologies TEXT NOT NULL);

CREATE TABLE education (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_institution TEXT NOT NULL,
    specialty TEXT NOT NULL,
    study_period TEXT NOT NULL);   

CREATE TABLE contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    icon TEXT NOT NULL,
    title TEXT NOT NULL,
    contact TEXT NOT NULL,
    contact_link TEXT NOT NULL);

CREATE TABLE tech_skills (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL);

CREATE TABLE soft_skills (
     id INTEGER PRIMARY KEY,
    title TEXT NOT NULL);

