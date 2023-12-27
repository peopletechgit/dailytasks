# file_operation : Perform the operation of files..
# A file can be opened in 2 ways
# 1st Way
# open(path of file,mode)
# 2nd Way
"""
with open(path of file,mode) as object-name:
    statements
"""
# opened_file = open('intro.txt')
# print(opened_file)
# print(opened_file.closed)
# opened_file.close() # this will close the opened file.
# print(opened_file.closed)
# with open('intro.txt') as file_obj:
#     print(file_obj)
# print(file_obj.closed)
# reading: This is for reading the data from the file..
    # read() - It will read the complete data from the file, but will read the data character by character..
    # readline() - It will read 1 line of data at a time..
    # readlines() - It will read all the lines, by line by line format which will return a list where each element is 1 line in the file..
# with open('sample_data.txt','r') as file_obj:
#     # for ele in file_obj.read():
#     #     print(ele)
#     # print(file_obj.readline())
#     # print(file_obj.readline())
#     print(file_obj.readlines())
# Writing: This is for writing the data into the file..
    # When the file is opened for writing mode, Write will overwrite the prevous content and only new content will be added..
    # write - Its for writing the data into the file, which takes 1 string of data at a time..
    # writelines -- It will take the list of string and will directly into the file..
# If the file is not present it will first create the file and will start writing the data into it..
# with open('write_data.txt','w') as file_obj:
#     # print(file_obj)
#     file_obj.write('Python is a programming language\nDjango is a webframework')
#     # file_obj.write('Django-restframwork is used for apis creation..')
#     file_obj.writelines(['Python is a programming language.\n', 'Django is a framework for Python.\n', 'Django-rest-framework is used for building the Rest Apis..\n', 'Python is used as scripting in Devops tools..'])
# appending : This is adding the content to the previous content..
    # write - Its for writing the data into the file, which takes 1 string of data at a time..
    # writelines -- It will take the list of string and will directly into the file..
# with open('append_data.txt','a') as file_obj:
#     # print(file_obj)
#     file_obj.write('Python is a programming language\nDjango is a webframework\n')
#     # file_obj.write('Django-restframwork is used for apis creation..')
#     file_obj.writelines(['Python is a programming language.\n', 'Django is a framework for Python.\n', 'Django-rest-framework is used for building the Rest Apis..\n', 'Python is used as scripting in Devops tools..'])
# CSV File Operations:
# CSV - Comma Seperated Values
import csv
# reader
# writer / append
with open('sample_data.csv','r') as file_obj:
    print(file_obj)
    # 1st Approach
    csv_data = csv.reader(file_obj)
    for row in csv_data:
        if row[2].startswith('9') and row[3] == 'Hyderabad':
            print(row)
    # 2nd Approach
    csv_data = csv.DictReader(file_obj)
    for data in csv_data:
        print(data)
# writing
# with open('write_data.csv','w',newline='') as file_obj:
#     # csv_write_data = csv.writer(file_obj)
#     # csv_write_data.writerow(['name','email','mobile','city'])
#     # csv_write_data.writerows([['ramesh', 'ramesh@gmail.com', '9488998444', 'Hyderabad'],['suresh', 'suresh@gmail.com', '8398494944', 'Chennai'],['mahesh', 'mahesh@gmail.com', '9889494849', 'Bangalore']])
#     csv_write_data = csv.DictWriter(file_obj,fieldnames=['name','email','mobile','city'])
#     print(help(csv_write_data))
#     # csv_write_data.writeheader()
#     csv_write_data.writerow({'name': 'ramesh', 'email': 'ramesh@gmail.com', 'mobile': '9488998444', 'city': 'Hyderabad'})
# Appending:
# with open('append_data.csv','a',newline='') as file_obj:
#     # csv_write_data = csv.writer(file_obj)
#     # csv_write_data.writerow(['name','email','mobile','city'])
#     # csv_write_data.writerows([['ramesh', 'ramesh@gmail.com', '9488998444', 'Hyderabad'],['suresh', 'suresh@gmail.com', '8398494944', 'Chennai'],['mahesh', 'mahesh@gmail.com', '9889494849', 'Bangalore']])
#     csv_write_data = csv.DictWriter(file_obj,fieldnames=['name','email','mobile','city'])
#     # csv_write_data.writeheader()
#     csv_write_data.writerow({'name': 'ramesh', 'email': 'ramesh@gmail.com', 'mobile': '9488998444', 'city': 'Hyderabad'})