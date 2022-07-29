import discord
from discord.ext import commands
from discord.utils import get
import time
from time import sleep
import json
import asyncio
import requests
import datetime
import aiohttp
import random
#intents = discord.Intents(messages=True, members = True, guilds=True)
intents = discord.Intents().all()
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)


@bot.event
async def on_ready():  
    print("Online")



@bot.command()
async def spam(ctx, arg1=None, arg2=None):
    if arg1 == "help":
        embed = discord.Embed(author="Webhook Spammer", description="Hilfe\n gehe auf den Jeweiligen Text Channel und drücke Rechtsklick, anschließend gehst du auf Kanal bearbeiten. Jetzt klickst du links im Menü auf den Punkt Integrationen, anschließend auf WebHooks und und Neuer WebHook, Nun Klickst du auf WebHook-URL kopieren. Du gehst jetzt auf CragHack und schreibst !spam [Webhook URL] und wie viele Nachrichten gespammt werden soll \nBeispiel:\n```!spam https://webhook.url 100```", color=0x0277fd)
        embed.set_image(url="https://cdn.discordapp.com/attachments/844989826246901801/1002719915523969024/Screenshot_136.png")
        await ctx.send(embed=embed)
        return
    if arg1 == None:
        arg1f = discord.Embed(author="Webhook Spammer", color=0x0277fd)
        arg1f.add_field(name="Fehler", value=f"```Bitte wähle ein weiteres Argument\n!spam help```", inline = True)
        await ctx.message.delete()
        await ctx.channel.send(embed=arg1f)
    elif arg1 and arg2 == None:
        arg2f = discord.Embed(author="Webhook Spammer", color=0x0277fd)
        arg2f.add_field(name="Fehler", value=f"```Bitte wähle ein weiteres Argument\n!spam help```", inline = True)
        await ctx.message.delete()
        await ctx.send(embed=arg2f)
    else:
        user_agent = "Mozilla/5.0 (Nintendo Switch; ShareApplet) AppleWebKit/601.6 (KHTML, like Gecko) NF/4.0.0.5.9 NintendoBrowser/5.1.0.13341"
        headers = {
            "User-Agent": user_agent,
            "Content-type": "application/json"}
        if int(arg2) >= 101:
            arg3f = discord.Embed(author="Webhook Spammer", color=0x0277fd)
            arg3f.add_field(name="Fehler", value=f"```Bitte wähle eine Nummer unter 100\n!spam help```", inline = True)
            await ctx.message.delete()
            await ctx.send(embed=arg3f)
        else:
            arg4f = discord.Embed(author="Webhook Spammer", color=0x0277fd)
            arg4f.add_field(name="| Angefordert von | ", value=f"```{str(ctx.message.author)}```", inline = True)
            arg4f.add_field(name=f"| Nachicht{'' if int(arg2) == 1 else 's'} |", value=f"```{arg2}```", inline = True)
            arg4f.add_field(name="| Verzögerung |", value=f"```0.2 Sekunden s```", inline = True)
            finish = (int(arg2)*0.20)
            arg4f.add_field(name="Ended in", value=f"```{finish} Sekunden {'' if int(finish) == 1 else 's'}```", inline = True)
            await ctx.message.delete()
            await ctx.send(embed=arg4f)
            for i in range(0, int(arg2)):
                    Webhook_Name = ""
                    Message = "123"
                    embed = {
                        "description": "Der Server wird gespammt!\n",
                        "title": "WebhookSpammer",
                        "footer": {
                            "text": "Coded by Kayyz#7302"
                        },
                        "color": 0x0277fd
                        }
                    payload = {"username": Webhook_Name, "embeds": [embed],}
                    requests.post(url=arg1, headers=headers, json=payload)
                    time.sleep(0.2)


bot.run("TOKEN")
