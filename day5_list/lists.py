lists = list() #one way to create list
#or
list_2 = [1,2,3,4,5]
fruits = ["mango", "banana", "waterlemon"]
vegetables = ["Tomato", "Potato", "Cabbage"]
print("Fruits:",fruits)
print("Vegetables:",vegetables)

#list can be accessed using positive indexing 
print(fruits[0]) #prints "mango"
print(fruits[1]) #prints "banana"
print(vegetables[0]) #prints "tomato"
print(vegetables[1]) #prints "potato"

last_vegetable = vegetables[len(vegetables)-1]
print(last_vegetable)

#can also be accesed using negative indexing 
#negtive indexinng means beginning for the end
#e.g
print(fruits[-1])#prints "waterlemon
first_fruits = fruits[-3]
print(first_fruits)

#unpacking list item
first_item,second_item, third_item= fruits
print(first_item)
#if you have so many other items to print you can use *
#e.g
car_brands = ["BMW", "Lambourgini", "Ferrari", "Audi", "Tesla", "Toyota", "Honda", "KIA"]
first_car,second_car,*remaining_car = car_brands
#when we use * it print the remaining items on the list
print(remaining_car) #['Ferrari', 'Audi', 'Tesla', 'Toyota', 'Honda', 'KIA']

#slicing items in a list 
car_i_want = car_brands[2:4]
car_i_have = car_brands[0:10]

#you can also modify a list
car_brands[1] = "Buggatti"
print(car_brands)

#checking items in a list 
print("Bugatti" in car_brands)
print("BMW" in car_brands)

#adding items to a list
#we use append() to add items to a list 
car_brands.append("Lexus")
print(car_brands)

#inserting items at a specific index in a list 
car_brands.insert(4, "Porsche")
print(car_brands)
#removing items from a list 
#using pop()- removes item specified using index, if index not specified, removes the last index
car_brands.pop()
print(car_brands)
car_brands.append("Lexus")
car_brands.pop(0) #pops "BMW"
print(car_brands)

#you can also remove itwms using del #e.g
del fruits[0]
print(fruits)
#can also delete via a rnge
#e.g
del car_brands[0:5]
print(car_brands)

#you cna also copy, join,count itmes in a list , find index of an item in alst 
#you can reverse a list
#you can sort itms in a list 