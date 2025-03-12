function say_something(sprite: Sprite) {
    sprite.sayText("Hello my name is Dane.")
}

info.onCountdownEnd(function on_countdown_end() {
    game.gameOver(true)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function on_on_overlap(sprite2: Sprite, otherSprite: Sprite) {
    OverlapFunction()
    info.changeLifeBy(1)
    music.play(music.createSoundEffect(WaveShape.Sine, 200, 600, 255, 0, 150, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.UntilDone)
})
info.onScore(100, function on_on_score() {
    game.gameOver(true)
})
info.onScore(0, function on_on_score2() {
    game.gameOver(false)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function on_on_overlap2(sprite3: Sprite, otherSprite2: Sprite) {
    EnemyChaserPlayer.setPosition(randint(10, 150), randint(10, 110))
    OverlapFunction()
    info.changeLifeBy(-1)
})
controller.B.onEvent(ControllerButtonEvent.Released, function on_b_released() {
    say_something(Duck)
})
function EnemyChaser() {
    
    EnemyChaserPlayer = sprites.create(img`
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
        `, SpriteKind.Enemy)
    EnemyChaserPlayer.setPosition(2, 2)
    EnemyChaserPlayer.follow(Duck, 88)
}

function OverlapFunction() {
    food.setPosition(randint(10, 150), randint(10, 110))
    info.changeScoreBy(1)
}

let EnemyChaserPlayer : Sprite = null
let food : Sprite = null
let Duck : Sprite = null
Duck = sprites.create(img`
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
    `, SpriteKind.Player)
food = sprites.create(img`
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
    `, SpriteKind.Food)
Duck.follow(food)
Duck.setStayInScreen(true)
food.setPosition(randint(10, 150), randint(10, 110))
info.setScore(0)
info.setLife(3)
EnemyChaser()
info.startCountdown(40)
