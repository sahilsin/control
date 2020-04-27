#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 22:55:10 2020

@author: Piyush Kumar Uttam
Released under GNU GPL
"""


import numpy as np
import matplotlib.pyplot as plt



def generaterouth(a):
    sign_changes=0
    marginal=0
    epsilon = 0.000001
    len_a = len(a)
    if(len_a%2 != 0):
        len_l = len_a + 1
    else:
        len_l = len_a
    routh = [[0 for x in range(int(len_l/2))] for y in range(len_a)]
    for i in range(len_l):
        if(i%2 == 0):
            try:
                routh[0][i//2] = a[i]
            except:
                routh[0][i//2] = 0
        else:
            try:
                routh[1][i//2] = a[i]
            except:
                routh[1][i//2] = 0
    print(routh)                                    # creation of the routh array
    for i in range(len_a):
                
        for j in range(int(len_l/2)):
            if(i > 1):
                try:
                    routh[i][j] = -(routh[i-2][0]*routh[i-1][j+1]-routh[i-1][0]*routh[i-2][j+1])/(routh[i-1][0])                 
                except:                            #calculation of the routh array
                    routh[i][j]=0

    for i in range(0,len_a):
        if((routh[i][0])==0):                       #checking for marginality
            print (routh[i][0])
            marginal=1
            break
    if (marginal==0):
        for iter in range(1,len_a):
            if(routh[i-1][0]*routh[i][0]<0):
                sign_changes=sign_changes+1
    routh =np.asarray(routh)
    return routh,sign_changes,marginal





if __name__=="__main__":
    a = [1,6,11,66]
    b, sign_changes, marginal =  generaterouth(a)
    print(b)
    if (sign_changes>0):
        print("System unstable")
        print("Sign changes", sign_changes-1)
    elif (marginal!=0):
        print("System Marginally stable")
    elif (sign_changes==0):
        print("System stable")
        print("Sign changes", sign_changes)
