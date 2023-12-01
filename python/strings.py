# strings : sequence of anything like char, numbers, special symbols donated with ""

# name="suresh"
# print(name)
# print(type(name))

# name='rajesh'
# print(name)
# print(type(name))

# name="""suresh"""
# print(name)
# print(type(name))

# single line '' or ""
# """""" or """""" ''' ''' -- mutiliple string
# poem = "balidhan param dharma ha"
# poem1 = 'balidhan param dharma ha'
# poem2 = """balidhan param
# dharma ha"""
# print(poem ,",", poem1,",",poem2)

# accesing the elements inside the string. -- indexing
# indexing starts from 0 and will go on depending on length, space also will caluclate as one word
# [] -- its the symbol for performing the indexing
str1="python is a programming language."
# print(str1[0])
# print(str1[7:20])

#slicing - performng the jumps
# print(str1[23:0:-1])

# negative indexing  -- it will start from -1 reverse of string
# print(str1[-1])
# print(str1[-7])
# print(str1[0:10:1]) # default value for 3rd argument will be 1
# print(str1[0:10:2])
# print(str1[-2:-9:1]) #this will return the output as empty since slicing is gooing to perform in positive order but we require it in negative order
# print(str1[-2:-10:-1]) #this will return the output as empty since slicing is gooing to perform in positive order but we require it in negative order
# len -- will return the length of string
# print(str1[-1:-len(str1):-1])
# print(str1[::-1])
# data=str1[-2:10:-1]
# print(data[::-1])
# print(str1[24:32])
# print(str1[-9:32])

# immutable -- those which we cannot change once the declaration is odne
# str1[0]="P"
# str1[0]="P" will throw error

#concatination. adding 2 or more strings and make it as single string.
#repetion. reprating the same string mutliple number of times.

# hero="major sandeep unnikrishnan "
# slogan= " sahas ki vijay "
# res = hero + slogan
# print( res )
# print( res*108 )

# methods 

#dir -- will list what are all the methods that i can perform on the value..
print(dir(str))