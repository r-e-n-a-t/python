# Создайте программу для игры в ""Крестики-нолики"".

import random
import os
import time

def clear():
	os.system('cls')

def symbol(n):
    if n == 1: return '◯' 
    elif n == 2: return '✖'

def showGame(movesList, player):
    nums = list(range(1, 10))
    for i in range(0, 9):
        if movesList[i] == 1: nums[i] = symbol(1)
        elif movesList[i] == 2: nums[i] = symbol(2)
        else: nums[i] = i + 1
    
    clear()
    print("\t\t   ------------------------------------")
    print("\t\t\t    КРЕСТИКИ -- НОЛИКИ")
    print("\t\t   ------------------------------------")
    print("\t\t\t   ____________________")
    print("\t\t\t  |      |      |      | ")
    print("\t\t\t  |  {}   |  {}   |  {}   |".format(nums[0], nums[1], nums[2]))
    print("\t\t\t  |______|______|______|")
    print("\t\t\t  |      |      |      | ")
    print("\t\t\t  |  {}   |  {}   |  {}   |".format(nums[3], nums[4], nums[5]))
    print("\t\t\t  |______|______|______|")
    print("\t\t\t  |      |      |      | ")
    print("\t\t\t  |  {}   |  {}   |  {}   |".format(nums[6], nums[7], nums[8]))
    print("\t\t\t  |______|______|______|")
    print("\t\t   ------------------------------------")
    print("\t\t\t     Вы играете за {}".format(symbol(player)))
    print("\t\t   ------------------------------------")
    print()

def playerChoise():
    player = 0
    clear()
    while player > 2 or player < 1:
        try:
            print("\t\t   ------------------------------------")
            print("\t\t\t    КРЕСТИКИ -- НОЛИКИ")
            print("\t\t   ------------------------------------")
            print("\t\t\t      1 - ◯     2 - ✖")
            player = int(input("\t\t\t За кого будете играть? = "))
        except ValueError:
            clear()
            print("\t\t\t    Вы ввели не число!")
            time.sleep(0.5)
        if 0 < player < 3:
            comp = 1 if player == 2 else 2
            rand = random.randrange(0, 2)
            print("\t\t Первый ходит - {} ".format(symbol(2)))
            return player, comp, bool(rand)
        else:
            clear()
            print("\t\tНекорректный ввод. Введите число от 1 до 2.")
            time.sleep(0.5)

def mover(player, movesList):
    valid = False
    while not valid:
        try:
            move = int(input("\t\t\t       Ваш ход? = "))
        except:
            print("\t\t\t    Вы ввели не число!")
            continue
        if 0 < move < 10:
            if (movesList[move - 1] == 0):
                movesList[move - 1] = player
                valid = True
            else:
                print ("Эта клетка уже занята")
        else:
            print("\t\tНекорректный ввод. Введите число от 1 до 9.")

def check(movesList):
    coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    for i in coord:
        if movesList[i[0]] == movesList[i[1]] == movesList[i[2]] and movesList[i[0]] != 0:
            return movesList[i[0]]
    return False

def win(movesList, s):
    res = False
    for i in range(9):
        if movesList[i] == 0:
            movesList[i] = s
            if check(movesList) == s: res = i
            movesList[i] = 0
    return res

def computer_move(movesList, comp, player):
    time.sleep(0.3)
    move = -1
    if win(movesList, comp):
        move = win(movesList, comp)
    elif win(movesList, player):
        move = win(movesList, player)
    else:
        while move == -1:
            x = random.randrange(9)
            if movesList[x] == 0:
                move = x
    movesList[move] = comp

def game():

    movesList = [0 for i in range(1, 10)]
    player, comp, playerMove = playerChoise()
    play = True
    count = 0
    showGame(movesList, player)

    while count < 9:
        if playerMove:
            mover(player, movesList)
            showGame(movesList, player)
            playerMove = False
        else:
            computer_move(movesList, comp, player)
            showGame(movesList, player)
            playerMove = True
        if check(movesList): break
        count += 1
        
    if check(movesList):
        if check(movesList) == player:
            showGame(movesList, player)
            print("\t\t\t       Вы выиграли!")
            print("")
        else:	
            showGame(movesList, player)
            print("\t\t     Вы проиграли! Попробуйте еще раз")
            print("")
    if count == 9: 
        showGame(movesList, player)
        print("\t\t\t\t  Ничья!")
        print("")
game()