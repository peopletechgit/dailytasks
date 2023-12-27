# functions : set of lines of code which performs a sepcific task...
    # wtite the code for ones and use it n number of times...


# a=32
# b=43

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)

# a=12
# b=13



# def ---- it is the keyword for function

# """"""
# def function-name():
#     statement
# """""""



# def arthimetic(a,b):
#     print(a+b)
#     print(a-b)
#     print(a*b)
#     print(a/b)
#     print(a%b)

# function call is mandatory....
# arthimetic(12,13)



# different ways of passing the arguments:
    # 1) posiitonal arguments
    # 2) default arguments
    # 3) keyword arguments
    # 4) arbitary positional arguments
    # 5) arbitary keyword arguments

# positional arguments : assigning the value to the arguments based on the position of values passed....

# def login(username,password):
    # if username=="ramesh" and password=="ramesh@123":
        # print("login sucessfull!")
    # else:
        # print("invalid credentials")


# login("ramesh","ramesh@123")


# default arguments : passing the default value to an anrgument at the function declaration
    # if we pass any value at the function call default value will be override

# def employee_info(emp_id,emp_name,work_location):
#     print(f"Hi {emp_name} your employee id is {emp_id} and your work location is {work_location}")

# employee_info(101,"Ramesh",'Banglore')
# employee_info(101,"Ramesh")




# keyword arguments :
    # passing the values at the function call based on the argument name....

# def employee_info(emp_id,emp_name,work_location):
    # print(f"Hi {emp_name} your employee id is {emp_id} and your work location is {work_location}")

# employee_info(emp_id=43, emp_name='suresh',work_location='bangalore')
# employee_info(43, 'suresh','bangalore')
# employee_info( emp_name='suresh',emp_id=43,work_location='bangalore') # by binding the value to the argument even though the place had changed we get estimated output, it does not based on order



# 4) arbitary positional arguments : passing multiple positional values to the function call.......
    
# * -- symbol for the declaring the multiple posiiton arguments
    

# def cred_tans(*trans): # for single * positional 
    # amount=0
    # for ele in trans:
        # amount+=ele # amount = amount+ele
        # print(f"hi, you have done {len(trans)} transaction for an amount of {amount}/-")
# 
# cred_tans(43245,55487,56489)
# 
# cred_tans(43245,55878,56489,4845)
# 
# cred_tans(1234,55878,56489,4845)



# arbitary keywords : passing the multiple keywords values to the function call..............
# ** -- symbol for declaring the arbitary keyword arguments........
    
# def cred_tans(**trans): # for single * positional 
    # print(trans)
    # amount=0
    # for ele in trans:
        # amount=amount+trans[ele]
    # print(f"hi, you have done {len(trans)} transaction for an amount of {amount}/-")
# cred_tans(date_2=6372, date_10=7484, date_18=8373)
# 
# cred_tans(date_2=6372, date_10=7484, date_18=8373,date_12=5645)
# 
# cred_tans(date_2=6372, date_10=7484, date_18=8373, date_12=7878)
# 
# cred_tans(date_2=6372, date_10=7484, date_18=8373)


# def cred_trans(*trans,**info):
    # print(trans)
    # print(info)
    # amount=0
    # for ele in trans:
        # amount += ele
    # print(f"Hi {info['name']}, your credit card statement for an amount of {amount}/- has been sent to {info['email']}")
# 
# cred_trans(5464,7474,7474, name="suresh",email="suresh@gmail.com")
# cred_trans(5464,7474,7474,8484,6474, name="ramesh",email="ramesh@gmail.com")


# local and global varaibles.......

# local variables : those variables which we passed as argument to the function inside the function and can be accessed only inside the function itself

#global variables : those vairables declared outside of the function and can be accessed for any where without restrictions

# name="suresh" # global variables

# def info(email,mobile): # local variables
    # global name # local to global 
    # global email1
    # email1=email
    # name="ramesh"
    # print(f"Hi {name}, your email is {email} and mobile number is {mobile}")
# 
# info("suresh@gmail.com","9848507255")
# 
# print(name)
# print(email1)

# return statement : 

# def add(a,b):
#     print(a+b)
#     return a+b
#     print("hello")



# def calc(a,b,c,d):
#    print(add(a,b)-(c-d))

# calc(3,4,2,1)



# recursion : a function calling itself...

# n! = n*(n-1)!
# 6! = 6*5!
#      6*5*4!
#      6*5*4*3!
#      6*5*4*3*2!
#      6*5*4*3*2*1!
#      6*5*4*3*2*1*1

# def cal_fact(a):
#     if (a==1 or a==0):
#         return 1
#     else:
#         return a * cal_fact(a-1)
    
# print(cal_fact(6))



# lambda functions or anonymous functions...... : a function whch doesnot have any nam at all...

# lambda arguments:expression
 
data =  lambda a,b:a+b

print(data(2,3))

# map
# filter

a=[35,64,44,22,44,99,44,74,65]

# new=[]

# def info(a):
    # for ele in a:
        # new.append(ele+2)
# info(a)
# 
# print(new)
# 
# print([ele+2 for ele in a])
# 
# 
# print(list(map(lambda i:i+2,a)))

a=["9290185587","9848507255","8019130171","9381932646","9490285177"]

new =[]

def check(a):
    for ele in a:
        if ele.startswith("9"):
            new.append(ele)
check(a)

print(new)

print([ele for ele in a if ele.startswith('9')])

print(list(map(lambda i:i.startswith('9'),a)))

print(list(filter(lambda i:i.startswith('9'),a)))