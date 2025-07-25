# Exercise-19
print("Exercise 19: Functions and Variables", end="\n\n")
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man, that's enough for a party!")
    print("Get a blanket.\n")
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)
print("OR, we can use variables from our script:")
cheese_amount = 10
cracker_boxes = 50
cheese_and_crackers(cheese_amount, cracker_boxes)
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)
print("And we can combine the two, variables and math:")
cheese_and_crackers(cheese_amount + 100, cracker_boxes + 1000)
print("\n")