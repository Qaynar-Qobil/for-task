CREATE TABLE useres (
    id int,
    fullname text,
    age int
);



show databases; --> Databasalarni korish
create database name_of_database; --> Bu database yaratish
use name_of_database; --> databazaga ulanish

create table name_of_table(column_name1 tipi,column_name2 tipi,.....); --> table yaratish
show tables; --> ulangan databazamiz ichidagi table larni korish

--> Data types : 
1. INT
2. VARCHAR
4. TEXT

select * from name_of_table; --> Bu table ichidagi malumotlarni hammasini korish
select name,surname from name_of_table; --> Bu table ichidagi belgilangan ustundagi malumotlarni korish

insert into name_of_table (column_name1,column_name2,..) values (value1,value2,..)
insert into foods (food_name,food_price) values ('Hot dog',17000);

drop table name_of_table; --> table ni ochirish

CREATE TABLE foods(id INT UNIQUE,food_name VARCHAR(20) UNIQUE,food_price int default 2000);
insert into foods(id,food_name,food_price) values (4,'Lavash',23000);

select * from name_of_table where column_name1='Hot dog'

select * from foods where food_price<10;
 select * from foods where food_price<30 and food_price>20;

 select * from foods where food_name like '%oo%';

select * from foods where food_price between 10 and 20;

select * from foods where food_name in ('Hot dog','Everyday clean'); 

select * from foods order by food_price desc; --> Kamayish tartibida saralash

create table users(id not null unique AUTO_INCREMENT,username varchar(40),age int);

delete from name_of_table where column_name1=some_thing

delete from foods where id=15;
-- ===================================================================================================


insert into users_info (name, surname, password, age, username, gender) values ('Abror', 'Barkasov', 'Impala', 45, 'obarkas13', 'M');
insert into users_info (name, surname, password, age, username, gender) values ('Ali', 'Saidov', 'Impala', 22, 'obarkas13', 'M');
insert into users_info (name, surname, password, age, username, gender) values ('Abror', 'Naimov', 'Impala', 78, 'obarkas13', 'M');
insert into users_info (name, surname, password, age, username, gender) values ('Gulnoza', 'Zaidova', 'Impala', 16, 'obarkas13', 'F');
insert into users_info (name, surname, password, age, username, gender) values ('Ali', 'Nomozov', 'Impala', 19, 'obarkas13', 'M')