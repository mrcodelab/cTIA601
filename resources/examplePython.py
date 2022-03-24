menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

"""
Challenge:
print out all the meals with 'spam' removed
result 1: remove spam from each list then print the list
result 2: print the items in each list excluding spam
output: a nested list without spam
"""

print("round1 start")
# my first solution to the challenge
for meal in menu:
    if "spam" not in meal:
        print(meal)

    for meal in menu:
        if "spam" in meal:
            meal.remove("spam")

print("round1 done")
print("*" * 80)

print("round2 start")
# my second solution to the challenge
for meal in menu:
    if meal != "spam":
        print(list(meal))
    else:
        print("it was spam")

print("round2 end")

print("*" * 80)
###########################################################
print("The 1st solution:")
for meal in menu:
    for index in range(len(meal) - 1, -1, -1):
        if meal[index] == "spam":
            del meal[index]

    print(meal)
print("end 1st solution")

print("*" * 80)
###########################################################
print("2nd solution:")
for meal in menu:
    for item in meal:
        if item != "spam":
            print(item)
    print()

print("end 2nd solution")
