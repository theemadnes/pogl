import pygame
from random import randint
from pygame.locals import *
from OpenGL.GL import * 
from OpenGL.GLU import * 


# the nodes
vertices = (

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

    glBegin(GL_QUADS)
    

    for surface in surfaces:
        #x=0
        for vertex in surface:
            x = randint(0,len(colors)-1)
            glColor3fv(colors[x])
            glVertex3fv(vertices[vertex])

    glEnd()

    glBegin(GL_LINES) # used to encase our drawing stuff
    
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])

    glEnd()

surfaces = (

    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)

    )

colors = (

    (1,0,0),
    (0,1,0),
    (0,0,1),
    (0,0,0),
    (1,0,1),
    (0,1,1),
    (1,1,0),
    (1,1,1)

    )

def main():

    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslate(0.0,0.0,-5)
    glRotatef(20, 0,0,0) # degrees, x,y,x

    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()
                quit()

        glRotatef(1,3,1,1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) # clears the slate
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)

main()
