import random
import requests
from os import getenv
from dotenv import load_dotenv
from discord import Embed
from discord.ext import commands

artifact5_pool = ["a-little-queens-huge-crown", "abyssal-crown", "alabastron", "alencinoxs-wrath", "alexas-basket", "ancient-dragons-legacy",
"bastion-of-perlutia", "black-hand-of-the-goddess", "bloodstone", "bloody-rose", "border-coin", "celestine", "circus-fantasia",
"cradle-of-life", "creation-destruction", "crimson-moon-of-nightmares", "crown-of-glory", "dignus-orb", "doctors-bag", "doubleedged-decrescent",
"durandal", "dux-noctis", "elbris-ritual-sword", "eticas-scepter", "holy-sacrifice", "idols-cheer", "iron-fan", "justice-for-all", "last-teatime",
"manica-of-control", "merciless-glutton", "noble-oath", "rhianna-luciella", "rise-of-a-monarch", "rod-of-amaryllis", "samsara-prayer-beads",
"secret-art-storm-sword", "shepherd-of-the-hollow", "shimadra-staff", "sigurd-scythe", "snow-crystal", "song-of-stars", "spirits-breath",
"stella-harpa", "sword-of-judgment", "sword-of-summer-twilight", "time-matter", "touch-of-rekos", "uberiuss-tooth", "unseen-observer",
"violet-talisman", "wind-rider"]

artifact4_pool = ["adamant-shield", "andres-crossbow", "aurius", "barthezs-orbuculum", "dust-devil", "els-fist", "elyhas-knife", "eternus",
"hell-cutter", "hilag-lance", "infinity-basket", "kaladra", "magarahas-tome", "moonlight-dreamblade", "rosa-hargana", "sashe-ithanes", "sepulcrum",
"silver-rain", "siraren", "steadfast-gatekeeper", "strak-gauntlet", "tagehels-ancient-book", "waters-origin", "wondrous-potion-vial"]

artifact3_pool = ["alsacian-spear", "ancient-sheath", "aqua-rose", "ascending-axe", "atmas-portal", "butterfly-mandolin", "cursed-compass",
"daydream-joker", "devils-brand", "egg-of-delusion", "envoys-pipe", "exorcists-tonfa", "forest-totem", "goblins-lamp", "grail-of-blood",
"labyrinth-cube", "mighty-yaksha", "oath-key", "prophetic-candlestick", "ranons-memorandum", "sword-of-the-morning", "timeless-anchor"]

hero5_pool = ["alencia", "aramintha", "baal-sezan", "basar", "bellona", "cecilia", "celine", "cermia", "charles", "charlotte", "chloe", "choux",
"destina", "elena", "ervalen", "flan", "haste", "iseria", "kawerik", "kayron", "ken", "kise", "krau", "lidica", "lilias", "lilibet", "ludwig", "luluca", "melissa",
"mort", "mui", "pavel", "ravi", "ray", "roana", "sez", "sigret", "tamarinne", "tenebria", "tywin", "vildred", "violet", "vivian", "yufine"]

hero4_pool = ["achates", "angelica", "armin", "cartuja", "cidd", "clarissa", "coli", "corvus", "crozet", "dingo", "dominiel", "furious", "karin", "khawana",
"khawazu", "leo", "lots", "maya", "purrgis", "rin", "romann", "rose", "schuri", "silk", "surin", "zerato"]

hero3_pool = ["adlay", "ains", "aither", "alexa", "azalea", "butcher-corps-inquisitor", "carmainerose", "carrot", "church-of-ilryos-axe", "enott", "glenn",
"godmother", "hataan", "hazel", "helga", "ian", "jecht", "jena", "judith", "kiris", "kluri", "lena", "mistychain", "montmorancy", "mucacha", "nemunas", "pearlhorizon",
"rima", "roozid", "taranor-guard", "taranor-royal-guard", "tieria", "wanda"]

ml5_pool = ["ambitious-tywin", "apocalypse-ravi", "arbiter-vildred", "archdemons-shadow", "blood-moon-haste", "briar-witch-iseria", "dark-corvus",
"desert-jewel-basar", "faithless-lidica", "fallen-cecilia", "maid-chloe", "martial-artist-ken", "operator-sigret", "remnant-violet",
"ruele-of-light", "sage-baal-sezan", "silver-blade-aramintha", "specter-tenebria", "top-model-luluca"]

ml4_pool = ["assassin-cartuja", "assassin-cidd", "assassin-coli", "benevolent-romann", "blaze-dingo", "blood-blade-karin", "celestial-mercedes",
"challenger-dominiel", "champion-zerato", "crescent-moon-rin", "crimson-armin", "fighter-maya", "general-purrgis", "guider-aither",
"kitty-clarissa", "roaming-warrior-leo", "shadow-rose", "shooting-star-achates", "sinful-angelica", "tempest-surin", "troublemaker-crozet",
"wanderer-silk", "watcher-schuri"]

ml3_pool = ["ainos", "arowell", "batisse", "celeste", "church-of-ilryos-axe", "doris", "eaton", "elson", "gunther", "hurado", "lorina", "mirsa",
"gloomyrain", "otillie", "pyllis", "requiemroar", "rikoris", "sonia", "sven", "wanda"]

def moonlight():
    """ Returns dict of summon name, type, rarity, img url."""
    rand_num = random.random()
    hero = None
    rarity = None

    if rand_num < 0.025:
        hero = random.choice(ml5_pool)
        rarity = "5"
    elif rand_num >= 0.025 and rand_num < 0.3:
        hero = random.choice(ml4_pool)
        rarity = "4"
    else:
        hero = random.choice(ml3_pool)
        rarity = "3"
    
    hero_data = requests.get("https://api.epicsevendb.com/hero/" + hero)
    hero_data_json = hero_data.json()
    img = hero_data_json["results"][0]["assets"]["icon"]
    hero_name = hero_data_json["results"][0]["name"]

    summon_dict = dict()
    summon_dict["name"] = hero_name
    summon_dict["type"] = "hero"
    summon_dict["rarity"] = rarity
    summon_dict["img"] = img

    return summon_dict

def covenant():
    """ Returns dict of summon name, type, rarity, img url."""
    rand_num = random.random()
    summon = None
    rarity = None
    type = None

    if rand_num < 0.0015:
        summon = random.choice(ml5_pool)
        rarity = "5"
        type = "hero"
    elif rand_num >= 0.0015 and rand_num < 0.0065:
        summon = random.choice(ml4_pool)
        rarity = "4"
        type = "hero"
    elif rand_num >= 0.0065 and rand_num < 0.05:
        summon = random.choice(ml3_pool)
        rarity = "3"
        type = "hero"
    elif rand_num >= 0.05 and rand_num < 0.0625:
        summon = random.choice(hero5_pool)
        rarity = "5"
        type = "hero"
    elif rand_num >= 0.0625 and rand_num < 0.1075:
        summon = random.choice(hero4_pool)
        rarity = "4"
        type = "hero"
    elif rand_num >= 0.1075 and rand_num < 0.5175:
        summon = random.choice(hero3_pool)
        rarity = "3"
        type = "hero"
    elif rand_num >= 0.5175 and rand_num < 0.535:
        summon = random.choice(artifact5_pool)
        rarity = "5"
        type = "artifact"
    elif rand_num >= 0.535 and rand_num < 0.6:
        summon = random.choice(artifact4_pool)
        rarity = "4"
        type = "artifact"
    else:
        summon = random.choice(artifact3_pool)
        rarity = "3"
        type = "artifact"

    if type == "hero":
        summon_data = requests.get("https://api.epicsevendb.com/hero/" + summon)
    else:
        summon_data = requests.get("https://api.epicsevendb.com/artifact/" + summon)

    summon_data_json = summon_data.json()
    img = summon_data_json["results"][0]["assets"]["icon"]
    summon_name = summon_data_json["results"][0]["name"]

    summon_dict = dict()
    summon_dict["name"] = summon_name
    summon_dict["type"] = type
    summon_dict["rarity"] = rarity
    summon_dict["img"] = img

    return summon_dict


heroes_dict = dict()
heroes_data = requests.get("https://api.epicsevendb.com/hero")
heroes_data_json = heroes_data.json()

for hero in heroes_data_json["results"]:
    heroes_dict[hero["name"].lower()] = hero["_id"].lower()

load_dotenv()
TOKEN = getenv('DISCORD_TOKEN')

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

    response = "The gear score for " + hero_name + " is: " + str(gear_score) + "."
    await ctx.send(response)

@bot.command(name='compare', help=help_c, aliases=["c"])
async def compare(ctx):
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

@bot.command(name='roll', help="Moonlight or covenant summons.", aliases=["r"])
async def compare(ctx, *args):
    if len(args) < 1:
        await ctx.send("Wrong format. Type u!r m or u!r c.")
        return

    if args[0] == "m" or args[0] == "moonlight":
        summon_dict = moonlight()
        response = "You have summoned " + summon_dict["rarity"] + "* " + summon_dict["type"] + " " + summon_dict["name"] + "!"
        embed = Embed()
        embed.set_image(url=summon_dict["img"])
        await ctx.send(response, embed=embed)
        return

    elif args[0] == "c" or args[0] == "covenant":
        summon_dict = covenant()
        response = "You have summoned " + summon_dict["rarity"] + "* " + summon_dict["type"] + " " + summon_dict["name"] + "!"
        embed = Embed()
        embed.set_image(url=summon_dict["img"])
        await ctx.send(response, embed=embed)
        return

    else:
        await ctx.send("Wrong format. Type u!r m or u!r c.")


@bot.command(name='roll-10', help="3* simulator... x10", aliases=["r10"])
async def compare(ctx, args):
    if len(args) < 1:
        await ctx.send("Wrong format. Type u!r m or u!r c.")
        return

    if args[0] == "m" or args[0] == "moonlight":
        for x in range(10):
            summon_dict = moonlight()
            response = "You have summoned " + summon_dict["rarity"] + "* " + summon_dict["type"] + " " + summon_dict["name"] + "!"
            embed = Embed()
            embed.set_image(url=summon_dict["img"])
            await ctx.send(response, embed=embed)
        return

    elif args[0] == "c" or args[0] == "covenant":
        for x in range(10):
            summon_dict = covenant()
            response = "You have summoned " + summon_dict["rarity"] + "* " + summon_dict["type"] + " " + summon_dict["name"] + "!"
            embed = Embed()
            embed.set_image(url=summon_dict["img"])
            await ctx.send(response, embed=embed)
        return

    else:
        await ctx.send("Wrong format. Type u!r10 m or u!r10 c.")

bot.run(TOKEN)