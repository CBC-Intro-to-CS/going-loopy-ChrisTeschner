age = 0
while age <= 16:
    print(age)
    age = age + 2
print("You have reached my age!")

ingredients = ['turkey', 'lettuce', 'mayo', 'tomato']
for ingredient in ingredients:
    print(f"Adding {ingredient}")

print("Your sandwhich is done!")

weight = 70
math_weight = 0.165
rate = 1
moon_weight = weight
for year in range(1,15):
    moon_weight = moon_weight + rate
    print("Year %s = %s" % (year, moon_weight))