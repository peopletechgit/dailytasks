# # First we have to download the library..

# # mysql - pymysql
# # postgres - psycopg2
# # oracle - oracle_cx
# # monogdb - pymongo
# # sqlite - sqlite

# # pip install pymysql

import pymysql

# # conn_data = pymysql.connect(user='root',password='password') # This is connecting to the direct mysql server..

conn_data = pymysql.connect(user='root',password='Hari@sql2023',database='player_info') # This is connecting to the particular database in the server..
cur_data = conn_data.cursor()

# # print(cur_data.execute('show databases'))

# # print(cur_data.fetchall())

# # cur_data.execute('create database python_8am_dec')
# # print(cur_data)
# # print(conn_data)


cur_data.execute("create table player_info(p_name varchar(20),p_franchasis varchar(4),p_role varchar(10))")