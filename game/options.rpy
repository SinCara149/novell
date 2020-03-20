define config.developer = True
define config.rollback_enabled = True
define config.allow_skipping = True

define limited_edition = False
define incest = False

define config.name = _("Blossoming Love")
define gui.show_name = True
define config.version = "14"
define gui.about = _("")
define build.name = "BL"
define config.has_sound = False
define config.has_music = False
define config.has_voice = False
define config.enter_transition = None
define config.exit_transition = None
define config.after_load_transition = None
define config.end_game_transition = None
define config.window = "auto"
define config.window_show_transition = None
define config.window_hide_transition = None
default preferences.text_cps = 30
default preferences.afm_time = 15
define config.save_directory = "BL-8511451177"
define config.window_icon = "gui/window_icon.png"

init python:

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.rpy', None)
    build.classify("game/**.rpyc", "archive")
    build.classify("game/**.mp3", "archive")
    build.classify("game/**.ttf", "archive")
    build.documentation('*.html')
    build.documentation('*.txt')

    build.classify("game/gui/**.png", "archive")
    build.classify("game/gui/**.jpg", "archive")

    build.classify("game/images/*.png", "archive")
    build.classify("game/images/*.jpg", "archive")
    build.classify("game/images/gallery/*.png", "archive")
    build.classify("game/images/gallery/*.jpg", "archive")
    build.classify("game/images/photostudio/*.png", "archive")
    build.classify("game/images/photostudio/*.jpg", "archive")
    build.classify("game/images/playground/*.png", "archive")
    build.classify("game/images/playground/*.jpg", "archive")

    build.classify("game/images/animation/**.jpg", "archive")
    if limited_edition:
        build.classify("game/images/animation/**.png", "archive")
    else:
        build.classify("game/images/animation/**.png", None)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
