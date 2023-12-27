# dictionaries : sequnce of key:value pairs seperated with comma (,) which are declared inside { }....

dict1={"name":"ramesh","email":"ramesh@gmail.com","mobile":9848507255,"state":"telangana"}


# print(dict1)

# accesing inside the dictionary is done using name of key which you want to access...

#[] - its the symbol for acccesing

# print(dict1['email'])


# keys inside the dictonary should be immutable only...(int,str,tuple)
# values : inside the dictionary can be of any type

# dict2 = {"name":"suresh",1:21,(1,2,3):[21,22,23]} correct format

# dict2 = {"name":"suresh",1:21,(1,2,3):[21,22,23],[1,2,3]:"sample"}  # error as you are declaring mutable element....
# unhashable means mutable data type which allow edit but hashable vice versa
# print(dict2)


# dictionaries are mutable

# dict1['country']='india' # if key is not present in dict it will be added as new key:value pair. 
# dict1['state']='andhra' # if the key is alredy present inside the dict it will update the previous key value with new value
# print(dict1)

# dict keys are unique

# if we have multiple keys in dict with repetion it will consider key value pair in the dict+


# print("mobile" in dict1)

# if 'city' in dict1:      # this is for checking wheather the key is alredy existed in the dict
#     pass
# else:
#     city=input("enter your city")
#     dict1['city']=city

# print(dict1)


dict1['city']='hyderabad'
print(dict1)

dict2={"city":"vizag","iplteam":"csk","captain":"ms dhoni sir"}

dict1.update(dict2)
print(dict1)

# nested_dict ={"states":{
#     "state1":"andhra",
#     "state2":"telanagana"
# }}

# print(nested_dict["states"]["state1"])   # accessing nested dict


# dict methods
    # update -- ading key:value pairs of 1 dict to other dict..
    # removal methods

# removal methods
    # pop
    # popItem
    # clear

# pop() -- it will take the key you want to remove and remove the key:value from the dict and wll return value as the output
# print(dict1.pop("iplteam"))