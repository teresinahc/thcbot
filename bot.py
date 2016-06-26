import asyncio
import sys
import telepot
import telepot.async
import settings
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from thcbotfunctions import *


async def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    command = ''

    save_id(chat_id)

    if content_type != 'text' and content_type != 'new_chat_member':
        return
    elif content_type == 'text':
        command = msg['text'].lower()

    if content_type == 'new_chat_member':
        if msg['new_chat_member']['id'] == BOT_ID:
            await bot.sendMessage(chat_id, 'Hey pessoal do <strong>' + msg['chat']['title'] + '</strong>! ' + (u'\U0001f596') + '\nSou o THCbot!\nBot do <a href="http://teresinahc.org/">Teresina Hacker Clube</a>\nObriago ao <strong>'+msg['from']['first_name']+'</strong> por me adicionar.\nUsem os comandos ou enviem "/menu"! ' + (u'\U0001f603'), parse_mode='HTML')
        else:
            await bot.sendMessage(chat_id,'Hey <strong>' + msg['new_chat_member']['first_name'] +\
             '</strong>! '+(u'\U0001f596')+'\nSeja bem-vind@ ao <strong>' + msg['chat']['title'] +\
              '</strong>!\nSou o THCbot!\nBot do <a href="http://teresinahc.org/">Teresina Hacker Clube</a>!\nUse os comandos ou envie "/menu"! ' +\
               (u'\U0001f603') +("\nLembrando que novatos pagam PIZZA!! "+(u'\U0001f355') if chat_id==-1001031289268 else ""), parse_mode='HTML')
        return

    if ('/open' in command or '/close' in command) and chat_type != 'private':
        await bot.sendMessage(chat_id,'Os comandos "/open" e "/close" devem ser utilizados em "private" comigo, pois preciso de "credenciais" para continuar. ' + (u'\U0001f609'),parse_mode='HTML')
        return
    elif '/start' in command:
        await bot.sendMessage(chat_id,'Hello <strong>' + msg['from']['first_name'] + '</strong>, sou o THCbot! ' + (u'\U0001f596') + '\nBot do <a href="http://teresinahc.org/">Teresina Hacker Clube</a>\nUse os comandos ou envie "/menu"! ' + (u'\U0001f603'), parse_mode='HTML')
        return
    elif '/status' in command:
        await bot.sendMessage(chat_id,"<strong>" + msg['from']['first_name'] + "</strong>, "+get_status()+"", parse_mode='HTML')
    elif '/menu' in command:
        #
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
    elif ('/open' in command) or ('/close' in command):
        list_com = command.split(" ")
        if len(list_com) != 3:
            await bot.sendMessage(chat_id,'<strong>'+msg['from']['first_name']+'</strong>, preciso do seu login e senha da Wiki do THC, então, envie o comando "' + list_com[0] + '" neste padrão:\n' + list_com[0] + '<code> meulogin minhasenha</code>', parse_mode="HTML")
        elif len(list_com) == 3:
            await bot.sendMessage(chat_id,'<strong>'+msg['from']['first_name']+'</strong><code>,'+set_status(list_com)+'</code>', parse_mode="HTML")
    else:
        return

async def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')

    chat_id = msg['message']['chat']['id']
    first_name = msg['from']['first_name']

    if query_data == 'Status':
        await bot.answerCallbackQuery(query_id,first_name+", " + get_status(),show_alert=True)
        await bot.sendMessage(chat_id,"<strong>" + first_name + "</strong>, " + get_status(), parse_mode='HTML')
    elif query_data == 'Local':
        await bot.sendMessage(chat_id,"<strong>" + first_name + "</strong>, o Teresina Hacker Clube fica bem aqui:", parse_mode='HTML')
        await bot.sendLocation(chat_id, -5.088308, -42.810024)
    elif query_data == "Projetos":
        await bot.sendMessage(chat_id,"<strong>" + first_name + "</strong>, projetos do Teresina Hacker Clube:\n\n" + get_projetos(), parse_mode='HTML')
    elif query_data == "Agenda":
        await bot.sendMessage(chat_id,"<strong>" + first_name + "</strong>, agenda semanal do Teresina Hacker Clube:\n" + get_agenda(), parse_mode='HTML')
    elif query_data == "Eventos":
        await bot.sendMessage(chat_id,"<strong>" + first_name + "</strong>, eventos do Teresina Hacker Clube:\n" + get_eventos(), parse_mode='HTML')



BOT_ID = settings.BOT_ID   # Coloque aqui o id do seu bot, utilizado pra detectar quando ele é adicionado em algum grupo

TOKEN = settings.TELEGRAM_API_KEY  # Pega a token via linha de comando!

bot = telepot.async.Bot(TOKEN)
answerer = telepot.async.helper.Answerer(bot)

loop = asyncio.get_event_loop()
loop.create_task(bot.message_loop({'chat': on_chat_message,
                                   'callback_query': on_callback_query}))
print('THCbot iniciado! <3')

loop.run_forever()
