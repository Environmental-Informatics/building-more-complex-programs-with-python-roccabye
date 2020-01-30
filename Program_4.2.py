#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 09:53:16 2020
Lab Assignment02
ThinkPython 2e, Chapter 4: Exercise 4.2
This Program draws three flowers with different number (7,10 and 20 number) of petals by using the "Turtle" module.

@author: tiwari13 (Alka Tiwari)
"""
# Importing required modules.
import numpy as np
import turtle
bob = turtle.Turtle()

def polyline(t, length, n, angle):
    for i in range(n):
        t.fd(length)                                                          # to draw forward length
        t.lt(angle)                                                           # for left turn angle input
        
def arc(t, r, a):
    arc_length = 2*np.pi*r*(abs(a)/360.0)
    n = int(arc_length/4)+3                                                   # to find the number of increments and add three 
    length = arc_length/n                                                     # to find increment in drawing length 
    angle = a/n                                                               # to find increment in turning angle 
    t.lt(angle/2)                                                             # to minimise linear approximation error
    polyline(t, length, n, angle)                                             
    t.rt(angle/2)                                                             # increment to draw an arc
        
def petal(t, r, a):
    """Draws a petal using two arcs.
    t: Turtle
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs
    """
    for i in range(2):                                                        # to draw two arcs of a petal
        t.lt(180-a)                                                           # to draw arc in opposite direction
        arc(t, r, a)
        

def flower(t, n, r, a):
    """Draws a flower with n petals.
    t: Turtle
    n: number of petals
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs
    """
    for i in range(n):
        petal(t, r, a)
        t.lt(360.0/n)
    
def draw_flower(t, length):
    """Move Turtle (t) forward (length) units without leaving a trail.
    Leaves the pen down.
    """
    t.pu()
    t.fd(length)
    t.pd()

# draw a sequence of three flowers, as shown in the book.
#draw flower with 7 petals
draw_flower(bob, -200) 
flower(bob, 7, 60.0, 60.0)

#draw flower with 10 petals
draw_flower(bob, 120)
flower(bob, 10, 40.0, 80.0)

#draw flower with 20 petals
draw_flower(bob, 120)
flower(bob, 20, 140.0, 20.0)
turtle.mainloop()                                                             # wait until user close it
    

