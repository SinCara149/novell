


label event_emma5(replay=False):

scene door
"When you reach the bathroom, the door is closed."
if incest:
    player "*** Seems mom is taking a bath..."
else:
    player "*** Seems Emma is taking a bath..."

if not replay:
    $ emma_corruption = 5

"You crack the door open and peek inside."
scene x001
player "*** Wow, she's absolutely naked!"
player "*** That gorgeous body is amazing!!!"
player "*** I love every inch of it!"
if incest:
    "You hold your breath and keep staring at your mom."
else:
    "You hold your breath and keep staring at Emma."
scene x002

if not replay:
    $ gallery.add(105)
    "== SCENE UNLOCKED =="

player "*** I guess, I'm quite safe here, she won't notice me..."
player "*** Besides, the water is running..."
player "*** What a view!!!"
player "*** I believe, I should be peeking more often!!!"
player "*** Oh, my! I'm having a boner!"
player "*** Although, it's no surprise to me..."
scene x003
"All of a sudden, the water stops running."
emma "Alex, is that you?"
player "*** Damn it! She knows I'm here!"
player "Emmm, yes..."
emma "Oh, ok... It's just that I can't see very well without my glasses..."
player "I'm sorry, I wanted to take a shower..."
player "The door was unlocked..."
player "And I didn't realize that you were here..."
emma "I'll be out in five minutes tops..."
player "Ok, I'll wait outside."
emma "And next time, please, knock before entering!"

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
