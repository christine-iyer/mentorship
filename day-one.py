# what is python? A beginner friendly programming language that is used for data analysis, web development, and AI. Python is notable for simple to read syntax, a large external library ecosystem, and used broadly in the industry.
# to run the script in python, run python3 name-of-file.py in the terminal. print()is a function that will display text. In the following case, it prints the string shown in quotes. 
print("Welcome to Python")

# variables and data types. a variable is like a container for a data type, it has a unique name and can encode an integer, float (decimal), string, or boolean
# to print a variable. Once the variable has been instantiated or defined, it can be be printed using the print() function. 
#below I define the variables simply using the name of the variable, and setting it to a value using the equal sign and the proper syntax for what it encodes.
name="Chris"
age=58
height=5.0
is_student=True
print("Name: ", name)
print("Age: ", age)
print("Height: ", height)
print("Is a student: ", is_student)
# Create variables for your favorite movie, year released, and rating (out of 10).
movie = "Airplane"
release_year= 1976
rating= 8.2
# Print the variables
print("Movie: ", movie)
print("Release Year: ", release_year)
print("Rating: ", rating)
# Print these variables, using a slightly different syntax
print(f"My favorite movie of all time is {movie} released in {release_year}. I'd give it a {rating}")

# LISTS AND INDEXING
# Lists are a specific data structure to python, where a variable is set to multiple items, each one accessible by it's place in the list. 
# the syntax for a list is list=["turn1", "turn2", "turn3", "turn4"], note that each item is in quotes and separated from the previous one with a comma.
# to access a particular list item, print the variable name followed by [] with the item position, remembering that the first item is accessed with [0].
colors=["purple", "magenta", "royal blue", "kelly green", "yellow (hued towards mustard)", "red", "red","red", "teal"]
print("First Color is ", colors[0])
# Add another color to the list...simply by stating the list name, followed by .append("new item")
colors.append("rust")
print(colors)
# python functions
#insert a new item at a specific position
colors.append("teal")	# Adds an element at the end of the list
colors_copy=colors.copy()	# Returns a copy of the list
colors.count("red")	# Returns the number of elements with the specified value
# extend()	# Add the elements of a list (or any iterable), to the end of the current list
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)
print(colors.index("teal"))	# Returns the index of the first element with the specified value
# insert()	# Adds an element at the specified position
# print(colors.insert(0, "orange") )
# print(colors.pop(4)	)# Removes the element at the specified position

print(colors.reverse())	# Reverses the order of the list
colors.sort()	# Sorts the list
colors.extend(fruits)
# colors.clear()	# Removes all the elements from the listprint(colors)
# print(colors_copy)
print(f"now colors are {colors}")

colors.remove("red")	# Removes the first item with the specified value
print(colors)
# 2. **Interactive Q&A:**
#     - What did you find easy/difficult?
# the print function is so much more intuitive than console.log
# i have come across the single f-string that preceed a template literal, but it's certainly not intuitive. However, it's much simpler than backticks.
#     - How could you use lists in real-life scenarios?
# lists could come in handy for a lot of different use cases. 1. A list could store the names of columns of a table. 2. I know lists are usedin R. Sometimes they're unlisted, sorted, and then relisted. This type of thing is used to calculate sentiment based on text analysis.analysis
# # 3. **Reflection Activity:**
#     - Write 3 key takeaways in your notebook.
# I am guessing that lists are a central data structure in pythion because they are so simple to manipulate. Of course they are also simple because they are unidimensional.

#     - Bonus question: How might you use lists in managing inventory?
# Lists would be very useful for inventory management; each product type contains a list of items. Lists can also be used when identifying categories. 