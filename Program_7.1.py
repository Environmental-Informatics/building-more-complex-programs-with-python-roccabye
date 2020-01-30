#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 09:55:50 2020
Lab Assignment02
ThinkPython 2e, Chapter 7: Exercise 7.1
This program finds the Square Root of a number by using the famous newton's Method approach
and using the function from 'math' library. And compares the absolute values estimated from the two approach.

@author: tiwari13 (Alka Tiwari)
"""
# Importing the required module
import math
# creating a function to compute sqaure root of 'a' using Newton's method.
def mysqrt(a):                                                            
    x= a/5                                                                #Initial estimate of square root of 'a' 
    while True:                                                            
        y=(x + a/x)/2                                                     # equation to estimate square root using newton's method.
        if abs(y-x)<0.0000001:                                            # the absolute magnitude difference between 'x' and 'y' is set to 0.0000001
            return(x)
            break
        x=y     
def test_square_root():  
    '''  This function tests Newton's method by comparing it with a built in function
         math.sqrt(). And prints a table with number ranging from 1 to 9 and second column 
         gives Newton's method estimate of sqaure root and third column has math.sqrt() estimate
         and fourth colum shows the difference in the magnitude of column two and three to compare
         the estimates from two methods.
    '''
         
    header = ['a', 'mysqrt(a)', 'math.sqtr(a)', 'diff']                   # Creates the header of the table
    print ('{:<8s}{:<30s}{:<30s}{:<30s}'.format(header[0], header[1], header[2], header[3]))
    print ('{:<8s}{:<30s}{:<30s}{:<30s}'.format('-','--------','------------','----')) # to represent --- as shown in table for first row after the header.
   
    for a in range (1,10):                                                # First Column of the table gives vallue of 'a' from 1 to 9
        my_sqrt = mysqrt(a)                                               # Second Column - Finding Square root of 'a' Using Newton's method                     
        math_sqrt = math.sqrt(a)                                          # Third Column - Finding Square root of 'a' Using built in function
        diff = abs(my_sqrt - math_sqrt)                                   # Fourth Column - to compare the estimates. 
        lt = [a, math_sqrt, math_sqrt, diff]                    
        print ('{:<8.1f}{:<30s}{:<30s}{:<30s}'.format(lt[0], str(lt[1]), str(lt[2]), str(lt[3])))
    
test_square_root()



