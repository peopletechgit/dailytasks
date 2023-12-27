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
# str1="python is a programming language."
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

# immutable -- strings are immutable datatypes those which we cannot change once the declaration is odne
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
# print(dir(str))

#startswith, endswith, isaplha, isalnum, isdigit, islower, isupper,lower,upper,title,capitalize,swapcase,index,find,count,split,strip,zfill,join, .format(dot),replace
# 
# dailouge="dont come up i will handle them"
#startswith() -- Its just for checking wheather the string is starting with what we specified or not. 
#endsswith() -- Its just for checking wheather the string is ending with what we specified or not.

# print(dailouge.startswith("d")) 
# print(dailouge.endswith("them"))
#isapha -- will check everything inside the string are alphabets only 
# print(dailouge.isalpha()) # false because spaces

#isnum() -- it will check weather everything inside the particular string are alphanumeric values
# pan="abcd1234ef"
# print(pan.isalnum())
# print(dailouge.isalnum())

#isdigit() -- it is to check weather everything inside the string is numbers only
# mobile="9848507255"
# print(mobile.isdigit())

#islower() -- its to check weather everything inside the string is lowr case only
#isupper() -- is to check weather evryrthing inside the string is upper case only

# sample1="python is programming language"
# print(sample1.isupper())
# print(sample1.islower())
# sample2="PYTHON IS PROGRAMMING LANGUAGE"
# print(sample2.isupper())
# print(sample2.islower())


#upper() - its for converting lowercase to uppercase
#lower() - its for converting upper to lower
# email = "doradla.hari@GMail.com"
# print(email.lower())
# print(email.upper())

#title() - its for making first letter of each word in a sentence to be capitalized.
# dailouge = "dont come i will handle them"
# print(dailouge.title())

#capitalize() - its for making first letter of each word in a sentence to be capitalized.
# print(dailouge.capitalize())

#swapcase() -- converting lower to upper , upper to lower
# print(dailouge.swapcase()," - swap case")

#index() - its same as find but if it doesnot finds then it gives error
# sample1="django is a web framework development 72 backend frame work for python"
# print(sample1.index('f'))
# print(sample1.index('is'))
# print(sample1.index('b frame'))
# print(sample1.index('o'))
# print(sample1.index('72'))
# print(sample1.index('z')) it will throw the error as the element is not present in the string

#count() - its for counting how many times a char/substring appears in the string
# print(sample1.count("o"))
#input("o has occured 4 times which occurence you want...")

#find() - its for finding the index position of substring in the main string
# print(sample1.find("f"))
# print(sample1.find('z'))
# print(sample1.find('is'))
# print(sample1.find('b frame'))
# print(sample1.find('o'))
# print(sample1.find('72'))

#replace() - its for replacing one character/string with another character/string
# print(sample1.replace("frame work","my frame work"))
# print(sample1.replace("frame work","my frame work",100))

#rsplit() - its similar to split() but works in reverse direction.
#split() - its for splitting the string into a list based on space
# print(sample1.split()) # splits the string into multiple strings based on spaces
# print(sample1.split('o')) # splits the string into multiple strings based on spaces
# print(sample1.split('z')) # splits the string into multiple strings based on spaces

#strip() - its for removing the escaping sequences from the string
# str1="\npython is a programming \nlanguage used for web\t development using \ndjango framework\n"
# print(str1)
# print(str1.strip()) #\n in starting doesnt consider
# print(str1.rstrip()) 
# print(str1.lstrip()) 

# email="doradla.hari@gmail.com"
# print(email.split('@')[0])
# print(email.strip('@gmail.com'))

#zfill() - its for adding zeros before the number till it reaches the length you want.
# str1="82188921"
# print(str1.zfill(10))

#join() -- its for joining the elements of a sequence to a string.
# str1="python"
# print("@".join(str1))
# list1=["python","django","datascience"]
# print(" ".join(list1))

#format() - its for formatting the data types like %s ,%d,%f etc..
# str1= "use otp 12359 for your purchase at flipkart.com for an amount of 5000/- rupees"
# data1= "use otp {} for your purchase at {} for an amount of {} rupees".format("13456","amazon.com", "5000")
# print(data1)
# print(data1)

#f-format -- 
otp=input("enter otp:")
website=input("enter website:")
amount=input("enter amount:")
# data1= "use otp {otp} for your purchase at {website} for an amount of {amount} rupees".format(otp="13456",website="amazon.com", amount="5000")
data1= f"use otp {otp} for your purchase at {website} for an amount of {amount} rupees/-"
print(data1)
#partition() - its for dividing the string at the given separator and returns three parts.
#expandtabs() - its for expanding tabs into white spaces.
#ljust(), rjust() - these two functions are used for padding characters to left, right respectively.
#center() - this function is used for centering text around a certain point.
#format_map() - its for formatting the data types using dictionary.
#translate() - its for translating the special characters into normal characters.
#maketrans() - its for creating translation table between different characters.
#encode() - its for encoding the string into bytes.
#decode() - its for decoding the byte into string.
#fromhex() - its for converting hexadecimal value into string.