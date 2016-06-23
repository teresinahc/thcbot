# -*- coding: UTF-8 -*-
import sys
import re
from mechanize import Browser


def toggleStatus(list_com):
    status = "On.png" if list_com[1] == "/open" else "Off.png"
    login = list_com[2]
    passwd = list_com[3]

    url = 'http://teresinahc.org/wiki/index.php?title=Especial:Autenticar-se&returnto=P%C3%A1gina+principal'

    br = Browser()

    br.set_handle_robots(False)
    br.addheaders = [('User-agent', 'Firefox')]
    br.open(url)

    if 'Autenticar-se' in br.response().read():
        br.select_form('userlogin')
        br.form['wpName'] = login
        br.form['wpPassword'] = passwd
        br.submit()
        pag = br.response().read()
        if '"wgUserName":null' not in pag:
            br.open('http://teresinahc.org/wiki/index.php?title=Status&action=edit')
            if 'value="Salvar página"' in br.response().read():
                br.select_form('editform')
                br.form['wpTextbox1'] = '<center>[[Arquivo:'+status+']]</center>'
                br.submit(name='wpSave')
                br.close()
                if status == 'On.png':
                    return 'no momento o Teresina Hacker Clube encontra-se ABERTO!'
                else:
                    return 'no momento o Teresina Hacker Clube encontra-se FECHADO!'
            else:
                br.close()
                return 'Voc\xc3\xaa n\xc3\xa3o tem permiss\xc3\xa3o para alterar p\xc3\xa1ginas da Wiki do Teresina Hacker Clube'
        else:
            br.close()
            output  = re.compile('<div class="errorbox">(.*?)</div>', re.DOTALL |  re.IGNORECASE).findall(pag)
            return "</code>"+output[0].replace("<br />", "").replace("\t", "")+"<code>"
    else:
        br.close()
        return 'Desculpe, por algum motivo n\xc3\xa3o foi poss\xc3\xadvel acessar a Wiki do Teresina Hacker Clube.'

print toggleStatus(sys.argv)