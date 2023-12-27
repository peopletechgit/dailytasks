# data = [{
#     "name":"ramesh",
#     "email":"ramesh@gmail.com",
#     "mobile":"8392982893"
# },
# {
#     "name":"ramesh",
#     "email":"ramesh@gmail.com",
#     "mobile":"8392982893"
# },
# {
#     "name":"ramesh",
#     "email":"ramesh@gmail.com",
#     "mobile":"8392982893"
# },
# {
#     "name":"ramesh",
#     "email":"ramesh@gmail.com",
#     "mobile":"8392982893"
# }]

# import json

# #dumps
# #dump

# # load
# # loads


# #loads : its for converting json string to python object..
# json_str="""
# [{
#     "name":"ramesh",
#     "email":"ramesh@gmail.com",
#     "mobile":"8392982893",
#         "city":""
# },
# {
#     "name":"ramesh",
#     "email":"ramesh@gmail.com",
#     "mobile":"8392982893",
#         "city":"hyderabad"
# },
# {
#     "name":"ramesh",
#     "email":"ramesh@gmail.com",
#     "mobile":"8392982893",
#         "city":"hyderabad"
# },
# {
#     "name":"ramesh",
#     "email":"ramesh@gmail.com",
#     "mobile":"8392982893",
#     "city":null
# }]
# """
# print(json_str)
# print(type(json_str))
# # print(help(json.loads))

# py_obj=json.loads(json_str) 

# print(py_obj)
# print(type(py_obj))

# #dumps -- this is  for converting python object into json str....
# py_obj.append({"name":"hari","email":"hari@gmail.com","mobile":"9848507255","city":"machilipatnam"})

# converted_str=json.dumps(py_obj)

# print(converted_str)
# print(type(converted_str))


import json


# print(help(json.load))

with open('sampledata_json.json') as file_object:
    json_data=json.load(file_object)

    # print(json_data)
    # print(type(json_data))

json_data.append({'name':'kishore','email':'kishore@gmail.com','mobile':'9290185587','city':'bandar'})

print(json_data)

# dump() -- its for adding the json into the json file

with open('wite_data.json','w') as file_object:
    json.dump(json_data,file_object, indent=10)



# loads -- converting string to python object
    
# dumps -- converting python object to string
    
# load -- load the json file and considering the data into python object
    
# dump -- considering the python object and saving it into json file
