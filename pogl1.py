import pygame
from pygame.locals import *
from OpenGL.GL import * 
from OpenGL.GLU import * 


# the nodes
verticies = (

    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)

    )


# connections between nodes
edges = (

    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)

    )

def Cube():

    glBegin(GL_LINES)
    
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertices])

    glEnd()

def main():

    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)