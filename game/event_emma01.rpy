


label event_emma1(replay=False):

scene x016
if incest:
    "You pass by the living room and see your mom, doing her yoga."
else:
    "You pass by the living room and see Emma, doing her yoga."
player "*** Wow, she's amazing!!!"
player "*** What a beautiful ass she has there!!!"
player "*** Those shapely round ass cheeks..."
player "*** Oh, she'll drive me crazy!!!"

if not replay:
    $ emma_corruption = 1

if incest:
    "You hold your breath and keep staring at your mom."
else:
    "You hold your breath and keep staring at Emma."
scene x017

if not replay:
    $ gallery.add(101)
    "== SCENE UNLOCKED =="

player "*** Oh, my!"
player "*** Please, stay in that position as long as possible!"
player "*** What an ass!"
player "*** It's a piece of art!!!"
player "*** Ok, now it's time to leave. Before she see me watching her."
scene x018
emma "Hey, Alex, it's you?"
player "*** Ooops, she saw me watching her, damn it!"
emma "Did you need something? I'm almost finished..."
if incest:
    emma "*** Did... did he just check me out?"
    emma "*** Like a girlfriend..."
    emma "*** Sure he is young and handsome man, but... I am his mother after all!"
else:
    emma "*** Wow, he was definitely checking me out!"
    emma "*** What a sincere compliment from such a young man!!!"
player "No, no, it's okay, it can wait..."
player "Sorry, didn't mean to interfere with your workout..."

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
