DROP DATABASE IF EXISTS facebook_db;    

CREATE DATABASE facebook_db;    

\c facebook_db;        

CREATE TABLE Data (
ID SERIAL PRIMARY KEY,
Name_page varchar(20),
Date_post timestamp,
Post varchar(500),
Likes INT(20),
Comments INT(20),
Shares INT(20),

);    
insert into Role(RoleName)
values ('Admin'),('User'),('postgres');