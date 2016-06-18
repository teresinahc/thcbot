# -*- coding: UTF-8 -*-
import re
import urllib.request, urllib.error, urllib.parse

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}

def getStatus():
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


def setStatus(list_com):
	status = "On.png" if list_com[0] == "/open" else "Off.png"
	login = list_com[1]
	passwd = list_com[2]

	url = 'http://teresinahc.org/wiki/index.php?title=Especial:Autenticar-se&returnto=P%C3%A1gina+principal'
	values = {'wpName':login,
			'wpPassword':passwd}
	
	data = urllib.parse.urlencode(values)
	data = bytes(data, 'ascii')

	req = urllib.request.Request(url, data, hdr)
	with urllib.request.urlopen(req) as response:
		the_page = response.read()
	f=open("site.html", "w")
	f.write(the_page.decode('utf-8'))
	f.close()


def getAgenda():
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


def getProjetos():
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

def getEventos():
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


setStatus(["/close", "philippeoz", "55363300"])
# print(getEventos())
# def toggleStatus(login, passwd, status):
# 	global url, hdr

# 	br = Browser()

# 	br.set_handle_robots(False)
# 	br.addheaders = [('User-agent', 'Firefox')]
# 	br.open(url)

# 	if 'Autenticar-se' in br.response().read():
# 		br.select_form('userlogin')
# 		br.form['wpName'] = login
# 		br.form['wpPassword'] = passwd
# 		br.submit()
# 		pag = br.response().read()
# 		if '"wgUserName":null' not in pag:
# 			br.open('http://teresinahc.org/wiki/index.php?title=Status&action=edit')
# 			if 'value="Salvar página"' in br.response().read():
# 				br.select_form('editform')
# 				stat=''
# 				if status:
# 					stat='On'
# 				else:
# 					stat='Off'
# 				br.form['wpTextbox1'] = '<center>[[Arquivo:'+stat+'.png]]</center>'
# 				br.submit(name='wpSave')
# 				br.close()
# 				if status:
# 					return 'O Teresina Hacker Clube no momento está ABERTO!'
# 				else:
# 					return 'O Teresina Hacker Clube no momento está FECHADO!'
# 			else:
# 				br.close()
# 				return 'Você não tem permissão para alterar páginas da Wiki do Teresina Hacker Clube'
# 		else:
# 			br.close()
# 			output  = re.compile('<div class="errorbox">(.*?)</div>', re.DOTALL |  re.IGNORECASE).findall(pag)
# 			return output[0].replace("<br />", "").replace("\t", "")
# 	else:
# 		br.close()
# 		return 'Desculpe, por algum motivo não foi possível acessar a Wiki do Teresina Hacker Clube.'