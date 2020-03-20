image blackbg = Solid("#000000FF")
image whitebg = Solid("#FFFFFFFF")
image whitebg33 = Solid("#FFFFFF33")
image whitebg66 = Solid("#FFFFFF66")
image whitebg99 = Solid("#FFFFFF99")
image whitebgCC = Solid("#FFFFFFCC")
image graybg = Solid("#CCCCCC19")
image nullbg = Solid("#00000000")

image emma neutral = "emma_neutral.png"
image emma smile = "emma_smile.png"
image emma frown = "emma_frown.png"
image emma angry = "emma_angry.png"
image vicky neutral = "vicky_neutral.png"
image vicky smile = "vicky_smile.png"
image vicky frown = "vicky_frown.png"
image vicky angry = "vicky_angry.png"
image ashley neutral = "ashley_neutral.png"

init 1000 python:

    import random

    left = Position(xpos=0.25)
    center = Position(xpos=0.5)
    right = Position(xpos=0.75)
    right2 = Position(xpos=0.63)

    player = Character("Alex")
    emma = Character("Emma", who_color="#FE67EB", what_color="#FE67EB")
    vicky = Character("Vicky", who_color="#FF4848", what_color="#FF4848")
    ashley = Character("Ashley", who_color="#FFC300", what_color="#FFC300")
    taxi = Character("Taxi driver")
    woman = Character("Woman", who_color="#FE67EB")
    girl = Character("Girl", who_color="#FE67EB")

    TIME_MORNING = 1
    TIME_DAYTIME = 2
    TIME_EVENING = 3
    TIME_NIGHT   = 4

    LOCATION_HOUSE          = 1
    LOCATION_LIVING_ROOM    = 2
    LOCATION_PLAYER_ROOM    = 3
    LOCATION_MASTER_BEDROOM = 4
    LOCATION_KITCHEN        = 5
    LOCATION_BATHROOM       = 6
    LOCATION_VICKY_ROOM     = 7

    CMD_GOTO_LIVING_ROOM    = 1001
    CMD_GOTO_PLAYER_ROOM    = 1002
    CMD_GOTO_MASTER_BEDROOM = 1003
    CMD_GOTO_VICKY_ROOM     = 1004
    CMD_GOTO_KITCHEN        = 1005
    CMD_GOTO_BATHROOM       = 1006
    CMD_WAIT                = 2001
    CMD_VIEW_GALLERY        = 2002
    CMD_DO_PUSHUPS          = 2005
    CMD_READ_BOOKS          = 2006
    CMD_WASH_DISHES         = 2007
    CMD_CLEAN_CARPET        = 2008
    CMD_TALK_EMMA           = 3001
    CMD_TALK_VICKY          = 3002
    CMD_TALK_ASHLEY         = 3003
    CMD_PHOTO_EMMA          = 4001
    CMD_PHOTO_VICKY         = 4002
    CMD_PLAY_ASHLEY         = 5003

    FLAG_TALK_EMMA1   = 10101
    FLAG_TALK_EMMA2   = 10102
    FLAG_TALK_EMMA3   = 10103
    FLAG_TALK_EMMA4   = 10104
    FLAG_TALK_EMMA5   = 10105
    FLAG_TALK_EMMA6   = 10106
    FLAG_TALK_EMMA7   = 10107
    FLAG_TALK_EMMA8   = 10108
    FLAG_TALK_EMMA9   = 10109
    FLAG_TALK_EMMA10  = 10110
    FLAG_TALK_EMMA11  = 10111
    FLAG_TALK_EMMA12  = 10112
    FLAG_TALK_EMMA13  = 10113
    FLAG_TALK_EMMA14  = 10114
    FLAG_TALK_VICKY1  = 10201
    FLAG_TALK_VICKY2  = 10202
    FLAG_TALK_VICKY3  = 10203
    FLAG_TALK_VICKY4  = 10204
    FLAG_TALK_VICKY5  = 10205
    FLAG_TALK_VICKY6  = 10206
    FLAG_TALK_VICKY7  = 10207
    FLAG_TALK_VICKY8  = 10208
    FLAG_TALK_VICKY9  = 10209
    FLAG_TALK_VICKY10 = 10210
    FLAG_TALK_VICKY11 = 10211
    FLAG_PHOTO_EMMA   = 20100
    FLAG_PHOTO_VICKY  = 20200
    FLAG_READ_PHOTO1  = 30101
    FLAG_READ_PHOTO2  = 30102
    FLAG_READ_PHOTO3  = 30103
    FLAG_PLAY_ASHLEY  = 40300

    time_map = dict()
    time_map[TIME_MORNING] = ("morning", "Morning")
    time_map[TIME_DAYTIME] = ("day", "Daytime")
    time_map[TIME_EVENING] = ("evening", "Evening")
    time_map[TIME_NIGHT] = ("night", "Night")

    location_map = dict()
    location_map[LOCATION_HOUSE] = ("house", "House")
    location_map[LOCATION_LIVING_ROOM] = ("living_room", "Living room")
    location_map[LOCATION_PLAYER_ROOM] = ("player_room", "Your room")
    location_map[LOCATION_MASTER_BEDROOM] = ("master_bedroom", "Master bedroom")
    location_map[LOCATION_KITCHEN] = ("kitchen", "Kitchen")
    location_map[LOCATION_BATHROOM] = ("bathroom", "Bathroom")
    location_map[LOCATION_VICKY_ROOM] = ("vicky_room", "Vicky's room")

    gallery_map = list()
    gallery_map.append((101,"emma1", "Emma 1"))
    gallery_map.append((102,"emma2", "Emma 2"))
    gallery_map.append((103,"emma3", "Emma 3"))
    gallery_map.append((104,"emma4", "Emma 4"))
    gallery_map.append((105,"emma5", "Emma 5"))
    gallery_map.append((106,"emma6", "Emma 6"))
    gallery_map.append((107,"emma7", "Emma 7"))
    gallery_map.append((108,"emma8", "Emma 8"))
    gallery_map.append((109,"emma9", "Emma 9"))
    gallery_map.append((110,"emma10","Emma 10"))
    gallery_map.append((111,"emma11","Emma 11"))
    gallery_map.append((112,"emma12","Emma 12"))
    gallery_map.append((113,"emma13","Emma 13"))
    gallery_map.append((114,"emma14","Emma 14"))
    gallery_map.append((201,"vicky1","Vicky 1"))
    gallery_map.append((202,"vicky2","Vicky 2"))
    gallery_map.append((203,"vicky3","Vicky 3"))
    gallery_map.append((204,"vicky4","Vicky 4"))
    gallery_map.append((205,"vicky5","Vicky 5"))
    gallery_map.append((206,"vicky6","Vicky 6"))
    gallery_map.append((207,"vicky7","Vicky 7"))
    gallery_map.append((208,"vicky8","Vicky 8"))
    gallery_map.append((209,"vicky9","Vicky 9"))
    gallery_map.append((210,"vicky10","Vicky 10"))
    gallery_map.append((211,"vicky11","Vicky 11"))

    emma_schedule = list()
    emma_schedule.append((TIME_MORNING, LOCATION_KITCHEN))
    emma_schedule.append((TIME_MORNING, LOCATION_BATHROOM))
    emma_schedule.append((TIME_MORNING, LOCATION_MASTER_BEDROOM))
    emma_schedule.append((TIME_MORNING, LOCATION_PLAYER_ROOM))
    emma_schedule.append((TIME_EVENING, LOCATION_LIVING_ROOM))
    emma_schedule.append((TIME_EVENING, LOCATION_KITCHEN))
    emma_schedule.append((TIME_EVENING, LOCATION_BATHROOM))
    emma_schedule.append((TIME_EVENING, LOCATION_MASTER_BEDROOM))

    emma_route = list()
    emma_route.append(( 0, TIME_EVENING, LOCATION_LIVING_ROOM, "emma1"))
    emma_route.append(( 1, TIME_MORNING, LOCATION_KITCHEN, "emma2"))
    emma_route.append(( 2, TIME_MORNING, LOCATION_MASTER_BEDROOM, "emma3"))
    emma_route.append(( 3, TIME_EVENING, LOCATION_LIVING_ROOM, "emma4"))
    emma_route.append(( 4, TIME_EVENING, LOCATION_BATHROOM, "emma5"))
    emma_route.append(( 5, TIME_EVENING, LOCATION_MASTER_BEDROOM, "emma6"))
    emma_route.append(( 6, TIME_EVENING, LOCATION_MASTER_BEDROOM, "emma7"))
    emma_route.append(( 7, TIME_EVENING, LOCATION_LIVING_ROOM, "emma8"))
    emma_route.append(( 8, TIME_MORNING, LOCATION_KITCHEN, "emma9"))
    emma_route.append(( 9, TIME_EVENING, LOCATION_LIVING_ROOM, "emma10"))
    emma_route.append((10, TIME_EVENING, LOCATION_MASTER_BEDROOM, "emma11"))
    emma_route.append((11, TIME_MORNING, LOCATION_PLAYER_ROOM, "emma12"))
    emma_route.append((12, TIME_EVENING, LOCATION_MASTER_BEDROOM, "emma13"))
    emma_route.append((13, TIME_EVENING, LOCATION_LIVING_ROOM, "emma14"))

    vicky_schedule = list()
    vicky_schedule.append((TIME_MORNING, LOCATION_BATHROOM))
    vicky_schedule.append((TIME_MORNING, LOCATION_KITCHEN))
    vicky_schedule.append((TIME_MORNING, LOCATION_VICKY_ROOM))
    vicky_schedule.append((TIME_DAYTIME, LOCATION_LIVING_ROOM))
    vicky_schedule.append((TIME_DAYTIME, LOCATION_VICKY_ROOM))
    vicky_schedule.append((TIME_EVENING, LOCATION_LIVING_ROOM))
    vicky_schedule.append((TIME_EVENING, LOCATION_KITCHEN))
    vicky_schedule.append((TIME_EVENING, LOCATION_BATHROOM))

    vicky_route = list()
    vicky_route.append(( 0, TIME_DAYTIME, LOCATION_LIVING_ROOM, "vicky1"))
    vicky_route.append(( 1, TIME_MORNING, LOCATION_BATHROOM, "vicky2"))
    vicky_route.append(( 2, TIME_EVENING, LOCATION_VICKY_ROOM, "vicky3"))
    vicky_route.append(( 3, TIME_MORNING, LOCATION_BATHROOM, "vicky4"))
    vicky_route.append(( 4, TIME_DAYTIME, LOCATION_VICKY_ROOM, "vicky5"))
    vicky_route.append(( 5, TIME_EVENING, LOCATION_LIVING_ROOM, "vicky6"))
    vicky_route.append(( 6, TIME_DAYTIME, LOCATION_LIVING_ROOM, "vicky7"))
    vicky_route.append(( 7, TIME_DAYTIME, LOCATION_KITCHEN, "vicky8"))
    vicky_route.append(( 8, TIME_DAYTIME, LOCATION_VICKY_ROOM, "vicky9"))
    vicky_route.append(( 9, TIME_EVENING, LOCATION_BATHROOM, "vicky10"))
    vicky_route.append((10, TIME_EVENING, LOCATION_LIVING_ROOM, "vicky11"))

    def time_code(time):
        x = time_map.get(time)
        return x[0] if x is not None else None

    def time_str(time):
        x = time_map.get(time)
        return x[1] if x is not None else None

    def location_code(id):
        x = location_map.get(id)
        return x[0] if x is not None else None

    def location_str(id):
        x = location_map.get(id)
        return x[1] if x is not None else None

    def pick_random_location(schedule, time, route, corruption):
        event_location = next(iter(l for c,t,l,e in route if c is corruption and t is time), None)
        if event_location is not None:
            return (event_location, True)
        available_locations = [l for t,l in schedule if t is time]
        if len(available_locations) == 0:
            return (None, False)
        return (random.choice(available_locations), False)

    def pick_event(route, time, location, corruption):
        return next(iter(e for c,t,l,e in route if c is corruption and t is time and l is location), None)

    def build_gallery():
        items = list()
        for i,(code,_,name) in enumerate(gallery_map):
            unlocked = code in gallery
            items.append((code,name,unlocked))
        return items

    def gallery_event(code):
        return next(iter(e for c,e,_ in gallery_map if c is code), None)

    def place_girls(location, girls):
        x = [(name, name + "_neutral") for name,loc in girls if loc is location]
        z = []
        for i,(name,pic) in enumerate(x):
            pos = None
            if i is 0:
                pos = center
            elif i is 1:
                pos = right
            elif i is 2:
                pos = left
            else:
                raise NotImplementedError
            z.append((name,pic,pos))
        return z




label game_init:
    $ ps_vicky_flags.add(PS_OUTFIT1 + PS_POSE1)
return

label after_load:
    call game_init
return

label start:


    $ day = 0
    $ time = 0
    $ karma = 0
    $ energy = 0
    $ max_energy = 100
    $ flags = Set()
    $ daily_flags = Set()
    $ gallery = Set()
    $ player_location = 0
    $ emma_location = 0
    $ emma_corruption = 0
    $ vicky_location = 0
    $ vicky_corruption = 0
    $ ashley_location = 0


    $ ps_skill = 0
    $ ps_emma_flags = Set()
    $ ps_vicky_flags = Set()


    $ pg_ashley_flags = Set()

    call game_init

    show blackbg
    show screen thankyou
    $ renpy.pause()
    hide screen thankyou

    scene poster
    menu:
        "Play intro":
            $ show_infobar = False
            call intro
        "Skip intro":
            pass
        "Start from update 14":

            $ emma_corruption = 13
            $ flags.add(FLAG_TALK_EMMA1)
            $ flags.add(FLAG_TALK_EMMA2)
            $ flags.add(FLAG_TALK_EMMA3)
            $ flags.add(FLAG_TALK_EMMA4)
            $ flags.add(FLAG_TALK_EMMA5)
            $ flags.add(FLAG_TALK_EMMA6)
            $ flags.add(FLAG_TALK_EMMA7)
            $ flags.add(FLAG_TALK_EMMA8)
            $ flags.add(FLAG_TALK_EMMA9)
            $ flags.add(FLAG_TALK_EMMA10)
            $ flags.add(FLAG_TALK_EMMA11)
            $ flags.add(FLAG_TALK_EMMA12)
            $ flags.add(FLAG_TALK_EMMA13)
            $ vicky_corruption = 10
            $ flags.add(FLAG_TALK_VICKY1)
            $ flags.add(FLAG_TALK_VICKY2)
            $ flags.add(FLAG_TALK_VICKY3)
            $ flags.add(FLAG_TALK_VICKY4)
            $ flags.add(FLAG_TALK_VICKY5)
            $ flags.add(FLAG_TALK_VICKY6)
            $ flags.add(FLAG_TALK_VICKY7)
            $ flags.add(FLAG_TALK_VICKY8)
            $ flags.add(FLAG_TALK_VICKY9)
            $ flags.add(FLAG_TALK_VICKY10)

            $ gallery.add(101)
            $ gallery.add(102)
            $ gallery.add(103)
            $ gallery.add(104)
            $ gallery.add(105)
            $ gallery.add(106)
            $ gallery.add(107)
            $ gallery.add(108)
            $ gallery.add(109)
            $ gallery.add(110)
            $ gallery.add(111)
            $ gallery.add(112)
            $ gallery.add(113)
            $ gallery.add(201)
            $ gallery.add(202)
            $ gallery.add(203)
            $ gallery.add(204)
            $ gallery.add(205)
            $ gallery.add(206)
            $ gallery.add(207)
            $ gallery.add(208)
            $ gallery.add(209)
            $ gallery.add(210)

            $ ps_skill = 30
            $ flags.add(FLAG_READ_PHOTO1)
            $ flags.add(FLAG_READ_PHOTO2)
            $ flags.add(FLAG_READ_PHOTO3)
            $ ps_vicky_flags.add(PS_OUTFIT1 + PS_POSE1)
            $ ps_vicky_flags.add(PS_OUTFIT1 + PS_POSE1 + PS_CAMERA1)
            $ ps_vicky_flags.add(PS_OUTFIT1 + PS_POSE1 + PS_CAMERA2)
            $ ps_vicky_flags.add(PS_OUTFIT1 + PS_POSE1 + PS_CAMERA3)
            $ ps_vicky_flags.add(PS_OUTFIT1 + PS_POSE1 + PS_CAMERA4)
            $ ps_vicky_flags.add(PS_OUTFIT1 + PS_POSE1 + PS_CAMERA5)
            $ ps_vicky_flags.add(PS_OUTFIT1 + PS_POSE2)
            $ ps_vicky_flags.add(PS_OUTFIT1 + PS_POSE2 + PS_CAMERA1)
            $ ps_vicky_flags.add(PS_OUTFIT1 + PS_POSE2 + PS_CAMERA2)
            $ ps_vicky_flags.add(PS_OUTFIT1 + PS_POSE2 + PS_CAMERA3)
            $ ps_vicky_flags.add(PS_OUTFIT1 + PS_POSE2 + PS_CAMERA4)
            $ ps_vicky_flags.add(PS_OUTFIT1 + PS_POSE2 + PS_CAMERA5)
            $ ps_vicky_flags.add(PS_OUTFIT1 + PS_POSE3)
            $ ps_vicky_flags.add(PS_OUTFIT1 + PS_POSE3 + PS_CAMERA1)
            $ ps_vicky_flags.add(PS_OUTFIT1 + PS_POSE3 + PS_CAMERA2)
            $ ps_vicky_flags.add(PS_OUTFIT1 + PS_POSE3 + PS_CAMERA3)
            $ ps_vicky_flags.add(PS_OUTFIT1 + PS_POSE3 + PS_CAMERA4)
            $ ps_vicky_flags.add(PS_OUTFIT1 + PS_POSE3 + PS_CAMERA5)
            $ ps_vicky_flags.add(PS_OUTFIT1 + PS_POSE4)
            $ ps_vicky_flags.add(PS_OUTFIT1 + PS_POSE4 + PS_CAMERA1)
            $ ps_vicky_flags.add(PS_OUTFIT1 + PS_POSE4 + PS_CAMERA2)
            $ ps_vicky_flags.add(PS_OUTFIT1 + PS_POSE4 + PS_CAMERA3)
            $ ps_vicky_flags.add(PS_OUTFIT1 + PS_POSE4 + PS_CAMERA4)
            $ ps_vicky_flags.add(PS_OUTFIT1 + PS_POSE4 + PS_CAMERA5)
            $ ps_vicky_flags.add(PS_OUTFIT1 + PS_POSE5)
            $ ps_vicky_flags.add(PS_OUTFIT1 + PS_POSE5 + PS_CAMERA1)
            $ ps_vicky_flags.add(PS_OUTFIT1 + PS_POSE5 + PS_CAMERA2)
            $ ps_vicky_flags.add(PS_OUTFIT1 + PS_POSE5 + PS_CAMERA3)
            $ ps_vicky_flags.add(PS_OUTFIT1 + PS_POSE5 + PS_CAMERA4)
            $ ps_vicky_flags.add(PS_OUTFIT1 + PS_POSE5 + PS_CAMERA5)
            $ ps_vicky_flags.add(PS_OUTFIT2 + PS_POSE1)
            $ ps_vicky_flags.add(PS_OUTFIT2 + PS_POSE1 + PS_CAMERA1)
            $ ps_vicky_flags.add(PS_OUTFIT2 + PS_POSE1 + PS_CAMERA2)
            $ ps_vicky_flags.add(PS_OUTFIT2 + PS_POSE1 + PS_CAMERA3)
            $ ps_vicky_flags.add(PS_OUTFIT2 + PS_POSE1 + PS_CAMERA4)
            $ ps_vicky_flags.add(PS_OUTFIT2 + PS_POSE1 + PS_CAMERA5)
            $ ps_vicky_flags.add(PS_OUTFIT2 + PS_POSE2)
            $ ps_vicky_flags.add(PS_OUTFIT2 + PS_POSE2 + PS_CAMERA1)
            $ ps_vicky_flags.add(PS_OUTFIT2 + PS_POSE2 + PS_CAMERA2)
            $ ps_vicky_flags.add(PS_OUTFIT2 + PS_POSE2 + PS_CAMERA3)
            $ ps_vicky_flags.add(PS_OUTFIT2 + PS_POSE2 + PS_CAMERA4)
            $ ps_vicky_flags.add(PS_OUTFIT2 + PS_POSE2 + PS_CAMERA5)
            $ ps_vicky_flags.add(PS_OUTFIT2 + PS_POSE3)
            $ ps_vicky_flags.add(PS_OUTFIT2 + PS_POSE3 + PS_CAMERA1)
            $ ps_vicky_flags.add(PS_OUTFIT2 + PS_POSE3 + PS_CAMERA2)
            $ ps_vicky_flags.add(PS_OUTFIT2 + PS_POSE3 + PS_CAMERA3)
            $ ps_vicky_flags.add(PS_OUTFIT2 + PS_POSE3 + PS_CAMERA4)
            $ ps_vicky_flags.add(PS_OUTFIT2 + PS_POSE3 + PS_CAMERA5)
            $ ps_vicky_flags.add(PS_OUTFIT2 + PS_POSE4)
            $ ps_vicky_flags.add(PS_OUTFIT2 + PS_POSE4 + PS_CAMERA1)
            $ ps_vicky_flags.add(PS_OUTFIT2 + PS_POSE4 + PS_CAMERA2)
            $ ps_vicky_flags.add(PS_OUTFIT2 + PS_POSE4 + PS_CAMERA3)
            $ ps_vicky_flags.add(PS_OUTFIT2 + PS_POSE4 + PS_CAMERA4)
            $ ps_vicky_flags.add(PS_OUTFIT2 + PS_POSE4 + PS_CAMERA5)
            $ ps_vicky_flags.add(PS_OUTFIT2 + PS_POSE5)
            $ ps_vicky_flags.add(PS_OUTFIT2 + PS_POSE5 + PS_CAMERA1)
            $ ps_vicky_flags.add(PS_OUTFIT2 + PS_POSE5 + PS_CAMERA2)
            $ ps_vicky_flags.add(PS_OUTFIT2 + PS_POSE5 + PS_CAMERA3)
            $ ps_vicky_flags.add(PS_OUTFIT2 + PS_POSE5 + PS_CAMERA4)
            $ ps_vicky_flags.add(PS_OUTFIT2 + PS_POSE5 + PS_CAMERA5)
            $ ps_vicky_flags.add(PS_OUTFIT3 + PS_POSE1)
            $ ps_vicky_flags.add(PS_OUTFIT3 + PS_POSE1 + PS_CAMERA1)
            $ ps_vicky_flags.add(PS_OUTFIT3 + PS_POSE1 + PS_CAMERA2)
            $ ps_vicky_flags.add(PS_OUTFIT3 + PS_POSE1 + PS_CAMERA3)
            $ ps_vicky_flags.add(PS_OUTFIT3 + PS_POSE1 + PS_CAMERA4)
            $ ps_vicky_flags.add(PS_OUTFIT3 + PS_POSE1 + PS_CAMERA5)
            $ ps_vicky_flags.add(PS_OUTFIT3 + PS_POSE2)
            $ ps_vicky_flags.add(PS_OUTFIT3 + PS_POSE2 + PS_CAMERA1)
            $ ps_vicky_flags.add(PS_OUTFIT3 + PS_POSE2 + PS_CAMERA2)
            $ ps_vicky_flags.add(PS_OUTFIT3 + PS_POSE2 + PS_CAMERA3)
            $ ps_vicky_flags.add(PS_OUTFIT3 + PS_POSE2 + PS_CAMERA4)
            $ ps_vicky_flags.add(PS_OUTFIT3 + PS_POSE2 + PS_CAMERA5)
            $ ps_vicky_flags.add(PS_OUTFIT3 + PS_POSE3)
            $ ps_vicky_flags.add(PS_OUTFIT3 + PS_POSE3 + PS_CAMERA1)
            $ ps_vicky_flags.add(PS_OUTFIT3 + PS_POSE3 + PS_CAMERA2)
            $ ps_vicky_flags.add(PS_OUTFIT3 + PS_POSE3 + PS_CAMERA3)
            $ ps_vicky_flags.add(PS_OUTFIT3 + PS_POSE3 + PS_CAMERA4)
            $ ps_vicky_flags.add(PS_OUTFIT3 + PS_POSE3 + PS_CAMERA5)
            $ ps_vicky_flags.add(PS_OUTFIT3 + PS_POSE4)
            $ ps_vicky_flags.add(PS_OUTFIT3 + PS_POSE4 + PS_CAMERA1)
            $ ps_vicky_flags.add(PS_OUTFIT3 + PS_POSE4 + PS_CAMERA2)
            $ ps_vicky_flags.add(PS_OUTFIT3 + PS_POSE4 + PS_CAMERA3)
            $ ps_vicky_flags.add(PS_OUTFIT3 + PS_POSE4 + PS_CAMERA4)
            $ ps_vicky_flags.add(PS_OUTFIT3 + PS_POSE4 + PS_CAMERA5)
            $ ps_vicky_flags.add(PS_OUTFIT3 + PS_POSE5)
            $ ps_vicky_flags.add(PS_OUTFIT3 + PS_POSE5 + PS_CAMERA1)
            $ ps_vicky_flags.add(PS_OUTFIT3 + PS_POSE5 + PS_CAMERA2)
            $ ps_vicky_flags.add(PS_OUTFIT3 + PS_POSE5 + PS_CAMERA3)
            $ ps_vicky_flags.add(PS_OUTFIT3 + PS_POSE5 + PS_CAMERA4)
            $ ps_vicky_flags.add(PS_OUTFIT3 + PS_POSE5 + PS_CAMERA5)
            $ ps_vicky_flags.add(PS_OUTFIT4 + PS_POSE1)
            $ ps_vicky_flags.add(PS_OUTFIT4 + PS_POSE1 + PS_CAMERA1)
            $ ps_vicky_flags.add(PS_OUTFIT4 + PS_POSE1 + PS_CAMERA2)
            $ ps_vicky_flags.add(PS_OUTFIT4 + PS_POSE1 + PS_CAMERA3)
            $ ps_vicky_flags.add(PS_OUTFIT4 + PS_POSE1 + PS_CAMERA4)
            $ ps_vicky_flags.add(PS_OUTFIT4 + PS_POSE1 + PS_CAMERA5)
            $ ps_vicky_flags.add(PS_OUTFIT4 + PS_POSE2)
            $ ps_vicky_flags.add(PS_OUTFIT4 + PS_POSE2 + PS_CAMERA1)
            $ ps_vicky_flags.add(PS_OUTFIT4 + PS_POSE2 + PS_CAMERA2)
            $ ps_vicky_flags.add(PS_OUTFIT4 + PS_POSE2 + PS_CAMERA3)
            $ ps_vicky_flags.add(PS_OUTFIT4 + PS_POSE2 + PS_CAMERA4)
            $ ps_vicky_flags.add(PS_OUTFIT4 + PS_POSE2 + PS_CAMERA5)
            $ ps_vicky_flags.add(PS_OUTFIT4 + PS_POSE3)
            $ ps_vicky_flags.add(PS_OUTFIT4 + PS_POSE3 + PS_CAMERA1)
            $ ps_vicky_flags.add(PS_OUTFIT4 + PS_POSE3 + PS_CAMERA2)
            $ ps_vicky_flags.add(PS_OUTFIT4 + PS_POSE3 + PS_CAMERA3)
            $ ps_vicky_flags.add(PS_OUTFIT4 + PS_POSE3 + PS_CAMERA4)
            $ ps_vicky_flags.add(PS_OUTFIT4 + PS_POSE3 + PS_CAMERA5)
            $ ps_vicky_flags.add(PS_OUTFIT4 + PS_POSE4)
            $ ps_vicky_flags.add(PS_OUTFIT4 + PS_POSE4 + PS_CAMERA1)
            $ ps_vicky_flags.add(PS_OUTFIT4 + PS_POSE4 + PS_CAMERA2)
            $ ps_vicky_flags.add(PS_OUTFIT4 + PS_POSE4 + PS_CAMERA3)
            $ ps_vicky_flags.add(PS_OUTFIT4 + PS_POSE4 + PS_CAMERA4)
            $ ps_vicky_flags.add(PS_OUTFIT4 + PS_POSE4 + PS_CAMERA5)
            $ ps_vicky_flags.add(PS_OUTFIT4 + PS_POSE5)
            $ ps_vicky_flags.add(PS_OUTFIT4 + PS_POSE5 + PS_CAMERA1)
            $ ps_vicky_flags.add(PS_OUTFIT4 + PS_POSE5 + PS_CAMERA2)
            $ ps_vicky_flags.add(PS_OUTFIT4 + PS_POSE5 + PS_CAMERA3)
            $ ps_vicky_flags.add(PS_OUTFIT4 + PS_POSE5 + PS_CAMERA4)
            $ ps_vicky_flags.add(PS_OUTFIT4 + PS_POSE5 + PS_CAMERA5)
            $ ps_vicky_flags.add(PS_OUTFIT5 + PS_POSE1)
            $ ps_vicky_flags.add(PS_OUTFIT5 + PS_POSE1 + PS_CAMERA1)
            $ ps_vicky_flags.add(PS_OUTFIT5 + PS_POSE1 + PS_CAMERA2)
            $ ps_vicky_flags.add(PS_OUTFIT5 + PS_POSE1 + PS_CAMERA3)
            $ ps_vicky_flags.add(PS_OUTFIT5 + PS_POSE1 + PS_CAMERA4)
            $ ps_vicky_flags.add(PS_OUTFIT5 + PS_POSE1 + PS_CAMERA5)
            $ ps_vicky_flags.add(PS_OUTFIT5 + PS_POSE2)
            $ ps_vicky_flags.add(PS_OUTFIT5 + PS_POSE2 + PS_CAMERA1)
            $ ps_vicky_flags.add(PS_OUTFIT5 + PS_POSE2 + PS_CAMERA2)
            $ ps_vicky_flags.add(PS_OUTFIT5 + PS_POSE2 + PS_CAMERA3)
            $ ps_vicky_flags.add(PS_OUTFIT5 + PS_POSE2 + PS_CAMERA4)
            $ ps_vicky_flags.add(PS_OUTFIT5 + PS_POSE2 + PS_CAMERA5)
            $ ps_vicky_flags.add(PS_OUTFIT5 + PS_POSE3)
            $ ps_vicky_flags.add(PS_OUTFIT5 + PS_POSE3 + PS_CAMERA1)
            $ ps_vicky_flags.add(PS_OUTFIT5 + PS_POSE3 + PS_CAMERA2)
            $ ps_vicky_flags.add(PS_OUTFIT5 + PS_POSE3 + PS_CAMERA3)
            $ ps_vicky_flags.add(PS_OUTFIT5 + PS_POSE3 + PS_CAMERA4)
            $ ps_vicky_flags.add(PS_OUTFIT5 + PS_POSE3 + PS_CAMERA5)
            $ ps_vicky_flags.add(PS_OUTFIT5 + PS_POSE4)
            $ ps_vicky_flags.add(PS_OUTFIT5 + PS_POSE4 + PS_CAMERA1)
            $ ps_vicky_flags.add(PS_OUTFIT5 + PS_POSE4 + PS_CAMERA2)
            $ ps_vicky_flags.add(PS_OUTFIT5 + PS_POSE4 + PS_CAMERA3)
            $ ps_vicky_flags.add(PS_OUTFIT5 + PS_POSE4 + PS_CAMERA4)
            $ ps_vicky_flags.add(PS_OUTFIT5 + PS_POSE4 + PS_CAMERA5)
            $ ps_vicky_flags.add(PS_OUTFIT5 + PS_POSE5)
            $ ps_vicky_flags.add(PS_OUTFIT5 + PS_POSE5 + PS_CAMERA1)
            $ ps_vicky_flags.add(PS_OUTFIT5 + PS_POSE5 + PS_CAMERA2)
            $ ps_vicky_flags.add(PS_OUTFIT5 + PS_POSE5 + PS_CAMERA3)
            $ ps_vicky_flags.add(PS_OUTFIT5 + PS_POSE5 + PS_CAMERA4)
            $ ps_vicky_flags.add(PS_OUTFIT5 + PS_POSE5 + PS_CAMERA5)


            $ flags.add(FLAG_PLAY_ASHLEY)
            $ pg_ashley_flags.add(FLAG_PG_HANDJOB_ASHLEY_END1)
            $ pg_ashley_flags.add(FLAG_PG_HANDJOB_ASHLEY_END2)
            $ pg_ashley_flags.add(FLAG_PG_HANDJOB_ASHLEY_END3)
            $ pg_ashley_flags.add(FLAG_PG_BLOWJOB_ASHLEY_END1)

    while True:
        $ day += 1
        $ time = TIME_MORNING
        $ player_location = LOCATION_PLAYER_ROOM
        $ energy = max_energy
        $ daily_flags.clear()
        $ show_infobar = True
        call day_loop

return




label day_loop:

$ skip_day = False
while not skip_day:
    $ skip_time = False
    $ emma_location, is_emma_storyline_event = pick_random_location(emma_schedule, time, emma_route, emma_corruption)
    $ vicky_location, is_vicky_storyline_event = pick_random_location(vicky_schedule, time, vicky_route, vicky_corruption)
    $ ashley_location = None
    if time is TIME_DAYTIME and FLAG_PLAY_ASHLEY in flags:
        $ ashley_location = random.choice([None, LOCATION_LIVING_ROOM, LOCATION_KITCHEN, LOCATION_VICKY_ROOM])


    if emma_location is not None and emma_location is vicky_location and is_emma_storyline_event:
        $ vicky_location = None
    if vicky_location is not None and vicky_location is emma_location and is_vicky_storyline_event:
        $ emma_location = None

    while not skip_day and not skip_time:
        window hide


        $ evt = None
        $ girls = place_girls(player_location, (("emma",emma_location), ("vicky",vicky_location), ("ashley",ashley_location)))
        if len(girls) is 1:
            if emma_location is player_location:
                $ evt = pick_event(emma_route, time, emma_location, emma_corruption)
            elif vicky_location is player_location:
                $ evt = pick_event(vicky_route, time, vicky_location, vicky_corruption)
            elif ashley_location is player_location:
                pass
            else:
                $ raise NotImplementedError

        if evt is not None:

            $ show_infobar = False
            $ renpy.call('event_' + evt)
            $ player_location = LOCATION_PLAYER_ROOM
            $ show_infobar = True
            $ skip_time = True
        else:


            $ loc = "location_" + location_code(player_location)
            $ bg = location_code(player_location) + "_" + time_code(time)
            $ renpy.scene()
            if len(girls) > 0:
                $ renpy.show(bg + "_blur")
                $ for name,pic,pos in girls: renpy.show(pic, tag=name, at_list=[pos])
            else:
                $ renpy.show(bg)


            $ navigation_menu = []
            $ navigation_menu.append((CMD_GOTO_PLAYER_ROOM, "Your room"))
            $ navigation_menu.append((CMD_GOTO_LIVING_ROOM, "Living room"))
            $ navigation_menu.append((CMD_GOTO_MASTER_BEDROOM, "Master bedroom"))
            $ navigation_menu.append((CMD_GOTO_VICKY_ROOM, "Vicky's room"))
            $ navigation_menu.append((CMD_GOTO_KITCHEN, "Kitchen"))
            $ navigation_menu.append((CMD_GOTO_BATHROOM, "Bathroom"))
            $ location_menu = []
            $ location_menu.append((CMD_WAIT, "Wait"))
            if player_location is LOCATION_PLAYER_ROOM:
                $ location_menu.append((CMD_VIEW_GALLERY, "View gallery"))
                $ location_menu.append((CMD_DO_PUSHUPS, "Do pushups"))
                $ location_menu.append((CMD_READ_BOOKS, "Read books"))
            if player_location is LOCATION_KITCHEN and time is TIME_DAYTIME:
                $ location_menu.append((CMD_WASH_DISHES, "Wash the dishes"))
            if player_location is LOCATION_LIVING_ROOM and time is TIME_DAYTIME:
                $ location_menu.append((CMD_CLEAN_CARPET, "Clean carpet"))
            if emma_location is player_location:
                $ location_menu.append((CMD_TALK_EMMA, "Talk to Emma"))
            if vicky_location is player_location:
                $ location_menu.append((CMD_TALK_VICKY, "Talk to Vicky"))
                $ location_menu.append((CMD_PHOTO_VICKY, "Invite Vicky to photo session"))
            if ashley_location is player_location:
                $ location_menu.append((CMD_TALK_ASHLEY, "Talk to Ashley"))
                $ location_menu.append((CMD_PLAY_ASHLEY, "Have fun with Ashley"))
            $ cmd = renpy.call_screen("navbar", navigation_menu, location_menu)


            if cmd is CMD_WAIT:
                call wait
            elif cmd is CMD_VIEW_GALLERY:
                call gallery
            elif cmd is CMD_TALK_EMMA:
                call talk_emma
            elif cmd is CMD_TALK_VICKY:
                call talk_vicky
            elif cmd is CMD_TALK_ASHLEY:
                call talk_ashley
            elif cmd is CMD_PHOTO_EMMA:
                call photo_emma
            elif cmd is CMD_PHOTO_VICKY:
                call photo_vicky
            elif cmd is CMD_PLAY_ASHLEY:
                call play_ashley
            elif cmd is CMD_DO_PUSHUPS:
                call do_pushups
            elif cmd is CMD_READ_BOOKS:
                call read_books
            elif cmd is CMD_WASH_DISHES:
                call wash_dishes
            elif cmd is CMD_CLEAN_CARPET:
                call clean_carpet
            elif cmd is CMD_GOTO_LIVING_ROOM:
                $ player_location = LOCATION_LIVING_ROOM
            elif cmd is CMD_GOTO_PLAYER_ROOM:
                $ player_location = LOCATION_PLAYER_ROOM
            elif cmd is CMD_GOTO_MASTER_BEDROOM:
                call location_master_bedroom
                if _return is None:
                    $ player_location = LOCATION_MASTER_BEDROOM
            elif cmd is CMD_GOTO_VICKY_ROOM:
                call location_vicky_room
                if _return is None:
                    $ player_location = LOCATION_VICKY_ROOM
            elif cmd is CMD_GOTO_KITCHEN:
                $ player_location = LOCATION_KITCHEN
            elif cmd is CMD_GOTO_BATHROOM:
                $ player_location = LOCATION_BATHROOM
            else:
                $ raise NotImplementedError

    if not skip_day:
        if time is TIME_NIGHT:
            call wait
        else:
            $ time += 1

return




label gallery:

$ show_infobar = False
while True:
    window hide
    $ renpy.scene()
    $ renpy.show("player_room_" + time_code(time) + "_blur")
    $ code = renpy.call_screen("gallery", build_gallery())
    if not code:
        $ show_infobar = True
        return
    $ code = renpy.call_screen("gallery_item", code)
    if code:
        $ evt = gallery_event(code)
        if evt:
            $ renpy.call("event_" + evt, replay=True)

return




label wait:

if time is TIME_NIGHT:
    if player_location is LOCATION_PLAYER_ROOM:
        "You throw yourself on the bed and fall asleep."
    else:
        scene player_room_night
        "You return back to your room and fall asleep."
    $ skip_day = True
else:
    "You spend some time fooling around."
    $ skip_time = True

return




label do_pushups:

"You do pushups and feel stronger."
$ karma += 1
$ max_energy += 1
"+1 karma\n+1 max energy"
$ skip_time = True

return




label read_books:

$ books_menu = []
$ books_menu.append(("Nevermind",0))
$ books_menu.append(("Browse wikipedia",1))

if ps_skill is 0 and FLAG_READ_PHOTO1 in flags:
    $ flags.remove(FLAG_READ_PHOTO1)
    $ books_menu.append(("Photography for dummies", 10))
if ps_skill > 0 and ps_skill < 10:
    $ books_menu.append(("Photography for dummies ({}%)".format(ps_skill*10), 10))
if ps_skill is 10 and FLAG_READ_PHOTO2 in flags:
    $ flags.remove(FLAG_READ_PHOTO2)
    $ books_menu.append(("Advanced photography", 11))
if ps_skill > 10 and ps_skill < 20:
    $ books_menu.append(("Advanced photography ({}%)".format((ps_skill-10)*10), 11))
if ps_skill is 20 and FLAG_READ_PHOTO3 in flags:
    $ flags.remove(FLAG_READ_PHOTO3)
    $ books_menu.append(("Practical photography for experts", 12))
if ps_skill > 20 and ps_skill < 30:
    $ books_menu.append(("Practical photography for experts ({}%)".format((ps_skill-20)*10), 12))

$ books_choice = renpy.display_menu(books_menu)
if books_choice is 0:
    return
elif books_choice is 1:
    "Scientia potentia est!"
elif books_choice is 10:
    "You get a very usefull information."
    $ ps_skill += 1
elif books_choice is 11:
    "You learn some new tricks."
    $ ps_skill += 1
elif books_choice is 12:
    "You master your skill."
    $ ps_skill += 1
else:
    $ raise NotImplementedError()

$ karma += 1
"+1 karma"
$ skip_time = True

return




label wash_dishes:

scene kitchen_day
"You wash the dishes. Emma will be pleased."
$ karma += 1
"+1 karma"
$ skip_time = True

return




label clean_carpet:

scene living_room_day
"You clean the carpet. Emma will be pleased."
$ karma += 1
"+1 karma"
$ skip_time = True

return




label location_master_bedroom:

if time is TIME_NIGHT:
    scene door
    player "*** Emma is sleeping. I should not disturb her, I guess."
    return False

return




label location_vicky_room:

if time is TIME_NIGHT:
    scene door
    player "*** Vicky is sleeping. I should not disturb her, I guess."
    return False

return




label intro:

scene house
taxi "Приехали. Улица Блоссом 11."
player "Спасибо."
"Вы подходите к входной двери и нажимаете кнопку звонка."
"ДИНЬ-ДИНЬ-ДОН"
woman "Входите!"
"Вы слышите шаги и дверь открывается."
scene house_blur
show emma neutral at center
player "Привет!"
woman "Чем я могу помочь?"
player "Это же я, Алекс! Вы что, меня не помните, тётя Эмма?"
show emma smile at center
emma "Алекс? Тот самый малыш Алекс, который жил по соседству?!"
player "Агась, именно! Это я!"
emma "Ну давай заходи! Рада тебя видеть! Ты так вырос!!!"
emma "*** Он выглядит таким взрослым! Совсем не такой, каким я его запомнила!"
player "Спасибо! А вы всё такая же молодая и красивая, какой я вас запомнил!"
player "*** Чёрт! Как же она горяча!"
show emma neutral at center
emma "После стольких лет... Что я могу сделать для тебя?"
player "Моя мама не звонила вам?!"
emma "Нет, не звонила... Погоди, я сменила номер... А что случилось?"
player "Ох, Я просто надеялся, что смогу остаться у вас на некоторое время..."
emma "Ох, конечно можешь! У нас есть свободная спальня!"
player "Вы уверены? Я вам не помешаю?"
emma "Конечно! Иди сюда, обними меня! И пожалуйста, зови меня Эмма!"
emma "Хорошо, давай я проведу тебе экскурсию."
player "Ох, спасибо!"
scene house
emma "Следуй за мной!"
scene living_room_day
emma "Значит, это у нас зал."
scene living_room_day_blur
show emma neutral at center
emma " Если хочешь посмотреть телевизор, ты спокойно можешь это делать тут."
emma "у нас есть разные ТВ каналы..."
player "О, отлично, спасибо!"
player "*** Что она имеет в виду под словом 'разные'?"
player "*** Она пытается на что-то намекнуть? Или я просто озабоченый?!"
scene kitchen_day
emma "Здесь у нас находится кухня."
scene kitchen_day_blur
show emma neutral at center
emma "Холодильник и вся еда в нём в твоём распоряжении."
emma "Не стесняйся, я знаю что юноши много едят, хах!"
player "Оу, хорошо, спасибо!"
scene bathroom_day
emma "Пойдем дальше. Это наша ванная."
scene bathroom_day_blur
show emma neutral at center
emma "Если тебе понадобятся дополнительные полотенца, они в твоей комнате."
emma "Пожалуйста, не забудь об этом! Это важно!"
player "Ок, не волнуйтесь! Я не забуду, обещаю!"
scene master_bedroom_day
emma "Это моя комната."
scene master_bedroom_day_blur
show emma neutral at center
emma "Так что, если тебе что-нибудь понадобится, ты знаешь где меня найти, хихи!"
scene player_room_day
emma "И, наконец, это ваша комната, молодой человек."
scene player_room_day_blur
show emma neutral at center
emma "Отдохни, располагайся тут..."
emma "И не забудь, мы скоро будем ужинать! Я приготовлю кое-что вкусное!"
player "О, спасибо, но это не обязательно..."
emma "О, для меня это вовсе не проблема. К тому же, я уверена, что ты найдешь другой способ отплатить мне!"
show emma smile at center
emma "Хаха, шучу! Отдохни хорошенько, ты выглядишь уставшим!"
scene player_room_day
"И она уходит."
player "*** Вау! Она такая горячая!"
player "*** Ок, немного вздремну и буду готов к ужину..."
show blackbg
"Вы ложитесь на кровать и засыпаете."
scene living_room_morning
"На следующее утро вы выходите из своей комнаты..."
scene living_room_morning_blur
show vicky neutral at center
"И сразу же врезаетесь в девушку!"
girl "Я дома!!!"
player "Эмммм... Привет!"
girl "Эй!!! А ты ещё кто???"
player "А ты кто?"
player "*** Кто это??? И почему она такая горячая???"
girl "Простите?!"
girl "Вообще-то я должна задавать этот вопрос, не ты, странный чувак!"
show emma neutral at right
"Появляется Эмма."
emma "Оу, привет, дорогошу! Ну же, Обними свою мамулю!!!"
player "*** 'Мамуля'??? Офигенно! Теперь их двое!"
player "*** В смысле, горячих девушек рядом со мной!"
girl "Мам, а это кто?!"
girl "Выглядит молодым... вроде..."
player "*** 'Вроде молодой'??? Вот так номер!"
emma "Хах, дорогая, ты разве не узнаёшь его?!"
emma "Это же Алекс, Он жил по соседству..."
girl "Ой, тот Алекс?! Я его с трудом помню..."
emma "Алекс, Это Вики. Она моя старшая дочка, как ты помнишь."
player "*** Та мелкая жируха Вики? Боже! Она стала такой красоткой!!!"
emma "Алекс поживёт у нас некоторое время..."
emma "И я с трудом могу вспомнить о твоих планах вернуться к родителям' так скоро домой..."
vicky "Да,на счёт этого... Мы расстались с Питом... Так что, теперь я тут..."
emma "Ох, дорогуша, вы были такой чудесной парой..."
emma "Но не волнуйся: ты можешь остаться тут на столько, на сколько захочешь..."
vicky "Ой, спасибо, мама! Я люблю тебя!"
emma "А я люблю тебя больше!"
player "***Вот жеж! Серьёзно?! И как вы мне прикажете выживать в доме, полном красоток???"

return




label talk_emma:

hide vicky
hide ashley
show emma neutral at center

if emma_corruption == 1 and FLAG_TALK_EMMA1 not in flags:
    $ flags.add(FLAG_TALK_EMMA1)
    emma "Hey there! Going out tonight?!"
    player "Nah, I don't think so... Just wanted to watch some TV..."
    emma "Oh, and I planned on doing yoga over there..."
    player "That's ok, I guess TV can wait..."
    player "*** What else? Maybe, I should compliment her about her yoga skills?!"
    emma "Oh, thanks... But I don't need the living room all to myself... We can share, I guess..."
    player "Oh, about that... I do really admire you doing yoga, that's quite impressive! I wish I could do what you can..."
    player "*** Oh, my! Why did I say it???"
    emma "*** Oh, his compliment sounded so sincere! Not many young men can do that... Maybe, I should invite him to join in?!"
    emma "Oh, it's really nothing... just patience and time..."
    player "..."
    emma "By the way, you can join me, if you want to... I could teach you some basic stuff, you know..."
    player "*** Is she serious about it?!"
    player "Wow, thanks! I'd love to!!!"
elif emma_corruption == 2 and FLAG_TALK_EMMA2 not in flags:
    $ flags.add(FLAG_TALK_EMMA2)
    emma "So, how's it going?"
    player "It's going, thanks!"
    emma "Want something to eat?"
    player "No, I'm fine, thanks."
    player "*** She's always so kind to me..."
    emma "Ok. But if want some home cooked meal, just tell me..."
    player "..."
    emma "It's been quite a long time since I had someone else eating on my kitchen..."
    emma "*** Oh, why am I telling it to him?!"
    emma "And I feel so lonely because of that... Missing it, you know..."
    emma "*** Oh, no! Now he'll consider me insecure old lady who can only complain about her life!"
    player "*** Lonely? She could use my support, I guess... Why not to give her little more warmth?!"
    player "Oh, we could drink coffee together... every morning... before you set off for work..."
    emma "Not that I'm complaining... Wow, it's an excellent idea! I like it already! Thank you!!!"
elif emma_corruption == 3 and FLAG_TALK_EMMA3 not in flags:
    $ flags.add(FLAG_TALK_EMMA3)
    player "Hi there!"
    emma "Oh, hi!"
    emma "*** Damn it, Emma, stop blushing! You are too old for that!"
    emma "..."
    emma "*** But why is he staring at me like that?!"
    emma "Is there anything you need?"
    player "No, nothing really..."
    player "*** Shit, she's still mad at me!"
    player "I... I just wanted to say that I'm sorry for... for what happened before!"
    emma "That's okay... I almost forgot about it..."
    player "*** Damn it! I knew I shouldn't have brought it up again!"
    player "Oh, ok... I... I wanted you to know that... that you have a great body!"
    emma "Oh, thank you!"
    player "But you, probably, hear it every day... from your admirers... and... and your boyfriend..."
    player "*** What an idiot! Why did I bring it up???"
    emma "I... I don't have a boyfriend..."
    player "Really??? Why not??? Oh, sorry, that's none of my business..."
    emma "No, no, it's okay... Besides, I've been asking myself the same question..."
    player "..."
    emma "It's just... after the death of my husband I had two kids to raise on my own... Not much time for dating left..."
    player "But now girls are grown up..."
    emma "You mean it's time to move on?!"
    player "Sort of..."
    emma "I guess, I don't have enough courage to do that... I haven't one out for a while..."
    player "I could ask you out... if you want to... as friends, of course!"
    player "*** She'll turn me down, that's for sure!"
    emma "Oh, it sounds great! I'd love to!!!"
elif emma_corruption == 8 and FLAG_TALK_EMMA8 not in flags:
    $ flags.add(FLAG_TALK_EMMA8)
    emma "Hey, Alex!"
    player "Hey!"
    emma "You know, I... I still can't forget that astonishing massage!"
    emma "*** Oh, my! What if he understands it in a weird way?!"
    player "*** Oh, she really liked it! Good, very good!"
    emma "I'm really impressed!"
    player "Oh, thanks!"
    player "But... but there's nothing to be impressed about..."
    emma "Oh, you don't say that!"
    emma "You... you are... a god of massage!!! I'm telling you!!!"
    emma "*** Damn it! Why did I say it? Now he'll think I'm some kind of a pervert!"
    player "*** Yes, she definitely liked it!!!"
    player "Oh, wow! So, when's the next session then?!"
    emma "Hm... Well... I... I... don't know..."
    player "Oh!"
    emma "Soon, I guess... If it's okay with you..."
    player "Nice! I'd love to show you more of my skillset... In massage, of course..."
    player "*** Shit! She'll believe now that I'm hitting on her!"
    player "Oh, it sounded... I... I didn't mean to..."
    "Emma gives you a wide and warm smile."
    emma "Don't worry, I get it: it was a slip of your tongue."
    player "Exactly!"
    emma "..."
    player "So, just let me know when you are in the mood for our next session of massage!"
    emma "Sure, I will!"
elif emma_corruption == 9 and FLAG_TALK_EMMA9 not in flags:
    $ flags.add(FLAG_TALK_EMMA9)
    emma "Listen, I wanted to apologize..."
    player "Oh?! What for?"
    player "*** She looks confused... What's wrong?"
    player "I don't think there..."
    emma "Listen, I know I overreacted before..."
    emma "I didn't mean to, honestly!"
    player "*** What is she talking about?!"
    emma "But lately I'm doing it all the time..."
    emma "*** Damn it! How can I explain it to him???"
    emma "I think that's because I'm not used to men helping me around..."
    emma "*** Hope, that will do..."
    player "*** It's either now or never! I should take my chance and ask her!!!"
    player "Really? I thought you were dating someone..."
    player "You... you mentioned it once..."
    "Emma starts coughing."
    emma "Oh, that date?!"
    player "Aha."
    emma "Yeah, I remember it!"
    emma "*** WHy is he asking? What is it: some sort of curiosity or jealosy?!"
    emma "It.. it was supposed to be a blind date... a colleague tried to set us up..."
    emma "But the guy... he... he was no show."
    player "Shit! You didn't tell me..."
    player "*** I'm so stupid! I shouldn't have asked her!"
    emma "..."
    player "He... he must have been scared of your radiant beauty that day!"
    emma "Oh!"
    emma "Yes, perhaps you are right about it!"
    emma "Let's just forget about this whole thing, ok?"
    player "Deal!"
elif emma_corruption == 10 and FLAG_TALK_EMMA10 not in flags:
    $ flags.add(FLAG_TALK_EMMA10)
    emma "Have a moment?"
    player "Sure. What is it?"
    emma "Eeemmm... I don't know how to put it delicately..."
    player "*** Shit! She's scaring me!"
    player "...."
    emma "Listen, I do respect your feelings for your girlfriend back home..."
    player "Girlfriend, right!"
    player "*** Damn it! She remembers?!"
    player "*** I thought she was too drunk to remember anything from that night!"
    player "*** I wonder what else she recalls?!"
    player "*** Oh, I'm screwed! So screwed!"
    emma "So, I thought..."
    emma "Hey, are you listening?"
    player "Sorry..."
    emma "Yes, I do understand you: memories of the two of you together, happy moments..."
    player "...."
    emma "But don't you think it's time to move on?!"
    emma "We need you here!"
    player "Oh?!"
    emma "Exactly! You are a young and handsome man..."
    player "Oh!"
    emma "You are not a monk, after all!"
    player "...."
    emma "Stop this unhealthy fixation on your ex-girlfriend!"
    player "But... she's not 'ex'!"
    player "*** Yeah, right! She doesn't exist at all!!!"
    emma "Listen, I get it. Believe me, I do!"
    emma "But you should move on!"
    emma "No matter how painful it is for you!"
    player "Oh... Okay..."
    emma "Okay?!"
    player "Okay. I guess, I could try..."
    emma "Very well! I've talked to Vicky..."
    player "*** Why the hell did you do it?!"
    emma "Do you worry: she'll introduce some of her friends to you..."
    emma "So, you can choose..."
    player "Choose what???"
    emma "A new girlfriend, you silly!"
    "Emma gently smacks you on the forehead."
    emma "That's the least we can do for you to stay happy!"
    player "Oh! Eeehhhmmm, thanks!"
    emma "You are welcome, sweetie!"
    emma "You are like family to us!"
    player "Oh!"
    emma "Yeah! Don't you ever forget about it!"
    player "*** Does it mean that now I can officially screw all Vicky's friends?!"
elif emma_corruption == 11 and FLAG_TALK_EMMA11 not in flags:
    $ flags.add(FLAG_TALK_EMMA11)
    player "Hey, Emma, how are you?"
    player "Long time, no see, as they say..."
    emma "Haha, we live in the same house, remember?"
    emma "So, this saying doesn't match our case..."
    player "Still, I've noticed that you've been extremely busy lately..."
    emma "Yeah, that's right... You know, the end of calendar year is always a bit apocalyptic at our company..."
    player "Oh!"
    emma "Add to it that stupid swimsuit contest piling up with other things..."
    player "Oh, I see..."
    player "How is it going, by the way?"
    emma "Hmmmm... frankly speaking, I don't know..."
    player "How come?"
    emma "Let's say it's going... But not the way I expected it to..."
    player "Oh?!"
    emma "Yeah... Our 'big boss' hated most of our swimsuits..."
    player "Oh! I wonder why..."
    emma "... including mine..."
    player "Oh! How could he???"
    player "*** My lord, her big boss can think with his brain, not with his dick, what a surprise!"
    player "*** I already respect him! It must be tough for him..."
    emma "Yeah, I was surprised, too."
    emma "So, now they are making designer suits for all of us... plus modelling classes, plus stylist's consultations... and I have no idea how it's going to end..."
    player "Oh!"
    emma "But now I have almost no time to do my actual work! And it irritates me a lot!"
    player "Oh! That's not what I expected to hear..."
    emma "Really? And this whole contest thing is not what I expected it to be... I'm very disappointed..."
    emma "I don't know... Maybe, I'm too old for all that stuff..."
    player "You??? My god, you are NOT old!"
    player "You are mature! And you are able of critical thinking, so this whole thing is not as fascinating for you, as for some little 'bimbo'..."
    emma "Oh, thank you, Alex!"
    emma "You are an awesome friend, you know that?"
    player "..."
    emma "We should definitely go out some time... Play bowling, perhaps... What will you say?"
    player "Oh, I'd love to!"
    emma "Okay, deal, then!"
elif emma_corruption == 12 and FLAG_TALK_EMMA12 not in flags:
    $ flags.add(FLAG_TALK_EMMA12)
    emma "Hey, Alex!"
    player "Oh, hi there!"
    player "*** Oh, no, not again!"
    player "*** Let's hope, at least, that she won't mention this morning!"
    player "*** Otherwise things will get awkward..."
    emma "Have you... have you just got up?"
    player "Aha, almost. You caught me on my way back from the shower."
    emma "Oh! You are a good sleeper, I guess..."
    player "*** She's definitely concerned about this morning."
    player "*** That's why she's asking me all these questions."
    player "*** I'd better comfort her before she suspects anything."
    player "Yeah, right! I am!"
    emma "Oh, that's good!"
    emma "*** I hope he didn't see me in his room this morning..."
    player "You bet! And when I sleep, it's almost impossible to wake me up!"
    player "No matter what happens around!"
    player "Even my alarm-clock can hardly cope with it, heh!"
    emma "Oh!"
    emma "*** It's good! Real good for me! I guess, I was lucky!"
    emma "I'll remember that!"
    player "*** Yeah, you do!"
    emma "*** Huh, what a relief for me!"
    emma "Listen, later on I'm going shopping... big time..."
    player "Oh!"
    emma "Yeah, I don't have a dress for our New Year's Eve party at work..."
    emma "Could you please help me?"
    emma "I mean, to choose one..."
    emma "You know how much I trust your judgement!"
    emma "I will be very grateful to you!!!"
    player "Sure, I'd love to join you!"
    player "*** And I have a couple ideas in mind how you could show your gratitude..."
    emma "Okay, then we could go shopping..."
    player "Deal!"
    player "See you later then!"
elif emma_corruption == 13 and FLAG_TALK_EMMA13 not in flags:
    $ flags.add(FLAG_TALK_EMMA13)
    player "Oh, hey!"
    emma "Hi!"
    player "So, how was your corporate party?"
    "Emma sniffs."
    emma "Really???"
    emma "Are you interested in the party or in the dress?!"
    player "I guess, both."
    player "But of course, I want to know if the dress was as awesome as you expected it to be..."
    emma "Oh, sure thing, it was."
    emma "Most of the girls envied me and tried to find out where I had bought that dress..."
    player "Oh, that's a success, congrats!"
    emma "Yeah, maybe it is..."
    player "And why not?!"
    emma "Because all the efforts were in vain..."
    player "I'm sorry, I lost you..."
    player "What is it that you are trying to say?!"
    emma "I... sort of... hoped that Boris from the finances department would notice me..."
    player "*** Boris??? Sounds more of a mobster department rather than finances..."
    player "And he didn't???"
    emma "And he didn't!!!"
    player "Well, maybe he brought his wife to the party..."
    emma "Yes, he did! How come you know it?!"
    player "Come on! A married man with his wife on board, seriously???"
    player "Next time I suggest you try a free man with less responsibilities..."
    player "If, of course, you weren't planning on having threesome with his wife..."
    emma "Oh, come on! How can you be so mean???"
    player "I'm not, hehe."
    player "I just remembered that shop assistant who helped you with the dress and thought that you might be into girls, too..."
    emma "Stop it, please!"
    emma "I still blush remembering that little incident..."
    player "Oh, so, you still think of her, right?!"
    player "Let me know when you plan on visiting her next time..."
    player "I may join you..."
    emma "Phew, that's disgusting!"
    player "It depends on what you were thinking..."
    emma "Oh, sweetie! Stop embarrassing me, please!"
    player "Okay, okay! You have enough time to figure it all out!"
    emma "Yeah, right, I do!"
elif emma_corruption == 14 and FLAG_TALK_EMMA14 not in flags:
    $ flags.add(FLAG_TALK_EMMA14)
    emma "Wow, I liked our movies evening a lot!"
    emma "And you?"
    emma "Did you like it?"
    player "Of course, I did!"
    player "*** More important, I liked what happened between the two of us..."
    player "*** And hope, you did, too!"
    emma "Nice to know!"
    emma "Then we should repeat it once again!"
    player "Movies? Again?"
    emma "Hmm, you don't sound very happy..."
    "You shrug your shoulders."
    player "I don't know..."
    player "I'm getting tired of movies, I guess..."
    emma "Oh, I see..."
    emma "Why don't you invite me to a dinner, then?!"
    player "A dinner?"
    player "You mean... like... at a restaurant?!"
    emma "Aha, exactly!"
    emma "Something more like a date..."
    emma "Not a real one, of course..."
    "She hastily adds when seeing your wide open eyes."
    "You raise one eyebrow."
    player "And why not?"
    player "Why can not it be real?!"
    emma "Come on, you know what I meant..."
    player "No, I'm being serious..."
    emma "Me, too..."
    emma "It's that... I miss sometimes all that romantic stuff, you know..."
    "Being absolutely serious, you nod to her."
    player "Yes, I know what you mean..."
    player "Well, I guess, it would be my pleasure then to go on a date with you..."
    "Emma gives you a radiant smile."
    emma "Oh, really?!"
    player "Of course!"
    player "It will be the most romantic of all dates you had, I promise you!"
    "Emma blushes."
    emma "Oh, thank you!"
    emma "I'll be waiting for it!"
else:
    "You spend some time chatting with Emma and your relationship has improved."
$ karma += 1
"+1 karma"
$ skip_time = True

return




label talk_vicky:

hide emma
hide ashley
show vicky neutral at center

if vicky_corruption == 1 and FLAG_TALK_VICKY1 not in flags:
    $ flags.add(FLAG_TALK_VICKY1)
    vicky "Hi there! Didn't know you were at home..."
    player "Hi! Well... I thought the same about you..."
    vicky "Yeah, you are right, I was supposed to be out..."
    player "Oh! What happened?"
    vicky "Nothing..."
    player "..."
    vicky "I'd rather not talk about it..."
    player "Ok, as you wish..."
    vicky "Ok, fine! My friends stood me up!"
    player "Oh! Sorry to hear that... You must be pissed off..."
    vicky "Exactly! I'm very pissed off!"
    player "Well... I... I don't know what to say... There's ice-cream in the fridge... if you feel like eating..."
    vicky "Oh, thanks! That's very thoughtful of you, but I'm fine..."
    player "*** She doesn't look fine to me..."
    player "Ok, if you say so..."
    vicky "No, no, it's really nice of you! Listen..."
    vicky "*** Oh, shit! What am I doing??? He's our tenant!"
    player "Yes?"
    vicky "You... you must feel lonely around here... Why... why don't we go out some time?!"
    vicky "*** Oh, no! Why did I say it?! He'll turn me down! I can tell!"
    player "*** Wow!!! She's asking me out??? Seriously?!"
    player "Well... I... I think it's a great idea! I'd like to take you up on it!"
    vicky "Oh, ok then! I'm sure we'll have a lot of fun!"
elif vicky_corruption == 2 and FLAG_TALK_VICKY2 not in flags:
    $ flags.add(FLAG_TALK_VICKY2)
    vicky "Listen, I'm really sorry for that misunderstanding in the bathroom earlier..."
    vicky "I... I... I didn't mean to..."
    player "*** She's apologizing?! OMG!!!"
    player "No, no, it's... it's okay... Anyway, it's me who should be apologizing, not you..."
    vicky "*** Wow! He can be really nice! So strange, I didn't notice it before..."
    vicky "It's okay! I guess, we both screwed up..."
    player "You bet!"
    vicky "So, let's forget about that little 'accident' and..."
    player "Move on?!"
    vicky "Exactly!"
    player "*** No way, I will ever forget your wonderful body..."
    player "Okay, it's fine with me... and..."
    vicky "I... I... just wanted you to know that I'm really sorry..."
    vicky "*** Oh my, how can I explain it to him???"
    vicky "It's... it's that I'm not used to men around our house..."
    player "..."
    vicky "Mom... mom... she has always been alone after... after... you know... after our dad passed away..."
    player "Oh! I'm sorry, I didn't know anything about... your... family tragedy..."
    player "*** What an idiot! I should change the topic now!!!"
    vicky "It's okay. How could you, if it all happened after we moved here?!"
    player "Oh! My... my condolences... I... I'm really sorry..."
    vicky "That's okay. Just don't judge me next time you see me acting a bit strange around you..."
    vicky "As I said: I'm not used to men in this house."
    player "I'll do my best to create as little inconvenience for you as possible!"
    vicky "Oh, you are really adorable, thanks!!!"
elif vicky_corruption == 3 and FLAG_TALK_VICKY3 not in flags:
    $ flags.add(FLAG_TALK_VICKY3)
    vicky "Listen, we need to talk about our photoshoots..."
    player "*** Oh, no! She must have changed her mind!"
    player "Yes? What's wrong?"
    vicky "Why 'wrong'? Everything is cool, man!!!"
    vicky "I love our photoshoots! They are amazing!"
    player "Oh!"
    player "*** Oh, what a relief!"
    vicky "*** Why does he sound so surprised?"
    vicky "I thought you knew that?!"
    player "Oh! I... I hoped... but... wasn't sure."
    vicky "It's awesome, man!"
    player "Thanks!"
    vicky "The pictures you take are great!!!"
    player "So? What's there to talk about, then?"
    vicky "Well... there is... one thing..."
    player "*** Hell, she doesn't want to do it any more... But why???"
    vicky "Em... I don't know how to say it, but..."
    vicky "But I showed some picture to my girls, I mean, friends, and they liked the photos."
    player "Oh, that's a relief!"
    vicky "Yes. And they wanted you... me to ask you... if you could do photoshoots for them, too..."
    player "Oh! I'd love to, I guess."
    vicky "*** So easy?! He even didn't hesitate for a single second!"
    vicky "*** I thought he enjoyed our photoshoots only because of me..."
    player "*** Vicky looks upset... But why???"
    player "*** Oh, my! What if she didn't like the fact that I agreed to it so easily???"
    player "Of course, I don't mind practising in photography more."
    player "So, I agree, but on one condition only."
    vicky "???"
    player "You and me... we continue working on your photosessions even harder than before..."
    player "Camera loves you!"
    player "And I... I enjoy working with you..."
    player "*** Shit! I shouldn't have said that! It sounded so wrong!"
    vicky "*** Wow, he likes working with me... Does it mean he likes me, too?!"
    vicky "Oh, okay, then we have a deal!"
elif vicky_corruption == 4 and FLAG_TALK_VICKY4 not in flags:
    $ flags.add(FLAG_TALK_VICKY4)
    vicky "Hey, are you always that open and trusting?!"
    player "Excuse me?!"
    player "*** What the hell is she talking about???"
    vicky "I mean, is it a matter of habit that you leave the bathroom door open?"
    player "*** Is this tricky question some kind of a test?!"
    player "Well, no... It was a one-time thing, I assume..."
    vicky "Oh!"
    player "*** 'Oh'??? What is it supposed to mean???"
    player "As I said: it was a mistake."
    player "And I'm sorry. It won't happen again!"
    vicky "Oh, what a shame to hear it! Why?"
    player "Hm, I lost you. What are you saying?"
    "Vicky shrugs her shoulders."
    vicky "Nothing. Apart from the fact that it would be such a misfortune not to use the bathroom whenever I need it..."
    player "Oh!!!"
    player "*** She's definitely hinting on something..."
    player "Are... are you saying you would prefer if I... 'forgot' to lock the door?!"
    player "*** Oh, my! She's hitting on me!!!"
    player "*** No, it can't be true!"
    player "*** It's... it's too good to be true!"
    vicky "Oh, yes, I wouldn't mind if... if you 'forgot' to lock that door..."
    player "Oh!"
    vicky "Who knows, maybe there will be some benefits you won't be able to resist?!"
    player "And the only chance for me to know is to leave the door unlocked?!"
    vicky "Yep, you got it right!"
    vicky "But, of course, I leave it to you to decide..."
    "Vicky gives you a charming smile and strolls away."
elif vicky_corruption == 5 and FLAG_TALK_VICKY5 not in flags:
    $ flags.add(FLAG_TALK_VICKY5)
    vicky "Listen, I wanted to ask you for a favor..."
    player "Yes, what is it?"
    player "*** Damn, what can it be?"
    player "*** She looks so... so mysterious!"
    vicky "Could you please not mention our... our little incident to my mom?!"
    player "To Emma?! Why would I???"
    "Vicky shrugs her shoulders."
    vicky "I don't know... Just wanted to exclude this possibility..."
    player "Okay, no problem."
    "The two of you stay silent for a moment."
    player "And may I ask... if it's okay with you..."
    vicky "???"
    player "What were you looking for... back there?"
    vicky "Oh, it was something personal... very personal."
    player "Very personal?! What, a love letter from your boyfriend?!"
    vicky "Not that personal. And I don't have any boyfriend at the moment. I... I was looking for my... vibrator."
    player "What???"
    vicky "Well, as you may know, girls need to jerk off from time to time..."
    vicky "As well as boys do..."
    player "Oh, wow... emmm... I'm speechless..."
    vicky "Why???"
    player "Didn't picture you as that type of girls..."
    vicky "There's NO 'that type' of girls... most women do it... discreetly... from time to time..."
    player "Oh, well... hope you found it..."
    player "*** Shit, I don't know what to say!!!"
    vicky "Yeah, I did."
    "Vicky hesitates for a moment, then continues after a pause."
    vicky "But it made me thinking..."
    player "About what?"
    "Vicky licks her lips, then answers."
    vicky "Maybe, next time you could join me?!"
    player "In searching for this... thing?!"
    vicky "No! In having fun."
    vicky "I bet your fingures can be very skillful!"
    "On hearing it, you chew on your own saliva and start coughing."
    "Vicky produces a short laughter."
    vicky "Promise me that you'll think about it, when you... when you feel better!"
elif vicky_corruption == 6 and FLAG_TALK_VICKY6 not in flags:
    $ flags.add(FLAG_TALK_VICKY6)
    vicky "Hey there!"
    player "*** Oh, no! Not again! What is it this time?!"
    player "Oh, hi!"
    vicky "Listen... You have a minute?"
    player "*** Oh, she looks nervous... I wonder why?!"
    player "Yep. What's up?"
    vicky "I... I... just... wanted to thank you... for... for not telling my mom..."
    player "Oh, my! What could I probably tell her???"
    vicky "Well, you know... that I wasn't looking for the shoes..."
    player "Oh, relax, I would never do that!"
    vicky "..."
    player "I figured she wouldn't be happy to know the truth..."
    vicky "Thanks. That's very thoughtful of you!"
    player "Welcome! By the way, and your BFF... does she know?"
    vicky "Oh, you mean Ashley?!"
    player "That's the only one I've been introduced to so far..."
    "Vicky prefers to ignore your bitter remark."
    vicky "Of course, she does... We share most of the secrets with each other..."
    player "*** 'Most?' But not 'all'???"
    vicky "And why are you asking? Did you like her?!"
    player "*** Wow, what is that?"
    player "*** Jealousy in her voice???"
    player "Well... I don't know... She seems okay..."
    vicky "Okay??? She's one of the hottest girls in the neighborhood!!!"
    player "*** But not as hot as you are!"
    player "Okay, maybe I wasn't paying enough attention... I was a bit distracted as you may know..."
    vicky "Oh!"
    "Vicky blushes, but then continues."
    vicky "I'm telling you: she's cool!"
    vicky "*** And she seems to be interested in you, too..."
    player "...."
    vicky "You should hang out with us some time..."
    player "Oh! Well... I don't know..."
    vicky "Promise me that you will!"
    player "*** Why is she so persistent?!"
    player "Okay, fine, I will!"
    vicky "Awesome!!!"
elif vicky_corruption == 7 and FLAG_TALK_VICKY7 not in flags:
    $ flags.add(FLAG_TALK_VICKY7)
    vicky "Hey, we need to talk!"
    player "Oh?!"
    player "*** How do women do it?! They have this talent... to make men panic with one phrase only!"
    vicky "Yeah!"
    player "Okay, what about?"
    player "*** She scares the hell out of me!"
    vicky "About Ashley."
    player "*** Shit! Here we go..."
    player "And what about Ashley?"
    vicky "I think she likes you..."
    player "Oh?!"
    vicky "Yeah!"
    player "*** Shit, I think we both are repeating the same meaningless phrases..."
    player "Why?"
    vicky "Why what?"
    player "Why are you telling me?!"
    "Vicky shrugs her shoulders."
    player "To make sure I don't hurt her, I guess?"
    vicky "You???"
    "Her eyes get big and round."
    vicky "Come on, man! Don't be ridiculous! Ashley is the least of my concerns."
    player "Oh?!"
    vicky "Yeah!"
    player "*** Damn, not again!"
    player "Then what?"
    vicky "You, silly!"
    vicky "Just a friendly warning: don't get serious with her."
    player "..."
    vicky "She changes men like a baby gets new diapers changed!"
    player "Oh, that was harsh!"
    "Vicky shrugs her shoulders again."
    vicky "That was honest, man."
    player "Wait a sec... Are you jealous?!"
    vicky "What a stupid idea! Why would I be?!"
    player "Yeah, why would you be jealous?"
    player "Maybe, because you wanted to keep me all to yourself?!"
    player "And now you'll have to share?!"
    vicky "Oh?!"
    player "Yeah!"
    vicky "Go fuck yourself, asshole!!!"
elif vicky_corruption == 8 and FLAG_TALK_VICKY8 not in flags:
    $ flags.add(FLAG_TALK_VICKY8)
    vicky "Hey, Alex! Hi there!"
    player "Hi, Vicky!"
    vicky "Listen, we need to talk..."
    player "Do we?"
    player "*** Oh, crap!"
    vicky "Yep!"
    player "Why, I did nothing wrong..."
    vicky "What?"
    player "Sorry, it was a lame joke..."
    vicky "Yeah, a bit strange one..."
    vicky "Listen, I wanted to ask you..."
    player "Yes, what is it?"
    vicky "Well... But you should promise first that you won't tell mom about it..."
    player "*** Sounds intriguing..."
    player "*** The topic must be 'delicate'... otherwise why would she bother asking?!"
    player "Come on, Vicky, have I ever?!"
    vicky "No. That's why I trust you... But still I had to warn you..."
    player "Okay, okay... So, what is it?"
    "Vicky takes a deep breath and spills it out."
    vicky "Is it true that men like oral sex most of all?!"
    player "*** Holy crap! Why is she asking?!"
    player "*** Did... did she see me with Ashley?!"
    player "*** Shit, I bet she did!"
    vicky "So?"
    player "Well... not most, of course..."
    player "Let's just say that it has its moments..."
    player "And... skillful girls are quite rare to meet..."
    vicky "But why?"
    player "Because not so many girls like doing it..."
    vicky "What if they just don't know how to do it properly?!"
    player "Well... there are many ways to learn..."
    player "*** I wonder why she's asking me..."
    vicky "Like what?"
    player "Like... like practicing on bananas..."
    player "*** Oh, shit! Why am I telling her this crap?!"
    vicky "Oh!"
    player "I guess, you could ask around. I'm sure, some of your friends could give you useful practical advice..."
    vicky "Like Ashley?"
    player "..."
    vicky "You like her, don't you?!"
    player "No, I don't. Why would I?"
    player "*** Damn it, she knows!"
    vicky "*** Oh, crap! Why did I say it?!"
    player "Wait a sec! You are jealous, right?"
    vicky "No, I'm not! Leave me alone!!!"
elif vicky_corruption == 9 and FLAG_TALK_VICKY9 not in flags:
    $ flags.add(FLAG_TALK_VICKY9)
    vicky "Hey, Alex!"
    player "Oh, hey!"
    player "*** I can tell: she's still mad at me! Shit!"
    player "*** Shit! Shit! Shit! I shouldn't have cummed on her!"
    vicky "Listen..."
    vicky "I... I... I... wanted to... to apologize!"
    player "*** Oh, that's something new!"
    player "*** I'm starting to like this conversation!"
    player "Oh... okay. What for?"
    vicky "You are asking me 'what for'?!"
    vicky "How can you even ask???"
    vicky "Don't you get it?!"
    player "Well... sort of..."
    player "Just wanted to make sure I get it right..."
    player "That's why I wanted to hear it from you..."
    vicky "Fine! Gosh, you are not making it easier for me! Are you?"
    player "Nope, I guess not."
    vicky "Okay, fine! I overreacted..."
    vicky "The other time..."
    vicky "And I admit it."
    player "Oh!"
    vicky "???"
    vicky "Oh? That's all you are going to say?"
    vicky "Just 'oh'?"
    player "And what did you expect me to say?"
    vicky "Well... I don't know..."
    vicky "Maybe... that you liked it..."
    vicky "I mean our little 'adventure'..."
    vicky "And wouldn't mind repeating it..."
    vicky "Soon..."
    player "'Soon'?"
    player "Oh... well..."
    player "Listen, I don't mean to be rude, but..."
    vicky "But you are not interested in me?"
    vicky "That's what you were trying to say?!"
    player "No, no! God, sometimes it's so difficult with you..."
    vicky "Sorry, I know I'm not good at listening to people..."
    player "I noticed. So, in brief: if you want, we can repeat it as many times as you like..."
    player "But! I won't be begging you for it."
    player "You came to me, right?"
    player "Not the other way round."
    player "Because I'm not the one who needs practice."
    vicky "Yeah, sure! You made your point..."
    vicky "And it's absolutely fair!"
    player "Okay."
    vicky "Till next time, then?"
    player "*** Wow, I guess, I can hear hope in her voice!"
    player "It's your call..."
    "Vicky adds confidence to her voice."
    vicky "Till next time, then!"
elif vicky_corruption == 10 and FLAG_TALK_VICKY10 not in flags:
    $ flags.add(FLAG_TALK_VICKY10)
    player "Oh, hey, Vicky!"
    vicky "Hey!"
    player "Long time no see."
    player "How are you?"
    vicky "Okay, I guess."
    player "Glad to hear that!"
    player "And how's your little ass doing?"
    player "Still aching?!"
    vicky "What???"
    vicky "How dare you ask me such things???"
    player "Come on, calm down!"
    player "I was just worried about you, that's it."
    vicky "Were you? Really?"
    vicky "Why weren't you when you slapped me?!"
    player "Because I wanted to teach you a lesson."
    vicky "Oh, you did!"
    player "And! I was very careful."
    player "I didn't slap you hard..."
    vicky "Oh, so you are saying that I should be grateful?!"
    player "No! All I'm saying is that you were supposed to like it!"
    vicky "Oh... well..."
    "She lowers her voice to whisper."
    vicky "The truth is that... I... I... kind of... liked it!"
    player "Oh! Good to know!"
    vicky "And... and it scares me!"
    player "It shouldn't. We were just having fun."
    vicky "You think so?"
    player "Absolutely certain!"
    player "There's nothing to be scared of!"
    vicky "Oh, well... If you say so..."
    vicky "Maybe you are right..."
    player "Of course I am!"
    player "Tell me when you are ready for the next session."
    vicky "Oh, you are impossible!"
elif vicky_corruption == 11 and FLAG_TALK_VICKY11 not in flags:
    $ flags.add(FLAG_TALK_VICKY11)
    vicky "Hey, Alex!"
    vicky "Listen, I need to talk to you..."
    player "Aha, me, too!"
    vicky "You too??? What about?!"
    player "What if I wanted to ask how you liked our little cock sucking experiment?!"
    player "And when you'd like to repeat it?!"
    vicky "Unbelievable!"
    vicky "Fuck off!"
    vicky "I'm not doing that again!"
    player "Oh, really???"
    player "Why not?!"
    vicky "Just because!!!"
    vicky "Gosh, you are so selfish!"
    player "Why wouldn't I be?!"
    player "I know, you liked it, too..."
    vicky "Enough!"
    vicky "I don't want to hear another word!"
    vicky "But! I still need to talk to you!"
    player "What about?"
    vicky "Listen, I found a nice part time job... as a shop girl..."
    vicky "But I need your help!"
    player "???"
    vicky "Mom doesn't let me drive her car!"
    player "And?"
    vicky "And I can't get there without a car!"
    player "And?"
    player "How do I come into the picture?"
    vicky "Can you... can you work with me?"
    vicky "Anyway, they were searching for two shop assistants..."
    vicky "And I told them that you are an expert in fashion..."
    player "Oh, crap!"
    vicky "Relax!"
    vicky "You get the job, you get to know plenty of nice girls and... you get to drive the car..."
    vicky "It's a win-win for both of us!"
    player "Oh, is it?"
    vicky "Yes, it is!"
    vicky "I'm telling you!!!"
    player "Nope, I don't agree!"
    vicky "But why???"
    vicky "I've planned it all so thoroughly..."
    player "Because there's nothing in it for me!"
    vicky "Okay, fine!"
    vicky "What do you want?"
    player "What if we make this cock sucking experiment our regular thing?!"
    vicky "WHAT???"
    player "You heard me..."
    vicky "I... I... no!!!"
    player "Okay then. My answer is 'no' as well..."
    vicky "Shit!"
    vicky "You're blackmailing me! Again!"
    player "That's because you need me. Not the other way round!"
    vicky "Okay, fine! I agree!"
    player "Deal? Promise?"
    vicky "Yes, you have my word!"
    player "Okay, nice! When do we start working?"
    vicky "In two days."
    player "Awesome! Don't forget to stop by my room and suck my cock before that!"
    vicky "Oh, go to hell, you, dickhead!"
    player "Nice talk!"
else:
    "You spend some time chatting with Vicky and your relationship has improved."

$ karma += 1
"+1 karma"
$ skip_time = True

return




label talk_ashley:

hide emma
hide vicky
show ashley neutral at center

"You spend some time chatting with Ashley and your relationship has improved."

$ karma += 1
"+1 karma"
$ skip_time = True

return




label photo_emma:

$ raise NotImplementedError()

return




label photo_vicky:

hide emma
hide ashley
show vicky neutral at center
player "Hey! What about a quick photoshoot?"
if FLAG_PHOTO_VICKY not in daily_flags:
    $ daily_flags.add(FLAG_PHOTO_VICKY)
    vicky "Sure!"
    call ps_main ("vicky", "Vicky", ps_vicky_flags)
    $ player_location = LOCATION_PLAYER_ROOM
    $ skip_time = True
else:
    vicky "Nah! Tomorrow maybe..."

return




label play_ashley:

hide emma
hide vicky
show ashley neutral at center
player "Let's have some fun!"
ashley "Well..."
call pg_main ("ashley", "Ashley", pg_ashley_flags)
$ player_location = LOCATION_PLAYER_ROOM
$ skip_time = True

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
