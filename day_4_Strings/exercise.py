#1
"""Concatenate the string
'Thirty', 'Days', 'Of', 'Python' to a single string,
'Thirty Days Of Python'.
""" #easy not doing
#challenging exercises only
company = "Coding for all"
print(company.upper())
print(company.swapcase())

print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier()) #isidentifier methods check if the variable is a good naming convention

#Create an acronym or an abbreviation for the name 'Python For Everyone'.

shit_to_abrreviate = "Python For Everyone"
without_space = shit_to_abrreviate.replace(" ", "")
print(without_space)
print(without_space[0] + without_space[6]+without_space[9])

#'   Coding For All      '  , remove the left and right trailing spaces in the given string.
coding = '   Coding For All      '
removed_space = coding.replace("   ","")
print(removed_space)

#The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined = "# ".join(python_libraries)
print(joined)
print(python_libraries)
print("Name\tAge\tCountry\tCity")
print("Pelumi\t19\tNigeria\tOta")