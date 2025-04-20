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
        if key_pressed[K_w] and self.rect.y > -50:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y < 350:
            self.rect.y += self.speed

class Player2(GameSprite):
    def update(self):
        if key_pressed[K_UP] and self.rect.y > -50:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y < 350:
            self.rect.y += self.speed

class Tennis_Ball(GameSprite):
    def update(self):
        self.rect.x += self.speed
        if self.rect.x >= 600:
            self.rect.x = 150


window = display.set_mode((700, 500))
display.set_caption('Пинг-понг')

player = Player('stick.png', -10, 50, 10, 70, 200)
player2 = Player2('stick.png', 650, 50, 10, 70, 200)
ball = Tennis_Ball('tennis.png', 200, 250, 5, 50, 50)


FPS = 60
clock = time.Clock()
game = True
finish = False
while game:
    window.fill((0, 150, 255))
    key_pressed = key.get_pressed()

    if finish != True:
        player.update()
        player2.update()
        ball.update()



    for e in event.get():
        if e.type == QUIT:
            game = False

    player.reset()
    player2.reset()
    ball.reset()
    clock.tick(FPS)

    display.update()    