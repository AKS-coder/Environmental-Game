import pygame, sys, os
import time
from pygame.locals import *
import random
import pickle

file = ('water.mp3')
file1 = ('sound1.mp3')
lightning = ('lightning.mp3')
background = pygame.image.load('rainy.png')
yay = ('yay.mp3')
 
 
class You:
    def __init__(self, dodged, missed, Hscore, chance):
        self.dodged = dodged
        self.missed = missed
        self.Hscore = Hscore
        self.chance = chance
 
 
 
 
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play(1000)
 
 
 
 
display_width = 800
display_height = 600
 
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (135,206,250)
yellow = (255, 255, 0)
 
 
dark_red = (160,0,0)
dark_blue = (0,0,205)
dark_green = (0,160,0)
 
 
 
car_width = 105
car_height = 70
 
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Water Saviour")
clock = pygame.time.Clock()
 
Pimg = pygame.image.load('bucket.png').convert()
raindrop = pygame.image.load('raindrop.png').convert()
 
 
def Tdodged(count):
    font= pygame.font.SysFont(None, 25)
    text = font.render("Drops of water saved:" + str(count), True, red)
    #count = PlayerIG.score
    gameDisplay.blit(text, (0, 0))
   
   
 
def Tmissed(count):
    font= pygame.font.SysFont(None, 25)
    text = font.render("Missed:" + str(count), True, red)
    #count = PlayerIG.missed
    gameDisplay.blit(text, (0, +50))
 
 
def Tspeed(count):
    font= pygame.font.SysFont(None, 25)
    text = font.render("Speed:" + str(count), True, red)
    gameDisplay.blit(text, (0, +25))
 
def Tscore(count):
    font= pygame.font.SysFont(None, 25)
    text = font.render("Highscore:" + str(count), True, red)
    gameDisplay.blit(text, (0, +75))
 
def chance(count):
    if chance >= 2:
        gameintro()
    else:
        pass
 
 
def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()
   
 
 
 
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 45)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)
 
    pygame.display.update()
 
    time.sleep(2)
 
 
 
 
 
 
def again():
    largeText = pygame.font.Font('freesansbold.ttf', 45)
    TextSurf, TextRect = text_objects("You have wasted too much water!!!", largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    clock.tick(60)
    learn()
   
   
 
 
def learn():
    tips = ["Take shorter showers",
            "Wash vegetables in a sink",
            "Choose to use reduced flush",
            "Don't waste water:)",
            "Fix a dripping tap",
            "Check your toilets for leak",
            "Insulate your water pipe",
            "Every drop counts:)"]
 
 
    gameDisplay.fill(blue)
    largeText = pygame.font.Font('freesansbold.ttf', 55)
    TextSurf, TextRect = text_objects(random.choice(tips), largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)
 
    pygame.display.update()
    time.sleep(3)
    





 
 
def Qns():
       
       
    gameDisplay.fill(red)
    largeText = pygame.font.Font('freesansbold.ttf', 55)
    TextSurf, TextRect = text_objects("Thank you", largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.flip()
    time.sleep(3)
                       
    gameintro()
   
   
#Raindrops
def things(thingx, thingy, thingw, thingh):
    raindrop.set_colorkey(white)
    gameDisplay.blit(raindrop, [thingx, thingy, thingw, thingh])
 
   
 
def car(x, y):
    Pimg.set_colorkey(white)
    gameDisplay.blit(Pimg, (x, y))
 
 
def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
   
    if x + w > mouse[0] > x and y + h > mouse[1] > y:            
        pygame.draw.rect(gameDisplay, ic,(x, y, w, h))
        if click[0] == 1 and action != None:            
            if action == "play":
                game_loop()
            elif action == "quit":
                pygame.quit()
                quit()
           
    else:
        pygame.draw.rect(gameDisplay, ac,(x, y, w, h))
 
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w / 2)), (y + (h/2)) )
    gameDisplay.blit(textSurf, textRect)
 
 
def gameintro():
    pygame.mixer.music.pause()
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(1000)
    cloudx = random.randint(0, 400)
    cloudy = random.randint(0, 300)
    cloud1x = random.randint(0, 400)
    cloud1y = random.randint(0, 300)
    cloud_speed = 2.5
    chance = 1
   
    intro = True
 
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(blue)              
        largeText = pygame.font.Font('freesansbold.ttf', 110)
        TextSurf, TextRect = text_objects("Water Saviour", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)
 
        button("start", 150, 450, 100, 50, dark_green, green, "play")
        button("quit", 550, 450, 100, 50, dark_red, red, "quit")

        if os.path.exists("savefile") == True:
            with open('savefile', 'rb') as f:
                count = pickle.load(f)
                font = pygame.font.SysFont(None, 35)
                text = font.render("High Score:" + str(count), True, red)
                gameDisplay.blit(text,(0,0))
        
        cloud = pygame.image.load('cloud.png')
        cloud1 = pygame.image.load('cloud.png')
        gameDisplay.blit(cloud, (cloudx, cloudy))
        gameDisplay.blit(cloud1, (cloud1x, cloud1y))
        if intro is True:
            cloudx += cloud_speed
            cloud1x += cloud_speed
            if cloudx >= display_width:
                cloudx = random.randint(0, 400)
                cloudy = random.randint(0, 300)
            if cloud1x >= display_width:
                cloud1x = random.randint(0, 400)
                cloud1y = random.randint(0, 300)
           
        #(self, image, height, width, speed)
       
 
        pygame.display.update()
        clock.tick(15)
       
pause = True
 
def unpause():
    global pause
    pause = False
   
   
def cont():
   
    global pause
    pause = False
    if pygame.mouse.get_pressed()[0]:
        return game_loop()
 
 
def paused():
   
 
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(blue)
        pygame.mixer.music.pause()
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("Pause", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)
        button("continue", 150, 450, 100, 50, dark_green, green, cont())
        button("quit", 550, 450, 100, 50, dark_red, red, gameintro())
       
       
        pygame.display.update()
        clock.tick(15)
       
 
 
 
def game_loop():
    pygame.mixer.music.pause()
    pygame.mixer.init()
    pygame.mixer.music.load(file1)
    pygame.mixer.music.play()
    global pause
   
 
    x = (display_width * 0.45)
    y = (display_height * 0.8)
 
    bg_pos = [0, 0]
   
    k = 8
    x_change = 0
    y_change = 0
    c = 0
 
    u = You(0, 0, 0, 1)
    thing_startx = random.randrange(0, 745)
    thing_starty = -600
    thing_speed = 5
    thing_width = 55
    thing_height = 80
    u.dodged = 0
    u.missed = 0
    u.Hscore = 0
    u.chance = 1
       
    gameEXIT = False
 
 
 
    while not gameEXIT:      
       
        for event in pygame.event.get():
           
            if event.type == pygame.QUIT:              
                pygame.quit()
                quit()
           
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -k
                elif event.key == pygame.K_RIGHT:
                    x_change = k
                if event.key == pygame.K_ESCAPE:
                    pause = True
                    gameintro()
 
               
               
               
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
               
 
   
 
 
        x += x_change
        y += y_change
                   
 
        #user()
 
 
        if os.path.exists("savefile") == True:
            with open('savefile', 'rb') as f:
                u.Hscore = pickle.load(f)
        else:
            pass
 
        if u.chance >= 3:
            gameDisplay.fill(green)
            largeText = pygame.font.Font('freesansbold.ttf', 55)
            TextSurf, TextRect = text_objects('Please let others have a go:)', largeText)
            TextRect.center = ((display_width / 2), (display_height / 2))
            gameDisplay.blit(TextSurf, TextRect)
 
            pygame.display.update()
            time.sleep(3)
            Qns()
        else:
            pass
               
        gameDisplay.blit(background, bg_pos)
 
        things(thing_startx, thing_starty, thing_width, thing_height)
        thing_starty += thing_speed
       
        #printing of objects
        car(x,y)
       
        Tdodged(u.dodged)
        Tmissed(u.missed)
        Tspeed(x_change)
        Tscore(u.Hscore)
 
 
       
        if x > display_width - car_width:
            x = (display_width - car_width)
        if x < 0:
            x = 0
        if y < 0:
            y = 0
        if y + car_height > display_height:
            y = (display_height - car_height)
 
 
       
 
       
        if (thing_startx + thing_width) > display_width:
            thing_startx = 690
 
 
 
       
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width - 110)
            u.missed += 1
           
            pygame.mixer.init()
            pygame.mixer.music.load(lightning)
            pygame.mixer.music.play()                        
 
            time.sleep(2.5)
            pygame.mixer.music.load(file1)
            pygame.mixer.music.play()
            pygame.display.flip()
               
            if u.missed == 3:
                if u.dodged >= u.Hscore:
                    u.Hscore == 0
                    u.Hscore = u.dodged                        
                    with open('savefile', 'wb') as f:
                        pickle.dump(u.Hscore, f)
                    gameDisplay.fill(red)
                    pygame.mixer.init()
                    pygame.mixer.music.load(yay)
                    pygame.mixer.music.play()                        
 
 
                    largeText = pygame.font.Font('freesansbold.ttf', 70)
                    TextSurf, TextRect = text_objects("New High Score!!!", largeText)
                    TextRect.center = ((display_width / 2), (display_height / 2))
                    gameDisplay.blit(TextSurf, TextRect)
                    pygame.display.flip()
                    time.sleep(2)
                    pygame.mixer.music.load(file1)
                    pygame.mixer.music.play()
                    time.sleep(1.8)
                    clock.tick(60)
                    u.missed = 0
                    u.dodged = 0
                    thing_speed = 5
                    u.chance += 1
                    continue
                
                
                   
                                           
                else:
                    pass              
                u.missed = 0
                u.dodged = 0
                thing_speed = 5
                u.chance += 1
                
                again()
 
            else:
                pass
   
            thing_startx = random.randrange(0, display_width - 110)
            #thing_speed += 1
       
 
        #checker
        if y <= thing_starty:
 
            centre = thing_startx + thing_width / 2
 
            if x < centre and x + car_width > centre:                
                u.dodged += 1
                thing_starty = 0 - thing_height
                thing_startx = random.randrange(0, display_width)
 
                #Rain Drop & bucket Speed increase
                if (u.dodged % 5 == 0) and (u.dodged != 0):
                    thing_speed += 0.43
                    k += 0.17
                #Yay
                if (u.dodged % 15 == 0) and (u.dodged != 0):
                   
                   
                    pygame.mixer.init()
                    pygame.mixer.music.load(yay)
                    pygame.mixer.music.play()                        
 
                    time.sleep(2)
                    pygame.mixer.music.load(file1)
                    pygame.mixer.music.play()
                    time.sleep(1.5)
                    pygame.display.flip()
                    continue
               
                else:
                    continue
               
        #if y <= (P_starty + P_height):
            #u.dodged -= 1
           
           
       
               
 
        pygame.display.update()
 
        clock.tick(80)
 
gameintro()
#game_loop()
pygame.quit()
quit()
