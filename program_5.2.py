#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 09:54:14 2020
Lab Assignment02
ThinkPython 2e, Chapter 5: Exercise 5.2
This Program defines the Fermat's Last Theorem which states that for no positive integer 'a', 'b', and 'c' 
and for any value of 'n' > 2, does the equation a^n+b^n=c^n holds true. In Part 1 this theorem has been checked whether it is true or not. 
In part 2, the integer values for the parameters are provided to check the Fermat's Last Theorem.

@author: tiwari13 (Alka Tiwari)
"""
#Part 1

def check_fermat(a,b,c,n) :
    ''' This function defines the four parameters a,b,c,n 
        and checks for n > 2; a^n + b^n = c^n holds true for
        no positive integer value of a,b and c.
    '''
      
    if n<=2 :                                                                # Checks if n is integer value and greater than 2
        print('Sorry, n must be integer and greater than 2')
    
    else:
        for val in a, b, c:                                                  # Checks if a, b, c are positive integers
            if val<0 or (isinstance(val, int)) != True:
                print('Sorry, %.2f must be a possitive integer' %(val))
                break
        else:                                                                # Calculates Fermat's Last theorem's equation.
            if a**n + b**n == c**n:                        
                print ('Holy smokes, Fermat was wrong!')
            else:
                print ("No, that doesn't work")
           
# Part 2

def fermat_inputs():
    ''' Input values for a,b,c,n 
        converts them to integers and checks Fermat's last theorem'''
          
    print("\nFermat's Last Theorem: \n\n\
          says that there are no positive integers a, b, and c, such that:\n\
                              a^n + b^n = c^n \n\
                      for any value of n greater than 2.\n")
    a= float(input("Enter value for a: "))
    a=int(a)
    b= float(input("Enter value for b: "))
    b=int(b)
    c= float(input("Enter value for c: "))
    c=int(c)
    n= float(input("Enter value for n: "))
    n=int(n)    
    check_fermat(a,b,c,n)                                                    # Checks if Fermat's Last theorem holds
      
fermat_inputs()

