# -*- coding: UTF-8 -*-
import re
import os
import urllib.request, urllib.error, urllib.parse

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}

#		Grava o id de todo chat iniciado com o bot
def save_id(chat_id):
	f = open("chat_ids", "r+")
	if str(chat_id) not in f.read():
		f.write(str(chat_id)+"\n")
		f.close()
	else:
		f.close()

#		Retorna o status do THC (aberto/fechado) de acordo com o que estiver setado na wiki.
def get_status():
	url = "http://teresinahc.org/wiki/index.php/P%C3%A1gina_principal"
	f = urllib.request.Request(url, headers = hdr)
	try:
		page = urllib.request.urlopen(f)
		if 'Off.png' in page.read().decode('utf-8'):
			return 'no momento o Teresina Hacker Clube encontra-se FECHADO! '+(u'\U0001f615')
		else:
			return 'no momento o Teresina Hacker Clube encontra-se ABERTO! '+(u'\U0001f603')
	except urllib.error.HTTPError:
		return 'Ocorreu um erro ao tentar verificar o status do THC!'

#		Gambiarra pra fazer login na Wiki do THC
def set_status(list_com):
	return os.popen('python gamb.py '+list_com[0]+' '+list_com[1]+' '+list_com[2]).read()

#		Retorna a agenda do THC (aberto/fechado) de acordo com o que estiver setado na wiki.	
def get_agenda():
	url = "http://teresinahc.org/wiki/index.php/Agenda_Semanal"
	f = urllib.request.Request(url, headers = hdr)
	try:
		page = urllib.request.urlopen(f)
		txt = page.read().decode('utf-8')
		output  = re.compile('class="mw-content-ltr">(.*?)\n\n', re.DOTALL |  re.IGNORECASE).findall(txt)
		result = output[0].replace("<ul>","").replace("</ul>","")
		result = result.replace("<li>","  "+u'\U0001f449'+" ").replace("</li>", "")
		return result.replace("/wiki","http://teresinahc.org/wiki")
	except urllib.error.HTTPError:
		return 'Ocorreu um erro ao tentar verificar a agenda semanal do THC!'

#		Retorna os projetos do THC (aberto/fechado) de acordo com o que estiver setado na wiki.
def get_projetos():
	url = "http://teresinahc.org/wiki/index.php/Projetos"
	f = urllib.request.Request(url, headers = hdr)
	try:
		page = urllib.request.urlopen(f)
		txt = page.read().decode('utf-8')
		output  = re.compile('<tr>\n<td>(.*?)<td align', re.DOTALL |  re.IGNORECASE).findall(txt)
		cleanr = re.compile(' title=".*?"')
		outputxt=""
		for i in output:
			cleantext = re.sub(cleanr,'', i)
			cleantext = cleantext.replace("> ", ">").replace("/wiki","http://teresinahc.org/wiki")
			cleantext = cleantext.replace("</a>\n</td>\n<td>", "</a> - ")
			cleantext = cleantext.replace("\n</td>\n<td>"," - ")
			cleantext = cleantext.replace("</td>","")
			outputxt+=u'\U0001f449'+" "+cleantext
		return outputxt
	except urllib.error.HTTPError:
		return 'Ocorreu um erro ao tentar verificar os projetos do THC!'

#		Retorna os eventos do THC (aberto/fechado) de acordo com o que estiver setado na wiki.
def get_eventos():
	url = "http://teresinahc.org/wiki/index.php/Pr%C3%B3ximos_Eventos"
	f = urllib.request.Request(url, headers = hdr)
	try:
		page = urllib.request.urlopen(f)
		txt = page.read().decode('utf-8')
		output  = re.compile('mw-content-ltr"><ul>(.*?)\n\n', re.DOTALL |  re.IGNORECASE).findall(txt)
		result = output[0].replace("<ul>","").replace("</ul>","").replace("<strike>", u'\u2705'+" ")
		result = result.replace("<li>","  "+u'\U0001f449'+" ")
		return result.replace("</strike>","").replace("</li>", "")
	except urllib.error.HTTPError:
		return 'Ocorreu um erro ao tentar verificar os eventos do THC!'