# module :every python file is going to be called as module..

# import -- its the keyword for loading the module..

# 1st syntax:
    # import module-name

# 2nd syntax:
    # from module-name import functionalities

# import module1 # loading the complete module

# print(module1.name)

# print(module1.add(3,4))

# from module1 import * ## going inside the module and loading the functionalities 

# print(name)
# print(add(3,4))

# from module1 import name,add

# print(name)
# print(add(3,4))

# from module1 import *

# from module2 import *


# print(name)
# print(email)
# print(sub(4,5,6))
# print(add(3,4))


# import module1

# import module2

# print(module1.add(3,2))

# print(module1.sub(4,5,6))

# print(module2.add(3,2,1))

# from module1 import add
# from module2 import add as module2_add

# print(add(3,4))
# print(module2_add(3,4,5))


#modules are divided into 3 types 
    # user defined modules -- those modules(python files) which we create..
    # inbuilt modules -- those which comes defaultly with python installation
    # external modules -- by downloading based on requirement


# python check into 3 paths when we import a module
    # 1) current working directory...
    # 2) where python is installed...
    # 3) where we set the env path....

# import sys

# print(sys.path)