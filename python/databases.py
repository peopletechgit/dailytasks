# # First we have to download the library..

# # mysql - pymysql
# # postgres - psycopg2
# # oracle - oracle_cx
# # monogdb - pymongo
# # sqlite - sqlite

# # pip install pymysql

# import pymysql

import pymysql 

# conn_data = pymysql.connect(user='root',password='Hari@sql2023') # this is connecting to the direct mysql server..

conn_data = pymysql.connect(user='root',password='Hari@sql2023',database='python_8am_dec' ) # this is connecting to the particular database..

cur_data = conn_data.cursor()

# print( cur_data.execute('show databases'))

# print(cur_data.fetchall())
# print(cur_data)
# print(conn_data)


# cur_data.execute('create database python_8am_dec')

# cur_data.execute('create table player_info(p_name varchar(500),p_franchasis varchar(500),p_role varchar(500))')
# cur_data.execute('create table player_info1(p_name varchar(500),p_franchasis varchar(500),p_role varchar(500))')
# cur_data.execute('create table player_info1(p_name varchar(500),p_franchasis varchar(500),p_role varchar(500))')

# cur_data.execute("insert into player_info(p_name,p_franchasis,p_role) values('Kohli','RCB','Batsmen'),('Bumrah','MI','Bowler'),('Rohit','MI','Batsmen'),('Jadeja','CSK','Allrounder'),('Maxwell','RCB','Allrounder');")

# print(cur_data.execute('select * from player_info'))

# print(cur_data.fetchall())

conn_data.commit()

# print(cur_data.execute("select * from player_info where p_role='Batsmen'"))
print(cur_data.execute("update player_info SET p_role='Batsmen' where p_name='Maxwell'"))

print(cur_data.fetchall())