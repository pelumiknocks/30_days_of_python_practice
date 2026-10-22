#strings
#multiline string
multiline_string = """Hello how are you doing
Today is 10th of october,2026 or rather 21st, 1month to my birthday
"""
#string_concatenation
first_name = "Pelumi"
last_name = "Adewale"
space = " "
full_name = first_name + space + last_name
print(full_name) #prints "Pelumi Adewale"

#escape sequences
print("Hi, I hope you are good?\nCall me when you receive this") #this prints the sentence after "\n" on a new line
print ("Players\t\Goals\t\tApperances") #this is a tab escape sequence that leaves spaces among words or characters
print("Kevin De Bruyne\t\t208\t680")
print("Lionel Messi\t\t945\t1130")
print("Cristiano Ronaldo\t981\t1300")
print("Erling Haaland\t\t302\t385")

#string formatting
#%s-strigns
#%d-integers
#%f-floating point numbers
#%.numberofdigitsf-floaitng point with precision

first_name = "Pelumi"
last_name = "Adewale"
language = "Python"
formatted_string = "I am %s %s and I love %s" %(first_name, last_name,language)
print(formatted_string) #I am Pelumi Adewale and I love Python

#with numbers
radius = 30
pi = 22/7
area = pi*radius**2
answer = "A circle with a radius of %d has an area of %.3f" %(radius, area)
print(answer) #A circle with a radius of 30 has an area of 2828.571

#with lists
python_libraries = ["Numpy", "Django", "Pandas"]
formatted_string_1= "Common python libraries are %s" %(python_libraries)
print(formatted_string_1)#Common python libraries are ['Numpy', 'Django', 'Pandas']

#new style of formattting strings 
new_formatted_string = "A circle of radius {} has an area of {:.3f}". format(radius, area)
print(new_formatted_string)

new_formatted_string_1 = "My name is {} {} and I love coding in {}".format(first_name, last_name, language)
print(new_formatted_string_1)


#string interpolation/f strings
a=7
b=9
print(f"My name is {first_name} {last_name}")
print(f"the addition of the numbers, {a} and {b} is {a+b}")

#so we know strings are arrays of characters
#so each character in a string have a swquence or index
#e.g
language = "Python"
a,b,c,d,e,f = language
print(language[0])#the prints p
print(e) #prints "o"
last_index = len(language) -1
print(last_index)
#for value in index
last_letter = language[-1]
print(last_letter)

#slicing python strings 
the_first_three_letters = language[0:3]
print(the_first_three_letters)
course = "Engineering"
shorted_form = "Comp" +" " + course[0:3] + course[-4] + course[(len(course)-2):(len(course))]
print(f"I studied {shorted_form} in Uni and I graduated with first class and secured international internships and masters in us and all across europe and asia")

#reverse a string
greeting = "Hello World"
print(greeting[::-1])

#skipping while slicing
pto= language[0:6:2]
print(pto)

#string methods
#capitalize()
challenge = "thirty days of python"
challenge_capitalize = challenge.capitalize()
print(challenge_capitalize)

#count()
#returns occurnces of substring in string
print(challenge.count("y")) #3
print(challenge.count("a")) #1 

#endswith()
#checks if a string ends with a specified ending 
print(challenge.endswith("n")) # prints True
print("Bombabious".endswith("ous")) #prints True

#join()
# #returns a concatenated string

web_tech = ["HTML", "CSS","Javascript", "React"]
result = ", " .join(web_tech) 
print(result)

"""
and many more , they are so much
"""

