


label event_emma7(replay=False):

scene door
if incest:
    "Passing by mom's room you see the door closed."
else:
    "Passing by Emma's room you see the door closed."
player "*** Should I peek or just pass by?!"

if not replay:
    $ emma_corruption = 7

player "*** Oh, hell! Why not to a chance?!"
player "*** Besides, I can always say that I was 'just passing by'..."
"So, you peek inside..."
scene x010
"And freeze."
"There she is: standing in front of the mirror."
"Critically studying herself."
if incest:
    "You hold your breath and keep staring at your mom."
else:
    "You hold your breath and keep staring at Emma."
scene x011

if not replay:
    $ gallery.add(107)
    "== SCENE UNLOCKED =="

player "*** Wooowww!!! That dress is something!!!"
player "*** Oh, my! She's bending over!"
player "*** Yeah, that's right!!!"
player "*** I... I can see her... her ass now?!"
player "*** Is she wearing nothing under that dress?!"
player "*** Hmm, that's strange! But hot, very hot!!!"
emma "Hey, Alex, is that you?"
player "*** Oh, fuck!"
player "Yes..."
emma "Why are you standing on the threshold? Come on in!"
player "Oh, okay, fine!"
scene x012
emma "What do you think of this dress?!"
player "Apart from the fact that it's insanely hot?!"
emma "..."
player "And what's the occasion?"
emma "Oh, nothing serious... I'm going on a date..."
player "A date?!"
player "*** Holy shit! In this???"
emma "Yes, a date... A friend of mine has set me up on a date... a blind date..."
emma "I thought it would be nice to wear something sexy..."
player "But it's too sexy... Especially for a first date... Don't you think???"
emma "Oh, you don't get it, do you?!"
emma "It's a trendy lace dress, and I..."
player "*** I would bang you myself, but there's no polite way to say it..."
player "Yes, but it's too hot... Wouldn't you prefer to wear something more conservative?!"
emma "Oh, come on! You don't get it!!!"
emma "Forget that we had this conversation!!!"

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
