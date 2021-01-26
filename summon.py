import random
import requests

# Artifact and Hero Pools. Each value represents the _id attribute in the JSON format for the corresponding artifact/unit in https://api.epicsevendb.com/.

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

    # Randomly selects a summon.
    if rand_num < 0.025:
        hero = random.choice(ml5_pool)
        rarity = "5"
    elif rand_num >= 0.025 and rand_num < 0.3:
        hero = random.choice(ml4_pool)
        rarity = "4"
    else:
        hero = random.choice(ml3_pool)
        rarity = "3"

    # Retrieves information from the database and puts relevant info in a dict.
    hero_data = requests.get("https://api.epicsevendb.com/hero/" + hero)
    hero_data_json = hero_data.json()
    img = hero_data_json["results"][0]["assets"]["icon"]
    hero_name = hero_data_json["results"][0]["name"]

    summon_dict = dict()
    summon_dict["name"] = hero_name
    summon_dict["rarity"] = rarity
    summon_dict["img"] = img

    return summon_dict

def covenant():
    """ Returns dict of summon name, type, rarity, img url."""
    rand_num = random.random()
    summon = None
    rarity = None
    type = None
    moonlight = None

    # Randomly selects a summon.
    if rand_num < 0.0015:
        summon = random.choice(ml5_pool)
        rarity = "5"
        type = "hero"
        moonlight = True
    elif rand_num >= 0.0015 and rand_num < 0.0065:
        summon = random.choice(ml4_pool)
        rarity = "4"
        type = "hero"
        moonlight = True
    elif rand_num >= 0.0065 and rand_num < 0.05:
        summon = random.choice(ml3_pool)
        rarity = "3"
        type = "hero"
        moonlight = True
    elif rand_num >= 0.05 and rand_num < 0.0625:
        summon = random.choice(hero5_pool)
        rarity = "5"
        type = "hero"
        moonlight = False
    elif rand_num >= 0.0625 and rand_num < 0.1075:
        summon = random.choice(hero4_pool)
        rarity = "4"
        type = "hero"
        moonlight = False
    elif rand_num >= 0.1075 and rand_num < 0.5175:
        summon = random.choice(hero3_pool)
        rarity = "3"
        type = "hero"
        moonlight = False
    elif rand_num >= 0.5175 and rand_num < 0.535:
        summon = random.choice(artifact5_pool)
        rarity = "5"
        type = "artifact"
        moonlight = False
    elif rand_num >= 0.535 and rand_num < 0.6:
        summon = random.choice(artifact4_pool)
        rarity = "4"
        type = "artifact"
        moonlight = False
    else:
        summon = random.choice(artifact3_pool)
        rarity = "3"
        type = "artifact"
        moonlight = False

    # Retrieves information from the database and puts relevant info in a dict.
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
    summon_dict["moonlight"] = moonlight
    summon_dict["img"] = img

    return summon_dict