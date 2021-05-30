from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title='Make a Bet', prompt='Which turtle will win? Enter a color: ')
colors = ['yellow', 'orange', 'red', 'green', 'blue', 'purple']
y_coordinate = [-100, -60, -20, 20, 60, 100]

all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-240, y=y_coordinate[turtle_index])
    all_turtles.append(new_turtle)

is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:    # checks to see if a turtle has reached the finish line
            is_race_on = False
            winner_turtle = turtle.pencolor()  # get the color of the winner
            if user_bet == winner_turtle:
                print(f"You've Won! {winner_turtle} turtle won the race")
            else:
                print(f"You've Lost! {winner_turtle} turtle won the race")

# randomizing the forward distance each turtle takes
        forward_distance = random.randint(0, 10)
        turtle.forward(forward_distance)

screen.exitonclick()
