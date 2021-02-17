def planets(x):
    for i in range (0,8):
        if number[i] == x:
            return i + 1
    return x + " is not a planet"

number= ["mercury", "venus", "earth", "mars", "jupiter", "saurnn", "uranus", "neptune"]

print (planets("comet"))
