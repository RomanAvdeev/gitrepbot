import telebot;
import datetime
import smtplib
from string import punctuation, whitespace
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

bot = telebot.TeleBot('1644775683:AAHq-BTszg4jho8eGs9qYFBn4S9T8T-advo');

def first_word(s):
    to_strip = punctuation + whitespace
    return s.lstrip(to_strip).split(' ', 1)[0].rstrip(to_strip)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Здравствуйте, {message.from_user.first_name}.')
    bot.reply_to(message, f'Напишите Ваш вопрос, и мы Вам поможем!. Пожалуйста, первым словом укажите адрес Вашей электронной почты, затем поставьте пробел,напишите номер Вашего мобильного телефона и вопрос')

@bot.message_handler(content_types=['text'])
def send_email(message):
    try:
        username = "{0.username}".format(message.from_user, bot.get_me())
        add = message.text;
        toaddr = add.split()[0]
        substr = '@'
        if substr in toaddr:
            fromaddr="roma.avdeyev@gmail.com"
            password='RomariO2002LIT'
            msg=MIMEMultipart()
            msg['From']=fromaddr
            msg['to']=toaddr
            msg['Subject']="Отправитель: Telegram bot"
            body="Message:Telegram bot \n" + "Заказчик:" + toaddr + "\n\n" +  message.text
            msg.attach(MIMEText(body,'plain'))
        
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(fromaddr, password)
            text = msg.as_string()
            server.sendmail(toaddr,fromaddr, text)
            server.quit()
        
            bot.reply_to(message, "Заявка успешно отправлена")
        else:
            bot.reply_to(message, "Ошибка, введено неверное имя почтового ящика")

    except Exception:
        bot.reply_to(message, "Ошибка, проверьте корректность отправляемого сообщения или воспользуйтесь формой подачи заявки на сайте")
        
bot.polling(none_stop=True)










