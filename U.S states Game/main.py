import turtle
from turtle import Turtle
import pandas

screen = turtle.Screen()
screen.setup(height=491, width=725)
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# read the csv file
data = pandas.read_csv("50_states.csv")
all_states = data["state"].tolist()

correct_answers_list = []  # lists of the correct states typed
correct_states_score = 0  # keeps track of score
missing_states = []  # keeps the states user couldn't answer
total_states = len(all_states)

while len(correct_answers_list) < 50:
    answer_state = screen.textinput(title=f"{correct_states_score}/{total_states} Guess the state",
                                    prompt="What's another state name").title()
    states_data = data[data.state == answer_state]  # getting states row

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in correct_answers_list]

        print(missing_states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        correct_answers_list.append(answer_state)
        correct_states_score += 1
        t = Turtle()  # whenever user guesses right a turtle is created
        t.hideturtle()
        t.penup()
        t.goto(int(states_data.x), int(states_data.y))
        t.write(states_data.state.item())

    # to update missing_states[]

# creating states_to_learn.csv to store states that not in correct_

# for s in states_data:
#     if answer_state == s:
#         correct_states_typed += 1
#         correct_answers_list.append(answer_state_titleCase)
#         input_write.goto(int(xcor, ycor))
#         input_write.write(answer_state)


# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
screen.exitonclick()  # keeps the screen open
