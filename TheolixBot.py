from telegram.ext import Updater

def star (bot,update):
    update.message.reply_text("saya Bot, Halo")

def main ():
    updater = Updater (token='2121092421:AAElnFg4Cc_8gU-QBOIS-V4z7ibHM20DOuM')
    dispatcher = updater.dispatcher
    print ("bot started")

if __name__=='__main__':
    main()