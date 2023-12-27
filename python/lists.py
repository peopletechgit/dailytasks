# lists : sequence of multiple values and sepereated with , and enclosed in []

# list1 = [62,5.36,"python","django",87]

# print(list1)

# print(type(list1)) # will return the type as lists...

# nested lists : declaring the lsists inside the lists...

# list = [32,"python",["mahesh","suresh","subhash"],73,"django",32,"datascience"] # nested lists

# accessing elements from the nested lists using --- indexing..

# indexing will start from 0 and will go depending on the length..

# print(list1[2:6])

# print(list1[-1:-6:-1])

# nested indexing : performing the indexing on other indexing outputs
# print(list1[2][1])
# print(list1[2][1][3])
# print(list1[2][-1::-1])
# print(list1[2][::-1])
# print(list1[::-1]) # will reverse the stirng / lists
# print(len(list1[2]))
# print(len(list1))


# lists is mutable....
# print(list)
# list[1] = "devops"
# print(list)

# list[2]="chennai"
# print(list)

# list[1:4]=[11,12,13,14,15,16] # this will add the element of the list as seperate value
# list[1]=[21,22,23,24] # it will add it as single nested lists with in the lists as we specifed as single index value

# print(list)
# del list[1]
# print(list)


#concatination(+) : adding of 2 elemets and making it as single 
# repetition(-) : repeating the elements of lists multiple no of times

# print([1,2,3,4]+['python',32,'django'])
# print([1,2,3,4,5]*3)

# list methods
# print(dir(list))

# adding methods
    # append
    # extend
    # insert

# removal methods
    # remove
    # pop
    # clear

# accesing methods
    # index
    # count

# alter methods
    # sort
    # reverse
    # copy



# adding methods - append -- addng single element in to the list and that element will be added last of right side
# print(list)
# list.append("datascience")
# list.append([31,32,33])
# print(list)



#extend -- adding multiple elements at a time into the list and will take only sequence
    # it wont accept numbers and dictionaries as value inside the extend method
# list.extend(["java","php"])
# list.extend(43) #-- because integer is not an iteration
# list.extend("datascience")
# list.extend(["datascience","devops",55])
# print(list)


# insert -- it also for adding only single element into the list at a specific index value
# list.insert(4,"machinelearning")
# print(list)


# removal methods

# remove -- its for removing the element from the list by specifying the element
# list = [32,"python",["mahesh","suresh","subhash"],73,"django",32,"datascience"] # nested lists
# print('ramesh' in list)
# list.remove("ramesh")
# print(list)
# if 'ramesh' in list:
#     list.remove('ramesh')
# print(list)


# pop -- its for removing the element from the list by specifying the element but based on index value
# list.pop(4)
# print(list.pop(4))
# print(list)


# clear() -- it will remove all elements from the list and makeit as empty list
# list.clear()
# print(list)


# accessing methods 
    # indexing -- we can access any element of the list using its index value
# list = [32,"python",["mahesh","suresh","subhash"],73,"django",32,"datascience"] # nested lists
# print(list.index('django'))

# count -- how many times a particular element is repeated in the list
# print(list.count(32))

# alerting methods:
    # sort() -- it sorts the entire list in ascending order or descending order
    # we have to make sure that all the elements inside the list should be of the same data type only
    # default it will perform ascending order
    # if it contains different data type it will throw the error
# print(list[2].sort()) 
# list = ['pavan kumar','sandeep unnikrishnan','maneekshaw','santhosh babu','mohit sharma','tushar mahajan']
# list.sort()
# list.sort(reverse=True)
# print(list) # it wont work for str and int

# list1=list.copy() # this will copy the values of list and create a new memory for the copy and will assign it to the list1

# print(list1)
# print(list1)
# list.append(43)
# print(list)
# print(list1)

# list1 = ['pavan kumar','sandeep unnikrishnan','maneekshaw','santhosh babu','mohit sharma','tushar mahajan']
# satisfied_data=[]
# for ele in list1:
#     if ele=="pavan kumar":
#        satisfied_data.append("i am para sf")
#     elif ele=="sandeep unnikrishnan":
#          satisfied_data.append('dont come up i will handle them')
#     elif ele=="mohit sharma":
#          satisfied_data.append("kill them")
#     else:
#         print("you are not patriotic")
# print(satisfied_data)

marks=[64,84,53,94,43,73,63,84,68,53,58]
# updated_marks=[]
# for ele in marks:
#     if ele<90:
#         updated_marks.append(ele+5)
#     else:
#         updated_marks.append(ele)
# print(updated_marks)

# list comphrehension methods:
# sytax1:
# [expression for ele in sequence]

# list comphrehension way
[ele+5 for ele in marks]

