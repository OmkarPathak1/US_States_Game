import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

user_name = screen.textinput(title="Guess the State Game",
                             prompt="Enter your name below").title()

data = pandas.read_csv("50_states.csv")
states_name = data["state"].tolist()

guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title="Guess the State",
                                    prompt="Enter the name of all the states in below textbox.").title()

    if answer_state in states_name:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

    if answer_state == "Exit":
        missing_states = []
        for state in states_name:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv(f"{user_name}_file.csv")
        break
screen.exitonclick()
