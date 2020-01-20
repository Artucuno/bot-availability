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
                        embed = discord.Embed(title="Bot is online!")
                        await channel.send(embed=embed)
                        data = {}
                        data['Config'] = []
                        data['Config'].append({
                            'status': "online",
                            })
                        with open("data/status.json", 'w+') as outfile:
                            json.dump(data, outfile)
                if bt.status == discord.Status.offline:
                    if p['status'] == "online":
                        embed = discord.Embed(title="Bot is offline! :(")
                        await channel.send(embed=embed)
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
