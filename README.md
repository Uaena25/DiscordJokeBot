# Epic-Seven-Discord-Bot
Discord bot for Epic Seven. Can calculate equipment substat score, check how much stats is needed to reach a desired amount,
and included a simulator for the Moonlight/Covenant summons.


Link to add the bot to your own Discord server: https://discord.com/oauth2/authorize?client_id=795393055167348756&scope=bot

Bot is only active if my computer is on.

Commands:

compare | c

Calculates how much percentage of a stat needed to reach the desired number of that stat.

Acceptable stat parameters: hp, def, atk

Example: u!c sage def 1428 1546

Example: u!compare kayron atk 3859 4000

gear_score | gs

Calculates gear score of the weapon substats for that character. Must put four stats; if only adding relevant stats, use 0 for useless subs.

Acceptable stat parameters:

"h%", "hp%", "a%", "atk%", "d%", "def%", "e", "eff", "er", "effres", "h", "hp", "a", "atk", "d", "def", "s", "spd", "cc", "crit", "cd", "cdmg"

Example: u!gs arbiter crit 8 cdmg 35 atk% 8 spd 12

Example: u!gear_score magic scholar doris h% 25 h 400 a% 0 er 12

roll | r

Moonlight or covenant summon.

Example: u!r m

Example: u!r c


roll-10 | r10

Moonlight or covenant summon x10

Example: u!r10 m

Example: u!r10 c
