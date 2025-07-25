print("Good Evening, World!\n\n")
# Exercise-4
print("Exercise 4: Variables and Names",end="\n\n")
cars=100
space_in_a_car=4.0
drivers=30
passengers=90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
print("\n")
# Exercise-5
print("Exercise 5: More Variables and Printing",end="\n\n")
my_name='Zed A. Shaw'
my_age=35 # not a lie
my_height=74 # inches
my_weight=180 # lbs
my_eyes='Blue'
my_teeth='White'
my_hair='Brown'
print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")
# this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")
print("\n")
# Exercise-6
print("Exercise 6: Strings and Text",end="\n\n")
types_of_people = 10
x = f"There are {types_of_people} types of people."
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."
print(x)
print(y)
print(f"I said: {x}")
print(f"I also said: '{y}'")
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
print(joke_evaluation.format(hilarious))
w= "This is the left side of..."
e = "a string with a right side."
print(w + e)
print("\n")
# Exercise-7
print("Exercise 7: More Printing",end="\n\n")
print("Mary had a little lamb.")
print("Its fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.")
print("." * 10)  # what'd that do?
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"
# watch end = ' ' at the end. try removing it to see what happens
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)
print("\n")
# Exercise-8
print("Exercise 8: Printing, Printing",end="\n\n")
formatter = "{} {} {} {}"
print(formatter.format(1,2,3,4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "own text here",
    "Maybe a poem",
    "Or a song about fear"
))
print("\n")
# Exercise-9
print("Exercise 9: Printing, Printing, Printing",end="\n\n")
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\Jul\nAug"
print("Here are the days: ", days)
print("Here are the months: \n", months) 
print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")
print("\n")
# Exercise-10
print("Exercise 10: What Was That?",end="\n\n")
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
print("\n")
# Exercise-11
print("Exercise 11: Asking Questions",end="\n\n")
print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()
print(f"So, you're {age} old, {height} tall and {weight} heavy.")
print("\n")
# Exercise-12
print("Exercise 12: Prompting People",end="\n\n")
age = input("How old are you? ")
height = input("How tall are you? ")
weight = input("How much do you weigh? ")
print(f"So, you're {age} old, {height} tall and {weight} heavy.")
print("\n")
