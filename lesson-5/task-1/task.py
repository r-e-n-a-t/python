# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

import random
import os
import time

def clear():
	os.system('cls')

def showGame(candies, player, player_2):
    amount = candies[0]
    amount_1 = ''
    if candies[1] < 9: amount_1 = ' {}     '.format(candies[1])
    elif candies[1] < 99: amount_1 = ' {}    '.format(candies[1])
    elif candies[1] < 999: amount_1 = ' {}   '.format(candies[1])
    elif candies[1] < 9999: amount_1 = ' {}  '.format(candies[1])
    clear()
    print("\t\t   ------------------------------------")
    print("\t\t\t      ИГРА В КОНФЕТЫ")
    print("\t\t   ------------------------------------")
    print("\t\t    Игрок 1 ▕▔╲┈╱▔▔▔▔▔▔▔▔╲┈╱▔▏ Игрок 2")
    if amount < 10:
        print("\t\t\t    ▕╯ ▕    {}    ▕  ╯▏".format(amount))
    elif amount < 100:
        print("\t\t\t    ▕╯ ▕    {}   ▕  ╯▏".format(amount))
    elif amount < 1000:
        print("\t\t\t    ▕╯ ▕   {}   ▕  ╯▏".format(amount))
    elif amount < 10000:
        print("\t\t\t    ▕╯ ▕   {}  ▕  ╯▏".format(amount))
    print("\t\t   {}  ▕▂╱┈╲▂▂▂▂▂▂▂▂╱┈╲▂▏ {}".format(amount_1, candies[player_2]))
    print("\t\t   ------------------------------------")
    if player < 3: print("\t\t\t       Ходит игрок {}".format(player))
    else: print("\t\t\t        Ходит бот ")
    print("\t\t   ------------------------------------")
    print()

def playerChoise():
    players = 0
    clear()
    while players > 2 or players < 1:
        try:
            print("\t\t   ------------------------------------")
            print("\t\t\t      ИГРА В КОНФЕТЫ")
            print("\t\t   ------------------------------------")
            print()
            print("\t\t\t     1 - ◯     2 - ◯")
            print()
            players = int(input("\t\t\t   Сколько игроков? = "))
        except ValueError:
            clear()
            print("\t\t\t    Вы ввели не число!")
            time.sleep(1)
        if 0 < players < 3:
            rand = random.randrange(1, 3)
            if players == 1:
                print()
                print("\t\t\t Вы выбрали игру с ботом - {} ".format(rand))
                print("\t\t\t Первым ходит - {} ".format('бот' if rand == 2 else "игрок 1"))
                time.sleep(2)
                return 1, 3, players if rand == 1 else 3
            if players == 2:
                print()
                print("\t\t\t Вы выбрали игру на двоих - {} ".format(rand))
                print("\t\t\t Первым ходит - {} ".format('игрок 2' if rand == 2 else "игрок 1"))
                time.sleep(2)
                return 1, 2, rand
        else:
            clear()
            print("\t\tНекорректный ввод. Введите число от 1 до 2.")
            time.sleep(1)

def mover(amount):
    valid = False
    while not valid:
        try:
            move = int(input("\t\t\t Сколько берете конфет? = "))
        except:
            print("\t\t\t    Вы ввели не число!")
            continue
        if 0 < move < 29:
            if (move <= amount):
                valid = True
                return move
            else:
                print("\t\tСтолько конфет нет")
        else:
            print("\t\tНекорректный ввод. Введите число от 1 до 28.")

def computer_move(amount):
    if amount <= 28: 
        print("\t\t\t      Бот взял = {}".format(amount))
        time.sleep(1.5)
        return amount
    else:
        while True:
            x = random.randrange(1, 29)
            if x <= amount:
                print("\t\t\t      Бот взял = {}".format(x))
                time.sleep(1.5)
                return x
    
def game():
    candies = [2021, 0, 0, 0]
    player_1, player_2, playerMove = playerChoise()
    showGame(candies, playerMove, player_2)

    while candies[0] > 0:
        if playerMove == player_1:
            showGame(candies, playerMove, player_2)
            move = mover(candies[0])
            candies[player_1] += move
            candies[0] = candies[0] - move
            playerMove = 3 if player_2 == 3 else 2
        elif playerMove == 2:
            showGame(candies, playerMove, player_2)
            move = mover(candies[0])
            candies[2] += move
            candies[0] = candies[0] - move
            playerMove = player_1
        elif playerMove == 3:
            showGame(candies, playerMove, player_2)
            move = computer_move(candies[0])
            candies[3] += move
            candies[0] = candies[0] - move
            playerMove = player_1

        
    
    showGame(candies, playerMove, player_2)
    if playerMove > 1:
        print("\t\t\t     Выиграл игрок - {}".format(player_1))
    elif player_2 == 2:
        print("\t\t\t     Выиграл игрок - {}".format(player_2))
    else:
        print("\t\t\t       Выиграл бот")
    print("")
game()