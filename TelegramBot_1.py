import telebot
token = '5130894463:AAHE_3wRuK7-dxNmXyC57aXXbi46Y_bE2Ws'
bot = telebot.TeleBot(token)
word = 'Gleb'
@bot.message_handler(content_types=['text'])
#bot.send_message(message.chat.id, message.text)
def echo(message):
    string = message.text
    if word in string:
        bot.send_message(message.chat.id, 'Ба! Какие люди!')

    else:
        bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)