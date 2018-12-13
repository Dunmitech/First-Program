from turtle import *


choice = input("What shape would you like? ")

if choice == "square":
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)

    exitonclick()

elif choice == "triangle":
    forward(100)
    left(120)
    forward(100)
    left(120)
    forward(100)
    left(120)

    exitonclick()

else:
    print("WARNING: your shape has not been recognised")

print()
input("Press return to continue ...")
