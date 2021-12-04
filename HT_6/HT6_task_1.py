#1. Traffic light program.
# Create a traffic light emulator program for cars and pedestrians.
# After launching the program, the color of the car is displayed in the l
# eft half, and the color of the pedestrian traffic light in the right half.
# The current colors are displayed every second. After a few iterations - there
# is a change of colors - the logic is the same as in conventional traffic lights.
#   The approximate result of the work is as follows:
#          Red        Green
#          Red        Green
#          Red        Green
#          Red        Green
#          Yellow     Green
#          Yellow     Green
#          Green      Red
#          Green      Red
#          Green      Red
#          Green      Red
#          Yellow     Red
#          Yellow     Red
#          Red        Green
#          .......

from time import sleep

color_auto = ["Red", "Yellow", "Green"]
color_walk = ["Red", "Green"]

while True:
    for _ in range(4):
        print(f"{color_auto[0]:<12} {color_walk[1]}")
        sleep(1.2)
    for _ in range(2):
        print(f"{color_auto[1]:<12} {color_walk[1]}")
        sleep(1.2)
    color_auto = color_auto[::-1]
    color_walk = color_walk[::-1]
