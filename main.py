import discord
import os
import utils
import gameboy

rom = None
started=False
control=False
gbchannel = None
gb=gameboy

class Client(discord.Client):
  async def on_ready(self):
    print("Bot started")
  async def on_message(self, message):
    msg = message.content.lower()
    guild = message.guild
    if(msg == "gb emotes"):
      await message.channel.send("**Emotes used:**\n\n**- Custom:**\n<:error:846794952520106014>, <:success:846794975265554483> \n*- Animated*\n<a:loading:846792664980389889>, <a:gb_success_alternative:847096609640415292>\n\n**- Default:**\n:paperclip:, :green_circle:")
    
    if(msg == "gb start"):
      global started
      if(started == False):
        gb_msg = await message.channel.send("__Starting Gameboy__.. %s" % (utils.Emotes.loading()))
        started = True
        if(len(message.attachments)==0):
          await utils.Embed.failWithFix("No Gameboy ROM file was attached! 📎", "Attach a Gameboy file ('.gb' file) you can get Gameboy games from this [site](https://www.romsgames.net/roms/gameboy/)", message)
          started = False
        else:
          rom = message.attachments[0]
          if(rom.filename.split(".")[-1] != "gb"):
            rom = None
            await utils.Embed.failWithFix("Did not find Gameboy file (.GB file)!", "Use a Gameboy game as the file attachment! you can get Gameboy games from this [site](https://www.romsgames.net/roms/gameboy/)", message)
            started = False
          elif(rom.filename.split(".")[-1] == "gb"):
            botmsg = await message.channel.send("Installing Gameboy ROM file.. %s" % (utils.Emotes.loading()))
            rom = message.attachments[0]
            os.system("curl -o rom.gb %s" % (rom.url))
            rom = None
            await botmsg.edit(content="Installed Gameboy ROM file %s" % (utils.Emotes.success()))
            botmsg = await message.channel.send("Creating private channel.. %s" %(utils.Emotes.loading()))
            if(utils.getBot(guild, self).guild_permissions.manage_channels):
              ctg=None
              for x in guild.categories:
                if x.name.lower() == "gameboy":
                  ctg = x
              if ctg == None:
                ctg = await guild.create_category("gameboy")
              global gbchannel
              gbchannel = await ctg.create_text_channel(message.author.display_name)
              await gbchannel.send(message.author.mention)
              await botmsg.edit(content="Created private channel %s" %(utils.Emotes.success()))
              await gbchannel.set_permissions(guild.default_role, view_channel=False)
              await gbchannel.set_permissions(message.author, read_messages=True, view_channel=True, send_messages=True)
              botmsg = await message.channel.send("Launching emulator.. %s" % (utils.Emotes.loading()))
              await botmsg.edit(content="Launched emulator %s"%(utils.Emotes.success()))
              await gb_msg.edit(content="Started Gamebot %s" %(utils.Emotes.success_Alt()))
              await gb.launch(gbchannel)
            else:
              await botmsg.edit(content="Could not create private channel %s" %(utils.Emotes.fail()))
              await utils.Embed.failWithFix("Could not create private channel, Bot is lacking MANAGE_CHANNELS and MANAGE_PERMISSIONS permissions!", "Re-Add the bot and allow the MANAGE_CHANNELS and MANAGE_PERMISSIONS permissions to the bot!", message)
            

            

      else:
        
        await utils.Embed.fail("Gameboy emulator is already on!", message)
        return
    if msg == "gb stop":
      if started:
        started=False
        gb.stop()
      else:
        await utils.Embed.fail("There was no instance of a Gameboy running to stop!", message)
    if msg == "gb use":
      if started and message.channel == gbchannel:
        global control
        if control:
          control=False
          gbchannel.send("***Disabled inputs!***")
        control=True
        await gbchannel.send("***Enabled inputs!***\nControls are **u** *up* **d** *down* **l** *left* **r** *right*\n**a** *button A* **s** *button B* **t** *button SELECT* **f** *button START*\n *do [inputs seperated by a space]*")
      else:
        await utils.Embed.fail("There was no instance of a Gameboy running on this channel to control!", message)
    if started and message.channel == gbchannel and control and msg.lower().startswith("do"):
      inputs = msg.split(" ")
      for input in inputs:
        gb.sendInput(input)

        

client = Client()
client.run("your token here")
