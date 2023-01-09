from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

s = Screen()
s.bgcolor("black")
s.setup(width=800, height=600)
s.title("Pauly's Pong Game")
s.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

s.listen()
s.onkey(r_paddle.go_up, "Up")
s.onkey(r_paddle.go_down, "Down")
s.onkey(l_paddle.go_up, "w")
s.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
     time.sleep(ball.move_speed)
     s.update()
     ball.move()

     #detect collision with wall
     if ball.ycor() > 280 or ball.ycor() < -280:
          ball.bounce_y()

     #detect colllision with r_paddle
     if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
          ball.bounce_x()


     #detect when r_paddle misses
     if ball.xcor() > 380:
          ball.reset_position()
          scoreboard.l_point()
          print()

     # detect when r_paddle misses
     if ball.xcor() < -380:
          ball.reset_position()
          scoreboard.r_point()


s.exitonclick()