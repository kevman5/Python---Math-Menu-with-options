# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 16:08:37 2021

@author: kevmm
"""
list1 = []
def NewList():
        list2 = []
        num = 3
        while num != -1:
            num = int(input("Input next number (-1 to quit) :"))
        if num != -1:
            list2.append(num)
        return list2
def printlist():
    print(list1)
    
def delete_element():
    print(list1)    
    choice = int(input("Which index (starts at 0!): "))
    list1.remove(choice)

def findmedian():
    if len(list1) % 2 == 1:
        print(list1[2:2])
        
def findavg():
    if len(list1) % 2 == 0:
            ans1 = list1[1 + 2 + 3 + 4]
            
            print(ans1)
        
def listmenu():
        print("\n\n")
        print("1: Build list")
        print("2: Print list")
        print("3: Delete an element")
        print("4: Find median")
        print("5: Find avg")
        print("9 to exit")
        choice = int(input("Pick a number: "))
        return choice
    

ch = 2
while (ch != 9):
    ch = listmenu()
    if ch == 1:
            list1 = NewList()
    elif ch == 2:
            printlist()
    elif ch == 3:
            delete_element()
    elif ch == 4:
            findmedian()


list1.sort()


    