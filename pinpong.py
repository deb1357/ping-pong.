from pygame import *
window = display.set_mode((700,500))
display.set_caption("Пинг Понг")
backgrount = transform.scale(image.load("1.webp"),(700, 500))

game = True
while game:
    window.blit(backgrount,(0, 0))


    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    