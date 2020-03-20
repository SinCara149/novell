


label event_emma4(replay=False):

scene x025
if incest:
    "You enter the living room and see your mom there. She didn't notice you at once."
else:
    "You enter the living room and see Emma there. She didn't notice you at once."
"She yawns and stretches her back."
"And her top just slips off her tits revealing even her nipples."
emma "*** Oh my! I had such a long day at work..."
emma "*** I feel so exhausted..."
player "*** Wow!!!"
player "*** That's much better than watching TV!!!"
player "*** Wish I could touch her!!!"

if not replay:
    $ emma_corruption = 4

if incest:
    "You hold your breath and keep staring at your mom."
else:
    "You hold your breath and keep staring at Emma."
scene x026

if not replay:
    $ gallery.add(104)
    "== SCENE UNLOCKED =="

player "*** Wow!!!"
player "*** Those hardened nipples!!!"
player "*** I will be seeing them in my dreams!!!"
emma "Alex?!"
player "You... your... your top..."
scene x027
emma "Oh my god! Please, stop looking at me!"
emma "*** Oh, I feel so ashamed now!"
emma "*** How couldn't I notice it?"
player "*** Wow, she's so shy! And beautiful!"
emma "*** Oh my! I think I just saw his penis!"
emma "*** But why is it so big???"
if incest:
    emma "*** I... I should not stare at him like that! He is my son!"
player "I came here to watch TV... I had no idea you were here, too... Sorry!"

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
