import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(game=Game(name='      '))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    if message.content == '!SCP173':
        await client.send_message(message.channel,'SCP-173 is to be kept in a locked container at all times. When personnel must enter SCP-173 container, no fewer than 3 may enter at any time and the door is to be relocked behind them. At all times, two persons must maintain direct eye contact with SCP-173 until all personnel have vacated and relocked the container.')
    if message.content == '!SCP079':
        await client.send_message(message.channel,'SCP-079 is an Exidy Sorcerer microcomputer built in 1978. In 1981, its owner, █████ ██████ (deceased), a college sophomore attending ███, took it upon himself to attempt to code an AI. According to his notes, his plan was for the code to continuously evolve and improve itself as time went on. His project was completed a few months later, and after some tests and tweaks, █████ lost interest and moved on to a different brand of microcomputer. He left SCP-079 in his cluttered garage, still plugged in, and forgot about it for the next five years.')
    if message.content == '!SCP049':
        await client.send_message(message.channel,'SCP-049 is contained within a Standard Secure Humanoid Containment Cell in Research Sector-02 at Site-19. SCP-049 must be sedated before any attempts to transport it. During transport, SCP-049 must be secured within a Class III Humanoid Restriction Harness (including a locking collar and extension restraints) and monitored by no fewer than two armed guards.')
if message.content == '!SCP1510':
    await client.send_message(message.channel,'SCP-1510 is to be kept in a standard storage compartment in the Artifact Containment section of Site 19, kept dry and cool to prevent any damage to the fragile metal. It is to be polished and checked for rust every two weeks. A D-class personnel is to wear SCP-1510 for two (2) hours every day, in order to allow interviewers and mental health personnel access to SCP-1510-1. If SCP-1510-1 exhibits any violent behavior, this procedure may be revoked at the discretion of Dr. Stevenson, project Resurgum supervisor.
client.run('NDk1Mjg4MTYxNjk4NTc4NDUy.DpGQVQ.AtNKmv_uqEyyFpk_75GyxqvEy04')                              
