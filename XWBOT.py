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
    await client.change_presence(game=Game(name='with Gate A'))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    if message.content == '!SCP079':
        await client.send_message(message.channel,'SCP-079 is an Exidy Sorcerer microcomputer built in 1978. In 1981, its owner, █████ ██████ (deceased), a college sophomore attending ███, took it upon himself to attempt to code an AI. According to his notes, his plan was for the code to continuously evolve and improve itself as time went on. His project was completed a few months later, and after some tests and tweaks, █████ lost interest and moved on to a different brand of microcomputer. He left SCP-079 in his cluttered garage, still plugged in, and forgot about it for the next five years.')
    if message.content == '!SCP049':
        await client.send_message(message.channel,'SCP-049 is contained within a Standard Secure Humanoid Containment Cell in Research Sector-02 at Site-19. SCP-049 must be sedated before any attempts to transport it. During transport, SCP-049 must be secured within a Class III Humanoid Restriction Harness (including a locking collar and extension restraints) and monitored by no fewer than two armed guards.')
    if message.content == '!SCP1510':
        await client.send_message(message.channel,'SCP-1510 is to be kept in a standard storage compartment in the Artifact Containment section of Site 19, kept dry and cool to prevent any damage to the fragile metal. It is to be polished and checked for rust every two weeks. A D-class personnel is to wear SCP-1510 for two (2) hours every day, in order to allow interviewers and mental health personnel access to SCP-1510-1. If SCP-1510-1 exhibits any violent behavior, this procedure may be revoked at the discretion of Dr. Stevenson, project Resurgum supervisor.')
    if message.content == '!SCP734':
        await client.send_message(message.channel,'SCP-743 is to be kept in a Level-4 carbide-steel secure container, 1.5 m x 75 cm x 75 cm, no less than 5 cm thick. This container will itself be kept in a Level-4 secure room, 10 m x 10 m, with enhanced hard-metal lining. A full array of redundant sensors within the container will remain trained on SCP-743; another array of sensors will watch the container for any signs of breach. Video, audio, and data feeds from all arrays will pass to a control room manned at all times by at least two personnel. Any abnormal or aggressive activity by SCP-743 must immediately be reported to Level 4 staff.')
    if message.content == '!SCP500':
        await client.send_message(message.channel,' SCP-500 is a small plastic can which at the time of writing contains forty-seven (47) red pills. One pill, when taken orally, effectively cures the subject of all diseases within two hours, exact time depending on the severity and amount of the subject conditions. Despite extensive trials, all attempts at synthesizing more of what is thought to be the active ingredient of the pills have been unsuccessful.')
    if message.content == '!SCP2598':
        await client.send_message(message.channel,'SCP-2598 is a Large Yellow Underwing moth (Noctua pronuba) wearing a small helmet. Apart from this, and its behavior, no other anomalous characteristics are discernible.')
    if message.content == '!SCP035':
        await client.send_message(message.channel,'SCP-035 appears to be a white porcelain comedy mask, although, at times, it will change to tragedy. In these events, all existing visual records, such as photographs, video footage, even illustrations, of SCP-035 automatically change to reflect its new appearance.')
    if message.content == '!SCP714':
        await client.send_message(message.channel,'Within minutes of putting on SCP-714, wearers report feeling worn out - physically and mentally exhausted. Due to this, they will feel driven to "sit down and rest for a bit" on the nearest available furniture, and will likely fall asleep within the space of a few hours. If someone falls asleep wearing SCP-714, the only known means of waking them is to remove SCP-714, at which point they may be roused by anything that would normally wake them up. Exhaustion effects pass within two or three hours of removing SCP-714 if removed from a conscious subject; those that fall asleep wearing SCP-714 report feeling well-rested if SCP-714 is removed, even if they slept for only a few minutes.')
    if message.content == '!SCP100':
        await client.send_message(message.channel,' SCP-100 is an abandoned scrapyard eighty (80) kilometers from █████████, South Carolina, known as "Jamaican Joe Junkyard Jubilee". The scrapyard covers roughly five thousand (5,000) square meters of fenced-off land, consisting of two warehouses, a storefront, and a small residential building, as well as neglected land and land used for storage. SCP-100 holds roughly fifteen hundred (1,500) vehicles, both pressed and unpressed, as well as roughly fourteen hundred (1,400) kilograms of separate scrap, estimated to be worth $5,000 (€3,870).')
    if message.content == '!SCP106':
        await client.send_message(message.channel,'No physical interaction with SCP-106 is allowed at any time. All physical interaction must be approved by no less than a two-thirds vote from O5-Command. Any such interaction must be undertaken in AR-II maximum security sites, after a general non-essential staff evacuation. All staff (Research, Security, Class D, etc.) are to remain at least sixty meters away from the containment cell at all times, except in the event of breach events.')
    if message.content == '!SCP009':
        await client.send_message(message.channel,'SCP-009 is approximately 3,700 liters of a substance which exhibits a number of unique properties. While small amounts of the substance, in all phases, are as colorless as mundane water, en masse it takes on a distinct deep red hue.')
client.run('NDk1Mjg4MTYxNjk4NTc4NDUy.DpZXUQ.qi6ksyswjkbsK6nTVlUE848nPEk')
