import pygame as pg

FPS=30

pg.init()
screen=pg.display.set_mode((640,480))
clock=pg.time.Clock()

RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen.fill(WHITE)

font3 = pg.font.SysFont("serif", 36)
text3 = font3.render("Вопрос", True, BLACK)

screen.blit(text3, (10, 10))
pg.display.update()

class Button:
    #конструктор
    def __init__(self, color, x, y, width, height):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def draw (self, screen):
        pg.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
    def is_over(self):
        pass
    def jumpto(self):
        pass
    
btn_yes = Button(GREEN, 10, 100, 150, 30)
btn_no = Button(RED, 180, 100, 150, 30)

running = True
while running:
    clock.tick(FPS)
    screen.fill(WHITE)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    btn_yes.draw(screen)
    btn_no.draw(screen)
    screen.blit(text3, (10, 10))
    pg.display.update()
pg.quit()
