from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

def game():

    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("#E4E6AC")
    screen.title("Welcome to Snake Game!")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")


    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # Detect collision with wall
        if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
            scoreboard.game_over()
            game_is_on = False
            again = screen.textinput("Want to play again?", "Y / N")

            if again in ("y", "Y"):
                game_is_on = True
                screen.clear()
                screen.bgcolor("#E4E6AC")
                game()
            else:
                exit()

        # Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.game_over()
                game_is_on = False
                again = screen.textinput("Want to play again?", "Y / N")

                if again in ("y", "Y"):
                    game_is_on = True
                    screen.clear()
                    screen.bgcolor("Black")
                    game()
                else:
                    exit()

    screen.exitonclick()


game()