import discord


# Easier emojis
class Emotes((discord.Client)):
    def loading():
        emoji = "<a:loading:846792664980389889>"
        return emoji

    def success():
        emoji = "<:success:846794975265554483>"
        return emoji

    def success_Alt():
      emoji = "<a:gb_success_alternative:847096609640415292>"
      return emoji

    def fail():
        emoji = "<:error:846794952520106014>"
        return emoji


# Easier embeds
class Embed():
    async def fail(errorDesc, message):

        embedmsg = discord.Embed(title="Error! <:error:846794952520106014> ",
                                 description=errorDesc,
                                 color=0xd10000)
        embedmsg.add_field(
            name="Not working?",
            value="Contact *UserUNP#3418* or *RedCommand#5373* for help.",
            inline=True)
        await message.channel.send(embed=embedmsg)

    async def failWithFix(errorDesc, possibleFix, message):
        embedmsg = discord.Embed(title="Error! <:error:846794952520106014> ",
                                 description=errorDesc,
                                 color=0xd10000)
        embedmsg.add_field(name="Possible fix", value=possibleFix, inline=True)
        embedmsg.add_field(
            name="Did not work?",
            value="Contact *UserUNP#3418* or *RedCommand#5373* for help!",
            inline=True)
        await message.channel.send(embed=embedmsg)

class RawEmbed():
    async def fail(errorDesc, message):

        embedmsg = discord.Embed(title="Error! <:error:846794952520106014> ",
                                 description=errorDesc,
                                 color=0xd10000)
        embedmsg.add_field(
            name="Not working?",
            value="Contact *UserUNP#3418* or *RedCommand#5373* for help.",
            inline=True)
        return embedmsg

    async def failWithFix(errorDesc, possibleFix, message):
        embedmsg = discord.Embed(title="Error! <:error:846794952520106014> ",
                                 description=errorDesc,
                                 color=0xd10000)
        embedmsg.add_field(name="Possible fix", value=possibleFix, inline=True)
        embedmsg.add_field(
            name="Did not work?",
            value="Contact *UserUNP#3418* or *RedCommand#5373* for help!",
            inline=True)
        return embedmsg

def getBot(guild):
  return guild.get_member(846392624700981289)