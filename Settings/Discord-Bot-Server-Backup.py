from Config.Util import *
from Config.Config import *
import discord
from discord.ext import commands
import json
import os
import asyncio
import logging
import aiohttp

logging.getLogger('discord.state').setLevel(logging.ERROR)
logging.getLogger('discord.ext.commands.bot').setLevel(logging.ERROR)

logging.basicConfig(level=logging.WARNING)

intents = discord.Intents.default()
intents.guilds = True  # Permet au bot d'accéder aux informations sur les guildes (serveurs)
intents.members = True  # Permet au bot d'accéder aux informations sur les membres du serveur
intents.message_content = True

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

async def select_bot_token():
    token_file = '2-Input/TokenDisc/BotTokenDisc.txt'
    with open(token_file, 'r') as f:
        tokens = [line.strip() for line in f.readlines()]

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

    choice = int(input(f"\n{INPUT} Token Number -> {reset}")) - 1

    if 0 <= choice < len(tokens):
        return bots_info[choice][1]
    else:
        print(f"Invalid Choice")
        return None

async def main():
    TOKEN = await select_bot_token()

    if TOKEN is None:
        exit(f"{ERROR} Invalid Token")

    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix='!', intents=intents)

    @bot.event
    async def on_ready():
        print(f"\n{secondary}[{primary}1{secondary}]{primary} Save a server backup")
        print(f"{secondary}[{primary}2{secondary}]{primary} Restore a server from a backup")
        choice = int(input(f"\n{INPUT} Choose an option -> {reset}"))

        if choice == 1:
            await save_server_backup(bot)
        elif choice == 2:
            backup_file = select_backup_file()
            if backup_file:
                await restore_server_backup(bot, backup_file)
            else:
                print(f"\n{ERROR} No backup selected.")
        else:
            print(f"\n{ERROR} Invalid choice.")
        await bot.close()

    await bot.start(TOKEN)

async def save_server_backup(bot):
    for i, guild in enumerate(bot.guilds):
        print(f"{secondary}[{primary}{i + 1}{secondary}]{primary} {guild.name}")

    server_choice = int(input(f"\n{INPUT}Choose a server -> {reset}")) - 1

    if 0 <= server_choice < len(bot.guilds):
        guild = bot.guilds[server_choice]
        await backup_server(guild)
        print(f"\n{INFO} Backup completed for server: {reset}{guild.name}\n")
        Continue()
        Reset()
    else:
        print(f"\n{ERROR} Invalid choice.")
        Continue()
        Reset()

async def restore_server_backup(bot, backup_file):
    for i, guild in enumerate(bot.guilds):
        print(f"{secondary}[{primary}{i + 1}{secondary}]{primary} {guild.name}")

    server_choice = int(input(f"\n{INPUT}Choose a server -> {reset}")) - 1

    if 0 <= server_choice < len(bot.guilds):
        guild = bot.guilds[server_choice]
        await delete_existing_server_content(guild)
        await load_server_backup(guild, backup_file)
        print(f"Server {guild.name} restored from backup.")
        Continue()
        Reset()
    else:
        print(f"\n{ERROR} Invalid choice.")
        Continue()
        Reset()

async def delete_existing_server_content(guild):
    for channel in guild.channels:
        try:
            await channel.delete()
        except discord.Forbidden:
            print(f"{ERROR} Impossible de supprimer le salon {channel.name} : missing permissions.")
        except discord.HTTPException as e:
            print(f"{ERROR} Error deleting channel {channel.name}: {e}")

    for role in guild.roles:
        if role.name != "@everyone":
            try:
                await role.delete()
            except discord.Forbidden:
                print(f"{ERROR} Impossible de supprimer le rôle {role.name} : missing permissions.")
            except discord.HTTPException as e:
                print(f"\n{ERROR} Error deleting role {role.name}: {e}")

async def backup_server(guild):
    categories = {
        category.name: {
            'channels': [
                {
                    'name': channel.name,
                    'type': str(channel.type),
                    'id': channel.id,
                    'permissions': {
                        str(role.id): channel.overwrites_for(role)._values
                        for role in guild.roles
                    }
                }
                for channel in category.channels
            ],
            'id': category.id
        }
        for category in guild.categories
    }

    roles = {
        role.name: {
            'permissions': role.permissions.value,  
            'id': role.id
        }
        for role in guild.roles
    }

    members = {
        member.name: {
            'roles': [role.name for role in member.roles],
            'id': member.id
        }
        for member in guild.members
    }

    backup_dir = '1-Output/Backup'
    os.makedirs(backup_dir, exist_ok=True)

    backup_file = os.path.join(backup_dir, f'{guild.name}_backup.json')
    with open(backup_file, 'w') as f:
        json.dump({'categories': categories, 'roles': roles, 'members': members}, f, indent=4)

async def load_server_backup(guild, backup_file):
    with open(backup_file, 'r') as f:
        data = json.load(f)

    categories = data['categories']
    roles = data['roles']

    role_map = {}
    for role_name, role_data in roles.items():
        existing_role = discord.utils.get(guild.roles, name=role_name)
        if existing_role is None:
            permissions = discord.Permissions(int(role_data['permissions']))  
            new_role = await guild.create_role(name=role_name, permissions=permissions)
            role_map[role_name] = new_role
        else:
            role_map[role_name] = existing_role

    for category_name, category_data in categories.items():
        category = await guild.create_category(category_name)
        for channel_data in category_data['channels']:
            if channel_data['type'] == 'text':
                channel = await category.create_text_channel(channel_data['name'])
            elif channel_data['type'] == 'voice':
                channel = await category.create_voice_channel(channel_data['name'])

            for role_id, permissions_data in channel_data['permissions'].items():
                role = discord.utils.get(guild.roles, id=int(role_id))
                if role:
                    overwrites = channel.overwrites_for(role)
                    for perm, value in permissions_data.items():
                        setattr(overwrites, perm, value)
                    await channel.set_permissions(role, overwrite=overwrites)

asyncio.run(main())
