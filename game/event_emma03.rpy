


label event_emma3(replay=False):

scene door
if incest:
    "Passing by mom's room you see the door closed."
else:
    "Passing by Emma's room you see the door closed."

if not replay:
    $ emma_corruption = 3

"You crack the door open and peek inside."
scene x022
player "*** Wow, what an astonishing view!!!"
player "*** She's almost naked, unbelievable!!!"
"While dressing up for work, Emma is checking herself in a large mirror."
emma "*** Yes, I do still look pretty."
emma "*** I guess, my body is quite okay."
emma "*** There's nothing wrong with men liking me!"
scene x023

if not replay:
    $ gallery.add(103)
    "== SCENE UNLOCKED =="

player "*** Oh, that ass!"
player "*** That wonderful ass!"
player "*** Only a brief view of that ass is giving me a huge boner!"
if incest:
    player "*** Mom's hot body is turning me on!!!"
else:
    player "*** Emma's hot body is turning me on!!!"
scene x024
emma "Oh, Alex? Is that you?"
emma "*** Oh, no, he's staring at me!"
emma "*** How should I react???"
player "Emmm... Sorry... I knocked, but you didn't answer..."
player "Don't worry, I closed my eyes..."
emma "Oh, thanks! You are a real gentleman!"
emma "*** Closed his eyes?! But he saw me already!"
if incest:
    emma "*** This is so wrong! He is my son!"
    player "Mom, you are gorgeous!"
else:
    player "You are a gorgeous woman, Emma..."
emma "Oh, please, stop it! Don't embarrass me, please!"
if incest:
    emma "*** He called me 'gorgeous'..."
    emma "*** Does... does it mean that he likes me... like a woman?!"
    emma "*** Oh, my god! This is so wrong!"
    player "Sorry, mom! I'm leaving!"
else:
    emma "*** He called me 'gorgeous'... He likes me!"
    player "Ok, I'm leaving, sorry for the embarrassment!"

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
