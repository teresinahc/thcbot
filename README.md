=====
THCbot
=====

Bot do Teresina Hacker Clube :)

---
Utilizamos no desenvolvimento
---

* [telepot - Python framework for Telegram Bot API](https://github.com/nickoala/telepot)
* Python 3.5 e 2.7 ^^'

---
Módulos Python
---

* Asyncio
    `pip3.5 install async`
* Telepot
    `pip3.5 install telepot`
* Mechanize (python 2.7)
    `pip2.7 install mechanize`

---
Como executar
---

1. Criar e ativar um [ambiente virtual](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
    * `mkvirtualenv botenv` para criar um virtualenv chamado botenv
    * `workon botenv` para ativar o virtualenv sempre que for trabalhar no projeto

2. Renomeie o arquivo `settings.template.py` para `settings.py`, adicione a TOKEN do bot em `TELEGRAM_API_KEY = ''` e ID do seu bot em `BOT_ID = 6666666`

3. Inicie o bot com `python bot.py`
