"""
Part 2: Visualize Dijkstra Shortest Path Planning
 ----------------------------------------------------------
"""

from dijkstra_module import *
from dijkstra_understand import *

import turtle
import random
import time

t = turtle.Turtle()
t.speed(0)
t.ht()

RADIUS = 25


def generate_vertix_location():

    x = random.randrange(-310, 310, 110)
    y = random.randrange(-300, 300, 100)
    return (x, y)


def generate_vertices_locations(num_vertices):

    if num_vertices < 1:
        print("vertices required")
        print()
        return
    else:
        vertices = []
        while len(vertices) < num_vertices:

            vertix = generate_vertix_location()
            # print(vertix)
            if vertix not in vertices:
                vertices.append(vertix)
            else:
                vertix = generate_vertix_location()
        return vertices


def draw_vertix(x, y, radius, counter):

    t.pu()
    t.pensize(3)
    t.goto(x, y)
    t.pd()
    t.circle(radius)

    msg = "V" + str(counter)
    t.pu()
    t.goto(x, y + radius * 0.6)
    t.write(msg, True, align="center", font=("Arial", 12, "normal"))


def draw_vertices(vertices, radius):
    # Draw vertices

    for counter, vertix in enumerate(vertices):
        draw_vertix(vertix[0], vertix[1], radius, counter)


def draw_broken_line(x1, y1, x2, y2, dist_btwn_vertices):

    t.pu()
    t.pensize(1)
    t.color("red")
    t.goto(x1, y1)
    direction = t.towards(x2, y2)
    distance = t.distance(x2, y2)
    t.setheading(direction)

    steps = int(distance / 20)
    for i in range(steps):
        t.pu()
        t.fd(10)
        t.pd()
        t.fd(10)

    # Add label with distance between vertices
    t.pu()
    t.goto(x1, y1)
    t.setheading(direction)
    t.fd(min(distance * 0.2, 60))
    t.color("blue")
    t.write(str(dist_btwn_vertices), True, align="center", font=("Arial", 10, "normal"))


def draw_path_line(v1, v2, radius, dist_btwn_vertices):

    # first vertix on top of second vertix
    if v1[1] > v2[1]:
        draw_broken_line(v1[0], v1[1], v2[0], v2[1] + 2 * radius, dist_btwn_vertices)

    # first vertix below second vertix
    elif v1[1] < v2[1]:
        draw_broken_line(v1[0], v1[1] + 2 * radius, v2[0], v2[1], dist_btwn_vertices)

    # first vertix right on second vertix
    elif v1[0] > v2[0]:
        draw_broken_line(
            v1[0] - radius,
            v1[1] + radius,
            v2[0] + radius,
            v2[1] + radius,
            dist_btwn_vertices,
        )

    # first vertix left on second vertix
    else:
        draw_broken_line(
            v1[0] + radius,
            v1[1] + radius,
            v2[0] - radius,
            v2[1] + radius,
            dist_btwn_vertices,
        )


def draw_path_lines(vertices, g):

    t.color("red")
    # Draw Path lines
    for column, vertix in enumerate(vertices):
        current_vertix = vertix
        for row, vx in enumerate(vertices):
            if vx != current_vertix:
                if g.graph[column][row] != 0:
                     dist_btwn_vertices = g.graph[column][row]

                    if row > column:
                        draw_path_line(current_vertix, vx, RADIUS, dist_btwn_vertices)


def visualize_graph():

    vertices = generate_vertices_locations(25)
    draw_vertices(vertices, RADIUS)
    draw_path_lines(vertices, g)

    time.sleep(2)
    # Animate visited path from V0 to V4
    print("\nVisited vertices from V0 to V4")
    visited_vertices = find_visited_vertices(paths, 4)
    print(visited_vertices)

    t.color("orange")
    t.seth(0)

    for vx in visited_vertices:
        draw_vertix(vertices[vx][0], vertices[vx][1], RADIUS, vx)
        time.sleep(1.5)

    print("\nCompleted")


visualize_graph()
