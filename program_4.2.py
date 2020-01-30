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
import turtle

def petal(t, r, angle):
    """Draws a petal using two arcs.
    t: Turtle
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs
    """
    for i in range(2):
        arc(t, r, angle)
        lt(t, 180-angle)

def flower(t, n, r, angle):
    """Draws a flower with n petals.
    t: Turtle
    n: number of petals
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs
    """
    for i in range(n):
        petal(t, r, angle)
        lt(t, 360.0/n)

def draw_flower(t, length):
    """Move Turtle (t) forward (length) units without leaving a trail.
    Leaves the pen down.
    """
    pu(t)
    fd(t, length)
    pd(t)

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

# draw a sequence of three flowers, as shown in the book.
#draw flower with 7 petals
draw_flower(bob, -100) 
flower(bob, 7, 60.0, 60.0)

#draw flower with 10 petals
draw_flower(bob, 100)
flower(bob, 10, 40.0, 80.0)

#draw flower with 20 petals
draw_flower(bob, 100)
flower(bob, 20, 140.0, 20.0)

    
