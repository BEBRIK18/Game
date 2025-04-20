from random import *

from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, length, higth):
        super().__init__()
        self.player_image = player_image
        self.image = transform.scale(image.load(player_image), (length, higth))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        if key_pressed[K_UP] and self.rect.y > -50:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y < 350:
            self.rect.y += self.speed


window = display.set_mode((700, 500))
display.set_caption('Пинг-понг')

player = Player('stick.png', -10, 50, 10, 70, 200)


FPS = 60
clock = time.Clock()
game = True
finish = False
while game:
    window.fill((0, 150, 255))
    key_pressed = key.get_pressed()

    if finish != True:
        player.update()



    for e in event.get():
        if e.type == QUIT:
            game = False

    player.reset()
    clock.tick(FPS)

    display.update()    