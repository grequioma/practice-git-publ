# Exercise 25: Dictionaries and Functions

# Dictionaries with Variables
color = input("color:")        # "RED"
texture = input("texture:")    # "SMOOTH"
surface = input("surface:")    # "SHINY"

corvette = {
    "color": color,
    "texture": texture,
    "surface": surface
}

print("LITTLE", corvette[input("property to show:")], "CORVETTE")   # original: corvette["color"]

# Dictionaries with Functions

def run():
    print("VROOM")

corvette = {
    "color": input("color:"),
    "texture": input("texture:"),
    "surface": input("surface:"),
    "run": run
}

corvette["run"]()
print("MY", corvette[input("property to show:")], "corvette")   # original: corvette["color"]



