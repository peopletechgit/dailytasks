# Sets:Sequence of elements seperated with comma(,) which are declared inside {} which contains only unique elements and unordered..
# set1 = {32,'python',(43,44,45),32,76,89.6,76}
# print(set1)
# Sets are mutuable - we can add or remove the elements.
# Elements inside the sets has to be immutable only..
# set1 = {32,'python',(43,44,45),32,76,89.6,76,[1,2,3]} -- This will be an error as we are declaring an mutubale element inside the set..
# print(set1)
# Accessing inside the sets is not possible as the ordered is unpredictable..
# Sets methods:
    # add,update,remove,discard,clear,pop,copy
# Sets Operations:
    # union(|),intersection(&),differene(-),symmetric_difference(^),intersection_update,difference_update,symmetric_difference_update,issubset,issuperset,isdisjoint etc.,
# print(dir(set))
# Add - for adding single element into the set at a time..
set1 = {32,'python',(43,44,45),32,76,89.6,76}
print(set1)
set1.add(89)
print(set1)
set1.add('django')
print(set1)
# update - for adding multiple elements into the set at time..
set1.update(['datascience',43,'aws',32])
print(set1)
# remove() - - If the element is not present it will throw the error..
# discard() -- If element is not present it wont do anyting..
# set1.remove(43)
# print(set1)
# set1.discard('django')
# print(set1)
set1.pop()
print(set1)
# clear()
set1.clear()
print(set1)
# empty set:
# set1 = set() -- empty set 