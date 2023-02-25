# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 13:22:27 2020

@author: Brian
"""
size = int(input("Please enter how many square feet of the wall space "))
paint = int(input("Please enter the price of the paint you are using "))

def gallons():
    amountOfPaint = size / 112 * 1
    costOfPaint = amountOfPaint * paint
    laborHours = size / 112 * 8
    laborCost = laborHours * 35.00
    grandTotal = costOfPaint + laborCost
    output(amountOfPaint, costOfPaint, laborHours, laborCost, grandTotal)

def output(amountOfPaint, costOfPaint, laborHours, laborCost, grandTotal ):
    print('You need ', format(amountOfPaint, '.2f'), 'gallons of paint')
    print('It will take ', format(laborHours, '.2f'), 'hours to paint')
    print('The paint will cost $', format(costOfPaint, '.2f'))
    print('The labor will cost $', format(laborCost, '.2f'))
    print('The total cost is $', format(grandTotal, '.2f'))


gallons()