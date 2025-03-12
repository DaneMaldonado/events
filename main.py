def say_something(sprite: Sprite):
    sprite.say_text("Hello my name is Dane.")

def on_countdown_end():
    game.game_over(True)
info.on_countdown_end(on_countdown_end)

def on_on_overlap(sprite2, otherSprite):
    OverlapFunction()
    info.change_life_by(1)
    music.play(music.create_sound_effect(WaveShape.SINE,
            200,
            600,
            255,
            0,
            150,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LINEAR),
        music.PlaybackMode.UNTIL_DONE)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap)

def on_on_score():
    game.game_over(True)
info.on_score(100, on_on_score)

def on_on_score2():
    game.game_over(False)
info.on_score(0, on_on_score2)

def on_on_overlap2(sprite3, otherSprite2):
    EnemyChaserPlayer.set_position(randint(10, 150), randint(10, 110))
    OverlapFunction()
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

def on_b_released():
    say_something(Duck)
controller.B.on_event(ControllerButtonEvent.RELEASED, on_b_released)

def EnemyChaser():
    global EnemyChaserPlayer
    EnemyChaserPlayer = sprites.create(img("""
            ........................
                    ....ffffff..............
                    ..ffeeeef2f.............
                    .ffeeeef222f............
                    .feeeffeeeef...cc.......
                    .ffffee2222ef.cdc.......
                    .fe222ffffe2fcddc.......
                    fffffffeeeffcddc........
                    ffe44ebf44ecddc.........
                    fee4d41fddecdc..........
                    .feee4dddedccc..........
                    ..ffee44e4dde...........
                    ...f222244ee............
                    ...f2222e2f.............
                    ...f444455f.............
                    ....ffffff..............
                    .....fff................
                    ........................
                    ........................
                    ........................
                    ........................
                    ........................
                    ........................
                    ........................
        """),
        SpriteKind.enemy)
    EnemyChaserPlayer.set_position(2, 2)
    EnemyChaserPlayer.follow(Duck, 88)
def OverlapFunction():
    food.set_position(randint(10, 150), randint(10, 110))
    info.change_score_by(1)
EnemyChaserPlayer: Sprite = None
food: Sprite = None
Duck: Sprite = None
Duck = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . 4 4 4 . . . . 4 4 4 . . . . 
            . 4 5 5 5 e . . e 5 5 5 4 . . . 
            4 5 5 5 5 5 e e 5 5 5 5 5 4 . . 
            4 5 5 4 4 5 5 5 5 4 4 5 5 4 . . 
            e 5 4 4 5 5 5 5 5 5 4 4 5 e . . 
            . e e 5 5 5 5 5 5 5 5 e e . . . 
            . . e 5 f 5 5 5 5 f 5 e . . . . 
            . . f 5 5 5 4 4 5 5 5 f . f f . 
            . . . 4 5 5 f f 5 5 6 f f 5 f . 
            . . . f 6 6 6 6 6 6 4 4 4 5 f . 
            . . . f 5 5 5 5 5 5 5 f f f . . 
            . . . f 5 4 5 f f f 5 f . . . . 
            . . . f f f f f . . f f . . . .
    """),
    SpriteKind.player)
food = sprites.create(img("""
        . . . . . . . 6 . . . . . . . . 
            . . . . . . 8 6 6 . . . 6 8 . . 
            . . . e e e 8 8 6 6 . 6 7 8 . . 
            . . e 2 2 2 2 e 8 6 6 7 6 . . . 
            . e 2 2 4 4 2 7 7 7 7 7 8 6 . . 
            . e 2 4 4 2 6 7 7 7 6 7 6 8 8 . 
            e 2 4 5 2 2 6 7 7 6 2 7 7 6 . . 
            e 2 4 4 2 2 6 7 6 2 2 6 7 7 6 . 
            e 2 4 2 2 2 6 6 2 2 2 e 7 7 6 . 
            e 2 4 2 2 4 2 2 2 4 2 2 e 7 6 . 
            e 2 4 2 2 2 2 2 2 2 2 2 e c 6 . 
            e 2 2 2 2 2 2 2 4 e 2 e e c . . 
            e e 2 e 2 2 4 2 2 e e e c . . . 
            e e e e 2 e 2 2 e e e c . . . . 
            e e e 2 e e c e c c c . . . . . 
            . c c c c c c c . . . . . . . .
    """),
    SpriteKind.food)
Duck.follow(food)
Duck.set_stay_in_screen(True)
food.set_position(randint(10, 150), randint(10, 110))
info.set_score(0)
info.set_life(3)
EnemyChaser()
info.start_countdown(40)