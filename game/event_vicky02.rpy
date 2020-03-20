


label event_vicky2(replay=False):

scene door
if incest:
    "When you approach the bathroom you hear your sister singing inside."
else:
    "When you approach the bathroom you hear Vicky singing inside."
player "*** Seems Vicky is taking a bath..."

if not replay:
    $ vicky_corruption = 2

"You step to the door and open it a crack..."
scene x004
player "*** I guess, one or two quick glances will do no harm..."
player "*** Oh, my!"
player "*** She is gorgeous!"
player "*** That body is perfect, absolutely perfect!!!"
scene x005

if not replay:
    $ gallery.add(202)
    "== SCENE UNLOCKED =="

"All of a sudden, Vicky starts talking to you."
vicky "Hey, pass me the towel, will you please?!"
player "..."
vicky "Hurry up, I can't see a thing!!!"
player "*** Oh, now I get it: her eyes are closed!"
player "*** Maybe, I shouldn't hurry, after all?!"
vicky "Hey, where is it? The towel?!"
"Very slowly, unwilling to do it, you hand the towel over to her."
player "Okay, here you go!"
scene x006
"Vicky opens her eyes and sees you. She hastily covers herself with the towel you gave her."
if incest:
    vicky "Hey, brother!!! What the hell are you doing here???"
else:
    vicky "Hey!!! What are you doing here???"
player "Emmm... Well... I just wanted to take a shower..."
player "I... I didn't mean to stare at you like... like... this..."
vicky "Oh, really?"
player "Yes! Besides, you didn't lock the door..."
vicky "That's because I never lock it!"
player "Oh?!"
vicky "That's because you were not supposed to be here!"
if incest:
    vicky "Besides, peeking at your elder sister is weird, do you realize it?"
else:
    vicky "I mean, I'm not used to men around the house!"
player "Really?! Then who, do you think, it was?"
vicky "Mom! Not you!"
player "Ok, I'm sorry! I'm not much of a gentleman..."
if incest:
    vicky "Exactly my point! A gentleman wouldn't be staring at his naked sister!"
else:
    vicky "Exactly my point! A gentleman wouldn't be staring at a naked girl!"
vicky "Making her blush..."
player "Oh, you blushed?!"
vicky "Of course, I did! A little..."
player "..."
vicky "So? Are you leaving or not?!"
player "Actually, I hoped that I could take a shower..."
vicky "Ok, fine! I'm leaving!!!"

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
