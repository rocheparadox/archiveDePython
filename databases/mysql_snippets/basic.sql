#create database literature;
#use literature;
  create table authors (
    author_id SERIAL PRIMARY KEY,
    author_name VARCHAR(30) NOT NULL,
    born_year INTEGER ,
    death_year INTEGER,
    era VARCHAR(2)
  );
