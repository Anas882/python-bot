import  discord
from discord.ext import commands

client = commands.Bot(command_prefix="-")

@client.event
async def on_ready():
    print("bot is ready")


@client.command()
@commands.has_permissions(manage_messages=True)
async def warn(ctx, member : discord.Member, * , reason = None):
    embed = discord.Embed(
    title = f"the member {member.name} has been warned successfully ",
    description = f"Reason for the Warning is: {reason}",
    color = discord.Colour.red())
    embed.add_field(name = f"Warning from {ctx.author.name}", value="dont make any mistakes now!")
    embed.set_thumbnail(url=member.avatar_url)

    emb = discord.Embed(title=f"you have been warned from {ctx.guild.name} because: {reason}",
    description=f"The Warning came from the user: {ctx.author.name}", color=discord.Colour.green())
    embed.set_image(url=member.avatar_url)

    await ctx.send(embed=embed)
    await member.send(embed=emb)

@client.command()
async def ava(ctx, member : discord.Member=None):
    embed=discord.Embed(title=f"Here is the Avatar for {member.name}",
    color=discord.Colour.red())
    embed.set_image(url=member.avatar_url)
    await ctx.send(embed=embed)



@client.command()
async def dm(ctx, member : discord.Member, * , msg=None):
    embed = discord.Embed(title = f"hey {member.name}, you have got a message from {ctx.author.name}", color = discord.Colour.blue())
    embed.add_field(name = "Message:", value = f"{msg}", inline = True)
    await member.send(embed=embed)


@client.command()
@commands.has_permissions(manage_messages=True)
async def voting(ctx, * , args):
    embed = discord.Embed(
    title = "This is a Voting session",
    description = f"{args}",
    color = discord.Colour.teal()
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764950717059825695/768174787410526268/431539-PE9O1K-661-1140x684.jpg")
    mess = await ctx.send(embed=embed)
    await mess.add_reaction("👍")
    await mess.add_reaction("👎")


@client.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount = 2):
    await ctx.channel.purge(limit=amount)

@client.command()
async def userinfo(ctx, member : discord.Member = None):
    roles = [role for role in member.roles]
    embed = discord.Embed(
    title = f"userinfo for the member {member.name}",
    timestamp = ctx.message.created_at,
    color = discord.Colour.default()
    )
    embed.add_field(name = "Member on Discord since:", value = member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name = "Member on Server since:", value = member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

    embed.add_field(name = "Roles:", value = "".join([role.name for role in roles]))
    embed.set_thumbnail(url=member.avatar_url)


    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member : discord.Member, * , reason = None):
    guild = ctx.guild
    for role in guild.roles:
        if role.name == "Gemuted":
            await member.add_roles(role)
            embed = discord.Embed(title = f"The Member {member.name} has been muted successfully",
            description = f"The reason for the mute is: {reason}",
            color = discord.Colour.blurple())
            await member.send(f"You have been muted in the Server {ctx.guild.name}, because of: {reason}")

            await ctx.send(embed=embed)






client.run("NzY3Nzk4MjU2Nzk2MTcyMzU5.X43J2Q.0D6En1NATzAuAZKgwJg4BTwkikc")
