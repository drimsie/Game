import random as rnd
import pygame as pg
#почему-то кнопки отображаются только после нажатия "закрыть"

class Window:
    width =640
    height = 480
    centr_x = width/2
    centr_y = height/2

FPS=1

pg.init()
screen=pg.display.set_mode ((Window.width, Window.height))
clock=pg.time.Clock()

GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
VIOLET = (180, 0, 150)
RED = (255, 0, 0)

screen.fill(WHITE)

font3 = pg.font.SysFont("serif", 36)
text3 = font3.render("Вопрос", True, BLACK)

screen.blit(text3, (10, Window.centr_x))


class Button:
    mouseIsOver= False
    mouseIsDown= False
    mouseIsClick= False
    mouseIsUp= False
    width = 0
    #конструктор
    def __init__(self, color, x, y, width, height):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def draw (self, screen):
        pg.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
    def is_over(self, mouse_x, mouse_y):
        return self.x <= mouse_x <= self.x+self.width and \
               self.y <= mouse_y <= self.y+self.height
    def jumpto(self, x, y):
        self.x = x
        self.y = y

distance_to_centr_x = 30
Button.width = 100
Button.height = 30
view_x = Window.centr_x - distance_to_centr_x - Button.height
view_y = Window.centr_y

btn_yes = Button(GREEN, view_x,view_y , Button.width, Button.height)
btn_no = Button(RED, view_x + Button.width + distance_to_centr_x, view_y, Button.width, Button.height)

running = True
while running:
    clock.tick(FPS)
    screen.fill(WHITE)


    list_events = pg.event.get() #список событий
    for event in list_events:
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEMOTION:
            mouse_x, mouse_y = event.pos #коррдинаты мышки
            if btn_no.is_over(mouse_x, mouse_y):
                new_x=rnd.randint (0, Window.width)
                new_y=rnd.randint (0, Window.height)
                btn_no.jumpto (new_x,new_y)
            btn_yes.mouseIsOver = btn_yes.is_over (mouse_x, mouse_y)
        if btn_yes.mouseIsOver:
            if event.type == pg.MOUSEBUTTONDOWN and event.button==1:
                btn_yes.mouseIsDown = True
            if event.type == pg.MOUSEBUTTONUP and event.button==1:
                btn_yes.mouseIsUp = True
            if btn_yes.mouseIsUp and btn_yes.mouseIsDown:
                btn_yes.mouseIsClick = True
                print ("Up on Yes")

btn_yes.draw(screen)
btn_no.draw(screen)
screen.blit(text3, (Window.centr_x, 10))
pg.display.update()

pg.quit()