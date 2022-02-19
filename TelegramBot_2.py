# import telebot
# token = 'Your Token'
# bot = telebot.TeleBot(token)
# word = 'Gleb'
#
# @bot.message_handler(content_types=['text'])
# #bot.send_message(message.chat.id, message.text)
# def echo(message):
#     string = message.text
#     if word in string:
#         bot.send_message(message.chat.id, 'Ба! Какие люди!')
#     else:
#         bot.send_message(message.chat.id, message.text)
#
# bot.polling(none_stop=True)

#Эхо-Бот
import emoji
#print(emoji.emojize("I love you :red_heart:", variant="emoji_type"))
import telebot
token = 'Your Token'
bot = telebot.TeleBot(token)
#word = 'Gleb'
#print('Я эхо-бот и я буду повторять за тобой почти все')
@bot.message_handler(content_types=['text'])
#bot.send_message(message.chat.id, message.text)
def echo(message):
#    string = message.text
    if message.text == 'Gleb':
        bot.send_message(message.chat.id, emoji.emojize("Ба, какие люди!:smiling_face_with_sunglasses:", variant="emoji_type"))
    elif message.text == 'Liza':
        bot.send_message(message.chat.id, emoji.emojize("Привет красотка!!!:red_heart:", variant="emoji_type"))
    else:
        bot.send_message(message.chat.id, message.text)
        bot.send_message(message.chat.id, 'Я эхо-бот и я буду повторять за тобой почти все')
bot.polling(none_stop=True)