import asyncio
import telepot
import telepot.async
from thcraw import *
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardHide, ForceReply
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.namedtuple import InlineQueryResultArticle, InlineQueryResultPhoto, InputTextMessageContent

async def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    comando = ''
    f = open("chat_ids.txt", "r")
    if str(chat_id) not in f.read():
        f.close()
        f = open("chat_ids.txt", "a")
        f.write(str(chat_id)+"\n")
        f.close()
    else:
        f.close()
    # pprint.pprint(msg)

    if content_type != 'text' and content_type != 'new_chat_member':
        return
    elif content_type == 'text':
        comando = msg['text'].lower()

    if content_type == 'new_chat_member':
        if msg['new_chat_member']['id'] == 214737879:
            await bot.sendMessage(chat_id, '<code>Hey pessoal do </code><strong>'+msg['chat']['title']+'</strong><code>! '+(u'\U0001f596')+'\nSou o THCbot!\nBot do </code><a href="http://teresinahc.org/">Teresina Hacker Clube</a><code>\nObriago ao </code><strong>'+msg['from']['first_name']+'</strong><code> por me adicionar.\nUsem os comandos ou enviem "</code>/menu<code>"! '+(u'\U0001f603')+'</code>', parse_mode='HTML')
        else:
            await bot.sendMessage(chat_id,'<code>Hey </code><strong>'+msg['new_chat_member']['first_name']+'</strong><code>! '+(u'\U0001f596')+'\nSeja Bem-vindo ao </code><strong>'+msg['chat']['title']+'</strong><code>!\nSou o THCbot!\nBot do </code><a href="http://teresinahc.org/">Teresina Hacker Clube</a><code>!\nUse os comandos ou envie "</code>/menu<code>"! '+(u'\U0001f603')+'</code>', parse_mode='HTML')
        return
    
    if ('/open' in comando or '/close' in comando) and chat_type != 'private':
        await bot.sendMessage(chat_id,'<code>Os comandos "/open" e "/close" devem ser utilizados em "private" comigo, pois preciso de "credenciais" para continuar.</code> '+(u'\U0001f609'),parse_mode='HTML')
        return
    elif '/start' in comando:
        await bot.sendMessage(chat_id,'<code>Hello </code><strong>'+msg['from']['first_name']+'</strong>,<code> sou o THCbot! '+(u'\U0001f596')+'\nBot do </code><a href="http://teresinahc.org/">Teresina Hacker Clube</a><code>\nUse os comandos ou envie "</code>/menu<code>"! '+(u'\U0001f603')+'</code>', parse_mode='HTML')
        return
    elif '/status' in comando:
        await bot.sendMessage(chat_id,"<strong>"+msg['from']['first_name']+"</strong><code>, "+getStatus()+"</code>", parse_mode='HTML')
    elif '/menu' in comando:
        # if chat_type == 'group' or chat_type == 'supergroup':
        #     markup = ReplyKeyboardMarkup(keyboard=[
        #              [KeyboardButton(text='Status (Aberto/Fechado)', callback_data='Status')],
        #              [KeyboardButton(text='Onde fica o THC?')],
        #              [KeyboardButton(text='Projetos')],
        #              [KeyboardButton(text='Agenda Semanal')],
        #              [KeyboardButton(text='Próximos Eventos')]
        #          ], resize_keyboard=True, one_time_keyboard=True)
        # else:
        markup = InlineKeyboardMarkup(inline_keyboard=[
                     [InlineKeyboardButton(text='Status (Aberto/Fechado)', callback_data='Status')],
                     [InlineKeyboardButton(text='Onde fica o THC?', callback_data='Local')],
                     [InlineKeyboardButton(text='Projetos', callback_data='Projetos')],
                     [InlineKeyboardButton(text='Agenda Semanal', callback_data='Agenda')],
                     [InlineKeyboardButton(text='Próximos Eventos', callback_data='Eventos')]
                 ])
        await bot.sendMessage(chat_id,'Selecione qualquer item do menu:', reply_markup=markup)
        return
    elif ('/open' in comando) or ('/close' in comando):
        list_com = comando.split(" ")
        if len(list_com) != 3:
            await bot.sendMessage(chat_id,'<strong>'+msg['from']['first_name']+'</strong><code>, preciso do seu login e senha da Wiki do THC, então, envie o comando "</code>'+list_com[0]+'<code>" neste padrão:\n</code>'+list_com[0]+'<code> meulogin minhasenha</code>', parse_mode="HTML")
        elif len(list_com) == 3:
            pass
    else:
        return

async def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')

    chat_id = msg['message']['chat']['id']
    first_name = msg['from']['first_name']
    
    print('Callback Query:', query_id, from_id, query_data)
    
    if query_data == 'Status':
        await bot.answerCallbackQuery(query_id,first_name+", "+getStatus(),show_alert=True)
        await bot.sendMessage(chat_id,"<strong>"+first_name+"</strong><code>, "+getStatus()+"</code>", parse_mode='HTML')
    elif query_data == 'Local':
        await bot.sendMessage(chat_id,"<strong>"+first_name+"</strong><code>, o Teresina Hacker Clube fica bem aqui:</code>", parse_mode='HTML')
        await bot.sendLocation(chat_id,-5.088308,-42.810024)
    elif query_data == "Projetos":
        await bot.sendMessage(chat_id,"<strong>"+first_name+"</strong><code>, projetos do Teresina Hacker Clube:</code>\n\n"+getProjetos(), parse_mode='HTML')
    elif query_data == "Agenda":
        await bot.sendMessage(chat_id,"<strong>"+first_name+"</strong><code>, agenda semanal do Teresina Hacker Clube:</code>\n"+getAgenda(), parse_mode='HTML')
    elif query_data == "Eventos":
        await bot.sendMessage(chat_id,"<strong>"+first_name+"</strong><code>, eventos do Teresina Hacker Clube:</code>\n"+getEventos(), parse_mode='HTML')





# TOKEN = sys.argv[1]  # get token from command-line
TOKEN = '214737879:AAGapVMozQRkMgxPNGBW8iLdkNEMv_yyj0U'

bot = telepot.async.Bot(TOKEN)
answerer = telepot.async.helper.Answerer(bot)

loop = asyncio.get_event_loop()
loop.create_task(bot.message_loop({'chat': on_chat_message,
                                   'callback_query': on_callback_query}))
print('Listening ...')

loop.run_forever()