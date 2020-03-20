










init -1 style default:
    font gui.default_font
    size gui.text_size
    color gui.text_color
    language gui.language

init -1 style input:
    color gui.accent_color

init -1 style hyperlink_text:
    color gui.accent_color
    hover_color gui.hover_color
    hover_underline True


init -1 style gui_text:
    font gui.interface_font
    color gui.interface_text_color
    size gui.interface_text_size


init -1 style button:
    properties gui.button_properties("button")

init -1 style button_text is gui_text:
    properties gui.button_text_properties("button")
    yalign 0.5


init -1 style label_text is gui_text:
    color gui.accent_color
    size gui.label_text_size

init -1 style prompt_text is gui_text:
    color gui.text_color
    size gui.interface_text_size


init -1 style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

init -1 style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

init -1 style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

init -1 style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

init -1 style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

init -1 style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


init -1 style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)





















init -501 screen say(who, what):
    style_prefix "say"
    window:
        id "window"
        if who is not None:
            window:
                style "namebox"
                text who id "who"
        text what id "what"



    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

init -1 style window is default
init -1 style say_label is default
init -1 style say_dialogue is default
init -1 style say_thought is say_dialogue
init -1 style namebox is default
init -1 style namebox_label is say_label

init -1 style window:
    xalign 0.5
    xfill True
    yalign 1.0
    ysize 150
    background Image("gui/textbox.png", xalign=0.5, yalign=0.0)

init -1 style namebox:
    xpos 250
    ypos 10

init -1 style say_label:
    color gui.accent_color
    font gui.name_font
    size gui.name_text_size
    xalign gui.name_xalign
    yalign 0.5
    outlines [(absolute(1), "#333", absolute(1), absolute(1))]

init -1 style say_dialogue:
    xpos 300
    xsize 1420
    ypos 50
    outlines [(absolute(1), "#333", absolute(1), absolute(1))]












init -501 screen input(prompt):
    style_prefix "input"

    window:

        has vbox:
            xpos gui.text_xpos
            xanchor gui.text_xalign
            ypos gui.text_ypos

        text prompt style "input_prompt"
        input id "input"


init -1 style input_prompt is default

init -1 style input_prompt:
    xmaximum gui.text_width
    xalign gui.text_xalign
    text_align gui.text_xalign

init -1 style input:
    xmaximum gui.text_width
    xalign gui.text_xalign
    text_align gui.text_xalign









init -501 screen choice(items):
    style_prefix "choice"
    vbox:
        for i in items:
            textbutton i.caption action i.action

define -1 config.narrator_menu = True

init -1 style choice_vbox is vbox
init -1 style choice_button is button
init -1 style choice_button_text is button_text

init -1 style choice_vbox:
    xalign 0.0
    yalign 0.5
    xoffset 10
    spacing 10

init -1 style choice_button is default:
    background "#1A5276AA"
    hover_background "#2471A3AA"
    insensitive_background "#BDC3C755"
    xsize 500
    ysize 50

init -1 style choice_button_text is default:
    size 24
    idle_color "#FFF"
    hover_color "#FFF"
    insensitive_color "#AAA"
    xalign 0.5
    yalign 0.5
    outlines [(absolute(1), "#333", absolute(1), absolute(1))]







init -501 screen quick_menu():


    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Prefs") action ShowMenu('preferences')




init -1 python:
    config.overlay_screens.append("quick_menu")

default -1 quick_menu = False

init -1 style quick_button is default
init -1 style quick_button_text is button_text

init -1 style quick_button:
    properties gui.button_properties("quick_button")

init -1 style quick_button_text:
    properties gui.button_text_properties("quick_button")











init -501 screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Start") action Start()

        else:

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("More Games") action OpenURL("https://discord.gg/AxyR9Wu")
        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        textbutton _("Patreon") action OpenURL("https://www.patreon.com/slonique")

        if renpy.variant("pc"):


            textbutton _("Help") action ShowMenu("help")


            textbutton _("Quit") action Quit(confirm=not main_menu)


init -1 style navigation_button is gui_button
init -1 style navigation_button_text is gui_button_text

init -1 style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

init -1 style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
    idle_color "#888"








init -501 screen main_menu():
    tag menu



    style_prefix "main_menu"

    add gui.main_menu_background


    frame




    use navigation

    if gui.show_name:
        vbox:
            text "Update [config.version]":
                style "main_menu_version"

    if limited_edition:
        add "limited_edition.png"

init -1 style main_menu_frame is empty
init -1 style main_menu_vbox is vbox
init -1 style main_menu_text is gui_text
init -1 style main_menu_title is main_menu_text
init -1 style main_menu_version is main_menu_text

init -1 style main_menu_frame:
    xsize 420
    yfill True
    background "gui/overlay/main_menu.png"

init -1 style main_menu_vbox:
    xalign 1.0
    yalign 1.0
    xoffset -20
    yoffset -20

init -1 style main_menu_text:
    xalign 1.0
    layout "subtitle"
    text_align 1.0
    color gui.accent_color

init -1 style main_menu_title:
    size 46
    color "#000"
    outlines [(absolute(3), "#EEE", absolute(0), absolute(0))]

init -1 style main_menu_version:
    size 24
    color "#000"
    outlines [(absolute(3), "#EEE", absolute(0), absolute(0))]











init -501 screen game_menu(title, scroll=None):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        has hbox


        frame:
            style "game_menu_navigation_frame"

        frame:
            style "game_menu_content_frame"

            if scroll == "viewport":

                viewport:
                    scrollbars "vertical"
                    mousewheel True
                    draggable True

                    side_yfill True

                    has vbox
                    transclude

            elif scroll == "vpgrid":

                vpgrid:
                    cols 1
                    yinitial 1.0

                    scrollbars "vertical"
                    mousewheel True
                    draggable True

                    side_yfill True

                    transclude

            else:

                transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


init -1 style game_menu_outer_frame is empty
init -1 style game_menu_navigation_frame is empty
init -1 style game_menu_content_frame is empty
init -1 style game_menu_viewport is gui_viewport
init -1 style game_menu_side is gui_side
init -1 style game_menu_scrollbar is gui_vscrollbar

init -1 style game_menu_label is gui_label
init -1 style game_menu_label_text is gui_label_text

init -1 style return_button is navigation_button
init -1 style return_button_text is navigation_button_text

init -1 style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

init -1 style game_menu_navigation_frame:
    xsize 420
    yfill True

init -1 style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

init -1 style game_menu_viewport:
    xsize 1380

init -1 style game_menu_vscrollbar:
    unscrollable gui.unscrollable

init -1 style game_menu_side:
    spacing 15

init -1 style game_menu_label:
    xpos 75
    ysize 180

init -1 style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

init -1 style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45









init -501 screen about():
    tag menu





    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")


            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")



define -1 gui.about = ""


init -1 style about_label is gui_label
init -1 style about_label_text is gui_label_text
init -1 style about_text is gui_text

init -1 style about_label_text:
    size gui.label_text_size











init -501 screen save():
    tag menu


    use file_slots(_("Save"))


init -501 screen load():
    tag menu


    use file_slots(_("Load"))


init -501 screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:



            order_reverse True


            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value


            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)


            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                textbutton _("{#auto_page}A") action FilePage("auto")

                textbutton _("{#quick_page}Q") action FilePage("quick")


                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()


init -1 style page_label is gui_label
init -1 style page_label_text is gui_label_text
init -1 style page_button is gui_button
init -1 style page_button_text is gui_button_text

init -1 style slot_button is gui_button
init -1 style slot_button_text is gui_button_text
init -1 style slot_time_text is slot_button_text
init -1 style slot_name_text is slot_button_text

init -1 style page_label:
    xpadding 75
    ypadding 5

init -1 style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

init -1 style page_button:
    properties gui.button_properties("page_button")

init -1 style page_button_text:
    properties gui.button_text_properties("page_button")

init -1 style slot_button:
    properties gui.button_properties("slot_button")

init -1 style slot_button_text:
    properties gui.button_text_properties("slot_button")









init -501 screen preferences():
    tag menu


    if renpy.mobile:
        $ cols = 2
    else:
        $ cols = 4

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "radio"
                    label _("Rollback Side")
                    textbutton _("Disable") action Preference("rollback side", "disable")
                    textbutton _("Left") action Preference("rollback side", "left")
                    textbutton _("Right") action Preference("rollback side", "right")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))




            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


init -1 style pref_label is gui_label
init -1 style pref_label_text is gui_label_text
init -1 style pref_vbox is vbox

init -1 style radio_label is pref_label
init -1 style radio_label_text is pref_label_text
init -1 style radio_button is gui_button
init -1 style radio_button_text is gui_button_text
init -1 style radio_vbox is pref_vbox

init -1 style check_label is pref_label
init -1 style check_label_text is pref_label_text
init -1 style check_button is gui_button
init -1 style check_button_text is gui_button_text
init -1 style check_vbox is pref_vbox

init -1 style slider_label is pref_label
init -1 style slider_label_text is pref_label_text
init -1 style slider_slider is gui_slider
init -1 style slider_button is gui_button
init -1 style slider_button_text is gui_button_text
init -1 style slider_pref_vbox is pref_vbox

init -1 style mute_all_button is check_button
init -1 style mute_all_button_text is check_button_text

init -1 style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

init -1 style pref_label_text:
    yalign 1.0

init -1 style pref_vbox:
    xsize 338

init -1 style radio_vbox:
    spacing gui.pref_button_spacing

init -1 style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/check_[prefix_]foreground.png"

init -1 style radio_button_text:
    properties gui.button_text_properties("radio_button")

init -1 style check_vbox:
    spacing gui.pref_button_spacing

init -1 style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

init -1 style check_button_text:
    properties gui.button_text_properties("check_button")

init -1 style slider_slider:
    xsize 525

init -1 style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

init -1 style slider_button_text:
    properties gui.button_text_properties("slider_button")

init -1 style slider_vbox:
    xsize 675










init -501 screen history():
    tag menu



    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport")):

        style_prefix "history"

        for h in _history_list:

            window:


                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"



                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                text h.what

        if not _history_list:
            label _("The dialogue history is empty.")


init -1 style history_window is empty

init -1 style history_name is gui_label
init -1 style history_name_text is gui_label_text
init -1 style history_text is gui_text

init -1 style history_text is gui_text

init -1 style history_label is gui_label
init -1 style history_label_text is gui_label_text

init -1 style history_window:
    xfill True
    ysize gui.history_height

init -1 style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

init -1 style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

init -1 style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

init -1 style history_label:
    xfill True

init -1 style history_label_text:
    xalign 0.5








init -501 screen help():
    tag menu


    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


init -501 screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


init -501 screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


init -501 screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


init -1 style help_button is gui_button
init -1 style help_button_text is gui_button_text
init -1 style help_label is gui_label
init -1 style help_label_text is gui_label_text
init -1 style help_text is gui_text

init -1 style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

init -1 style help_button_text:
    properties gui.button_text_properties("help_button")

init -1 style help_label:
    xsize 375
    right_padding 30

init -1 style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0















init -501 screen confirm(message, yes_action, no_action):


    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 45

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 150

            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action


    key "game_menu" action no_action


init -1 style confirm_frame is gui_frame
init -1 style confirm_prompt is gui_prompt
init -1 style confirm_prompt_text is gui_prompt_text
init -1 style confirm_button is gui_medium_button
init -1 style confirm_button_text is gui_medium_button_text

init -1 style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

init -1 style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

init -1 style confirm_button:
    properties gui.button_properties("confirm_button")

init -1 style confirm_button_text:
    properties gui.button_text_properties("confirm_button")









init -501 screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        has hbox:
            spacing 9

        text _("Skipping")

        text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"



transform -1 delayed_blink(delay, cycle):
    alpha .5

    pause delay
    block:

        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


init -1 style skip_frame is empty
init -1 style skip_text is gui_text
init -1 style skip_triangle is skip_text

init -1 style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

init -1 style skip_text:
    size gui.notify_text_size

init -1 style skip_triangle:


    font "DejaVuSans.ttf"









init -501 screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text message

    timer 3.25 action Hide('notify')


transform -1 notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


init -1 style notify_frame is empty
init -1 style notify_text is gui_text

init -1 style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

init -1 style notify_text:
    size gui.notify_text_size









init -501 screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing


        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)



        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


init -501 screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            has fixed:
                yfit gui.nvl_height is None

            if d.who is not None:

                text d.who:
                    id d.who_id

            text d.what:
                id d.what_id




define -1 config.nvl_list_length = 6

init -1 style nvl_window is default
init -1 style nvl_entry is default

init -1 style nvl_label is say_label
init -1 style nvl_dialogue is say_dialogue

init -1 style nvl_button is button
init -1 style nvl_button_text is button_text

init -1 style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

init -1 style nvl_entry:
    xfill True
    ysize gui.nvl_height

init -1 style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

init -1 style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

init -1 style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

init -1 style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

init -1 style nvl_button_text:
    properties gui.button_text_properties("nvl_button")







init -1 style pref_vbox:
    variant "medium"
    xsize 675



init -501 screen quick_menu():
    variant "touch"

    zorder 100

    hbox:
        style_prefix "quick"

        xalign 0.5
        yalign 1.0

        textbutton _("Back") action Rollback()
        textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)

        textbutton _("Menu") action ShowMenu()


init -1 style window:
    variant "small"
    background "gui/phone/textbox.png"

init -1 style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

init -1 style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

init -1 style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

init -1 style game_menu_navigation_frame:
    variant "small"
    xsize 510

init -1 style game_menu_content_frame:
    variant "small"
    top_margin 0

init -1 style pref_vbox:
    variant "small"
    xsize 600

init -1 style slider_pref_vbox:
    variant "small"
    xsize None

init -1 style slider_pref_slider:
    variant "small"
    xsize 900




init -501 screen infobar():
    zorder 100
    style_prefix "infobar"
    if show_infobar:
        frame xalign 0.0 xoffset 5 yoffset 5:
            text "Karma {}".format(karma)
        frame xalign 0.0 xoffset 5 yoffset 42:
            text "Energy {}/{}".format(energy, max_energy)
        frame xalign 0.5 yoffset 5:
            text "{}".format(location_str(player_location))
        frame xalign 1.0 xoffset -5 yoffset 5:
            text "Day {} {}".format(day, time_str(time))
        if incest:
            frame xalign 1.0 xoffset -5 yoffset 42:
                text "Incest ON"

init -1 python:
    config.overlay_screens.append("infobar")

default -1 show_infobar = False

init -1 style infobar_frame is default:
    background "#BDC3C777"
    xpadding 3

init -1 style infobar_text is default:
    size 28
    color "#FFF"
    outlines [(absolute(1), "#333", absolute(1), absolute(1))]




init -501 screen navbar(navigation_menu, location_menu):
    style_prefix "navbar"
    if location_menu:
        vbox xalign 0.0 yalign 0.5 xoffset 10:
            for (cmd,txt) in location_menu:
                textbutton txt action Return(cmd) xsize 500
    if navigation_menu:
        hbox xalign 0.0 yalign 1.0 yoffset -10:
            for (cmd,txt) in navigation_menu:
                textbutton txt action Return(cmd) xsize 250

init -1 style navbar_vbox is vbox
init -1 style navbar_hbox is hbox
init -1 style navbar_button is choice_button
init -1 style navbar_button_text is choice_button_text

init -1 style navbar_vbox:
    spacing 10

init -1 style navbar_hbox:
    xoffset 10
    spacing 10




init -501 screen gallery(items):
    style_prefix "gallery"
    vpgrid:
        cols 5
        xsize 1920
        ysize 1000
        xpos 10
        ypos 10
        scrollbars "vertical"
        spacing 5
        for code,name,unlocked in items:
            vbox:
                if unlocked:
                    add "gallery/{}_preview.jpg".format(code)
                    textbutton name action Return(code) xalign 0.5 yalign 1.0
                else:
                    add "gallery/{}_blur.jpg".format(code)
                    textbutton name action None xalign 0.5 yalign 1.0

    textbutton "Close" action Return(False) style "choice_button" xalign 0.5 yalign 1.0 yoffset -10

init -501 screen gallery_item(code):
    style_prefix "gallery"
    add "gallery/{}.jpg".format(code)
    hbox xalign 0.5 yalign 1.0 spacing 10:
        textbutton "Replay scene" action Return(code) style "choice_button" yoffset -10
        textbutton "Close" action Return(False) style "choice_button" yoffset -10

init -1 style gallery_button is choice_button:
    background "#1A5276AA"
    hover_background "#2471A3AA"
    insensitive_background "#BDC3C755"
    xsize 150
    ysize 60
    xpadding 10
    ymargin 10
    yoffset -5

init -1 style gallery_button_text is choice_button_text:
    size 20
    idle_color "#FFF"
    hover_color "#FFF"
    insensitive_color "#AAA"
    xalign 0.5
    yalign 0.5
    outlines [(absolute(1), "#333", absolute(1), absolute(1))]




init -501 screen ps_infobar():
    zorder 100
    style_prefix "ps_infobar"
    if ps_show_infobar:
        frame xalign 0.0 xoffset 5 yoffset 5:
            text "Karma {}".format(karma)
        frame xalign 0.0 xoffset 5 yoffset 42:
            text "Energy {}/{}".format(energy, max_energy)
        frame xalign 0.5 yoffset 5:
            text ps_name xalign 0.5

init -1 style ps_infobar_frame is infobar_frame
init -1 style ps_infobar_text is infobar_text

init -1 python:
    config.overlay_screens.append("ps_infobar")

default -1 ps_show_infobar = False




init -501 screen ps_menu(outfit_menu, pose_menu, stars):
    style_prefix "ps"
    hbox xalign 0.5 yalign 0.0 yoffset 50:
        for x in stars:
            text "{{image={}.png}}".format("star" if x else "starko")

    vbox xalign 0.0 yalign 0.5 xoffset 10:
        text "Outfit" xalign 0.5
        for (cmd,txt) in outfit_menu:
            if cmd is not None:
                textbutton txt action Return(cmd) xsize 250
            else:
                textbutton txt action None xsize 250
    vbox xalign 1.0 yalign 0.5 xoffset -10:
        text "Pose" xalign 0.5
        for (cmd,txt) in pose_menu:
            if cmd is not None:
                textbutton txt action Return(cmd) xsize 250
            else:
                textbutton txt action None xsize 250
    textbutton "Camera 1\n({} energy)".format(ps_camera_price(PS_CAMERA1)) action Return(CMD_PS_USE_CAMERA1) style "ps_camera_button" xoffset -300 yoffset -300
    textbutton "Camera 2\n({} energy)".format(ps_camera_price(PS_CAMERA2)) action Return(CMD_PS_USE_CAMERA2) style "ps_camera_button" xoffset 300 yoffset -300
    textbutton "Camera 3\n({} energy)".format(ps_camera_price(PS_CAMERA3)) action Return(CMD_PS_USE_CAMERA3) style "ps_camera_button" xoffset -300 yoffset 100
    textbutton "Camera 4\n({} energy)".format(ps_camera_price(PS_CAMERA4)) action Return(CMD_PS_USE_CAMERA4) style "ps_camera_button" xoffset 300 yoffset 100
    textbutton "Camera 5\n({} energy)".format(ps_camera_price(PS_CAMERA5)) action Return(CMD_PS_USE_CAMERA5) style "ps_camera_button" yoffset 420
    textbutton "Quit" action Return(0) style "navbar_button" xalign 0.0 yalign 1.0 xoffset 10 yoffset -10 xsize 250

init -1 style ps_text is infobar_text
init -1 style ps_vbox is navbar_vbox
init -1 style ps_button is navbar_button
init -1 style ps_button_text is navbar_button_text

init -1 style ps_camera_button is navbar_button:
    xalign 0.5
    yalign 0.5
    xsize 180
    ysize 100

init -1 style ps_camera_button_text is navbar_button_text:
    xalign 0.5
    text_align 0.5




init -501 screen ps_camera():
    style_prefix "ps"
    textbutton "Click" action Return(True) style "navbar_button" xalign 0.5 yalign 1.0 yoffset -10 xsize 250




init -501 screen pg_infobar():
    zorder 100
    style_prefix "pg_infobar"
    if pg_show_infobar:
        frame xalign 0.0 xoffset 5 yoffset 5:
            text "Karma {}".format(karma)
        frame xalign 0.5 yoffset 5:
            text pg_name xalign 0.5

init -1 style pg_infobar_frame is infobar_frame
init -1 style pg_infobar_text is infobar_text

init -1 python:
    config.overlay_screens.append("pg_infobar")

default -1 pg_show_infobar = False




init -501 screen pg_menu(action_menu):
    style_prefix "pg"
    vbox xalign 0.0 yalign 0.5 xoffset 10:
        for (cmd,txt) in action_menu:
            if cmd is not None:
                textbutton txt action Return(cmd) xsize 500
            else:
                textbutton txt action None xsize 250
    textbutton "Quit" action Return(0) style "navbar_button" xalign 0.0 yalign 1.0 xoffset 10 yoffset -10 xsize 250

init -1 style pg_text is infobar_text
init -1 style pg_vbox is navbar_vbox
init -1 style pg_button is navbar_button
init -1 style pg_button_text is navbar_button_text




init -501 screen thankyou():
    style_prefix "thankyou"
    text "Many thanks to:" xalign 0.5 yalign 0.0 yoffset 5
    vbox xalign 0.5 yalign 0.5:
        textbutton "Robert L" action OpenURL("https://www.patreon.com/Hels")
        textbutton "Drew Guerrero" action OpenURL("https://www.patreon.com/user?u=10063664")
        textbutton "Andrea Aliaj" action OpenURL("https://www.patreon.com/user?u=19405922")
        textbutton "Rett Young" action OpenURL("https://www.patreon.com/user?u=28723132")
        textbutton "Camilo" action OpenURL("https://www.patreon.com/user?u=13111993")
        textbutton "Gabear Lord" action OpenURL("https://www.patreon.com/user?u=28682068")
        textbutton "Sebastian Brück" action OpenURL("https://www.patreon.com/user?u=3271424")
        textbutton "Krishneel Mani" action OpenURL("https://www.patreon.com/user?u=18702645")
    text "Press any key to continue..." xalign 0.5 yalign 1.0 yoffset -5

init -1 style thankyou_vbox is vbox
init -1 style thankyou_button is button:
    xalign 0.5

init -1 style thankyou_button_text is button_text:
    idle_color "#FFF"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
