import pygame, sys
pygame.init()

#set refresh rate and clock
FPS = 30
fps_clock = pygame.time.Clock()

#create your own custom colors here

#names
#player1 = pygame.image.load("model.png")

sf = 0.3
#player1 = pygame.transform.scale(, (int(w * sf), int(h * sf)))
frames = 0
p1x = 500
p1y = 380
speed = -2

p2x = 200
p2y = 280
is_jump = False
jump_height = 15
jump_pos = 0
jump = -9
jump_count = 0
grass = pygame.image.load("grass.png")
raindrop1 = pygame.image.load("rain_drop.png")
raindrop2 = pygame.image.load("rain_drop1.png")
raindrop3 = pygame.image.load("rain_drop2.png")
raindrop4 = pygame.image.load("rain_drop3.png")
raindrop5 = pygame.image.load("rain_drop4.png")
raindrop6 = pygame.image.load("rain_drop5.png")
raindrop7 = pygame.image.load("rain_drop6.png")
raindrop8 = pygame.image.load("rain_drop7.png")
raindrop9 = pygame.image.load("rain_drop8.png")
blink_bounce1 = pygame.image.load("blink_bounce1.png")
blink_bounce2 = pygame.image.load("blink_bounce2.png")
blink_bounce3 = pygame.image.load("blink_bounce3.png")
blink_bounce4 = pygame.image.load("blink_bounce4.png")
rain1 = pygame.image.load("rain.tile.png")
rain2 = pygame.image.load("rain_tile1.png")
rain3 = pygame.image.load("rain_tile2.png")
rain4 = pygame.image.load("rain_tile3.png")
rain5 = pygame.image.load("rain_tile4.png")
blink1 = pygame.image.load("bounceani2.png")
blink2 = pygame.image.load("model2_blink1.png")
blink3 = pygame.image.load("model2_blink2.png")
blink4 = pygame.image.load("model2_blink1.png")
blink_images = [blink1, blink2, blink3, blink3, blink4, blink1, blink1, blink1, blink1, blink1, blink1]
bounce1 = pygame.image.load("bounceani1.png")
bounce2 = pygame.image.load("bounceani2.png")
bounce_images = [bounce2, bounce2, bounce1, bounce1, bounce2, bounce2, bounce1, blink_bounce3, blink_bounce1, blink_bounce4, blink_bounce2, blink_bounce3, blink_bounce1, blink_bounce3]
rain_images = [rain1, rain2, rain3, rain4, rain5]
raindrop_images = [raindrop1, raindrop2, raindrop3, raindrop4, raindrop5, raindrop6, raindrop7, raindrop8, raindrop9]
for i in range(len(blink_images)):
    (w, h) = blink_images[i].get_size()
    blink_images[i] = pygame.transform.scale(blink_images[i], (int(w * sf), int(h * sf)))
for i in range(len(bounce_images)):
    (w, h) = bounce_images[i].get_size()
    bounce_images[i] = pygame.transform.scale(bounce_images[i], (int(w * sf), int(h * sf)))
for i in range(len(rain_images)):
    (w, h) = rain_images[i].get_size()
    rain_images[i] = pygame.transform.scale(rain_images[i], (int(w * sf), int(h * sf)))
for i in range(len(raindrop_images)):
    (w, h) = raindrop_images[i].get_size()
    raindrop_images[i] = pygame.transform.scale(raindrop_images[i], (int(w * 0.2), int(h * 0.2)))
for i in range(1):
    (w, h) = grass.get_size()
    grass = pygame.transform.scale(grass, (int(w * sf), int(h * sf)))


pygame.mixer.music.load("JJD.mp3")
pygame.mixer.music.play(-1, 0.0)
frames = 0
p1x = 500
p1y = 498
speed = 15

p2x = 200
p2y = 250

background = pygame.image.load("start.png")
bgrect = background.get_rect()
bgrect.center = (500, 350)
#set up window
screen = pygame.display.set_mode((1000, 700))

#set caption for game
pygame.display.set_caption('My Game!')


#set background color for game
#screen.fill(OCEAN_BLUE)


#game loop
while True:
#start here
    '''
#use for qucisand

    if is_jump:
        if jump_count >= jump_height:
            jump = 1
        p1y += jump
        jump_count += 1
        if jump_count == jump_height * 2:
            is_jump == False
            jump_count = 0
    '''
    screen.fill((0, 0, 0))
    screen.blit(background, bgrect)
    if is_jump:
        if jump_count >= jump_height:
            jump = 9
        p1y += jump
        jump_count += 1
        if jump_count >= jump_height * 2:
            is_jump = False
            jump_count = 0
            jump = -9
    #screen.blit(player1,(p1x, p1y))
    index = round (frames/5)%11
    screen.blit(blink_images[index], (p2x, p2y))
    index = round (frames/20)%13
    screen.blit(bounce_images[index], (p1x, p1y))
    #index = round (frames/6)%5
    #screen.blit(rain_images[index], (300, 350))
    index = round (frames/6)%9
    for i in range(20):
        screen.blit(raindrop_images[index], (20 + i * 65, 370))
    for i in range(20):
        screen.blit(grass, (20 + i * 125, 527))
    
    
    #screen.blit(player2,(p2x, p2y))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        is_jump = True
        
    '''
    if keys[pygame.K_DOWN]:
        p1y += speed
    '''
    if keys[pygame.K_LEFT]:
        p1x -= speed
        p1x
    if keys[pygame.K_RIGHT]:
        p1x += speed
        p1x
        
    if keys[pygame.K_w]:
        p2y -= speed
    if keys[pygame.K_s]:
        p2y += speed
    if keys[pygame.K_a]:
        p2x -= speed
    if keys[pygame.K_d]:
        p2x += speed
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()
    fps_clock.tick(FPS)
    frames += 4
