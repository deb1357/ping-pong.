from pygame import *
window = display.set_mode((700, 500))
display.set_caption("Пинг-Понг") 
background = transform.scale(image.load("1.webp"),(700, 500))
clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, Image, xx, yy, x, y, speed):
        super().__init__()

        self.image = transform.scale(
            image.load(Image),
            (xx, yy)
        )
        self.Size = SIZE
        self.rect = self.image.get_rect()
        self.Speed =speed
        self.x = x
        self.y = y

        self.rect.x = self.x
        self.rect.y = self.y
   

    def show(self, Window):
        window.blit(self.image, (self.rect.x, self.rect.y))




class Player(GameSprite):

    def Control(self, keys):
        if keys[pygame.K_w] and self.rect.y - self.speed >= 0:
            self.y -= self.speed
        if keys[pygame.K_s] and self.rect.y + self.speed <= SIZE[0] - SHIP_SIZE[0]:
            self.y += self.speed
    
    def Control2(self, keys):
        if keys[pygame.K_up] and self.rect.y - self.speed >= 0:
            self.y -= self.speed
        if keys[pygame.K_down] and self.rect.y + self.speed <= SIZE[0] - SHIP_SIZE[0]:
            self.y += self.speed

#ball = GameSprite('пинпонг мяч.png', 50, 50, 400, 150, 5)
game = True
while game:
    window.blit(background,(0,0))
    #ball.show(window)
    for e in event.get():
        if e.type == QUIT:
            game = False   
    clock.tick(60)
    display.update()            

    








    