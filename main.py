def on_a_pressed():
    say_something(my_sprite)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def say_something(sprite: Sprite):
    sprite.say_text("Hello my name is Dane.")
my_sprite: Sprite = None
my_sprite = sprites.create(img("""
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
my_sprite.set_stay_in_screen(True)


# Create the food sprite and place it at a random location
food = sprites.create(img("""
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    . . . . .
"""), SpriteKind.food)
food.set_position(randint(10, 150), randint(10, 110))

# Handle collision between player and food
def on_overlap(sprite, otherSprite):
    # Actions to take when the player collides with food
    food.set_position(randint(10, 150), randint(10, 110))  # Move food to a new random location
    info.change_score_by(1)  # Increment the score by 1

# When the player collides with the food, run the on_overlap function
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_overlap)

def on_update():
    pass
game.on_update(on_update)