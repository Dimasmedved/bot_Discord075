import discord
from discord.ext import commands

TOKEN="NzM1Nzc0MDM0NjU4MTk3NTY1.XxlI9w.Q1PbQUCGGehdi3SXYKotnzULtYE"
PREFIX="#"
client=commands.Bot(command_prefix="#")
client.remove_command("help")

#команды
@client.event
async def on_member_join(member):
    channel=client.get_channel(735049701874860115)
    role=discord.utils.get(member.guild.roles, id=762259371509415957)
    await member.add_roles(role)
    await channel.send(embed=discord.Embed(description=f"Пользователь``{member.name}``присоединился к нам!!!",color=0x0))


@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def clear(ctx,amout=50):
    await ctx.channel.purge(limit=amout)

@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def kick(ctx,member:discord.Member,*,reason=None):
    await ctx.channel.purge(limit=1)
    await member.kick(reason=reason)
    await ctx.send(f"kick user{member.mention}")

@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def ban(ctx,member:discord.Member,*,reason=None):
    await ctx.channel.purge(limit=1)
    await member.ban(reason=reason)
    await ctx.send(f"ban user{member.mention}")

@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def unban(ctx , * , member):
    await ctx.channel.purge(limit=1)
    banned_users=await ctx.guild.bans()

    for ban_entry in banned_users:
        user=ban_entry.user
        await ctx.guild.unban(user)
        await ctx.send(f"Разбанен пользователь{user.mention}")
    return

@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def help(ctx):
    emb=discord.Embed(title="Все команды(только для администрации)",colour=discord.Color.blurple())
    emb.add_field(name="{}clear".format(PREFIX),value="Очистка чата")
    emb.add_field(name="{}kick".format(PREFIX), value="Кикнуть пользователя")
    emb.add_field(name="{}ban".format(PREFIX), value="Забанить пользователя")
    emb.add_field(name="{}unban".format(PREFIX), value="Разбанить пользователя")
    await ctx.send(embed=emb)


client.run(TOKEN)
