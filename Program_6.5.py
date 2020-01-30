#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 09:55:00 2020
Lab Assignment02
ThinkPython 2e, Chapter 6: Exercise 6.5
This program computes the greatest commom divisor of 'a' and 'b'. 
The GCD is the largest number that divides both the numbers 'a' and 'b'.
If 'r' is the remainder when 'a' is divided by 'b', then GCD(a,b) = GCD(b,r)

@author: tiwari13 (Alka Tiwari)
"""
#function to compute greatest commomn divisor of two integers a and b.
def GCD(a,b):
    if b == 0: 
        return a
    else:
        r = a%b
        return GCD(b,r)                    # GCD(a,b) = GCD(b,r)
#function to give input for GCD function
def GCD_input():
    a= int(input("Enter a: "))             # input the integer value of 'a'
    b= int(input("Enter b: "))             # input the integer value of 'b'
    print("GCD= ", GCD(a,b))

GCD_input() 

