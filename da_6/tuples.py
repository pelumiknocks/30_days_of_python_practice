"""
Tuple is a collection of different data types
which is ordered and unchangeable(immutable)

"""
#unlike list tuples have few methods(hell yeah im happy)
#creating a tuple
empty_tuple = ()
empty_tuple = tuple()

tuple_1 = ("item 1", "item 2", "item 3", "item 4", "item 5")
tuple_2 = ("banana", "waterlemon")
#tuple length 
print(len(tuple_1))

#accesing tuple items
first_item = tuple_1[0]
print(first_item)
last_index = len(tuple_1) - 1
last_item  = tuple_1[last_index]
print(last_item)

#can also be accesed thriugh negative indexing 
#e.g tuple_1[-1]

#slicing tuples
sliced = tuple_1[1:3]
print(sliced)

#changing tuples to list
#to modify a tuple change it to list then change it back
tuple_2= list(tuple_2)
print(type(tuple_2))
tuple_2[0]="item .5"
tuple_2 = tuple(tuple_2)
print(type(tuple_2))
print(tuple_2)

#checking an itme in tuple
if "item 1" in tuple_1:
    print("True")

#joining tuples
tuple_3 = tuple_1 + tuple_2
print(tuple_3)

#deleting tuples
del tuple_3
print(tuple_3) # not defined, has been deleted 
