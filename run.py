import discord
from discord.ext import commands
from discord.ext import tasks

bot = commands.Bot(command_prefix=config.prefix)

bot.remove_command("help")

@tasks.loop(seconds=18.0)
async def statusup():
    svr = bot.get_guild(662541523740786708) # Server
    bt = svr.get_member(391132891024850945) # Bot
    channel = bot.get_channel(662541926817333258) # Channel
    if os.path.isfile('data/status.json'):
        with open('data/status.json') as json_file:
            data = json.load(json_file)
            for p in data['Config']:
                if bt.status == discord.Status.online:
                    if p['status'] == "offline":
                        await channel.send("Bot is online!")
                        data = {}
                        data['Config'] = []
                        data['Config'].append({
                            'status': "online",
                            })
                        with open("data/status.json", 'w+') as outfile:
                            json.dump(data, outfile)
                if bt.status == discord.Status.offline:
                    if p['status'] == "online":
                        await channel.send("Bot is offline!")
                        data = {}
                        data['Config'] = []
                        data['Config'].append({
                            'status': "offline",
                            })
                        with open("data/status.json", 'w+') as outfile:
                            json.dump(data, outfile)
@bot.event
async def on_ready():
    statusup.start()
    print("Started!")
    
print("Starting...")
bot.run(config.token, reconnect=True)
