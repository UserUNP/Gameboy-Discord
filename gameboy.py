from pyboy import *
import os
import discord
import time
gb=None
async def launch(channel):
  for file in os.listdir("recordings"):
    os.remove("recordings/%s" %(file))
  global gb
  gb = PyBoy('rom.gb')
  gb.set_emulation_speed(10)
  skippedframes=6
  while not gb.tick():
    if len(os.listdir("recordings"))==1 or len(os.listdir("recordings"))==0:
      gb.send_input(WindowEvent.SCREEN_RECORDING_TOGGLE)
    else:
      os.remove("recordings/%s"%(os.listdir("recordings"))[0])
      gb.send_input(WindowEvent.SCREEN_RECORDING_TOGGLE)
    if len(os.listdir("recordings"))!=0:
      if skippedframes==0:
        skippedframes=50
        frame = discord.File("recordings/{}".format(os.listdir("recordings")[0]))
        await channel.send(file=frame)
        gb.tick()
        gb.tick()
        gb.tick()
        gb.tick()
        gb.tick()
        gb.tick()
        gb.tick()
        gb.tick()
        gb.tick()
        gb.tick()
        gb.tick()
        gb.tick()
      if not skippedframes==0:
        skippedframes = skippedframes-1
        continue
    pass

def getRomName():
  return gb.cartridge_title()
def stop():
  gb.stop()

def sendInput(cmd):
  if(cmd.lower() == "a"):
    gb.send_input(WindowEvent.PRESS_BUTTON_A)
  if(cmd.lower() == "s"):
    gb.send_input(WindowEvent.PRESS_BUTTON_B)
  if(cmd.lower() == "t"):
    gb.send_input(WindowEvent.PRESS_BUTTON_SELECT)
  if(cmd.lower() == "f"):
    gb.send_input(WindowEvent.PRESS_BUTTON_START)
  if(cmd.lower() == "u"):
    gb.send_input(WindowEvent.PRESS_ARROW_UP)
  if(cmd.lower() == "d"):
    gb.send_input(WindowEvent.PRESS_ARROW_DOWN)
  if(cmd.lower() == "l"):
    gb.send_input(WindowEvent.PRESS_ARROW_LEFT)
  if(cmd.lower() == "r"):
    gb.send_input(WindowEvent.PRESS_ARROW_RIGHT)