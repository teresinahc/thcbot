=====
THCbot
=====

Bot do Teresina Hacker Clube :)

---
Utilizamos no desenvolvimento
---

* [telepot - Python framework for Telegram Bot API](https://github.com/nickoala/telepot" target="_blank)
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

2. Abra o arquivo `bot.py` e adicione o ID do seu bot em `BOT_ID=6666666`

3. Inicie o bot com a token via linha de comando
    * `python3.5 bot.py AQUI_VOCÊ_ADICIONA_A_TOKEN_DO_BOT`

4. Ou substitua `sys.argv[1]` por sua TOKEN no arquivo `bot.py` em:
    * `TOKEN = AQUI_VOCÊ_ADICIONA_A_TOKEN_DO_BOT`
    * Daí inicie o bot `python3.5 bot.py`
