import os
import requests
from dotenv import load_dotenv
from discord.ext import commands

heroes_dict = dict()
heroes_data = requests.get("https://api.epicsevendb.com/hero")
heroes_data_json = heroes_data.json()
for hero in heroes_data_json["results"]:
    heroes_dict[hero["name"].lower()] = hero["_id"].lower()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='u!')

help_gs = """Calculates gear score of the weapon for that character.
Acceptable stat parameters:
"h%", "hp%", "a%", "atk%", "d%", "def%", "e", "eff", "er", "effres", "h", "hp", "a", "atk", "d", "def", "s", "spd", "cc", "crit", "cd", "cdmg"
Example: u!gs arbiter crit 8 cdmg 35 atk% 8 spd 12
Example: u!gear_score magic scholar doris h% 25 h 400 d% 8 er 12"""

help_c = """Calculates how much percentage of a stat needed to reach the desired number of that stat.
Acceptable stat parameters: hp, def, atk
Example: u!c sage def 1428 1546
Example: u!compare kayron atk 3859 4000"""

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='gear_score', help=help_gs, aliases=["gs"])
async def gear_score(ctx):
    print("Calclating gear score.")
    message = ctx.message.content.split()[1:]

    if len(message) < 9:
        await ctx.send("Wrong format. Use u!help gear_score or u!help gs for examples.")
        return

    hero = " ".join(message[0:-8]).lower()
    stats = message[-8:]
    hero_id = None
    hero_name = None

    for h in heroes_dict.keys():
        if h.lower().startswith(hero):
            hero_id = heroes_dict[h]
            hero_name = h
            break

    if hero_id == None:
        await ctx.send("Cannot find hero.")
        return

    hero_data = requests.get("https://api.epicsevendb.com/hero/" + hero_id)
    hero_data_json = hero_data.json()
    hero_stats_dict = hero_data_json["results"][0]["calculatedStatus"]["lv60SixStarFullyAwakened"]

    gear_score = 0
    percent_stat_list = ["h%", "hp%", "a%", "atk%", "d%", "def%", "e", "eff", "er", "effres"]
    try:
        # The last three stats have more weight than the regular percentage stats.
        for i in range(0, len(stats)-1, 2):
            if stats[i] in percent_stat_list:
                gear_score += int(stats[i+1])
            elif stats[i] == "h" or stats[i] == "hp":
                gear_score += int(stats[i+1])*100/int(hero_stats_dict["hp"])
            elif stats[i] == "a" or stats[i] == "atk":
                gear_score += int(stats[i+1])*100/int(hero_stats_dict["atk"])
            elif stats[i] == "d" or stats[i] == "def":
                gear_score += int(stats[i+1])*100/int(hero_stats_dict["def"])
            elif stats[i] == "s" or stats[i] == "spd":
                gear_score += int(stats[i+1])*2
            elif stats[i] == "cc" or stats[i] == "crit":
                gear_score += int(stats[i+1])*1.6
            elif stats[i] == "cd" or stats[i] == "cdmg":
                gear_score += int(stats[i+1])*1.1429
            else:
                await ctx.send("Wrong format for stats. Use u!help gear_score or u!help gs for examples")
                return
   
    except:
        await ctx.send("An error occured while calculating stats.")
        return

    response = "The gear score for " + hero_name + " is: " + str(gear_score)
    await ctx.send(response)

@bot.command(name='compare', help=help_c, aliases=["c"])
async def compare(ctx):
    print("Comparing stat difference.")

    message = ctx.message.content.split()[1:]

    if len(message) < 4:
        await ctx.send("Wrong format. Use u!help compare or u!help c for examples.")
        return

    hero = " ".join(message[0:-3]).lower()
    stats = message[-3:]
    hero_id = None
    hero_name = None

    if stats[0] not in ["atk", "def", "hp"]:
        await ctx.send("Wrong format. Use u!help compare or u!help c for examples.")
        return

    for h in heroes_dict.keys():
        if h.lower().startswith(hero):
            hero_id = heroes_dict[h]
            hero_name = h
            break

    if hero_id == None:
        await ctx.send("Cannot find hero.")
        return

    hero_data = requests.get("https://api.epicsevendb.com/hero/" + hero_id)
    hero_data_json = hero_data.json()
    hero_stats_dict = hero_data_json["results"][0]["calculatedStatus"]["lv60SixStarFullyAwakened"]

    try:
        stat_difference = int(stats[2])-int(stats[1])
        percentage = stat_difference*100/int(hero_stats_dict[stats[0]])

    except:
        await ctx.send("An error occured while calculating stats.")
        return
    
    response = "The stat difference for " + hero_name + " is: " + str(percentage) + " percent."
    await ctx.send(response)

bot.run(TOKEN)