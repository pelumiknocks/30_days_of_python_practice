#adding items to a set
set_practice = {"pratice 1", "practice two"}
print(set_practice)
set_revise = {"set revise 1", "set revise two"}
set_mastery = set_practice.union(set_revise)
print(set_mastery)
st1 = {"item 1", "balls", "leg", "teeth", "eyes", "skin", "meat"}
st1.add("nose")
print(st1)
#update() allows us to add multiple items at once
st1.update(["bot", "shins", "lungs"])

#removing items from a list 
st1.remove("item 1")

#pop() removes a random item
st1.pop()
print(st1)

st2 = {"item 8", "item 9", "item 10"}
#joining a set 
st3 = st1.union(st2)
print(st3)  #or we can use the update()
st1.update(st2)
print(st1)

#finding intersections
set_zero = {'banana', 'orange', 'mango', 'lemon'}
set1 = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
favorite= {"banana", "mango", "onion"}
favorite_1 = {"banana", "mango"}
worst = {"lemon", "potato", "carrot"}

set_zero.intersection(favorite)
print(set_zero.intersection(favorite))


#checking subsets and supersets
set_zero.issuperset(favorite_1)
favorite.issuperset(set_zero)

#checking diff btw two sets