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
    def __init__(self,player_image, player_x, player_y, player_speed, length, higth, speed_x = 3, speed_y = 3, count = 0):
        super().__init__(player_image, player_x, player_y, player_speed, length, higth)
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.count = count

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.y > 450 or self.rect.y < 0:
            self.speed_y *= -1
        if sprite.collide_rect(player, self) or sprite.collide_rect(player2, self):
            self.speed_x *= -1 
            self.count += 1 
        if self.count == 4:
            self.speed_x += 1
            self.speed_y += 1
            self.count = 0



window = display.set_mode((700, 500))
display.set_caption('Пинг-понг')

player = Player('stick1.png', -10, 50, 10, 70, 200)
player2 = Player2('stick1.png', 650, 50, 10, 70, 200)
ball = Tennis_Ball('tennis.png', 200, 250, 5, 50, 50)

counter1 = 0
counter2 = 0

font.init()
font1 = font.Font(None, 70)
font2 = font.Font(None, 40)
win1 = font1.render('Player1 won', True, (255, 0, 0))
win2 = font1.render('Player2 won', True, (255, 0, 0))


FPS = 60
clock = time.Clock()
game = True
finish = False
speed_x = 3
speed_y = 3
while game:
    window.fill((0, 150, 255))
    key_pressed = key.get_pressed()

    if finish != True:
        player.update()
        player2.update()
        ball.update()
        countt1 = font2.render(f'Player1:{counter1}', True, (255, 0, 0))
        countt2 = font2.render(f'Player2:{counter2}', True, (255, 0, 0))
        window.blit(countt1, (50, 50))
        window.blit(countt2, (530, 50))


    if ball.rect.x < 0:
        # window.blit(win2, (350, 250))
        # finish = True
        counter2 += 1
        ball.rect.x = 200
        ball.rect.y = 200
    if ball.rect.x > 700:
        # window.blit(win1, (100, 250))
        # finish = True
        counter1 += 1
        ball.rect.x = 200
        ball.rect.y = 200
    if counter2 == 2:
        window.blit(win2, (100, 250))
        finish = True    

    if counter1 == 2:
        window.blit(win1, (100, 250))
        finish = True 


    for e in event.get():
        if e.type == QUIT:
            game = False

    player.reset()
    player2.reset()
    ball.reset()
    clock.tick(FPS)

    display.update()    