from Config.Util import *
from Config.Config import *
import discord
from discord.ext import commands
import logging
import asyncio
import aiohttp

logging.getLogger('discord').setLevel(logging.CRITICAL)

async def get_bot_info(token):
    try:
        async with aiohttp.ClientSession() as session:
            intents = discord.Intents.none()
            bot = commands.Bot(command_prefix='!', intents=intents, session=session)
            
            async with bot:
                await bot.login(token)
                user = await bot.fetch_user(bot.user.id)
            return {"status": "Valid", "user": user.name}
    except Exception:
        return {"status": "Invalid", "user": None}

async def main():
    with open("2-Input/TokenDisc/BotTokenDisc.txt", "r") as file:
        tokens = [line.strip() for line in file.readlines()]

    bots_info = []
    print(f"\n{primary}Bot Token Discord ({secondary}./2-Input/TokenDisc/BotTokenDisc.txt{primary}):")

    for idx, token in enumerate(tokens, 1):
        bot_info = await get_bot_info(token)
        if bot_info["status"] == "Valid":
            bot_info_str = f"{secondary}[{primary}{idx}{secondary}]{primary} -> Status: {secondary}{bot_info['status']}{primary} | User: {secondary}{bot_info['user']}{primary} | Token: {secondary}{token[:47]}..."
        else:
            bot_info_str = f"{secondary}[{primary}{idx}{secondary}]{primary} -> Status: {secondary}{bot_info['status']}{primary} | Token: {secondary}{token[:47]}..."
        
        bots_info.append((idx, token, bot_info_str))
        print(bot_info_str)

    choice = int(input(f"\n{INPUT} Token Number -> {reset}"))

    chosen_token = None
    for idx, token, bot_info_str in bots_info:
        if idx == choice:
            chosen_token = token
            break

    if chosen_token:
        intents = discord.Intents.default()
        intents.guilds = True
        intents.message_content = True

        async with aiohttp.ClientSession() as session:
            bot = commands.Bot(command_prefix='!', intents=intents, session=session)

            @bot.event
            async def on_ready():
                
                for i, guild in enumerate(bot.guilds):
                    if guild.text_channels:
                        channel = guild.text_channels[0]
                        
                        if channel.permissions_for(guild.me).create_instant_invite:
                            invite = await channel.create_invite(max_age=0, max_uses=0)
                            print(f"\n{INFO} Server {i+1}: '{secondary}{guild.name}{primary}' - L'invitation est : {secondary}{invite.url}{primary}")
                            Continue()
                            Reset()
                        else:
                            print(f"Serveur {i+1}: '{guild.name}' - Le bot n'a pas la permission de créer une invitation.")
                            Continue()
                            Reset()
                    else:
                        print(f"Serveur {i+1}: '{guild.name}' - Aucun canal texte disponible pour créer une invitation.")
                        Continue()
                        Reset()

                await bot.close()

            await bot.start(chosen_token)
    else:
        print("Invalid Token.")
        Continue()
        Reset()

asyncio.run(main())
