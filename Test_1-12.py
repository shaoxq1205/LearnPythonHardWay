# 1. Print HelloWorld
print('Hello, world!')
print('Hello, world!')
print('Hello, world!')
print("I like typing this.")
print("This is fun.")
print('Yay! Printing.')
print("I'd much rather you 'not'.")
print('I "said" do not touch this.')

# 2. Comments

# 3. numbers and maths
print "I will now count my chickens:"

print "Hens", 25 + 30 / 6
print "Roosters", 100 - 25 * 3 % 4
print "Now I will count the eggs:"
print 3/4
print 4/5
print "Is it true that 3 + 2 < 5 - 7?"
print 3 + 2 < 5 - 7
print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7
print "Oh, that's why it's False."
print "How about some more."
print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2
print "Hey %s there." % "you"

# 4. Variables and Names
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven
print "There are %d cars available." %cars
print "There are only %d drivers available." %drivers
print "There will be %d empty cars today." %cars_not_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

# 5. More Variables
my_age = 35  # not a lie
my_height = 74  # inches
my_weight = 180  # lbs
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

# 6. String and Text
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)
print x
print y
print "I said: %r." % x
print "I also said: '%s'." % y
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
print joke_evaluation % hilarious
w = "This is the left side of..."
e = "a string with a right side."
print w + e

# 7. More printing
print "." * 8

# 8. Printing Formatter
formatter = "%s %s %s %s"

print formatter % ('Hello', "World", "Test", "Works")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

formatter2 = "%0.3f %s %s %s"
print formatter2 % (3, 4, 1, 2)

# 9. More Printing
print """
This is a test
about paragraph
Oops
%s %s %s
""" % (1, 2, 3)

print """
Another Test
"""
print formatter2 % (1, 2, 3, 4)

# 10. Some marks
for i in ["/", "-", "|", "\\", "|"]:
    print "%s\r" % i

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
fat_cat = """ I'll do a list: \t* Cat food \t* Fishies
\t* Catnip\n\t* Grass """
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# 11. Input
print "How old are you?"
# age = raw_input()
print "How tall are you?"
# height = raw_input()
print "How much do you weigh?"
# weight = raw_input()

# print "So you are %r old, %r tall, and %r heavy" % (age, height, weight)

# 12. raw_input() prompt
# age = raw_input("How old are you?\n")
# height = raw_input("How tall are you?\n")
# weight = raw_input("How much do you weigh?\n")
# print "So you are %r old, %r tall, and %r heavy" % (age, height, weight)

# 13. Argument Vector, see Test_13_Argv.py
# $python Test_13_Argv.py one two three

# 14. Argument Vector + raw_input(), see Test_14_Argv_raw.py
# $ python Test_14_Argv_raw.py xiaoqiang
