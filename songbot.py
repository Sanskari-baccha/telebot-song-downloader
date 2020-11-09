token='1498024006:AAEd5NWvoK9GxZF0z4aHHggQa_zaWNF9T5A'
import telepot
import time
from telepot.loop import MessageLoop
from main import *
bot=telepot.Bot(token)
# def handle(msg):
#     chat_id=msg['chat']['id']
#     cmd=msg['text']
#     #    if cmd=='/download':
#     rep=bot.getUpdates()
#     req=rep['text']
#     print 'got this song name %s' %req
#     tmp=get_link(cmd)
#     fname=get_filename(cmd)
#     # bot.sendMessage(chat_id,'Got ur file ka link '+tmp)
#     download(tmp,fname)
#     audio=open(fname+'.mp3','rb')
#     bot.sendAudio(chat_id,audio)

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
            bot.sendMessage(chat_id, msg['text'])
            print 'got this song name'
            tmp=get_link(msg['text'])
            fname=get_filename(msg['text'])
            # bot.sendMessage(chat_id,'Got ur file ka link '+tmp)
            download(tmp,fname)
            audio=open(fname+'.mp3','rb')
            bot.sendAudio(chat_id,audio)
    

MessageLoop(bot,handle).run_as_thread()
while 1:
    time.sleep(10)
