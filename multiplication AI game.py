# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 16:43:46 2022

@author: snazm
"""
from sys import exit
from copy import deepcopy
CurrentVal = 1



def multiply(mark, multiplier):
    global CurrentVal
    previous_val = CurrentVal
    CurrentVal = CurrentVal * multiplier
    #Mark_update.append(mark)
    #CurrentVal = value
    if CheckforWin():
        if mark == 'h':
            print(f'Human takes = {multiplier} # Previous value is = {previous_val} ##  multiplied Result is = {CurrentVal}')
            print("\n\n                 Human Wins!\n\n")
            #exit()
        else:
            print(f'Computer takes = {multiplier} # Previous value is = {previous_val} ## multiplied Result is = {CurrentVal}')
            print("\n\n                 Computer Wins!\n\n ")
            #exit()
        return 1

def HumanMove():
    global CurrentVal
    num = int(input("## Human : "))
    if num == 2 or num == 3 or num == 5 or num == 7 or num == 9:
        previous_val = CurrentVal
        res = multiply(human, num)
        if res:
            return 
        else:
            print(f'## Human takes = {num} # Previous value is = {previous_val} multiplied Result is = {CurrentVal}')
        
    else:
        print(" Your enter wrong number!! Again Enter 2, 3, 5, 7 or 9 ", end=' ')
        HumanMove()
        



def comp():
    checking = []
    bestScore = -800
    bestValue = 0
    #for key in board.keys():
    global CurrentVal
    tempVal = deepcopy(CurrentVal)
    
    for key in multiplier:
        #if (board[key] == ' '):
            #board[key] = bot
        tempVal = tempVal * key
        checking.append('c')
        score = minimax(tempVal, 0, False, checking)       
        tempVal = tempVal / key
        checking.pop()
        if (score > bestScore):
            bestScore = score
            bestValue = key

    #insertLetter(bot, bestMove)
    return bestValue



def minimax(tempVal , depth, isMaximizing , checking):
    if (checkWhichMarkWon_Bot(tempVal,checking)):
        return 1
    elif (checkWhichMarkWon_Human(tempVal,checking)):
        return -1
    
    if (isMaximizing):
        
        bestScore = -800
        # max node
        for key in multiplier:
            tempVal = tempVal * key
            checking.append('c')
            score = minimax(tempVal, depth + 1, False, checking)
            tempVal = tempVal / key                                     
            checking.pop()
            if (score > bestScore):
                bestScore = score
        return bestScore

    else:
        bestScore = 800
        # min node
        for key in multiplier:
            tempVal = tempVal * key
            checking.append('h')
            score = minimax(tempVal, depth + 1, True , checking)
            tempVal = tempVal / key
            checking.pop()
            if (score < bestScore):
                bestScore = score
        return bestScore


def CompMove():
    global CurrentVal
    num = comp()
    if num == 2 or num == 3 or num == 5 or num == 7 or num == 9:
        previous_val = CurrentVal
        res = multiply(bot, num)
        if res:
            return
        else:
            print(f'Computer takes = {num} # Previous value is = {previous_val} ## multiplied Result is = {CurrentVal}')
        
    else:
        print(" Computer enter wrong number!! Again Enter 2, 3, 5, 7 or 9 ", end=' ')
        CompMove()

def CheckforWin():
    if CurrentVal >= Target:
        return True
    else:
        return False

def checkWhichMarkWon_Bot(tempVal,checking):
    if tempVal >= Target and checking[-1] == 'c':
        return True

def checkWhichMarkWon_Human(tempVal,checking):
    if tempVal >= Target and checking[-1] == 'h':
        return True
    
def instruction():
    global Target
    print("\nEach Step human and Computer Enter 2 , 3, 5, 7, 9. Whoever cross the target first , win the match.")
    Target = int(input("Enter the target value: "))
    print(f"\nTarget Value is {Target} and initial Value is = {CurrentVal}\n")
    
human = 'h'
bot = 'c'
multiplier = [2, 3, 5, 7, 9]

play_again = True


while play_again:
    instruction()
    while not CheckforWin():
        CompMove()
        if not CheckforWin():
            HumanMove()
    
    yes_no= input("Do you want to play again ?(y/n): ")
    if yes_no == 'n' or yes_no == 'N':
        play_again = False
    elif  yes_no == 'y' or yes_no == 'Y':
        CurrentVal = 1
    else:
        print("          Invalid input. Please try again. Thank You !!!!     ")
        exit()
        
    
