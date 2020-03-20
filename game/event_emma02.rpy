


label event_emma2(replay=False):

scene kitchen_morning
"You enter the kitchen hoping to drink some coffee..."
scene kitchen_morning_blur
show emma neutral at center
if incest:
    "And bump into your mom."
else:
    "And bump into Emma."

emma "Oh, hi there! Would you like some coffee?"
player "Oh, I would die for it!"
show emma smile at center
emma "Haha, no need to die!"
scene x019
emma "Here you go!"
player "Oh, thanks, you are a savior!"
player "*** Oh, my!"
player "*** Why is she leaning like that?"
player "*** Doesn't she realize that I can see that deep cleavage of hers?!"
if incest:
    player "*** She is my mom after all..."

if not replay:
    $ emma_corruption = 2

"You take a sip and keep staring at Emma."
scene x020

if not replay:
    $ gallery.add(102)
    "== SCENE UNLOCKED =="

player "*** Wow!!!"
player "*** I wish I could touch that soft velvet skin of hers!"
player "*** Those boobs are just staring at me, calling for action!!!"
emma "Is it ok with you?!"
player "What? I'm sorry, you were saying..."
scene x021
emma "Hey, are you dreaming?"
emma "I was saying that you can have a spare key..."
emma "*** Oh, my! I feel so embarrassed!"
emma "*** He's looking at my breasts!"
if incest:
    emma "*** That's wrong!"
    emma "*** He is my son!"
emma "*** What should I do now?"
player "*** I should stop looking at her or she'll notice it!"
emma "*** His long stare makes me all wet down there, it's not good!"
emma "Ok, I'm in a hurry, have a nice day!"

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
