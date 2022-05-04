import colorgram
colors= colorgram.extract('hrist.jpg',30)
#below code will extract list of RGB values from the image
rgb_colors =[]
for color in colors:
    r = color.rgb.r
    g = color.rgb.r
    b = color.rgb.r
    final_rgb_colors = (r,g,b)
    rgb_colors.append(final_rgb_colors)

print(rgb_colors)

#from turtle import Turtle, Screen
import random
import turtle
import turtle as t

t.colormode(255)
#colorlists = [ (199, 199, 199), (124, 124, 124), (210, 210, 210), (168, 168, 168), (222, 222, 222), (186, 186, 186), (6, 6, 6), (109, 109, 109), (113, 113, 113), (22, 22, 22), (64, 64, 64), (39, 39, 39), (76, 76, 76), (9, 9, 9), (90, 90, 90), (181, 181, 181), (132, 132, 132), (210, 210, 210), (141, 141, 141), (179, 179, 179), (172, 172, 172), (212, 212, 212), (176, 176, 176), (150, 150, 150), (202, 202, 202), (40, 40, 40), (46, 46, 46), (47, 47, 47)]
color_list = [(202, 164, 110), (149, 75, 50),
              (222, 201, 136), (53, 93, 123),
              (170, 154, 41), (138, 31, 20),
              (134, 163, 184), (197, 92, 73),
              (47, 121, 86), (73, 43, 35),
              (145, 178, 149), (14, 98, 70),
              (232, 176, 165), (160, 142, 158),
              (54, 45, 50), (101, 75, 77),
              (183, 205, 171), (36, 60, 74),
              (19, 86, 89), (82, 148, 129),
              (147, 17, 19), (27, 68, 102),
              (12, 70, 64), (107, 127, 153),
              (176, 192, 208), (168, 99, 102)]
timmy1 = t.Turtle()
screen = t.Screen()
timmy1.shape("arrow")
timmy1.speed("fastest")

timmy1.pensize(1)
timmy1.setheading(225)
timmy1.penup()
timmy1.forward(300)
timmy1.setheading(0)
number_of_dots = 500


def random_color():
    return random.choice(color_list)


for dot_count  in range(1, number_of_dots):
    print(random_color())
    timmy1.dot(20,random_color())
    timmy1.penup()
    timmy1.forward(50)
    timmy1.pendown()

    if dot_count % 10 == 0:
        timmy1.setheading(90)
        timmy1.penup()
        timmy1.forward(50)
        timmy1.setheading(180)
        timmy1.penup()
        timmy1.forward(500)
        timmy1.setheading(0)



screen.exitonclick()


