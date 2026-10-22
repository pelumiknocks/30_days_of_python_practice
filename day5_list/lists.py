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
