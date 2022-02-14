import os
from keep_alive import keep_alive
from discord.ext import commands
import asyncio


bot = commands.Bot(
	command_prefix="!",  # Change to desired prefix
	case_insensitive=True  # Commands aren't case-sensitive
)
bot2 = commands.Bot(command_prefix='!')
bot3= commands.Bot(command_prefix='!')
bot4= commands.Bot(command_prefix='!')
bot5= commands.Bot(command_prefix='!')


bot.author_id = enter id here  # Change to your discord id!!!

@bot.event 
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier


extensions = [
	'cogs.cog_example'  # Same name as it would be if you were importing it
]

if __name__ == '__main__':  # Ensures this is the file being ran
	for extension in extensions:
		bot.load_extension(extension)  # Loades every extension.




keep_alive()  # Starts a webserver to be pinged.
loop = asyncio.get_event_loop()
loop.create_task(bot.start('enter token here'))
loop.create_task(bot2.start('enter token here'))
#loop.create_task(bot3.start('enter token here'))
#loop.create_task(bot4.start('enter token here'))
#loop.create_task(bot5.start('enter token here'))
# you can add more if you wish you just need to copy loop.create_task(bot5.start('enter token here')) and bot5 = commands.Bot(command_prefix='!'), and change 
# and change the bot5 to bot6 and so forth with how many more bots you want to add
loop.run_forever()
