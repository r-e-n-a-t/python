from telegram import Update
from telegram.ext import filters, ApplicationBuilder, ContextTypes, MessageHandler, CommandHandler
from random import randrange

def showStats(playerMove, context: ContextTypes):
    candies = context.user_data.get('stats')
    return "Всего конфет: {}\nКонфет у игрока: {}\nКонфет у бота: {}\n\n{}".format(candies[0], candies[1], candies[2], "Ваш ход" if playerMove == 1 else "Ходит бот")

async def start(update: Update, context: ContextTypes):
    context.user_data['stats'] = [222,0,0]
    playerMove = randrange(1, 3)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Игра в конфеты")
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Для остановки игры введите /stop')
    if playerMove == 1:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=showStats(1, context))
    else: 
        await context.bot.send_message(chat_id=update.effective_chat.id, text=showStats(2, context))
        await computer_move(update, context) 

async def stop(update: Update, context: ContextTypes):
    context.user_data['stats'] = [0,0,0]
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Для начала игры введите /start')
 

async def player_move(update: Update, context: ContextTypes):   
    candies = context.user_data.get('stats')
    move = 0
    while move == 0:
        if candies == None or candies[0] == 0: 
            await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Для начала игры введите /start')
            return
        try:
            msg = int(update.message.text) 
            if 0 < msg < 29:
                if (msg <= candies[0]):
                    move = msg
                else:
                    await context.bot.send_message(chat_id=update.effective_chat.id, text='Столько конфет нет!')
                    return
            else:
                await context.bot.send_message(chat_id=update.effective_chat.id, text='Можно брать не больше 28!')
                return
        except Exception:
            await context.bot.send_message(chat_id=update.effective_chat.id, text='Вы ввели не число!')
            return
        
    candies[1] += move
    candies[0] = candies[0] - move
    context.user_data['stats'] = candies
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Вы взяли - {move}")
    await context.bot.send_message(chat_id=update.effective_chat.id, text=showStats(2, context))
    await computer_move(update, context) 

async def computer_move(update: Update, context: ContextTypes): 
    candies = context.user_data.get('stats')
    move = 0  
    if candies[0] == 0: 
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Вы выиграли! :)')
        return
    elif candies[0] < 57 and candies[0] != 29:
        if candies[0] <= 28:
            move = candies[0]
        else: move = candies[0] - 29
    else:
        while move == 0:
            x = randrange(1, 29)
            if x <= candies[0]:
                move = x
    candies[2] += move
    candies[0] = candies[0] - move
    context.user_data['stats'] = candies
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"бот взял - {move}")
    await context.bot.send_message(chat_id=update.effective_chat.id, text=showStats(1, context))
    if candies[0] == 0: await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Вы проиграли! :(')

if __name__ == '__main__':
    application = ApplicationBuilder().token('TOKEN').build()
    start_handler = CommandHandler('start', start)
    stop_handler = CommandHandler('stop', stop)
    num_handler = MessageHandler(filters.TEXT, player_move)
    application.add_handler(start_handler)
    application.add_handler(stop_handler)
    application.add_handler(num_handler)
    application.run_polling()
