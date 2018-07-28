import telebot

bot = telebot.TeleBot("")

print(bot.get_me())

a = 42
b = "qwerty"
print(type(a), type(b))

def log(message, answer):
    print("\n ~~~~~")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1}.(id = {2}) \n Текст - {3}".format(message.from_user.first_name,
                                                                  message.from_user.last_name,
                                                                  str(message.from_user.id),
                                                                  message.text))
    print(answer)


@bot.message_handler(commands=['help'])
def handle_text(message):
    bot.send_message(message.chat.id, """Чем Вам помочь?""")


@bot.message_handler(content_types=['text'])
def handle_text(message):
    answer = "No"
    if message.text == "a":
        answer = "B"
        log(message, answer)
        bot.send_message(message.chat.id, "B")
    elif message.text == "v":
        answer = "R"
        bot.send_message(message.chat.id, "R")
        log(message, answer)
    elif message.text == "1" or message.text == "2":
        bot.send_message(message.chat.id, "3")
    elif message.text == "?" and str(message.from_user.id) == "170120871":
        bot.send_message(message.chat.id, "только этот айди")
    else:
        bot.send_message(message.chat.id, answer)
        log(message, answer)


bot.polling(none_stop=True, interval=0)

