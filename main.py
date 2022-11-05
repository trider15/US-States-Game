import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        states_data = pandas.read_csv("50_states.csv")
        missing_states = [state for state in states_data.state if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    else:
        state_turtle = turtle.Turtle()
        state_turtle.hideturtle()
        state_turtle.penup()
        state_data = pandas.read_csv("50_states.csv")
        for state in state_data["state"]:
            if state == answer_state:
                guessed_states.append(state)
                correct_answer_row = state_data[state_data["state"] == state]
                x = int(correct_answer_row["x"])
                y = int(correct_answer_row["y"])
                state_turtle.goto(x, y)
                state_turtle.write(f"{state}")
