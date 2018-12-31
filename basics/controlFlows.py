value = 42
#let's check if statements
if (value == 42): print("We found the anwser for everything!!!")
if (value < 43):
    print("multiple")
    print("line in one if")
if (value < 41):
    print("This part will not call")
else:
    print("This part will call in else")
if (value < 41):
    print("This part will not call")
elif (value == 42) :
    print("The value is 42")
else:
    print("This part will call in else")

#let's play with loops
index = 0;
while (index < 10):
    if (index % 2 == 0):
        print("This number is even: " + str(index))
    index = index + 1
else:
    print("This else called when the while cycle finished")

list = ["sajt", "egy", "ketto", "harom"]
for tmp in list:
    print(tmp)

for tmp in range(0, 10):
    print(tmp)
