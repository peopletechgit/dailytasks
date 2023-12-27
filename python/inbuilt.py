# in built modules : these modules will come from python installation

# print(help('modules'))

# random
# datetime
# pdb - python debugger
# dateutil
# tkinter
# json
# csv


# import random

# print(dir(random))
    # randit -- 
    # randrange
    # choice
    # choices

# print(random.randint(1000,10000))

# print(random.randint(1000,1000000))

# print(random.randrange(1000,1000000))

# print(random.randrange(10,35,3))


# a=['SWIGGYIT','SWIGGY50','SWIGGY24','SWIGGYBIRTHDAY']

# print(random.choice(a))

# lotteries=['LOT1','LOT2','LOT3','LOT16','LOT71','LOT43','LOT66']

# print(random.choices(lotteries,k=3))


# datetime -- 

# from datetime import datetime

# print(dir(datetime))

# print(datetime.now())

# print(datetime.today())


# print(datetime.now().date().month)

# print(datetime.now().time())

# from datetime import timedelta

# subscription_date= datetime.now()

# print(subscription_date)
# subscription_end_date = subscription_date+timedelta(days=30)

# print(subscription_end_date)

# session_started = datetime.now()

# session_ended=session_started+timedelta(minutes=10)

# print(session_ended)

# from dateutil.relativedelta import relativedelta

# strftime -- this is for conversion python date time to string...
# strptime -- 

# today_date=datetime.now()

# print(today_date)
# print(type(today_date))

# # print(today_date.strftime("%y-%m-%d"))
# print(today_date.strftime("%d-%m-%y %H:%M:%S %A %a"))

# print(type(today_date.strftime("%y-%m-%d")))

import os

# print(dir(os))

# getcwd()
# listdir()
# mkdir()
# makedirs()
# rmdir()
# removedirs()
# remove()
# rename()
# open()
# environ()

# print(os.getcwd())  # current working directory..
# 
# os.chdir('C:/Users/DoradlaHari/Downloads')
# 
# print(os.getcwd())
# 
# print(os.listdir('.')) # this will return all the folders and files current working directory

# external modules

# pip -- python package manager

# pip install package-name -- command

# pymysql
# mySQLdb
# pyscopg2
# python-facebook-api

# pip uninstall package-name

# pip list or pip freeze -- for listing all the libraries which are installed externally..

# boto3 --
# pandas -- 