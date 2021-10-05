import pygame,sys
pygame.init()
pygame.font.init()

# define font
myfont = pygame.font.SysFont('Comic Sans MS', 30)

# window / tps
window = pygame.display.set_mode((500, 720))
pygame.display.set_caption('Calculator')
clock = pygame.time.Clock()

# Calculator Texture
calculator = pygame.image.load(r'calculator2.png')
calculator = pygame.transform.scale(calculator, (500, 720))

# Show Hitbox lines
showLines = False
showTexture = True

# define varibles
maths = []
mathsString = ''

run = True
while run:
    window.fill((255,255,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # CODE
        if event.type == pygame.MOUSEBUTTONUP:
            curser = pygame.mouse.get_pos()
            if curser[0] > 65 and curser[0] < 155:
                if curser[1] > 265 and curser[1] < 350:
                    maths.append('1')
                elif curser[1] > 370 and curser[1] < 460:
                    maths.append('4')
                elif curser[1] > 475 and curser[1] < 565:
                    maths.append('7')
                elif curser[1] > 580 and curser[1] < 675:
                    maths.append('*')
            elif curser[0] > 170 and curser[0] < 260:
                if curser[1] > 265 and curser[1] < 350:
                    maths.append('2')
                elif curser[1] > 370 and curser[1] < 460:
                    maths.append('5')
                elif curser[1] > 475 and curser[1] < 565:
                    maths.append('8')
                elif curser[1] > 580 and curser[1] < 675:
                    maths.append('0')
            elif curser[0] > 275 and curser[0] < 360:
                if curser[1] > 265 and curser[1] < 350:
                    maths.append('3')
                elif curser[1] > 370 and curser[1] < 460:
                    maths.append('6')
                elif curser[1] > 475 and curser[1] < 565:
                    maths.append('9')
                elif curser[1] > 580 and curser[1] < 675:
                    maths.append('+')
            elif curser[0] > 375 and curser[0] < 465:
                if curser[1] > 265 and curser[1] < 350:
                    maths.append('-')
                elif curser[1] > 370 and curser[1] < 460:
                    maths.append('/')
                elif curser[1] > 475 and curser[1] < 675:
                    mathsString = ''.join(maths)
                    maths.clear()
                    try:
                        maths.append(str(eval(mathsString)))
                    except:
                        maths.append('Syntaxt Error')
            if curser[0] > 390 and curser[0] < 460 and curser[1] > 20 and curser[1] < 40:
                if len(maths)!=0:maths.pop()

    # Display:

    if showTexture == True:
    
        window.blit(calculator, (0, 0))

    #TEXT --------------

    textsurface = myfont.render(''.join(maths), False, (0, 0, 0))
    window.blit(textsurface,(100,125))
    

    if showLines == True:

        # Verticle ------------------------------

        pygame.draw.line(window,(255,0,0),(65,1),(65,1000))
        pygame.draw.line(window,(255,0,0),(155,1),(155,1000))  

        pygame.draw.line(window,(255,0,0),(170,1),(170,1000))
        pygame.draw.line(window,(255,0,0),(260,1),(260,1000))  

        pygame.draw.line(window,(255,0,0),(275,1),(275,1000))
        pygame.draw.line(window,(255,0,0),(360,1),(360,1000))  

        pygame.draw.line(window,(255,0,0),(375,1),(375,1000))
        pygame.draw.line(window,(255,0,0),(465,1),(465,1000))

        # Flat ------------------------------  

        pygame.draw.line(window,(255,0,0),(1,265),(1000,265))
        pygame.draw.line(window,(255,0,0),(1,350),(1000,350))

        pygame.draw.line(window,(255,0,0),(1,370),(1000,370))
        pygame.draw.line(window,(255,0,0),(1,460),(1000,460))

        pygame.draw.line(window,(255,0,0),(1,475),(1000,475))
        pygame.draw.line(window,(255,0,0),(1,565),(1000,565))

        pygame.draw.line(window,(255,0,0),(1,580),(1000,580))
        pygame.draw.line(window,(255,0,0),(1,675),(1000,675))

        # equal sign ------------------------

        pygame.draw.line(window,(0,0,255),(1,475),(1000,475))
        pygame.draw.line(window,(0,0,255),(1,675),(1000,675))

        # delete button -----------------------

        pygame.draw.line(window,(255,0,255),(1,20),(1000,20))
        pygame.draw.line(window,(255,0,255),(1,45),(1000,45))

        pygame.draw.line(window,(255,0,255),(390,1),(390,1000))
        pygame.draw.line(window,(255,0,255),(460,1),(460,1000))

    pygame.display.update()
    clock.tick(20)
pygame.quit()
sys.exit()