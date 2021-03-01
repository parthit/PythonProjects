import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")

image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

guessed_states = []


data = pandas.read_csv("50_states.csv")

while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{50-len(guessed_states)} out of 50 remaining", prompt="'What's another state's name?'").title()

    all_states = data['state'].tolist()

    if answer == 'Exit':
        # missing_states = []
        # for states in all_states:
        #     if states not in guessed_states:
        #         missing_states.append(states)
        # Replaced by list comprehension below
        missing_states = [states for states in all_states if states not in guessed_states]

        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('states_to_learn')

        print(missing_states)
        break
    if answer in all_states:
        guessed_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)

#
# def get_mouse_click(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click)
# turtle.mainloop()
#





screen.exitonclick()