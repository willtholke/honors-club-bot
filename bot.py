import discord
import random

client = discord.Client()
finals_words = ["bot bad", "bad bot", "bot average", "bot mediocre"]
encouragements = [
    "I disapprove of your sentiment.",
    "You're entitled to your opinion.",
    "Maybe so, maybe not.",
    "Hmm...\n\n\n\n\n\n\n\nEnjoy this empty white space.",
    "Interesting statement, **but wrong**."
]


@client.event
async def on_ready():
    """ Indicate when bot is ready to start being used and change bot
    activity/presence.
    """
    print("Logged in as {0.user}!".format(client))
    await client.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching,
        name='finals week'))


@client.event
async def on_message(message):
    """ Receive user input and send responses through Discord. """
    if message.author == client.user:
        return

    msg = message.content

    if any(word in msg for word in finals_words):
        await message.channel.send(random.choice(encouragements))

    if message.content.startswith('bot good'):
        await message.channel.send('Thank you, {0.author.mention}!'.format(message))

    if message.content.startswith('$uc'):
        await message.channel.send('**University of California Fall 2021 Admissions Dates:**\n'
                                   '__UC Berkeley Admissions Date:__ April 23rd, 2021\n'
                                   '__UC Davis Admissions Date:__ April 16th, 2021\n'
                                   '__UC Irvine Admissions Date:__ April 9th, 2021\n'
                                   '__UCLA Admissions Date:__ April 23rd, 2021\n'
                                   '__UC Merced Admissions Date:__ rolls out in batches starting mid-March\n'
                                   '__UC Riverside Admissions Date:__ rolls out in batches starting early March\n'
                                   '__UC San Diego Admissions Date:__ around April 23rd, 2021\n'
                                   '__UC Santa Barbara Admissions Date:__ April 21, 2021\n'
                                   '__UC Santa Cruz Admissions Date:__ March 17, 2021\n')


@client.event
async def on_member_join(member):
    """ Welcome new users in DM. """
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to the Honors Scholars Club Discord server!\n'
        f'Please change your username to your first name & last initial _ex: John S._ so we know who you are.\n'
        f'Head over to #introductions and introduce yourself!'
    )


client.run('ODI0NzkwNDc2NTMxMDQwMzA3.YF0f_Q._YzQvLC6hM6DMdyH8vaTPbHuAf0')
