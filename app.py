import os  # Lib necessária para acessar arquivos em pastas

import discord  # Importando a lib do pycord
from dotenv import load_dotenv  # utilziando para acessar as credencias em .env

from get_calendar import SeleniumMethod

# Carregando variáveis do arquivo .evn
load_dotenv()

# Crendenciais de acesso
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
MATRICULA = os.getenv('MATRICULA')
SENHA_UNOESTE = os.getenv('SENHA_UNOESTE')


# conexão ao Discord
intents = discord.Intents.default()  # Usado p derrubar recursos de gateway
intents.message_content = True  # Atributo para pertmitir Send msg
client = discord.Client(intents=intents)


# Decorator para registrar um evento/ação no discord.
# A função do evento tem q esta sob esse decorator.
@client.event
async def on_ready():
    print(f'Nós acessamos em {client.user}')


# Capturando msgs do grupo no discord, aqui fazemos duas validações
@client.event
async def on_message(message):  # Se a mensagem for do proprio bot, ele ignora
    if message.author == client.user:
        return

    # Se a mensagem for o comando $hello, ele irá responder com  função
    if message.content.startswith('#calendar'):
        await message.channel.send('Carregando informações')
        instance = SeleniumMethod()
        await message.channel.send(instance.mostrar_atividades())


client.run(DISCORD_TOKEN)
