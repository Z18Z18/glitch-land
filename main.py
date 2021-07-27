def on_up_repeated():
    animation.run_image_animation(mySprite,
        [img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . f f f f . . . . . . . 
                        . . . f f e e e e f f . . . . . 
                        . . f e e e f f e e e f . . . . 
                        . . f f f f 2 2 f f f f . . . . 
                        . f f e 2 e 2 2 e 2 e f f . . . 
                        . f e 2 f 2 f f f 2 f e f . . . 
                        . f f f 2 f e e 2 2 f f f . . . 
                        . f e 2 f f e e 2 f e e f . . . 
                        f f e f f e e e f e e e f f . . 
                        f f e e e e e e e e e e f d f . 
                        . . f e e e e e e e e f f b f . 
                        . . e f f f f f f f f 4 f b f . 
                        . . 4 f 2 2 2 2 2 e d d f c f . 
                        . . e f f f f f f e e 4 f f . . 
                        . . . f f f . . . . . . . . . .
            """),
            img("""
                . . . . . f f f f . . . . . . . 
                        . . . f f e e e e f f . . . . . 
                        . . f e e e f f e e e f . . . . 
                        . f f f f f 2 2 f f f f f . . . 
                        . f f e 2 e 2 2 e 2 e f f . . . 
                        . f e 2 f 2 f f 2 f 2 e f . . . 
                        . f f f 2 2 e e 2 2 f f f . . . 
                        f f e f 2 f e e f 2 f e f f . . 
                        f e e f f e e e e f e e e f . . 
                        . f e e e e e e e e e e f . . . 
                        . . f e e e e e e e e f . . . . 
                        . e 4 f f f f f f f f 4 e . . . 
                        . 4 d f 2 2 2 2 2 2 f d 4 . . . 
                        . 4 4 f 4 4 4 4 4 4 f 4 4 . . . 
                        . . . . f f f f f f . . . . . . 
                        . . . . f f . . f f . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . f f f f . . . . . . . 
                        . . . f f e e e e f f . . . . . 
                        . . f e e e f f e e e f . . . . 
                        . . f f f f 2 2 f f f f . . . . 
                        . f f e 2 e 2 2 e 2 e f f . . . 
                        . f e f 2 f f f 2 f 2 e f . . . 
                        . f f f 2 2 e e f 2 f f f . . . 
                        . f e e f 2 e e f f 2 e f . . . 
                        . f e e e f e e e f f e f f . . 
                        . f e e e e e e e e e e f f . . 
                        . f f e e e e e e e e f . . . . 
                        . f 4 f f f f f f f f e . . . . 
                        . f d d e 2 2 2 2 2 f 4 . . . . 
                        . f 4 e e f f f f f f e . . . . 
                        . . . . . . . . f f f . . . . .
            """),
            img("""
                . . . . . f f f f . . . . . . . 
                        . . . f f e e e e f f . . . . . 
                        . . f e e e f f e e e f . . . . 
                        . f f f f f 2 2 f f f f f . . . 
                        . f f e 2 e 2 2 e 2 e f f . . . 
                        . f e 2 f 2 f f 2 f 2 e f . . . 
                        . f f f 2 2 e e 2 2 f f f . . . 
                        f f e f 2 f e e f 2 f e f f . . 
                        f e e f f e e e e f e e e f . . 
                        . f e e e e e e e e e e f . . . 
                        . . f e e e e e e e e f . . . . 
                        . e 4 f f f f f f f f 4 e . . . 
                        . 4 d f 2 2 2 2 2 2 f d 4 . . . 
                        . 4 4 f 4 4 4 4 4 4 f 4 4 . . . 
                        . . . . f f f f f f . . . . . . 
                        . . . . f f . . f f . . . . . .
            """)],
        200,
        True)
controller.up.on_event(ControllerButtonEvent.REPEATED, on_up_repeated)

def on_left_pressed():
    animation.run_image_animation(mySprite,
        [img("""
                . . . . . f f f f f f . . . . . 
                        . . . . f 2 f e e e e f f . . . 
                        . . . f 2 2 2 f e e e e f f . . 
                        . . . f e e e e f f e e e f . . 
                        . . f e 2 2 2 2 e e f f f f . . 
                        . . f 2 e f f f f 2 2 2 e f . . 
                        . . f f f e e e f f f f f f f . 
                        . . f e e 4 4 f b e 4 4 e f f . 
                        . . f f e d d f 1 4 d 4 e e f . 
                        . f d d f d d d d 4 e e e f . . 
                        . f b b f e e e 4 e e f f . . . 
                        . f b b e d d 4 2 2 2 f . . . . 
                        . . f b e d d e 2 2 2 e . . . . 
                        . . . f f e e f 4 4 4 f . . . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . . . . f f f . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . f 2 f e e e e f f . . . 
                        . . . f 2 2 2 f e e e e f f . . 
                        . . . f e e e e f f e e e f . . 
                        . . f e 2 2 2 2 e e f f f f . . 
                        . . f 2 e f f f f 2 2 2 e f . . 
                        . . f f f e e e f f f f f f f . 
                        . . f e e 4 4 f b e 4 4 e f f . 
                        . . . f e d d f 1 4 d 4 e e f . 
                        . . . . f d d d e e e e e f . . 
                        . . . . f e 4 e d d 4 f . . . . 
                        . . . . f 2 2 e d d e f . . . . 
                        . . . f f 5 5 f e e f f f . . . 
                        . . . f f f f f f f f f f . . . 
                        . . . . f f f . . . f f . . . .
            """),
            img("""
                . . . . . f f f f f f . . . . . 
                        . . . . f 2 f e e e e f f . . . 
                        . . . f 2 2 2 f e e e e f f . . 
                        . . . f e e e e f f e e e f . . 
                        . . f e 2 2 2 2 e e f f f f . . 
                        . . f 2 e f f f f 2 2 2 e f . . 
                        . . f f f e e e f f f f f f f . 
                        . . f e e 4 4 f b e 4 4 e f f . 
                        . . f f e d d f 1 4 d 4 e e f . 
                        . f d d f d d d d 4 e e e f . . 
                        . f b b f e e e 4 e e f f . . . 
                        . f b b e d d 4 2 2 2 f . . . . 
                        . . f b e d d e 2 2 2 e . . . . 
                        . . . f f e e f 4 4 4 f . . . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . . . . f f f . . . . . .
            """)],
        200,
        True)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_pressed():
    animation.run_image_animation(mySprite,
        [img("""
                . . . . . f f f f f f . . . . . 
                        . . . f f e e e e f 2 f . . . . 
                        . . f f e e e e f 2 2 2 f . . . 
                        . . f e e e f f e e e e f . . . 
                        . . f f f f e e 2 2 2 2 e f . . 
                        . . f e 2 2 2 f f f f e 2 f . . 
                        . f f f f f f f e e e f f f . . 
                        . f f e 4 4 e b f 4 4 e e f . . 
                        . f e e 4 d 4 1 f d d e f f . . 
                        . . f e e e 4 d d d d f d d f . 
                        . . . f f e e 4 e e e f b b f . 
                        . . . . f 2 2 2 4 d d e b b f . 
                        . . . . e 2 2 2 e d d e b f . . 
                        . . . . f 4 4 4 f e e f f . . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . . . f f f . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . f f f f f f . . . . . 
                        . . . f f e e e e f 2 f . . . . 
                        . . f f e e e e f 2 2 2 f . . . 
                        . . f e e e f f e e e e f . . . 
                        . . f f f f e e 2 2 2 2 e f . . 
                        . . f e 2 2 2 f f f f e 2 f . . 
                        . f f f f f f f e e e f f f . . 
                        . f f e 4 4 e b f 4 4 e e f . . 
                        . f e e 4 d 4 1 f d d e f . . . 
                        . . f e e e e e d d d f . . . . 
                        . . . . f 4 d d e 4 e f . . . . 
                        . . . . f e d d e 2 2 f . . . . 
                        . . . f f f e e f 5 5 f f . . . 
                        . . . f f f f f f f f f f . . . 
                        . . . . f f . . . f f f . . . .
            """),
            img("""
                . . . . . f f f f f f . . . . . 
                        . . . f f e e e e f 2 f . . . . 
                        . . f f e e e e f 2 2 2 f . . . 
                        . . f e e e f f e e e e f . . . 
                        . . f f f f e e 2 2 2 2 e f . . 
                        . . f e 2 2 2 f f f f e 2 f . . 
                        . f f f f f f f e e e f f f . . 
                        . f f e 4 4 e b f 4 4 e e f . . 
                        . f e e 4 d 4 1 f d d e f f . . 
                        . . f e e e 4 d d d d f d d f . 
                        . . . f f e e 4 e e e f b b f . 
                        . . . . f 2 2 2 4 d d e b b f . 
                        . . . . e 2 2 2 e d d e b f . . 
                        . . . . f 4 4 4 f e e f f . . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . . . f f f . . . . . . .
            """)],
        200,
        True)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_down_pressed():
    animation.run_image_animation(mySprite,
        [img("""
                . . . . . . f f f f . . . . . . 
                        . . . . f f f 2 2 f f f . . . . 
                        . . . f f f 2 2 2 2 f f f . . . 
                        . . f f f e e e e e e f f f . . 
                        . . f f e 2 2 2 2 2 2 e e f . . 
                        . . f e 2 f f f f f f 2 e f . . 
                        . . f f f f e e e e f f f f . . 
                        . f f e f b f 4 4 f b f e f f . 
                        . f e e 4 1 f d d f 1 4 e e f . 
                        . . f f f f d d d d d e e f . . 
                        . f d d d d f 4 4 4 e e f . . . 
                        . f b b b b f 2 2 2 2 f 4 e . . 
                        . f b b b b f 2 2 2 2 f d 4 . . 
                        . . f c c f 4 5 5 4 4 f 4 4 . . 
                        . . . f f f f f f f f . . . . . 
                        . . . . . f f . . f f . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . f f f f . . . . . . 
                        . . . . f f f 2 2 f f f . . . . 
                        . . . f f f 2 2 2 2 f f f . . . 
                        . . f f f e e e e e e f f f . . 
                        . . f f e 2 2 2 2 2 2 e e f . . 
                        . f f e 2 f f f f f f 2 e f f . 
                        . f f f f f e e e e f f f f f . 
                        . . f e f b f 4 4 f b f e f . . 
                        . f f e 4 1 f d d f 1 4 e f . . 
                        f d f f e 4 d d d d 4 e f e . . 
                        f b f e f 2 2 2 2 e d d 4 e . . 
                        f b f 4 f 2 2 2 2 e d d e . . . 
                        f c f . f 4 4 5 5 f e e . . . . 
                        . f f . f f f f f f f . . . . . 
                        . . . . f f f . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . f f f f . . . . . . 
                        . . . . f f f 2 2 f f f . . . . 
                        . . . f f f 2 2 2 2 f f f . . . 
                        . . f f f e e e e e e f f f . . 
                        . . f e e 2 2 2 2 2 2 e f f . . 
                        . f f e 2 f f f f f f 2 e f f . 
                        . f f f f f e e e e f f f f f . 
                        . . f e f b f 4 4 f b f e f . . 
                        . . f e 4 1 f d d f 1 4 e f . . 
                        . . e f f f f d d d 4 e f . . . 
                        . . f d d d d f 2 2 2 f e f . . 
                        . . f b b b b f 2 2 2 f 4 e . . 
                        . . f b b b b f 5 4 4 f . . . . 
                        . . . f c c f f f f f f . . . . 
                        . . . . f f . . . f f f . . . .
            """)],
        200,
        True)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

moving = False
mySprite: Sprite = None
game.splash("press A to start ")
mySprite = sprites.create(img("""
        ........................
            .....ffff...............
            ...fff22fff.............
            ..fff2222fff............
            .fffeeeeeefff...........
            .ffe222222eef...........
            .fe2ffffff2ef...........
            .ffffeeeeffff...........
            ffefbf44fbfeff..........
            fee41fddf14eef..........
            .ffffdddddeef...........
            fddddf444eef............
            fbbbbf2222f4e...........
            fbbbbf2222fd4...........
            .fccf45544f44...........
            ..ffffffff..............
            ....ff..ff..............
            ........................
            ........................
            ........................
            ........................
            ........................
            ........................
            ........................
    """),
    SpriteKind.player)
controller.move_sprite(mySprite)
scene.camera_follow_sprite(mySprite)
effects.clouds.start_screen_effect()
tiles.set_tilemap(tiles.create_tilemap(hex("""
            1000100001010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101
        """),
        img("""
            . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . .
        """),
        [myTiles.transparency16, sprites.castle.tile_path5],
        TileScale.SIXTEEN))
dark_shadow = sprites.create(img("""
        ........................
            ........................
            ........................
            ........................
            ........................
            ........................
            ........................
            ..........bbbb..........
            ........bbddddbb........
            .......bddbbbbddb.......
            ......bdbbddddbbdb......
            .....bdbbdbbbbdbbdb.....
            .....bdbdbddddbdbdb.....
            .....cdbbdbbbbdbbdc.....
            .....cbdbbddddbbdbc.....
            .....efbddbbbbddbce.....
            .....eeffbddddbccee.....
            .....eeeeffcccceee......
            .....ceeeeeeeeeeee......
            .....ceeeeeeeeeeee......
            .....feeeeeeeeeeee......
            .....cceeeeeeeeeee......
            ......feeeeeeeeeee......
            .....6fceeeeeeeeee6.....
            ....6776eeeeeeeee676....
            ...6777666eeee6666776...
            ..67768e67766777667776..
            ...668ee7768867788666...
            ......ee77eeee77ecee....
            ......ee6eeeeee6eef.....
            ......eeeeeeeeeeeef.....
            ......eeeeeeeeeeeef.....
            ......eeeeeeeeeeecf.....
            ......ceeeeeeeeeecf.....
            ......ceeeeeeeeeeff.....
            ......feeeeeeeeeefe.....
            .....6feeeeeeeeeef6.....
            ....6776eeeeeeeee676....
            ...6777666eeee6667776...
            ..6776ee67777777667776..
            ...668ee7768867788666...
            ......ee77eeee67ee......
            ......ee6eeeeee6ce......
            ......eefeeeeeeece......
            ......eeceeeeeeece......
            ......eeceeeeeeefe......
            ......eeceeeeeeefe......
            ......eeeeeeeeeefe......
            ......eeeeeeeeeece......
            .....6eeeeeeeeeece6.....
            ....6776eeeeeeeee676....
            ...6776666eeee6766776...
            ..6776ee77777777667776..
            ...668ce7768867788666...
            ......ce77eeee67ee......
            ......ce6eeeeee6ee......
    """),
    SpriteKind.enemy)

def on_on_update():
    global moving
    moving = controller.left.is_pressed() or (controller.right.is_pressed() or (controller.up.is_pressed() or controller.down.is_pressed()))
    if not (moving):
        animation.stop_animation(animation.AnimationTypes.ALL, mySprite)
game.on_update(on_on_update)

def on_forever():
    pass
forever(on_forever)

def on_update_interval():
    pass
game.on_update_interval(200, on_update_interval)
