# Tuples : sequence of multiple values seperated with comma (,) declared inside ()....

# tuple1=(62,5.6,"python","django",84)

# print(tuple1)

# print(type(tuple1))

# list1=[32]

# print(type(list1))

# tuple2=(32,) # single value tuple needs , for single value

# print(type(tuple2))


# tuple1=62,5.6,"python","django",84

# print(tuple1)


# accesing the element insde the tuple is done using ---- indexing


tuple2=(32,'python',['mahesh','suresh','shubhash'],73,'django',32,'datascience',(11,12,13))
# print(tuple2)

# print(tuple2[3])

# print(tuple2[2:6])

# print(tuple2[1:7:2])

# print(tuple2[-3])


# print(tuple2[-1::-1])

# print(tuple2[2][1])

# tuples are immutable...

# print(dir(tuple))

# print(tuple2.index(73))

# print(tuple2.count(73))

#nested indexing
print(tuple2[2][1])

tuple2[2][1]="venkatesh"
print(tuple2) #can edit since it is immutable