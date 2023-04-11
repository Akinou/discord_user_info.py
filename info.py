import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')

@client.command()
async def userinfo(ctx, member: discord.Member):
    embed = discord.Embed(title="Informations sur l'utilisateur", color=member.color)
    embed.set_thumbnail(url=member.avatar_url)
    embed.add_field(name="Nom", value=member.name, inline=True)
    embed.add_field(name="Surnom", value=member.nick, inline=True)
    embed.add_field(name="ID", value=member.id, inline=True)
    embed.add_field(name="Création du compte", value=member.created_at.strftime("%d/%m/%Y %H:%M:%S"), inline=True)
    embed.add_field(name="Date d'arrivée sur le serveur", value=member.joined_at.strftime("%d/%m/%Y %H:%M:%S"), inline=True)
    roles = [role.mention for role in member.roles if role != ctx.guild.default_role]
    embed.add_field(name="Rôles", value=" ".join(roles), inline=True)
    await ctx.send(embed=embed)
